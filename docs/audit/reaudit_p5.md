# Re-audit of Math Inquirers Level 5 (Primary 5, ages 10-12)

Date: 2026-10-22. Independent re-score of the CURRENT material on the same two instruments as the earlier audits, followed by a like-for-like comparison. Read-only on content: nothing in `p5/`, `rebuild/`, `split/`, `outputs/` or `diag/` was edited. Written files: this report and `docs/audit/reaudit_p5.py` (helper: brute-force checks, diagnostic simulation, and every number in the tables below; run `python3 -I docs/audit/reaudit_p5.py`).

**Process.** Phase 1 (blind): I scored the current content before opening any earlier audit file. Phase 2: I then opened `gifted_p5.md`, `gifted_fixes_p5.md`, `journey_p5.md`, `fixpass_p5.md`, `close_gaps_p5.md`, `fixes_p5.md` and compared. The Phase 1 scores below were fixed before Phase 2; the only change afterwards is that I converted the journey Fit scores to the earlier audit's convention (raw 3 = just right, converted to fit quality for the means) so the heatmaps can be compared. Sources read: `p5/content/l1..l10.js`, `p5/data.js`, `p5/workbook_html.js`, `rebuild/gen_p5l*.py` (via the built decks in `split/p5l*/project/slides`, all 10 decks, 26 to 28 slides each, title, check, warm, explore, ws, stretch, challenge, talk, exit, reflect slides sampled in every lesson), the rebuilt PDFs (student workbook 57 pages, tutor guide 86 pages, question bank 28 pages, What Learners Get, Free Taster), `diag/content/p5.json`, `diag/build_diag.py` and the built `Math_Inquirers_Level5_Placement_Check.pdf` / `Tutor_Key.pdf`. The workbook text I scored is the text of the built PDF (checked against the content source), not a fix log.

**How the two audits differ in strictness (read before comparing deltas).**
1. These are desk reviews by a model. No child saw any of it. Two different reviewing passes disagree by about 0.3 on a 1-5 cell and by about 1 point on a /24 rubric total even with identical material, so deltas under that size are noise.
2. Rubric: the earlier audit withheld a 2 on criterion 7 (student-led inquiry, "teaching is tutor-led") and criterion 11 (pacing, "no pre-check, early-finisher tiers") and gave 1 on criterion 10 unless a written look-back existed. I credit the planned structures that are now physically in the pages and slides (choose line, sneak-peek, talk rules, reflection box). If I apply the earlier audit's stance on criteria 7 and 11, my level mean falls from 20.2 to 18.2 (shown as "conservative" below). I am stricter than the earlier audit on criterion 8 (pure geometry with no context scores 0, not 1).
3. Tier compliance: the earlier audit judged workbook questions "compliant when there is a way in (a printed fact, started table, picture or first step)". By that rule the current material has no violations. I also applied the owner's stricter STEP 2 principle (Core must be doable by a child who has not been taught the method; the formal method must not be required). By that reading the printed Start-here pages are still only 45% clean. Both are reported; they are not interchangeable.
4. Journey: same personas, same 1-5 scale, same Fit convention as the earlier audit. The diagnostic simulation re-uses the earlier audit's per-item probabilities (`journey_p5.py`) so the placement shares are comparable; those probabilities are assumptions, not data.

---

# PHASE 1 (BLIND): current material scored before reading any earlier audit

## A. Instrument A: gifted-style rubric (12 criteria, 0/1/2) and tier compliance

### A.0 Evidence that applies to every lesson (cited in the tables as S2, S6, S7, S10, S11)
Checked in the content, not in a log. `p5/data.js` TIMELINE, the slides, the tutor guide and the workbook all carry the same timeline (0-3 sneak-peek, 3-9 warm-up, 9-21 explore, 21-33 mini-lesson, 33-37 break, 37-49 page 1 in pairs, 49-53 check, 53-58 teaching before page 2, 58-72 page 2 alone, 72-76 check, 76-82 talk, 82-86 exit, 86-88 reflection, 88-90 stamp).
* **S1 (criterion 1).** Every lesson has an access puzzle (sneak-peek puzzle 1), an explore with objects, an Investigation printed on the page every child gets ("An open puzzle for everyone. Easy first step: ...", parts (a) to (c) climbing to "what if / is it always true / write a rule") and a second what-if on the explore slide (`whatIf`). Model answers sit in `p5/content/inv.js`.
* **S2 (criterion 2).** Page 1 gets 12 minutes (2 or 3 items), page 2 gets 14 minutes (3 items), each check 4 minutes. A lesson prints 14 items (5 or 6 Start-here, 4 Think harder, 3 Go further, 1 Investigation) in a 90-minute plan. "A menu, not a wall" and "Nobody has to finish" soften this, but pace and coverage are still set by the pages. The longest protected thinking block is the 12-minute explore. Never scored above 1.
* **S6 (criterion 6).** Neutral labels "Start here / Think harder / Go further / Investigation"; the line "After question 3 you may choose: carry on, or try Think harder. You can swap at any time."; no "fast track", "strong thinkers" or "early finishers" in the workbook, slides or tutor guide (one residual: slide `p5l7-ws2` says "Finished early? Try the Think harder page"). The first item of every Start-here page has a win-sized part (L1 Q1a, L2 Q1a, L3 Q1a "Try $60 first", L4 Q1a, L5 Q1a, L6 Q1 table, L7 Q1 10% row, L8 Q1a, L9 Q1a, L10 Q1 logic grid).
* **S7 (criterion 7).** Explore and page 1 in pairs (breakout rooms online); a talk slide per lesson with sentence starters, "volunteers first", "pass is always allowed", "no cold-calling, no tallies"; talk questions are claim-testing ("Siti says ... who is right?"). Tutor-led blocks (mini-lesson 12 min, teaching before page 2 5 min, two checks 8 min) are about a third of the lesson. Student noticings are not recorded anywhere.
* **S10 (criterion 10).** The reflection box on the Investigation page ("Something I did well", "The hardest part was...", "What helped me" ticks, "I am still stuck (my tutor will check in with me)", "Pass"), 2 minutes at 86-88, tutor reads it privately. This is a strategy record, not a Polya look-back inside the tasks; look-back items appear only in places (L1 "check every clue", L5 Q5 sum check, L10 Q6b "which start did you use").
* **S11 (criterion 11).** Sneak-peek (private answers, nobody marked), the choice line, the page-2 "Start with ... then choose" plan, the Investigation first step offered to the whole group in talk time. The whole-group teaching blocks remain lockstep and the sneak-peek does not let anyone skip them. Credited 2 on the strength of the choice mechanism; conservative reading 1.

### A.1 Per-lesson rubric (current material, blind)
#### Lesson 1: Million Puzzles  (re-audit 20/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Sneak puzzle 1 (cards 3,6,7,9) and Million Maker start any child; Investigation (p3) has an easy first step then targets 3M to 8M; model answer in inv.js. |
| 2 | Depth over speed | 1 | S2. Page 1 Q1-Q3 in 12 min, page 2 Q4-Q6 in 14 min; Q3 riddle and Q6 find-ALL cannot be thought through in that time. |
| 3 | Abstraction / generalising | 2 | Investigation (c) 'write a rule that tells which side wins', tested on 7M and 8M; explore what-if 'a BILLION seconds'. |
| 4 | Justification | 2 | Q6(b) 'how do you know you have them all'; Q4 'which answers must be wrong'; share Siti v Ravi (999 999). |
| 5 | Multiple paths | 1 | One taught method per task (test both sides; clue order); Q5(d) hint is the only second route. |
| 6 | Challenge ladder | 2 | S6. Printed Core still holds the six-clue riddle (Q3) and find-ALL (Q6); ladder is real but the floor is uneven. |
| 7 | Student-led inquiry | 2 | S7. Pairs in breakout for explore and p1; talk slide 'I noticed / I tested / I know because'. |
| 8 | Complexity / context | 1 | Million seconds, calculator checks, heartbeats (bank only); otherwise number puzzles. |
| 9 | Creativity / posing | 1 | No make-up item on any printed page or slide; riddle posing exists only in bank Challenge C1. |
| 10 | Metacognition | 2 | S10. Reflection box; look-back is 'check every clue' (Q3 key) and Q5 'did you test both ways'. |
| 11 | Pacing flexibility | 2 | S11. Choice after Q3 and a what-if on explore2; mini-lesson (min 21-33) and teaching before p2 are whole-group. |
| 12 | Extension w/o acceleration | 2 | Stays in P5 number work; billion seconds and palindromes are enrichment, not next-year procedure. |

#### Lesson 2: Fraction Feats  (re-audit 20/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Pizza sharing with paper circles; Investigation easy first step (cut a bar into 6) then unit-fraction differences; sneak puzzle 1 (2 pizzas among 4). |
| 2 | Depth over speed | 1 | S2. Q2(c) 'find TWO ways for 3/8' and Q4 telescoping need thinking time the 14-min page-2 slot does not give. |
| 3 | Abstraction / generalising | 2 | Investigation (b) 'is it always true', (c) uses the rule; Q4(c) predict sum to 1/90. |
| 4 | Justification | 2 | Q1(c) which group gets more (shortfall hint) 'Explain'; share 'Ben says 1/2 + 1/3 = 2/5'. |
| 5 | Multiple paths | 1 | Common denominator v shortfall reasoning mentioned, not compared by children; one method for unit fractions. |
| 6 | Challenge ladder | 2 | S6. Q2 and Q4(c) sit in Start-here; Q1(d) removed so page 1 is gentler. |
| 7 | Student-led inquiry | 2 | S7. Face-off vote with whispered reasons, volunteers share; talk 'why is each sum 1 take away a unit fraction'. |
| 8 | Complexity / context | 1 | Pizzas, ribbon, money, Egyptian unit fractions; thin contexts. |
| 9 | Creativity / posing | 1 | Bank C4 only (own fraction-of-remainder story); not on pages or slides. |
| 10 | Metacognition | 2 | S10. Reflection box; 'Did you test both ways?' on Q6. |
| 11 | Pacing flexibility | 2 | S11. Choose after Q3; Q1 win then Q2 wall on same page. |
| 12 | Extension w/o acceleration | 2 | Unit fractions and telescoping on P5 fractions; fraction / whole number flagged as P6 preview in bank S6. |

#### Lesson 3: Before and After  (re-audit 21/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Counter-swap explore (18 and 6) is open to all; sneak puzzle 1 (Ben 8, father 32) is arithmetic; Investigation easy first step then 'which totals work'. |
| 2 | Depth over speed | 1 | S2. Q1-Q2 on page 1 and Q3-Q5 on page 2, each 3-5 sub-parts; no unhurried slot. |
| 3 | Abstraction / generalising | 2 | Investigation (b)(c) 'for which totals can it be done; write a rule'; explore 'what never changes'. |
| 4 | Justification | 2 | Q3(a) test Ben's claim; Q4(a) 'total or difference?'; talk 'can the difference still be 20?'. |
| 5 | Multiple paths | 1 | Model v 'what stays the same' triage named; guess-and-check entry ('Try $60 first') versus bars; not compared on slides. |
| 6 | Challenge ladder | 2 | S6. Q2 and Q5 are the lesson's own method (unit bars), so Core is not low floor on those. |
| 7 | Student-led inquiry | 2 | S7. Counter table in pairs; talk questions are claim-testing. |
| 8 | Complexity / context | 1 | Money, stickers, ages; thin coating. |
| 9 | Creativity / posing | 2 | Tutor extension and bank C1 'make up your own before-and-after story'; Investigation (b) varies the total. |
| 10 | Metacognition | 2 | S10. Reflection box; Q5 asks which colour did not change (look-back on the model). |
| 11 | Pacing flexibility | 2 | S11. Choice line 'after question 3' falls on page 2 (Q3 is there), so the choice arrives late. |
| 12 | Extension w/o acceleration | 2 | P5 fraction models; no algebra. |

#### Lesson 4: Triangle Areas  (re-audit 20/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Cut-and-cover explore for anyone; sneak puzzle 1 (6x4 rectangle, cut diagonal); Investigation easy first step (3-4 right triangle) then 'find ALL of area 6'. |
| 2 | Depth over speed | 1 | S2. Fewer items (5) but Q3-Q4 are multi-step; page 2 has the same 14 min. |
| 3 | Abstraction / generalising | 2 | Investigation (b) 'what do you notice about all top corners' (a line); Q2(c) explain same area; Go further Q6 two squares. |
| 4 | Justification | 2 | Q2(c) explain; Q1(d) 'which lengths did you NOT need'; share 'longer sides means bigger area?'. |
| 5 | Multiple paths | 2 | Slides teach 'split' and 'take away'; bank C1 asks for TWO ways; children compare in pairs. |
| 6 | Challenge ladder | 2 | S6. Think harder S1-S4 are one-step (ladder rung is low); Go further is strong. |
| 7 | Student-led inquiry | 2 | S7. Paper-cutting in pairs; talk 'how can different triangles have the same area'. |
| 8 | Complexity / context | 0 | Pure geometry; no real-world or cross-subject link anywhere in the lesson. |
| 9 | Creativity / posing | 1 | Bank C1 'make up your own shaded-area puzzle'; none on pages; whatIf asks for three triangles of area 12. |
| 10 | Metacognition | 2 | S10. Reflection box; Q1(d) is a built-in strategy look-back. |
| 11 | Pacing flexibility | 2 | S11. Page 1 holds only Q1-Q2 so 'after question 3' is the first item on page 2. |
| 12 | Extension w/o acceleration | 2 | Same-grade geometry reasoning. |

#### Lesson 5: Volume Vault  (re-audit 19/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | 24-cube explore for anyone; sneak puzzle 1 (4x3x2 box); Investigation easy first step (boxes of 12) then 48 and 64. |
| 2 | Depth over speed | 1 | S2. 6 items with figures; Q3-Q6 are 3-5 sub-parts each; 638 words on pages 1-2. |
| 3 | Abstraction / generalising | 1 | Investigation (c) 'is there a number with only ONE box shape'; otherwise counting and formulas. |
| 4 | Justification | 2 | Q1(b) explain; share 'a 1000 cm3 stone always raises 1 cm?'; Q5 'do your four numbers add to 64'. |
| 5 | Multiple paths | 1 | Layers v multiply shown by tutor only; no children's comparison. |
| 6 | Challenge ladder | 2 | S6. Q4 (displacement) and Q6(c) are the lesson's method at the end of Start-here. |
| 7 | Student-led inquiry | 2 | S7. Pairs build cuboids; talk 'why does a big tank rise only a little'. |
| 8 | Complexity / context | 1 | Tanks, water, packing sugar cubes; several quantities interact (modest). |
| 9 | Creativity / posing | 1 | Bank C5 'make up your own tank puzzle'; none on pages. |
| 10 | Metacognition | 2 | S10. Reflection box; check-sum on Q5. |
| 11 | Pacing flexibility | 2 | S11. Choice after Q3 (page 1 has Q1-Q3); page-2 plan names Q5 (painted cube) as a first item. |
| 12 | Extension w/o acceleration | 2 | Volume and displacement at P5 level; painted-cube pattern is enrichment. |

#### Lesson 6: Rate Racers  (re-audit 19/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Better Buy Showdown starts with whole numbers; sneak puzzle 1 (12 L in 4 min); Investigation easy first step then 'all ways for 24 L'. |
| 2 | Depth over speed | 1 | S2. 6 items, long stems (car park, three shops); 633 words on pages 1-2. |
| 3 | Abstraction / generalising | 1 | Investigation (c) 'what if 25 litres, what changes'; otherwise applied rate tasks, no rule statement. |
| 4 | Justification | 1 | Only talk-time and Investigation (b) ask 'why'; none of Q1-Q6 says 'explain'. |
| 5 | Multiple paths | 1 | Value-of-one v scaling hint in bank C3; one method on pages. |
| 6 | Challenge ladder | 2 | S6. Q4(c) and Q5 are Challenge-grade inside Start-here. |
| 7 | Student-led inquiry | 2 | S7. Printer race in pairs; talk 'is the biggest pack always best?'. |
| 8 | Complexity / context | 2 | Shops, car park, gym fees, taps and leaks: several variables and a tariff rule in words. |
| 9 | Creativity / posing | 2 | Lesson extension 'better-buy poster' (swap and prove), bank C6, Investigation (c) what-if; none printed as posing. |
| 10 | Metacognition | 1 | S10 box only; no look-back item inside the tasks. |
| 11 | Pacing flexibility | 2 | S11. Choice after Q3; page-2 plan 'Q4(a), Q6(a) then Q5'. |
| 12 | Extension w/o acceleration | 2 | P5 rate work; no later-year procedures. |

#### Lesson 7: Percentage Puzzles  (re-audit 21/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Hundred-square snap and predict 'up 10% then down 10%'; sneak puzzle 1 (35 of 100 shaded); Investigation easy first step then order of discounts. |
| 2 | Depth over speed | 1 | S2. 5 items but Q2/Q5 are multi-step with decimals. |
| 3 | Abstraction / generalising | 2 | Investigation (b) 'does ORDER ever change it, always true?' and (c) is 20 then 10 the same as 30; share GST v discount order. |
| 4 | Justification | 2 | Q3(c) Siti's claim; Q4(d) Ben's 45%; Investigation tests claims. |
| 5 | Multiple paths | 2 | Q1(a) 'how did you find 35% from the boxes', Siti's 15% method; teaching compares routes. |
| 6 | Challenge ladder | 2 | S6. Q5 (two wholes) is Think-harder grade; P6 previews are labelled. |
| 7 | Student-led inquiry | 2 | S7. Predict then compare in pairs; talk 'GST first or discount first'. |
| 8 | Complexity / context | 2 | Singapore prices, GST, discounts, hawker; several interacting variables. |
| 9 | Creativity / posing | 1 | Bank C1 'make up your own percentage trap'; Investigation (b) 'test pairs of your own'; none printed as posing. |
| 10 | Metacognition | 2 | S10. Reflection box; Siti/Ben claims are look-back checks. |
| 11 | Pacing flexibility | 2 | S11. Choose after Q3; Think-harder S1 and Go further are P6 previews for those who choose. |
| 12 | Extension w/o acceleration | 1 | Think-harder S1 and Go further Q5 are labelled P6 previews and the discount-then-GST and up-then-down reasoning in Q2/Q3 leans on P6-type percentage change, so only 1. |

#### Lesson 8: Angle Chasers  (re-audit 19/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Guess the angle (paper corner, fold) and tear-corners explore; sneak puzzle 1 (split a right angle 30/60); Investigation easy first step (base angle 10) then all tens. |
| 2 | Depth over speed | 1 | S2. 5 items but Q2 has 3 shapes and Q3/Q4 are 4-step chains; 543 words. |
| 3 | Abstraction / generalising | 2 | Explore 'does it work for every triangle'; whatIf five-sided shape (predict 540); Investigation (c) multiples of 15. |
| 4 | Justification | 2 | Reasons A-F and 'write the reason' on Q2-Q4; talk 'can an isosceles triangle have an angle over 90?'. |
| 5 | Multiple paths | 1 | One chain per figure; no compared routes. |
| 6 | Challenge ladder | 2 | S6. Q3 and Q4 are the method (angle chases) in Start-here. |
| 7 | Student-led inquiry | 2 | S7. Tear-and-fit in pairs; talk questions are claims. |
| 8 | Complexity / context | 0 | Pure geometry; surveyors / pilots only in the hook sentence. |
| 9 | Creativity / posing | 1 | Bank C2 'make up your own angle-chase puzzle'; none on pages. |
| 10 | Metacognition | 2 | S10. Reflection box; 'which angle fact did you use' on Q1(d). |
| 11 | Pacing flexibility | 2 | S11. Page 1 holds Q1-Q2 only; choice falls on page 2. |
| 12 | Extension w/o acceleration | 2 | P5 angle properties explored deeply. |

#### Lesson 9: Pattern Generalisers  (re-audit 21/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | High-fives explore for anyone; sneak puzzle 1 (stick triangles, picture); Investigation easy first step (1, 4, 9) then L-borders and evens. |
| 2 | Depth over speed | 1 | S2. 5 items but Q3-Q5 are table / supposition tasks; 463 words. |
| 3 | Abstraction / generalising | 2 | Investigation (b) 'is it always true, use an L-border picture' (c) even numbers; every Q asks for a rule in words. |
| 4 | Justification | 2 | Q1(d) Ben's doubling claim, Q2(a) 'why not 6', Q5(b) 'why must she be wrong'; share Mei's 62 sticks. |
| 5 | Multiple paths | 2 | Guess-and-check table v supposition v border picture; talk asks which children preferred. |
| 6 | Challenge ladder | 2 | S6. Core is the best low floor of the level; TH and GF climb well. |
| 7 | Student-led inquiry | 2 | S7. High fives in pairs; talk compares methods. |
| 8 | Complexity / context | 1 | Hawker tables, tickets, quiz marks; thin coating. |
| 9 | Creativity / posing | 1 | Bank C2 'make up your own growing pattern'; none printed. |
| 10 | Metacognition | 2 | S10. Reflection box; 'check it another way' in Investigation (c). |
| 11 | Pacing flexibility | 2 | S11. Page 1 holds Q1-Q2; choice falls on page 2. |
| 12 | Extension w/o acceleration | 2 | Pattern and number-structure ideas on P5 content. |

#### Lesson 10: Challenge Day  (re-audit 22/24)

| # | Criterion | Score | One-line evidence (current material) |
|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | Puzzle menu (pick 2 of 4); sneak puzzle 1 (shirt colours) ; Investigation easy first step (staircase 1-3 steps). |
| 2 | Depth over speed | 1 | S2. 6 items from mixed topics; the menu and 'teach one puzzle' reward explaining over finishing. |
| 3 | Abstraction / generalising | 2 | Investigation (b)(c) Fibonacci reason + 'what if 3 steps'; whatIf 'make up your own card whose answer is 10'. |
| 4 | Justification | 2 | Q5 'try each child, count liars', Q6(b) 'which start, why'; talk frame 'I started by..., I know it is right because'. |
| 5 | Multiple paths | 2 | Mini-lesson is a toolbox of 6 starts; share 'could another start also work?'; bank asks. |
| 6 | Challenge ladder | 2 | S6. Strong ladder; Q2 / Q3 on page 1 need a first step but have 'Start here' lines. |
| 7 | Student-led inquiry | 2 | S7. Pairs choose cards and teach in two sentences (pass allowed). |
| 8 | Complexity / context | 1 | Hawker logic, chairs puzzle, ages; mixed but no cross-subject link. |
| 9 | Creativity / posing | 2 | whatIf and extension 'write your own logic puzzle', bank C5 posing; one printed hook only. |
| 10 | Metacognition | 2 | S10 plus Q6(b) strategy look-back and exit 'say which start you used'. |
| 11 | Pacing flexibility | 2 | S11. Menu choice is genuine; 'after question 3' works (Q3 on page 1). |
| 12 | Extension w/o acceleration | 2 | Mixed strategies on P5 content. |

**Level, blind rubric:** mean 20.2/24 (range 19 to 22). Conservative reading (criteria 7 and 11 at 1): 18.2.

### A.2 Tier compliance (blind), every Core / Think Harder / Challenge item
Method: the question bank (231 items: 6 Core, 8 or 9 Think harder, 9 Challenge per lesson) and the printed workbook pages (55 Start-here items; the printed Think harder page is bank S1-S4 and the printed Go further page is bank C7-C9, so those are inside the 231). Verdicts: C compliant; B borderline (counted against it in "strict", for it in "lenient"); V violation of the tier principle. The slide-only Think harder / Go further items (for example L3 slide "3/8 ticket and $15 food", L5 "tank 1/5 to 3/5", L6 "bath 168 l", L7 "$90 jacket 10% twice", L8 "rhombus ADC 130") were read and are all compliant; they are not counted.

**Question bank.** Core (60): all 60 are doable with objects, drawing, counting or guess-and-check or state the fact needed (L4 C1 cut a 6x4 rectangle on its diagonal; L5 C1 build 3x2x2 with cubes; L8 C1 tear off a triangle's corners; L2 C1 share 3 bars among 4 friends). Two borderline: L7 C4 (24 of 40 as a percentage) and C5 (25% of $60) assume 25% = a quarter. Think harder (81): 9 borderline because they need no idea from the lesson or sit at Core level (L1 S4, L2 S4 and S8, L4 S4, L8 S6 clock hands, S7 minute hand and S9 crossing lines, L7 S4 12% of $250) or lean on P6 content with a hint (L7 S1). Challenge (90): 2 borderline (L9 C1 staircase of 10 steps and C3 squares on a 4x4 grid, both close to Core counting); the rest need mastery plus extension (find-all, generalise, work backwards, justify, pose). No bank item needs the lesson's formal method as a Core item.

**Printed Start-here pages (what the child actually does).**

| Lesson | Items | V (needs the lesson's method, no way for an untaught child) | B (borderline) |
|---|---|---|---|
| 1 | 6 | Q3 six interlocking clues incl. rounding to 100 000 (the START HERE line only begins it); Q6 range + list ALL numbers + digit sum | Q5 (d) "make 100" is a search |
| 2 | 6 | Q2 unlike-denominator subtraction + unit-fraction idea ("TWO ways for 3/8") | Q4 (c) predict the sum to 1/90 |
| 3 | 5 | Q2 ratio after a swap (unit bars are the lesson); Q5 unchanged-part bar | Q3 (b) "3/5 as many" |
| 4 | 5 | Q4 shaded triangle by subtracting three white triangles | Q1 (formula printed, executable but not discoverable); Q3 split along AC |
| 5 | 6 | Q4 rise of water = volume / base (displacement) | Q3 layers + litres; Q5 painted-cube table; Q6 (c) equal depth |
| 6 | 6 | Q4 (c) split 900 pages so both printers finish together | Q2 three shops; Q3 add rates and a leak; Q5 car-park tariff |
| 7 | 5 | Q5 two wholes in a table | Q2 discount then GST; Q3 up 25% down 20%; Q4 remainder bar |
| 8 | 5 | Q3 four-step chain with reasons; Q4 parallelogram + isosceles chain | Q2 three shapes with reasons; Q5 find every case |
| 9 | 5 | none | Q5 (b) why must she be wrong |
| 10 | 6 | none | Q2 backwards with a fraction; Q3 model with a $10 gap |
| **Level** | **55** | **11** | **19** |

**Compliance, current.**

| Basis | Core bank | Think harder bank | Challenge bank | Printed Start-here | All |
|---|---|---|---|---|---|
| Earlier audit's rule (a way in exists) | 60/60 | 81/81 | 90/90 | 55/55 (a few parts have none: L5 Q6 c, L6 Q4 b c) | 286/286 = 100% |
| Owner's strict principle, B counted as fail | 58/60 (97%) | 72/81 (89%) | 88/90 (98%) | 25/55 (45%) | 243/286 = **85%** |
| Strict, B counted as pass | 60/60 | 81/81 | 90/90 | 44/55 (80%) | 275/286 = 96% |

Per lesson, strict (B as fail): L1 25/29 (86%), L2 25/29 (86%), L3 25/28 (89%), L4 24/28 (86%), L5 25/29 (86%), L6 25/29 (86%), L7 20/28 (71%), L8 22/29 (76%), L9 25/28 (89%), L10 27/29 (93%).

**Ladder shape.** In the bank the three tiers form a real low-floor ladder (Core objects and pictures, Think harder the taught idea in a new setting, Challenge find-all / generalise / pose). On the printed pages the ladder is flatter: Start here already contains method-dependent items (L3, L5 to L8), and Think harder is often one step (L4 S1-S4 are all "area, reversed" with no figure). The Go further pages are the strongest tier (L4 Q5 height on the hypotenuse, L9 Q5 diamonds, L8 Q6 square and equilateral triangle).

### A.3 Strengths and gaps (blind)
Strengths: a low-floor start in every lesson that is physically in the lesson (paper pizzas, counters, cubes, cutting, tearing, high fives); an Investigation that every child receives with an easy first step; claim-testing talk ("who is right?"); neutral labels and private answers; reflection that allows pass; same-grade content explored deeply with brute-forced find-all claims. Gaps: depth over speed (14 printed items, fixed slots); problem posing is not on any printed page; multiple solution paths are mostly shown by the tutor; real-world or cross-subject complexity is thin outside L6 and L7 (L4 and L8 have none); several Start-here items still need the lesson's own method; Think harder geometry pages have no figures.

**Safe language (research note section 3).** Safe: "a maths enrichment programme for curious, capable children focused on reasoning and problem solving"; "inspired by research-based approaches such as low-floor high-ceiling tasks and Polya"; "open investigations with room to go further"; "explaining why, more than one method, learning from mistakes"; "small groups, differentiated challenge" (true only if the tutor runs the choice). Not yet supportable: "focused on depth / not a drill programme" as a headline (criterion 2 is 1 in every lesson), "extends beyond the syllabus not ahead of it" without the caveat that L7 (and one bank item in L2) are flagged P6 previews. Do not claim identification, GEP equivalence or results.

---

## B. Instrument B: student journey (three personas x six scores x ten lessons)

Personas as in the brief: LOW (slow reader, school maths roughly 40-50%, easily discouraged, shaky on fractions of a quantity, unlike fractions, decimal division), MIDDLE (typical, needs worked examples), HIGH (fast, bored by repetition, may rush). Scores: Participate / Fit (raw, 3 = just right, under 3 too hard, over 3 too easy) / Fun / Confidence / Motivation / Social-online. Mean of six converts Fit to fit quality (3 becomes 5, 2 or 4 becomes 3, 1 or 5 becomes 1).

### B.0 Level-wide observations (blind, from walking the real artefacts)
1. **Sneak-peek (minutes 0-3).** Two puzzles on untaught ideas, answers shown privately (own paper to the tutor, or everyone holds paper up at once), "guessing and I do not know are welcome", no tally, volunteers explain. Puzzle 1 is an access puzzle in all ten lessons (L1 cards 3,6,7,9; L3 ages Ben 8 and father 32; L6 12 L in 4 min; L9 stick triangles with a picture; L10 shirt colours). This removes the old public, explanation-demanding check. Residual: puzzle 2 is a thinking puzzle (L1 "how do you know no other place makes 47?"), three minutes for two puzzles plus reading is tight for a slow reader, and the correct answer is clicked onto the shared slide.
2. **Choosing a start.** One neutral line on page 1, invitation to the whole group, no announcement, pairs not split, swap any time. Defect: the line says "After question 3" but page 1 holds only Q1-Q2 in L3, L4, L8 and L9, so Q3 is the first item on page 2 after the 4-minute check and 5-minute teaching; a ready child in those four lessons does not get their choice at minute 49.
3. **Guaranteed early win for LOW.** 10/10 lessons open Start-here with a win-sized first part (listed in S6). Page 1 still usually ends on its hardest item.
4. **Page 2 "Start with ..." plan.** Names the entry items, but for L5 ("Q4 (a) to (c) and Q5") and L6 ("Q4 (a), Q6 (a) and then Q5") the named items include the painted-cube table and the car-park tariff, the hardest stems of those lessons.
5. **Reading load.** Words on pages 1-2 of the PDF (all text incl. numbers): L5 638, L6 633, L1 588, L3 579, L2 559, L8 543, L4 519, L10 507, L9 463, L7 443 (mean 547). The earlier audit counted prose words differently (306 to 425), so only the ranking is comparable: L5/L6 are now the heaviest, L8 has dropped from first to sixth, L7 is lightest.
6. **Labels and language.** "Think harder" and "Go further" remain, but there is no ability or speed vocabulary on the workbook or slides; strategy praise ("Praise strategy, not speed", "wait 10 seconds", "never record scores") is in every script. The parent-facing What Learners Get still mentions a readiness tracker and a "Challenge Group for children who show the signs" and progress marks "secure / developing / needs help" (tutor-and-parent side only).
7. **Reflection.** Safe for a low-confidence child: single small box, pass allowed, an "I am still stuck (my tutor will check in with me)" tick, private reading, check-in in the open session. It sits on the Investigation page every child receives, at 86-88 minutes (2 minutes, not squeezed out by the exit ticket).
8. **Pairs and online.** Camera shows paper; answers are shown to the tutor only; pass is always allowed; the relay in L10 is volunteers-first. Cubes (L5) and a protractor (L8) depend on the parent at home.
9. **Numbering.** Core Q1-Q6, then Think harder 1-4, Go further 5-7 and the Investigation "No.8": Q4, Q5 and Q6 each appear twice in a lesson, and the page-2 plans and tutor notes say "Q5". Ambiguous for a LOW child and for a tutor on a video call.

### B.1 Per-lesson scores (current material, blind)
#### Lesson 1: Million Puzzles

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 4 | 5 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 4 |
| Fun | 3 | 4 | 4 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 4 | 4 |
| Social / online | 4 | 4 | 4 |
| **Mean of six (Fit converted)** | **3.33** | **4.33** | **4.00** |

* **LOW**: Sneak puzzle 1 (p5l1-check) and Million Maker (warm1) are doable and private; calculators for the million-seconds explore; Q1(a)/Q2(a) are wins and exit (a) place value is fair. Wall: page 1 Q3 six-clue riddle (~80 words, START HERE helps) and page 2 Q6 find ALL numbers with digit sum 9; 7-digit reading is new.
* **MIDDLE**: Million seconds gives a wow (about 11.5 days); Q4 estimate-by-rounding and Q5 comfortable; Q3 and Q6 stretch but the Start-here lines carry.
* **HIGH**: Sneak puzzle 2 and the billion-seconds what-if give early thinking, but warm-up quick Qs, Q1, Q2 and the 12-min reading-numbers teach are trivial; real choice only after Q3 (about minute 45); Investigation targets and Go further Q6/Q7 pay off.
* Flags: Minute 0-3: two puzzles in three minutes, puzzle 2 asks 'how do you know no other place makes 47?'. Minute 37-49 LOW: Q3 six clues. Minute 58-72 LOW: Q6 alone, no partner. Reading 588 words on pages 1-2.

#### Lesson 2: Fraction Feats

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 3 | 5 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 3 |
| Fun | 3 | 4 | 5 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 4 | 4 |
| Social / online | 4 | 4 | 4 |
| **Mean of six (Fit converted)** | **3.17** | **4.33** | **4.50** |

* **LOW**: Face-off vote and paper-pizza explore are real low floor; Q1(a) 5/8 a win. Walls: warm-up Qs '2/5 x 3/4', '4/5 / 2' before any teaching, Q2 needs 7/10 - 1/2 type subtraction (Start here covers only the first), Q2(c) 'TWO ways for 3/8', Q4(c).
* **MIDDLE**: Face-off, explore and Q3 (240 stickers bar) reachable; Q2(c), Q4(c) stretch but do not break.
* **HIGH**: Egyptian unit fractions, telescoping (Q4, Investigation, Go further Q5) are the best ideas in the level; first 12 minutes and Q1 are easy.
* Flags: Minute 3-9: warm-up Qs include fraction x fraction before teaching (private whiteboards). Q2 and Q4(c) on the same pages as the win.

#### Lesson 3: Before and After

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 4 | 4 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 3 |
| Fun | 3 | 4 | 4 |
| Confidence | 3 | 3 | 4 |
| Motivation | 3 | 4 | 4 |
| Social / online | 3 | 4 | 4 |
| **Mean of six (Fit converted)** | **3.17** | **4.00** | **4.33** |

* **LOW**: Sneak puzzle 1 now ages arithmetic (Ben 8, father 32); counter-swap explore concrete; Q1(a) 'Try $60 first' is a win; (d) is optional. But Q2 (3/4 as many after a swap) and Q5 (beads) ARE the method; 40-60-word stems and 'gives/must give' language; page-2 plan still asks Q3(a), Q4(a)(b), Q5(a)(b).
* **MIDDLE**: Scaffolds ('try a gift of $10', 5-part bar) help; Q2 and Q5 still stretch to the edge of her level.
* **HIGH**: Total / difference / unchanged-amount triage and Investigation 'which totals work' are good; core feels easy until Q5.
* Flags: Minute 21-33 and 53-58 are the method; 'After question 3 you may choose' lands on page 2 (Q3 is there). Reading 579 words.

#### Lesson 4: Triangle Areas

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 5 | 5 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 3 | 3 | 4 |
| Fun | 4 | 5 | 4 |
| Confidence | 4 | 4 | 4 |
| Motivation | 3 | 4 | 4 |
| Social / online | 4 | 4 | 4 |
| **Mean of six (Fit converted)** | **4.17** | **4.50** | **4.00** |

* **LOW**: Half-or-not vote (no reading), cutting an 8x6 rectangle, formula printed; Q1(a) 24 cm2 is a win; Q2 half-rectangle is visual. Page 2: Q3 (split along AC) and Q4 (three subtractions) are the cliff but the plan routes to Q5 and Q3; slanting sides 13/15/17 are a trap.
* **MIDDLE**: Best-fitting core; Q2(c) 'explain why same area' is an aha; Q4 stretches.
* **HIGH**: Think harder S1-S4 are one-step; Go further Q5 (height on hypotenuse), Q6 (two squares) and the Investigation (all triangles of area 6, line of top corners) are strong.
* Flags: Choice line misfires (page 1 has Q1-Q2 only). Think harder pages have no printed figures (Q2 right triangle, Q3 square) so LOW must draw from words.

#### Lesson 5: Volume Vault

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 4 | 5 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 3 |
| Fun | 4 | 5 | 4 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 4 | 4 |
| Social / online | 3 | 4 | 4 |
| **Mean of six (Fit converted)** | **3.33** | **4.50** | **4.33** |

* **LOW**: 24-cube explore and Q1 (count cubes) are wins; Missing Edge Match is silent; dice/Lego if no cubes. Walls: Q3 (50x30x18, litres), Q4 (water rise from 5 metal cubes), Q5 (painted 4x4x4 table) - and the page-2 plan lists Q5 among the first items; 638 words.
* **MIDDLE**: Q1, Q2 and Q4 are the right size; 'Words and signs' line explains cm3 / l / breadth.
* **HIGH**: Painted-cube table, 48 and 64 boxes (a prime gives one box) and Go further three-face product are good; trivial front end.
* Flags: Page-2 plan 'Q4(a) to (c) and Q5' starts LOW on the hardest 3-D items. Cubes at home are not guaranteed.

#### Lesson 6: Rate Racers

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 3 | 4 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 3 |
| Fun | 3 | 4 | 4 |
| Confidence | 2 | 3 | 4 |
| Motivation | 2 | 4 | 4 |
| Social / online | 3 | 4 | 4 |
| **Mean of six (Fit converted)** | **2.67** | **4.00** | **4.33** |

* **LOW**: Better Buy starts with whole numbers (4 pens $2 v 10 pens $4) and sneak puzzle 2 uses whole numbers; Q1 table is a win and Q2 has 'Start here $4.20 / 6'. Still decimals ($2.92 / 4, $7.80 / 12), Q2(c) search, Q3 four parts, Q4 'finish together', Q5 car-park tariff (printed timeline helps); page-2 plan puts Q5 third.
* **MIDDLE**: Q1, Q3, Q4(a) fine; Q2(c) and Q5 hurt; 633 words on pages 1-2.
* **HIGH**: Printers, leak, candles and '3 cats' are well pitched; Q2(c) search is a good puzzle.
* Flags: Highest-risk stem: Q5 car park (time after noon + part-of-half-hour rule). Decimal division remains in Q2.

#### Lesson 7: Percentage Puzzles

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 4 | 5 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 3 |
| Fun | 4 | 5 | 5 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 5 | 4 |
| Social / online | 4 | 4 | 4 |
| **Mean of six (Fit converted)** | **3.50** | **4.67** | **4.50** |

* **LOW**: Hundred-square snap and 'up 10% down 10%' predict are starts anyone can make; Q1 table from 10%/5%/1% is a win. Strain: Q2 discount then GST on the sale price (decimals), Q3 claim test, Q5 two-wholes table; sneak puzzle 2 needs $81.
* **MIDDLE**: Best relevance (Singapore prices, GST) and the 'percentage of WHAT?' refrain.
* **HIGH**: Investigation 'does the order of two discounts matter' with the 4/5, 9/10 hint is a real conjecture task; P6 previews flagged.
* Flags: Slide ws2 says 'Finished early? Try the Think harder page' (speed framing). Q2 needs two decimal steps.

#### Lesson 8: Angle Chasers

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 4 | 4 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 3 |
| Fun | 3 | 4 | 5 |
| Confidence | 2 | 3 | 5 |
| Motivation | 3 | 4 | 4 |
| Social / online | 3 | 4 | 4 |
| **Mean of six (Fit converted)** | **3.00** | **4.00** | **4.67** |

* **LOW**: Guess-the-angle with a paper fold and tear-corners are concrete; Q1(a) 180-68 a win; 'Angle BOC means...' line added. But the mini-lesson gives eight angle facts in 12 min and Q2-Q4 ask for written 'because' reasons (sentence frame and A-F strip given) on a 3-shape page and 4-step chains.
* **MIDDLE**: Q3 'reason only for (b) and (d)' is reachable; Q4 and Q5 are heavy.
* **HIGH**: Detective chains: Think harder S4, Go further Q5-Q7 and the isosceles-in-tens Investigation are satisfying.
* Flags: Page 1 holds Q1-Q2 only; 'Write the reason' is a new genre of answer; highest fact load in the mini-lesson.

#### Lesson 9: Pattern Generalisers

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 5 | 5 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 3 | 3 | 4 |
| Fun | 4 | 5 | 5 |
| Confidence | 3 | 4 | 5 |
| Motivation | 3 | 4 | 5 |
| Social / online | 4 | 4 | 4 |
| **Mean of six (Fit converted)** | **4.00** | **4.50** | **4.50** |

* **LOW**: High fives (dots, lines, table) is social and low floor; the stick-triangle check has a picture; Q1/Q2 draw-and-count are wins; Q3 table has its first row filled. Wall: Q4/Q5 supposition (hint: suppose all 20c) and Q5(b) 'why must she be wrong'. 'Nobody races' in Guess My Rule.
* **MIDDLE**: Q3 guess-and-check is the sweet spot; Q4-Q5 tough but hinted.
* **HIGH**: Best lesson for HIGH: odd-number L-border proof, diamonds (61), 100th digit, even-number rule.
* Flags: Choice line lands on page 2 (page 1 has Q1-Q2). Supposition vocabulary is explained only through a hint.

#### Lesson 10: Challenge Day

| | LOW | MIDDLE | HIGH |
|---|---|---|---|
| Participate | 4 | 5 | 5 |
| Fit (raw: 3 just right, <3 too hard, >3 too easy) | 2 | 3 | 3 |
| Fun | 4 | 5 | 5 |
| Confidence | 3 | 4 | 4 |
| Motivation | 3 | 4 | 5 |
| Social / online | 3 | 4 | 4 |
| **Mean of six (Fit converted)** | **3.33** | **4.50** | **4.67** |

* **LOW**: Puzzle menu (pick 2 of 4) is the one real choice; Q1 is now the logic grid (win); relay is volunteers-first with pass and green/orange cards. But Q2 (backwards with a fraction) and Q3 follow, topics from lessons 1-9 resurface, and 'teach one puzzle in two sentences' is public (frame provided).
* **MIDDLE**: Good synthesis day; the 'How to START' toolbox helps.
* **HIGH**: Best ceiling: staircase / Fibonacci Investigation, logic chairs, make-your-own puzzle.
* Flags: Mix-up relay can land a lesson-6 question on a child who missed lesson 6 (volunteer and pass reduce this); exit ticket plus certificates share minutes 82-90.

### B.2 Diagnostic check (blind)

**Current rule** (from `diag/build_diag.py` and the built PDF): child sheet = 4 warm-up (level below) + 6 main + 2 optional "Brain stretchers"; each question has a "not learnt yet" tick; the parent adds the marks. Main 4 to 6: join Ages 10-12 (Level 5); if a stretcher was right "you could try the Level 6 check". Main 2 or 3: "a short chat with a tutor and the free taster ... Level 5 with a little support suits many children; if the warm-up is 2 or less, Level 4 may be more comfortable". Main 0 or 1: "We suggest Ages 9-11 (Level 4)". Warm-up is used only inside the 2-3 row; stretchers only add the try-up line. (`docs/levels_and_placement.md` still describes a percentage rule, 70%+ / 40-69% / under 40%, and the brief's 6-8 of 8 rule is also stale: three descriptions of the rule exist.)

**(a) True skill demand and fairness.** W1 5/6 - 1/3 (related denominators, P4, fair). W2 2.4 / 6 (decimal / whole number, P4, fair). W3 3/4 of 48 (fraction of a set, P4 and a real prerequisite for L2, L3, L10, fair; replaces the old 24 x 35). W4 perimeter 36 and length 11 then area (two-step, P4; fair, though it reuses the numbers of the Level 4 check's core question). M1 round 4,386,512 to the nearest hundred thousand (transfer of rounding; fair). M2 Sam 2/5 then 1/3 of the remainder, $24 left (60; fraction of a remainder, standard P5, hard for the average child). M3 triangle area 40, base 16 (5; reverse formula; fair). M4 tank 50x30x40 at 6 l/min (10; volume + conversion given + rate; hardest main item). M5 60% of 40 then 25% (6; percentage of a quantity twice; fair). M6 isosceles, apex 50 (65; in syllabus and in L8, fair; replaces the invalid quadrilateral-sum item). S1 2, 5, 10, 17, 26 ... 10th (101; competition style, persistence works). S2 3:1 then 2:1 after giving 18 (162; a P6 before-and-after heuristic; fair as an optional stretch). All answers verified (helper script).

**(b) Six profiles on the current rule, my own blind assumptions** (per-question success probabilities listed in the helper; exact calculation, not random).

| Profile | Mean warm / main / stretch | Join (main 4-6) | Chat (2-3) | Level 4 (0-1) | Right level against what the lessons demand? |
|---|---|---|---|---|---|
| Strong for age | 3.7 / 5.3 / 1.1 | 97% (78% also see "try Level 6") | 3% | 0% | Yes. |
| Typical for age | 3.2 / 3.8 / 0.3 | 62% | 36% | 2% | Yes (Level 5 is right; the chat row is gentle). |
| Weak for age | 1.9 / 1.5 / 0.0 | 3% | 45% (34% with warm-up 2 or less, so "Level 4 may be more comfortable") | 53% | Mostly. The chat row tells weak children Level 5 "suits many children". |
| Younger and strong (age 9, P4) | 3.7 / 2.8 / 0.8 | 24% | 63% | 12% | Mostly. The 12% who score 0-1 are sent to Level 4 even with 4/4 warm-up. |
| Older and weak (age 12, P6) | 1.7 / 1.9 / 0.1 | 7% | 56% | 37% | Mostly. |
| Rusher / guesser | 2.2 / 2.5 / 0.2 | 20% | 60% | 20% | Cannot tell "cannot" from "did not check"; the unscored "How did you start?" box helps a tutor but is not in the rule. |

**(c) Cut scores and the warm-up.** Six main marks, cut at 4: a child who gets each main question right with probability 0.6 is told "join" 54%, "chat" 41%, "down" 4%; at 0.7 it is 74% / 24% / 1%; at 0.8 it is 90% / 10% / 0%. The cut is still noisy (same band on two sittings: 47% at p = 0.6) but the errors now fall into the soft middle, and the step-down is rare for anyone above p = 0.5. Warm-up questions are genuinely from the level below (W1, W2, W3, W4 are P4 content). The warm-up still does no work except in the 2-3 row. Guessing cannot place anyone (open answers).

**(d) Wording.** Child sheet: "This is a friendly check, not a test", "Not learnt it yet? ... tick", stretchers "meant to be tricky, most children will not finish": good. Result page: "Found it hard? That is useful to know, and it says nothing about how clever your child is" (better than "failure", still frames the card as "found it hard"); "Finding it easy?" replaces "Strong?"; the 0-1 row keeps "a confident start matters more than a fast one" (a line that can read as "your child is not confident"). Nothing tells the parent not to mark in front of the child. The answer key is now a separate PDF (good) but says "Questions the child ticked 'not learnt yet' score 0 but ... do not count against the child", which contradicts a rule that counts the score. The sheet gives no time guidance ("stop when time is up").

**(e) Recommended changes** are in section C.4 below.

---

# PHASE 2 (COMPARE): against the baselines
Baselines opened only now: `gifted_p5.md` (original, pre-fix), `gifted_fixes_p5.md` (the "after" estimate: criteria 6 and 9 only), `journey_p5.md` (original heatmap; written after the close-gaps additions and before the journey fix pass), `fixpass_p5.md`, `close_gaps_p5.md`, `fixes_p5.md`.

## C.1 Rubric per lesson: before / earlier-claimed-after / re-audit now

| Lesson | Before | Claimed after | Re-audit now | Delta vs before | Delta vs claimed | Conservative (crit. 7, 11 at 1) |
|---|---|---|---|---|---|---|
| 1 Million Puzzles | 13 | 15 | 20 | +7 | +5 | 18 |
| 2 Fraction Feats | 14 | 16 | 20 | +6 | +4 | 18 |
| 3 Before and After | 15 | 16 | 21 | +6 | +5 | 19 |
| 4 Triangle Areas | 16 | 17 | 20 | +4 | +3 | 18 |
| 5 Volume Vault | 16 | 18 | 19 | +3 | +1 | 17 |
| 6 Rate Racers | 17 | 18 | 19 | +2 | +1 | 17 |
| 7 Percentage Puzzles | 15 | 17 | 21 | +6 | +4 | 19 |
| 8 Angle Chasers | 15 | 17 | 19 | +4 | +2 | 17 |
| 9 Pattern Generalisers | 16 | 18 | 21 | +5 | +3 | 19 |
| 10 Challenge Day | 18 | 19 | 22 | +4 | +3 | 20 |
| **Level mean** | **15.5** | **17.1** | **20.2** | **+4.7** | **+3.1** | **18.2** |

Bands (research note): 20-24 depth-oriented, 12-19 enrichment-flavoured with gaps. Now: four lessons at 19, one at 22 and five at 20 or 21 on my reading; all ten are in 17-20 on the conservative reading, so the level straddles the 19/20 line and I would not call it "genuinely depth-oriented" without the caveat.

**Per-criterion deltas (level mean, before -> now) and per lesson.**

| Criterion | Before | Now | Delta | Where it moved |
|---|---|---|---|---|
| 1 Low floor, high ceiling | 2.0 | 2.0 | +0.0 | unchanged (2 everywhere) |
| 2 Depth over speed | 1.0 | 1.0 | +0.0 | unchanged (1 everywhere) |
| 3 Abstraction | 1.5 | 1.8 | +0.3 | +1 in L1, L2, L3, L10; -1 in L5 (my reading: only a counting what-if) |
| 4 Justification | 1.9 | 1.9 | +0.0 | +1 L1; -1 L6 (no "explain" item in Q1-Q6) |
| 5 Multiple paths | 1.3 | 1.4 | +0.1 | +1 L4 (split v take-away compared), L7; -1 L6 |
| 6 Challenge ladder | 1.0 | 2.0 | +1.0 | +1 in all ten (claimed in the earlier fixes; credited) |
| 7 Student-led inquiry | 1.1 | 2.0 | +0.9 | +1 in nine lessons (talk rules, claim-testing talk; L10 already 2) |
| 8 Complexity / context | 1.3 | 1.0 | -0.3 | -1 in L4, L5, L8 (stricter than the earlier audit; no content removed) |
| 9 Creativity / posing | 0.4 | 1.3 | +0.9 | +1 in nine lessons; L3, L6, L10 now 2 (lesson extension plus Investigation what-if), the rest 1 because posing is bank-only |
| 10 Metacognition | 1.1 | 1.9 | +0.8 | +1 in eight lessons (reflection box); L6 stays 1, L10 already 2 |
| 11 Pacing flexibility | 1.0 | 2.0 | +1.0 | +1 in all ten (choice line, sneak-peek, page-2 menu) |
| 12 Extension w/o acceleration | 1.9 | 1.9 | +0.0 | unchanged; L7 stays 1 (P6 previews) |

The earlier fixes document claimed to raise criteria 6 and 9 only, and the criterion-6 and criterion-9 gains are real, but criterion 9 is smaller than it looks: posing items live in the question bank and the tutor extension, not on any printed page (printed posing: none; closest is Investigation "test two more pairs of your own", L7). Criteria 7, 10 and 11 rose because the journey fix pass added the choice line, sneak-peek, talk rules and the reflection box; these were never rescored in the logs, so "claimed after" understates the structural gain and my 20.2 is mostly that. Criteria 2 (depth over speed) and 8 (context) did not move, and 8 is lower in three lessons on my stricter reading.

## C.2 Journey: heatmap before -> now (mean of six, Fit converted)

| Lesson | LOW | MIDDLE | HIGH | Lesson mean |
|---|---|---|---|---|
| 1 Million Puzzles | 3.00 -> 3.33 | 4.17 -> 4.33 | 3.50 -> 4.00 | 3.56 -> 3.89 |
| 2 Fraction Feats | 2.67 -> 3.17 | 4.00 -> 4.33 | 3.67 -> 4.50 | 3.44 -> 4.00 |
| 3 Before and After | 2.00 -> 3.17 | 3.17 -> 4.00 | 4.00 -> 4.33 | 3.06 -> 3.83 |
| 4 Triangle Areas | 3.50 -> 4.17 | 4.50 -> 4.50 | 3.67 -> 4.00 | 3.89 -> 4.22 |
| 5 Volume Vault | 3.00 -> 3.33 | 4.17 -> 4.50 | 3.83 -> 4.33 | 3.67 -> 4.06 |
| 6 Rate Racers | 2.17 -> 2.67 | 3.67 -> 4.00 | 3.83 -> 4.33 | 3.22 -> 3.67 |
| 7 Percentage Puzzles | 3.50 -> 3.50 | 4.67 -> 4.67 | 3.83 -> 4.50 | 4.00 -> 4.22 |
| 8 Angle Chasers | 2.83 -> 3.00 | 4.00 -> 4.00 | 4.00 -> 4.67 | 3.61 -> 3.89 |
| 9 Pattern Generalisers | 3.33 -> 4.00 | 4.17 -> 4.50 | 4.33 -> 4.50 | 3.94 -> 4.33 |
| 10 Challenge Day | 3.00 -> 3.33 | 4.17 -> 4.50 | 4.33 -> 4.67 | 3.83 -> 4.17 |
| **Level mean** | **2.90 -> 3.37** | **4.07 -> 4.33** | **3.90 -> 4.38** | **3.62 -> 4.03** |

**Six dimensions, level means before -> now (Fit shown as fit quality; raw Fit in brackets).**

| Persona | Participate | Fit quality (raw) | Fun | Confidence | Motivation | Social / online |
|---|---|---|---|---|---|---|
| LOW | 3.2 -> 4.0 | 2.6 -> 3.4 (1.8 -> 2.2) | 3.5 -> 3.5 | 2.8 -> 2.9 | 2.7 -> 2.9 | 2.6 -> 3.5 |
| MIDDLE | 4.1 -> 4.7 | 4.6 -> 5.0 (2.8 -> 3.0) | 4.3 -> 4.5 | 3.7 -> 3.7 | 3.9 -> 4.1 | 3.8 -> 4.0 |
| HIGH | 4.5 -> 5.0 | 3.4 -> 4.4 (3.8 -> 3.3) | 4.2 -> 4.5 | 4.2 -> 4.2 | 4.1 -> 4.2 | 3.0 -> 4.0 |

Reading it: the LOW child gains most where the fix pass aimed (Participate 3.2 -> 4.0, Fit 2.6 -> 3.4, Social 2.6 -> 3.5; weakest cells L3 2.00 -> 3.17 and L6 2.17 -> 2.67) but Confidence (2.8 -> 2.9) and Motivation (2.7 -> 2.9) hardly moved: the printed Start-here pages are still hard for her in L3, L5, L6, L7, L8. The HIGH child gains in Social (3.0 -> 4.0, the fast-track isolation is gone) and Fit (raw 3.8 -> 3.3), but still waits for the group in the first 45 minutes. MIDDLE was already well served (4.07 -> 4.33). Without the Fit conversion the level means are LOW 2.77 -> 3.17, MIDDLE 3.77 -> 4.00, HIGH 3.97 -> 4.20, so about half of the HIGH and MIDDLE gain is the conversion rewarding a "just right" fit; the LOW gain (+0.4 to +0.5) is the more trustworthy number. The weakest cells now: L6 LOW 2.67, L8 LOW 3.00, L2 LOW 3.17, L3 LOW 3.17, L5 LOW 3.33 (the earlier 5 weakest were L3, L6, L2, L8, L10 LOW). Strongest now: L10 HIGH 4.67, L7 MIDDLE 4.67, L8 HIGH 4.67.

## C.3 Tier compliance, before vs now

| Basis | Core bank | Think harder bank | Challenge bank | Printed Start-here | All items |
|---|---|---|---|---|---|
| Before (earlier audit's rule, as found) | 29/60 (48%) | 73/80 (91%) | 72/90 (80%) | 44/55 (80%) | 218/285 (76%) |
| Now, same rule | 60/60 (100%) | 81/81 (100%) | 90/90 (100%) | 55/55 (100%) | 286/286 (100%) |
| Now, owner's strict principle (B = fail) | 58/60 (97%) | 72/81 (89%) | 88/90 (98%) | 25/55 (45%) | 243/286 (85%) |

The strict row has no "before" because the earlier audit did not measure it; the earlier bank Core violations were mostly strict-type (formula-first items), so the bank improvement is real and large (48% -> 97-100%). The printed Start-here pages are the same kind of content as before, with scaffolds added: the earlier audit counted scaffolded questions as compliant (80%), and so do I under that rule (100%), but eleven printed Start-here items still need the lesson's own method and nineteen more are borderline. By lesson (earlier rule, before -> strict now): L1 83% -> 86%, L2 66% -> 86%, L3 75% -> 89%, L4 68% -> 86%, L5 69% -> 86%, L6 76% -> 86%, L7 86% -> 71%, L8 68% -> 76%, L9 93% -> 89%, L10 83% -> 93% (columns not on the same rule; L7, L8 and L9 look worse only because the strict rule is harsher on their scaffolded workbook items).

## C.4 Diagnostic: were the earlier findings fixed?

| Earlier finding | Status now | Evidence |
|---|---|---|
| Noisy cut scores (8 items, join at 6, stretch counted) | **Partly fixed.** | Placement is on the 6 main marks; stretchers no longer move anyone across a line (`build_diag.py` table). Still a hard cut at 4 of 6 (p = 0.6 child: 54% join / 41% chat / 4% down); the middle row absorbs the noise. |
| Typical-for-age child told to go down (43%) | **Fixed.** | Level 4 recommendation 43% -> 3% (like-for-like table). |
| Younger strong child mis-placed (64% down) | **Mostly fixed.** | 64% -> 11% Level 4, 62% chat, 15% join, 10% join + try Level 6. The 0-1 row still sends 11% of them down regardless of 4/4 warm-up and "not learnt yet" ticks; the earlier recommendation (warm-up 3-4 gets a chat before any step down) was not adopted. |
| Rusher / guesser (82% down) | **Improved, not solved.** | 82% -> 27% Level 4; cannot separate "cannot" from "did not check". |
| Weak child | Sensitivity fell. | Level 4 recommendation 95% -> 39% (54% chat, 7% join): intended, but the row text "Level 5 with a little support suits many children" is generous for a child whose journey scores in L3, L6 and L8 are still 3.2 or below. |
| Older weak child | Sensitivity fell. | Level 4 79% -> 16%. |
| M6 invalid (quadrilateral sum) | **Fixed.** | M6 is now "isosceles apex 50 degrees" (65). |
| W3 too easy | **Fixed.** | "3/4 of 48" (36). |
| Discouraging wording ("failure", "Strong?") | **Mostly fixed.** | "Found it hard? ... says nothing about how clever"; "Finding it easy?". Residual: "a confident start matters more than a fast one"; no "do not mark in front of your child". |
| Stretchers unscored / "meant to be tricky" | **Fixed.** | Sheet text; tutor key shows "2 marks, optional". |
| "How did you start?" unscored lines (M2, M4) | **Fixed** | present on both. |
| Key printed with child sheet | **Fixed.** | Separate `Level5_Tutor_Key.pdf`; accepts 4.4 million. |
| Time guidance ("12 questions, stop when time is up") | **Not fixed.** | Sheet says only "About 30 minutes". |
| Key line "not learnt yet ... score 0 ... do not count against the child" | **New contradiction.** | The rule counts them. |

Like-for-like placement shares (earlier audit's per-item assumptions, new M6, current rule vs the old rule on the old items):

| Profile | BEFORE (old rule) | NOW (current rule) |
|---|---|---|
| Strong for age | P5 69%, P5 with support 20%, P5 + try P6 10%, P4 1% | Join 100% (75% also "try Level 6 check"), chat 1% |
| Typical for age | **P4 43%**, with support 41%, support or P4 8%, P5 7% | Join 60% (14% with try-up), chat 37%, **P4 3%** |
| Weak for age | P4 95% | P4 39%, chat 54%, join 7% |
| Younger and strong | P4 64%, with support 33%, P5 3% | **P4 11%**, chat 63%, join 25% |
| Older and weak | P4 79%, support or P4 11% | P4 16%, chat 61%, join 23% |
| Guesser / rusher | P4 82% | P4 27%, chat 60%, join 15% |

**Diagnostic verdict:** earlier "mostly" (typical children demoted 43%, younger strong 64%, noisy cut, "failure" wording); now **mostly yes**: it no longer demotes typical or younger strong children and places clearly weak ones in the soft row, but the soft row is wide (45-63% of every non-strong profile) and so the diagnostic mainly says "talk to us" for most children, and a few mechanical gaps remain (below).

**Recommended changes (exact text).**
1. 0-1 row: add "If the warm-up score was 3 or 4, or many questions were ticked 'not learnt yet', please book a free 10-minute chat before choosing Ages 9-11 (Level 4)."
2. Replace the 0-1 row's second sentence ("Ideas build step by step, and a confident start matters more than a fast one.") with "Ages 9-11 (Level 4) is likely to be the more comfortable start, because the ideas build step by step."
3. Under the result table: "Please do not mark in front of your child. Say 'Let's look at that together in class' rather than 'that's wrong'."
4. Child sheet intro: "There are 12 questions and about 30 minutes. Stop when time is up; questions you did not reach count as zero. If you finish early, check each answer a second way."
5. Tutor key last line: change to "Questions the child ticked 'not learnt yet' score 0 for the total, but the tutor should read them first: they show what to teach, not what the child cannot do."
6. Make the middle row text for a warm-up of 2 or less say "Ages 9-11 (Level 4) may suit better; a short chat will help decide" rather than "Level 5 ... suits many children".
7. Update `docs/levels_and_placement.md` to the 4-6 / 2-3 / 0-1 rule (it still says 70% / 40-69% / under 40%).

## C.5 REGRESSIONS and unfixed items

**Regressions (worse than before, or new defects introduced by the fix passes).**
1. **"After question 3 you may choose" misfires in L3, L4, L8, L9.** Page 1 holds only Q1-Q2 there, so the choice point is the first item on page 2, after a 4-minute check and 5 minutes of teaching. The old fast-track box at least sat on page 1. (workbook pages 8, 18, 38, 43 of the PDF; `p5/workbook_html.js` `choose()` is the same sentence for all lessons.)
2. **Diagnostic sensitivity for weaker children fell** (weak 95% -> 39% sent to Level 4; older weak 79% -> 16%) while LOW journey scores in L3, L6, L8 are still 2.7-3.2, so some weak children may now start in Level 5 where the Start-here pages are hard. A deliberate trade-off, but it is a loss of protection.
3. **New contradiction in the tutor key** ("not learnt yet" scores 0 but "does not count against the child").
4. **Load increased.** Student workbook 47 -> 57 pages, tutor guide 68 -> 86; 14 printed items per lesson. Not a score regression, but it works against criterion 2.
5. Rubric criterion 8 is lower in L4, L5, L8 (-1 each) and criterion 3/4/5 in L5/L6 (-1): all differences of reading, not content that was removed. I found no case where a fix removed something that was working.

**Logged as fixed but not (fully) true in the content.**
1. `gifted_fixes_p5.md`: "every lesson's tiers comply". True on the way-in rule; on the owner's principle 11 printed Start-here items still need the lesson's method and 19 more are borderline (section A.2).
2. `fixes_p5.md` item 12 (figures for Think harder items): admitted as partly applied; still no printed figures for L4 S2/S3, L8 S3/S4, L5 S1; only a line "Draw a big, neat diagram first".
3. `fixpass_p5.md` diagnostic list "changes needed in build_diag.py": the text fixes were made but the child-sheet intro (12 questions, stop when time is up), "do not mark in front of your child" and the warm-up 3-4 chat exception were not.
4. `fixpass_p5.md`: "every strong thinkers / early finishers / gifted label removed". True for the workbook, slides, guide; residual "Finished early?" on slide `p5l7-ws2`, and the parent pack's "Challenge Group for children who show the signs" and secure / developing / needs-help marks.
5. `close_gaps_p5.md` known small gap (check slides L1, L3-L6, L8, L10 have no drawn diagram) remains: only L2, L7, L9 have an svg.
6. Both the Think harder and Go further slides (`stretch`, `challenge`) print items that differ from the workbook's Think harder page (L1 slide uses bank S5-S7, the workbook S1-S4; L3, L5-L8 slide items exist nowhere else), so "Think harder" on the slide and in the book are different questions.

**Unfixed from the earlier audits.** Problem posing only in bank and tutor notes (not printed); depth over speed; duplicate question numbers (Q4-Q6); reading load top of the level (L5, L6); page-2 plan routes LOW to Q5 painted cubes (L5) and the car-park tariff (L6); sparse real-world / cross-subject complexity in L4 and L8; the Go further what-if on slides only; multiple solution paths mostly tutor-shown; the story material in `docs/stories/final_p5.*` is not wired into the lessons.

## C.6 Improvements that are real (with evidence)
1. **Bank Core is now low floor everywhere** (60/60; earlier 29/60). Examples: L4 C1 "On 1-cm grid paper draw a rectangle 6 cm by 4 cm. Cut it along a diagonal"; L8 C1 "tear off its three corners"; L5 C1 "Build a box 3 cubes long, 2 wide, 2 high"; L2 C1 "4 friends share 3 chocolate bars".
2. **An Investigation every child receives**, with an "Easy first step", on its own page in all ten lessons (workbook p5 of each lesson, 57-page PDF), first step done by the whole group in talk time (76-82). Earlier: only fast-track children reached it.
3. **Neutral choice instead of a fast track**: "Fast track", "Challenge (for strong thinkers)", "For early finishers" are gone (grep of workbook, tutor guide, all 10 decks; one residual in L7 ws2). The check is private and called a sneak-peek; talk rules ban cold-calling and tallies.
4. **Reflection is safe and present** in every lesson, with a "still stuck" tick and a pass. Earlier: only L10 recorded a strategy.
5. **One timeline** in deck, script, guide and workbook (identical rows in `data.js`, the guide PDF page 3 and the slide notes); checks now get 4 minutes; reflection gets 2.
6. **LOW entry points**: every lesson's first Start-here part is a win-sized item (10/10; earlier 8/10), L3 "Try $60 first", L6 whole-number Better Buy pair and "Start here $4.20 / 6", L8 "Angle BOC means ...", sentence frame and reasons strip, L10 logic grid first.
7. **Diagnostic**: invalid M6 and trivial W3 replaced; scoring on 6 main marks; stretchers optional; separate tutor key; "not learnt yet" tick; gentler result page. Typical children demoted 43% -> 3%.
8. **Answer keys hold up.** I brute-forced about 40 keys and claims (list below); no arithmetic error found.

**Keys and claims checked by brute force or exact arithmetic (all pass):** L1 Q3 riddle unique 7 253 609; L1 Q6 six numbers; L1 Q2 (9 865 320, 2 035 698, 5 986 320); L1 Go further Q6 6 953 487; L1 sneak puzzles (6973, 47); L2 unit-fraction decompositions (7/10, 9/20, 3/8 two ways, 2/3 one way, 5/12, 1 one way, 3/4 three ways); L2 telescoping 5/14, tank 54 l; L3 bank C2 eight ways and Investigation totals divisible by 3; L4 Investigation 3/3/4 triangles; L5 boxes of 48 (9), 64 (7), 60 (10), three-face product 60; L8 isosceles in tens (8) and 15s (5); L9 tickets 8, coins 14, quiz 5 wrong, diamond 61, 100th digit 5, 49 yellow beads; L10 coins (3, 6, 16), chairs unique, digit 4 count 15, 3-digit sum 5 count 15; L6 shop unit prices; L7 lamp shops $60 v $61.20; diagnostic answers 1/2, 0.4, 36, 77, 4 400 000, 60, 5, 10, 6, 65, 101, 162.

## C.7 Top remaining gaps
1. **Start-here pages are still the hardest part for the LOW child**: 11 method-dependent items and 19 borderline (L3, L5-L8 worst), 440-640 words per lesson on pages 1-2, page-2 plans that start on the hardest items (L5 Q5, L6 Q5). Fix: reorder so each page ends with its hardest item, give L8 Q3/Q4 and L3 Q2/Q5 a started model, move L5 Q5 and L6 Q5 out of the "start with" list.
2. **The choice line and the first 45 minutes for the HIGH child**: fix "After question 3" to "After question 2" where page 1 has two questions (L3, L4, L8, L9) or print Q3 on page 1; consider an optional Investigation step or what-if during the 4- and 5-minute group blocks.
3. **Problem posing and depth**: no printed posing prompt; add one "make up your own" line to each Go further page and one protected think-time block.
4. **Diagnostic**: apply the exact changes in C.4 (warm-up 3-4 chat exception, time guidance, no marking in front of the child, key contradiction), and reconcile the three descriptions of the placement rule.
5. **Consistency**: make the slide Think harder / Go further items match the printed pages (or label them as extra), renumber the printed pages (Think harder A1-A4, Go further B1-B3, Investigation C), print figures on the Think harder geometry items, and remove the last "Finished early?" and the "Challenge Group for children who show the signs" wording.
