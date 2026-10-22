# Re-audit: Math Inquirers Level 6 (ages 11-13, after the PSLE, maths plus Scratch bridge)

Date 2026-10-22. Read-only on content. Written: this file and `docs/audit/reaudit_p6.py` (all means, deltas, tier percentages and the placement scenarios; run `python3 docs/audit/reaudit_p6.py`).

## 0. Headline and how to read it

| Measure | Original (pre-fix) | Earlier "after" claim | Re-audit now |
|---|---|---|---|
| Gifted rubric, level mean /24 | 16.8 | 18.3 | **20.0** (lessons: 20, 19, 18, 20, 20, 20, 19, 21, 22, 21) |
| Journey mean LOW / MIDDLE / HIGH (of 5) | 2.78 / 3.87 / 4.05 | not claimed | **3.17 / 4.05 / 4.27** |
| Tier compliance, 289-item basis | 83% (240/289) | 100% | **95.7%** on the earlier lenient reading; **90.8%** strict. Question bank alone: 78.7% -> **97.2%** |
| Diagnostic | "Mostly no" (typical child sent down about 47%) | not claimed | **Mostly yes, with two open faults** (section 4) |

**Method and honesty about independence.**
- Phase 1 was blind: I read the rubric, the two brief templates and the CURRENT material (all ten `p6/content/lN.js` including real workbook text rendered through each `workbook()` function, `gaps.json`, qbank, scripts, deck data; slide HTML for L1, L4 and L8 in full and the check/go/stretch/exit/reflect slides, timing labels for all 10 decks; the rebuilt workbook, question bank and tutor guide PDFs as text; `diag/content/p6.json`, `diag/build_diag.py` and both diagnostic PDFs) before opening any earlier audit. I scored 10 lessons x 12 criteria, every bank and workbook item for tier compliance, and 10 lessons x 3 personas x 6 scores. Blind results: rubric mean **20.4**, journey LOW **3.30** / MID **4.03** / HIGH **4.35**, bank compliance **97.2%**, workbook 83.3% strict. Those first-run numbers are recorded in the header of `reaudit_p6.py`.
- Phase 2 I opened `gifted_p6.md`, `gifted_fixes_p6.md`, `journey_p6.md`, `fixpass_p6.md`, `close_gaps_p6.md`, `fixes_p6.md`. **I then revised some cells** so that my own standard was applied the same way in every lesson (rubric: C2 for L6 and L10, C3 for L5/L6/L10, C4 for L8, C5 for L8, C8 for L7, C12 for L1/L2/L6; journey: about 25 cells, mostly difficulty fit and social). The revisions moved the totals by -0.4 on the rubric and -0.13 / +0.02 / -0.08 on the personas, mostly toward the baseline, so some anchoring cannot be excluded. The revised values are the ones reported; the blind values are given above so a reader can see the size of the adjustment.
- **Desk reviews by a model, no real children.** Every persona score and every diagnostic probability is judgement. Treat differences under about 0.5 on a persona mean, or 1 point on a lesson rubric total, as noise.

**Where the two audits differ in strictness (do not over-read the deltas).**
1. *Worksheet items.* The earlier gifted audit counted a printed worksheet item as a violation only if a child "with no route in" could not start it and found none. I classify each "Start here" item against the owner's principle (approachable without prior teaching). The Start-here pages are post-teaching practice, so on that reading about a third of them are not low floor. I give both bases below.
2. *Criterion 12.* I apply the earlier standard (negative numbers, equations, probability, polygon angle sums, prime factorisation, the nth-term rule are lower-secondary procedures taught early, so 1) and score L1 one lower than the baseline did (the nth-term rule is an algebra preview).
3. *Criteria the later passes targeted* (6, 9, 10) are scored on what is actually in the workbook, deck or guide now. Criterion 11 stays at 1 (see 1.2): a child may go deeper, but nothing lets a child skip the teaching, and the sneak-peek is deliberately never recorded.
4. *Journey.* Same personas and the same direction of the fit scale as the earlier review (5 = just right; the note says too hard or too easy). The earlier review's lowest scores were driven by moments that were later removed (printed fast-track criterion, "for strong thinkers" label, race wording, cold calls). Those deltas are real. Difficulty fit and participation for the LOW child moved very little, and I say so.
5. *Diagnostic.* Per-question success rates are mine (stated in the script). To isolate the effect of the rule, I ran the OLD 8-item rule and the CURRENT rule on the same current questions and the same rates.

---

## 1. Phase 1 (blind): Instrument A, gifted rubric

### 1.1 Scores per lesson (12 criteria, 0/1/2)

| # | Criterion | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Low floor, high ceiling | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | Depth over speed | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 3 | Generalisation | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 |
| 4 | Justification | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 5 | Multiple solution paths | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 2 | 1 |
| 6 | Challenge ladder | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 7 | Student-led inquiry | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 8 | Complexity / context | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 2 |
| 9 | Creativity / problem posing | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 10 | Metacognition | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 11 | Pacing flexibility | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | Extension, not acceleration | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 |
| | **Total /24** | **20** | **19** | **18** | **20** | **20** | **20** | **19** | **21** | **22** | **21** |
| | Verdict (20-24 / 12-19) | depth-oriented, borderline | enrichment+ | enrichment+ | borderline | borderline | borderline | enrichment+ | depth-oriented | depth-oriented | depth-oriented |

### 1.2 One-line evidence per criterion and lesson

**Criteria that are the same routine in every lesson (evidence is shared; lesson-specific examples follow):**
- **C1 = 2 everywhere.** Each lesson has an access puzzle in the sneak-peek slide (`pNlK-check`, "try it with objects, a drawing or counting"), a pair task in Explore, a "Go further: a what-if" slide from minute 12 (`pNlK-go`), and a Finish-page Investigation with a "First step:" line and a model answer that lists what to look for and a stretch (`gaps.json` `inv.a`). The tutor guide states the expected range of answers.
- **C2 = 1 everywhere.** Start here has 6, 6, 7, 7, 6, 5, 5, 5, 6, 6 multi-part items (L1..L10) in a 40-72 minute window with three to four teaching slides inside it; "no racing, no points" and "explain" prompts soften it, but pace is still set by covering the set. Not 2 because there is no scheduled single long think (the 15-minute Explore is the longest).
- **C6 = 2 everywhere.** Neutral tiers "Start here / Think harder / Go further" with "After question N you may choose: carry on, or try Think harder" printed on page 1 (N = 3, 2, 3, 3, 3, 3, 2, 2, 4, 3), Go further what-if on a slide at minute 12, Investigation at any time; nobody waits (guide: "never announce who is on which page").
- **C7 = 2 everywhere.** Pair Explore (10-25), whiteboards held up together, Talk time (75-82) with volunteers first and sentence starters, circulate prompts ("Ask: ...") in every script; partner-led tasks in L4 (partner guesses the secret machine), L8 (swap coded names), L9 (class data hunt), L10 (showcase).
- **C9 = 2 everywhere.** Printed Go further has a make-up or what-if task in every lesson (L1 Q5 sequence puzzle, L2 "Who am I?", L3 temperature story, L5 "answer is exactly 24", L6 design a fair game, L7 design a star, L8 secret message, L9 "mean mystery", L10 mixed question); L4 posing is the secret machine in Explore plus the "find all machines" investigation.
- **C10 = 2 everywhere.** "Looking back" block on every Finish page (did well / hardest part / what helped, with ticks, "I am still stuck" and "pass"), a `reflect` slide at 86-88, and a guide line for strategy-based praise. One element of the Polya look-back is missing (see 5.1: "what I would try next" was dropped).
- **C11 = 1 everywhere.** A child can go deeper (Go further from min 12, Think harder after question N, Investigation any time), which is more than a fast-finisher bonus. But there is no route that skips the teaching: `teach1/we1/try1` (25-35) and one to three teaching slides inside the worksheet block (about 52-59) are for everyone, and the sneak-peek is explicitly "not a mark", so nothing is compacted.

**Lesson-specific evidence (C3, C4, C5, C8, C12):**

| L | C3 generalisation | C4 justification | C5 paths | C8 context | C12 beyond syllabus |
|---|---|---|---|---|---|
| 1 | 2: nth-term rule, "n-1 jumps", Investigation `(k-1)n+1` for any shape | 2: Q1a "Why not 4?", Q3c, Q6c; talk "Ali 307?" | 2: rule vs add 99 times vs code, "when is each better?" | 1: matchsticks, taxi, fence | 1: the nth-term rule is an algebra preview |
| 2 | 2: squares have an odd number of factors, "exactly 3 factors" (Q5b), lockers | 2: Q1b "Ali: 87 prime", Q4b "why 27 cannot", exit shows the test | 1: factor trees "whichever way", hand vs code not compared | 1: pure number theory, Euclid teaser | 1: primes and factorisation taught early; Goldbach and lockers are real depth |
| 3 | 1: rules for moving left/right and "a-b is the jump from b to a" are told; Investigation asks "what do you notice" only | 1: mostly computation; Q6 "find the bug"; no explain prompt on the Finish page | 1: number line only, "check by adding back" told | 2: Harbin, lift, diver, "no level 0" ambiguity trap | 1: negative numbers are next year's topic, concrete |
| 4 | 2: rules with n, Q7 trick explained with n, `3n+5` vs `3(n+2)` | 2: Q2c "can P and Q ever agree?", Q7c, talk Ravi vs Mei | 2: search (Q6) vs run backwards (Q3), compared in Talk | 1: taxi, ages | 1: equations are Sec 1 |
| 5 | 1: handshakes 7 and 45 point to a rule but nothing asks for n people | 2: Q4b "Ali: 7 x 6 = 42, what is wrong?", Investigation "none missing, none twice" | 2: list, tree, multiply, 4+3+2+1 vs 20/2, nested loop | 1: outfits, handshakes, dominoes | 2: combinatorics is outside primary content, done with multiplication only |
| 6 | 2: Investigation "two outcomes is always fair, test 3 games"; fair = same probability | 2: Q1d, Q2b "is her code broken?", Q4c fair? | 2: list 36 outcomes vs simulate 1000 | 1: games, spinners | 1: probability is next year's topic |
| 7 | 2: sides x turn = 360, n-sided rule (Q5b), Investigation table over t | 2: Q1b "Mei: 130 degrees", Q2a, talk inside vs outside | 1: one route (360/n); turn vs inside told | 1: turtle graphics, honeycomb | 1: polygon angle sums are lower-secondary |
| 8 | 2: Investigation (a) "is it always true that shifts a and 26-a undo each other?", Q5 shifts add | 2: Investigation (a) "Explain", Q5c "Why?", talk "why does 26 change nothing?" | 1: clock, formula and Scratch shown, not compared | 2: ciphers, calendar, history | 2: modular arithmetic is pure enrichment |
| 9 | 2: Investigation "what changes, what stays", C5 test Ali's three claims | 2: Q3 predict up/down/same, Q4e "is $22 fair?", C4 who would say "well paid" | 2: levelling vs total/n vs code; mean vs median | 2: pocket money, Singapore temperatures, misleading averages | 2: mean-as-balance and misleading averages stay inside primary content |
| 10 | 2: Q1b hexagon-chain rule, Investigation "why no term of 7n-3 is a multiple of 7" | 2: challenge-round points for answer, check, reason; showcase explains the maths | 1: maths-first vs code check, no contrast of solutions | 2: self-chosen puzzle program | 2: mixed review by building |

### 1.3 Tier compliance, current material

Classification rule: **compliant** = a child who has not yet learnt the topic can start it with objects, drawing, counting, guess-and-check, patterns or earlier skills, with all notation explained (Core / Start here); applies the idea taught in this lesson in a new setting (Think harder); needs mastery plus extension (Challenge). `~` = partial (half credit).

**Question bank (230 items = 6 Core + 8 Think harder + 9 Challenge per lesson): 223.5 / 230 = 97.2%.**

| L | Violations and partials | Reason |
|---|---|---|
| 1 | Core C5 `~`; Challenge X1 violation | C5 reads "repeat 3 [change n by 4]" with no gloss for a child who has never coded; X1 (squares, pattern 10 = 100) needs no sequence mastery, it is Core level |
| 2 | Challenge X1 violation | "Largest prime below 200" is one application of the taught test with more tests, no extension |
| 3 | Challenge X3, X4 violations | X3 (6 repeats of -30) and X4 (`-3-4` vs `-3-(-4)`) are single steps of the taught idea |
| 4 | Core C6 `~` | "ask ... answer" blocks used with only "* means x" explained |
| 5, 6, 8, 9 | none | |
| 7 | Core C2 `~` | "turn clockwise 60" symbol not glossed in the item |
| 10 | Challenge X4 violation | "50 as the sum of two primes" repeats the Lesson 2 Think harder idea once |

Per tier: Core 58.5/60 (97.5%), Think harder 80/80 (100%), Challenge 85/90 (94.4%).

**Printed workbook, Start here pages (59 items) = Core. Strict reading: 39 / 59 = 66%.** Think harder pages (40 items): 38.5 / 40 (three "moved" fourth items, L2 TH4, L5 TH4 and L6 TH4, are Challenge-level and sit one tier low: `~` each). Go further (30 items): 30 / 30.

| L | Start-here items | Credit | Compliant | Partial / violation (reason) |
|---|---|---|---|---|
| 1 | 6 | 2.5 | Q1 (table, objects), | Q2 and Q3 need the nth-term method (violation); Q4 `~` (trace is fine, (b) "repeat 100, explain" needs the rule); Q5 `~`, Q6 `~` (fill-in, but (b) uses the rule) |
| 2 | 6 | 4.5 | Q1, Q2, Q4, Q5 | Q3 `~` (trace is fine, "6 mod d" in the table header); Q6 violation (order six blocks using mod) |
| 3 | 7 | 6 | Q1, Q2, Q3, Q5, Q6 | Q4 `~` ((e) `5-(-3)` and (f) `-1-(-7)` need subtracting negatives); Q7 `~` |
| 4 | 7 | 6 | Q1 (first row is one-step), Q2, Q4, Q5, Q6 | Q3 `~` (equation form `7n+4=74`); Q7 `~` (letter algebra in (b)) |
| 5 | 6 | 5 | Q1-Q5 | Q6 violation (fill the `a < b` test of a nested loop) |
| 6 | 5 | 3 | Q3, Q4 | Q1 `~` ((c)(d) expected counts), Q2 `~`, Q5 violation (complete the doubles program) |
| 7 | 5 | 1 | | Q1 `~` (one example row given, but backwards rows need `180 - inside`); Q2, Q4, Q5 violations (the star formula and angle sum are the taught method); Q3 `~` |
| 8 | 5 | 3 | Q2 (formula and strip on the page), Q3 | Q1 `~` ((d)(e) need mod), Q4 `~`, Q5 violation (combine shifts on a 26 clock) |
| 9 | 6 | 4.5 | Q1, Q3, Q5 | Q2 `~` (mean back to total is the lesson), Q4 `~` (median, mode used before being defined on the page), Q6 `~` |
| 10 | 6 | 3.5 | Q1 | Q2-Q6 `~` (review items that need earlier lessons; fair for Lesson 10, not a low floor) |

**Totals on the 289-item basis (230 bank + 59 Start-here, as in `gifted_p6.md`):**

| L | Before (original) | Now, lenient worksheet reading | Now, strict worksheet reading |
|---|---|---|---|
| 1 | 83% | 88% | 83% |
| 2 | 83% | 97% | 91% |
| 3 | 80% | 93% | 90% |
| 4 | 90% | 98% | 95% |
| 5 | 93% | 100% | 97% |
| 6 | 75% | 100% | 93% |
| 7 | 71% | 88% | 84% |
| 8 | 86% | 96% | 93% |
| 9 | 79% | 100% | 95% |
| 10 | 90% | 97% | 88% |
| **Level** | **83.0% (240/289)** | **95.7% (276.5/289)** | **90.8% (262.5/289)** |

"Lenient" counts six Start-here violations (L1 Q2, Q3; L7 Q2, Q4, Q5; L8 Q5) and treats the rest as the earlier audit did.

---

## 2. Phase 1 (blind): Instrument B, student journey

Method: I walked the slide order and minute labels of every deck (`check` 2-5, `warm1` 5-8, `warm2` 8-10, `explore1` 10-25, `go` from 12, `teach` 25-35, `break` 35-40, `ws1/ws2` 40-72, `ws2ans` 72-75, `talk` 75-82, `exit` 82-86, `reflect` 86-88; L10 has its own plan), the tutor script, and the printed workbook (Lesson N: Start here pages 5N-2 and 5N-1, Finish page 5N, Think harder 5N+1, Go further 5N+2). Scores are P / D / F / C / M / S = participate / difficulty fit (5 = just right; H = too hard, E = too easy) / fun / confidence / motivation / social-online.

Start-here text load (words, including the optional Python box): 304, 294, 272, 245, 285, 309, 336, 451, 429, 380 for L1..L10. Think harder items are 50-124 words per lesson.

### 2.1 Per lesson

**L1 Code the Pattern**
- LOW 4 2 3 3 3 3 (3.00). Wins: `check` puzzle 1 (draw 4 triangles, 9 sticks), wb p3 Q1 table with the first cell given, Q4 trace table. Lost: wb Q2/Q3 need the nth-term rule (H); first-ever loop and variable in Scratch at `explore1` with no starter file or pre-lesson handout in the repo; `teachtrace/teachplan/teachbug` (56-59) are three teaching slides before page 4 Q4-Q6.
- MID 5 4 4 4 4 4 (4.17). `explore1` "predict pattern 100, do not build it"; `we1/try1` on whiteboards; Q1-Q3 fit; papers held to camera together.
- HIGH 5 3 4 4 4 4 (4.00). `go` (squares, 31 sticks) from min 12, Think harder Q1-Q4, Go further Q6 "in BOTH sequences" fit; still waits through `teach1/we1/try1` (25-30) and `teachwhich/trywhich` (40-44) on `3n+2`; Think harder and Go further slides carry the label 40-72 with no check-together slot.

**L2 Prime Hunters**
- LOW 4 2 3 3 3 3 (3.00). Win: sieve on the 1-100 grid (`explore1`), factor-pair hunt with no race (`warm1`). Lost: Q1 needs quick factor facts for 28 and 51; Q3 header "6 mod d" is unexplained notation on the page; Q6 orders six blocks with mod (H); ws2 holds Q3-Q6 in 61-72.
- MID 5 3 4 4 4 4 (4.00). "91 looks prime" (`teach1`) is a real reveal; Q3 and Q6 are the hard moments.
- HIGH 5 3 4 4 5 4 (4.17). "Why stop at 7?" (`explore2`), Think harder Q2-Q3, and the Finish-page Investigation ("two primes never add to a prime?") are the best items in the level; `teach1`-`we3` (25-35) is known material.

**L3 Below Zero**
- LOW 5 3 4 3 3 4 (3.67). Best-pitched lesson: `warm1` city line-up, p13 Q1 read A, B, C off the line (a win in the first 3 minutes), Q2 Harbin counting, Q6 "find Siti's bug" normalises error. Lost: Q4 (e)(f) double negatives with no scaffold (slightly H); the sneak-peek freezer/fridge puzzle is public.
- MID 5 4 4 4 4 4 (4.17). Number line plus "split the jump at 0"; every question has a context.
- HIGH 5 3 4 4 4 4 (4.00). Core is E; Think harder Q1-Q4 and Go further Q6 (lifts) fit; magic grid (Challenge 1) is fun.

**L4 Algebra Machines**
- LOW 4 2 3 3 3 3 (3.00). `warm1` tutor-as-machine is safe (call any number); wb Q1 now opens with a one-step row. Lost: `explore1` needs nested reporter blocks and the notes say the tutor sends a `Machine.sb3` that is not in the repo; Q3 `7n+4=74` is equation notation; Q7 trick needs `2n+10` (H).
- MID 5 3 4 4 4 4 (4.00). Guess-my-rule in pairs is fun; Q2 "same steps, different order" is the aha; Q3 and Q7 are heavy.
- HIGH 5 3 5 4 5 4 (4.33). Secret machine design, Think harder Q3 (both machines agree), Investigation "find all machines for IN 4, OUT 17"; waits through the 25-35 teach.

**L5 Every Possible Way**
- LOW 4 3 4 3 3 3 (3.33). Bubble-tea list on paper first (`explore1`), Q1 outfits, Q2 digit cards, Q5 grid with the add-up rule given are wins. Lost: Q3 nested-loop trace and Q6 `a < b` plan; the "Every Order" starter is not in the repo.
- MID 5 3 5 4 4 4 (4.17). Handshake "is 5 x 5 right?" is the high point; Q3 trace is the one hard moment.
- HIGH 5 3 5 4 5 4 (4.33). Think harder Q2-Q3, Go further dominoes, Investigation (50c coins, find all); Core is E.

**L6 Fair or Unfair?**
- LOW 4 2 4 3 3 4 (3.33). Dice Race is a real game with a surprise; no timer now; Q1 has the "random is not exact" hint; difference table rows 1-2 prefilled. Lost: Q1 (c)(d) expected counts, Q5 plan the doubles program (H).
- MID 5 4 5 4 4 4 (4.33). Predict, play 20 rounds, pool the group's tallies, explain with 36 outcomes is the best arc in the level.
- HIGH 5 4 5 4 5 4 (4.50). "Two outcomes is always fair?" investigation, Go further Q2-Q3, what-if (A wins on 2-6) from min 12.

**L7 Turtle Geometry**
- LOW 3 2 3 2 3 3 (2.67). Wins: `warm1` "use your arm as the turtle's nose", the vocabulary box at the top of page 1, trace rows prefilled, setup now 2 steps. Lost: nothing in Start here is a low-floor entry (0 of 5 fully compliant): Q1 six-row table forwards and backwards, Q2 buggy nonagon, Q4 star formula "turn = 360 x times round / points"; 336 words; Pen extension and turn blocks without a starter file (H).
- MID 4 3 4 3 4 4 (3.67). Drawing is satisfying, "predict then run" for pentagon and hexagon; page 2 is tight.
- HIGH 5 4 5 4 5 4 (4.50). Stars and rosettes; Go further Q5 "p and k share no common factor" is excellent; Investigation table over t.

**L8 Secret Codes**
- LOW 4 2 4 3 3 3 (3.17). Wins: `warm1` clock jumps, code-strip Explore (names), printed letter-number strip, Q2 formula given. Lost: wrap past 25 and below 0; Q3 `(n+5) mod 26`; Q5 two shifts on a 26 clock (H); longest Start-here text in the level (451 words, with a greyed Python corner).
- MID 5 3 5 4 4 4 (4.17). "What happens to X, Y, Z?" and "which 3-letter word appears twice" are detective moments.
- HIGH 5 4 5 4 5 4 (4.50). Crack the code (Q4), Think harder Q4, Go further Q1 "write a message and explain how a friend could crack it", Investigation "which shift is its own decoder".

**L9 Data Detectives**
- LOW 4 4 3 4 3 4 (3.67). Familiar PSLE content: Q1 (4, 7, 2, 8, 9) is a sure win; the "even your PSLE results" phrase is gone from the hook; Q4 gives the total ($154). Lost: Q4 `154 / 7` still needs division; lists in Scratch are new; 429 words.
- MID 5 4 4 4 4 4 (4.17). Quick-eye estimate; misleading mean in Q4 ($22 vs median $15).
- HIGH 5 3 3 4 4 4 (3.83). The first 40 minutes (`warm1`, `we1`, `we2`, ws1 Q1-Q3) are PSLE revision (E); value is median/mode, lists, Challenge C4/C5, "change two numbers, keep the mean". Still the highest boredom risk in the level.

**L10 Showcase Challenge**
- LOW 3 2 3 3 3 3 (2.83). Wins: relay by volunteers and "pass is always fine" (`warm1`), each team keeps its own score, "a working copy of one starter with one change is full marks", screenshot option, "two stars and a question". Lost: Start here is six mixed review puzzles (380 words); the showcase is still expected of everyone (2:30 in front of seven peers); starters A-D are not in the repo.
- MID 4 3 4 4 4 3 (3.67). Challenge round with answer/check/reason points gives structure; starter plus one twist is a sensible target.
- HIGH 5 4 5 4 5 4 (4.50). Building and presenting his own puzzle; two rounds of four so nobody waits more than about 12 minutes.

### 2.2 Concrete moments flagged (current)

| Where | Who | Flag |
|---|---|---|
| All lessons, `check` min 2-5 | LOW, MID | Public: answers are held to the camera "at the same moment" for a puzzle on an idea not yet taught. Softened ("nobody is marked", "I do not know is welcome", "never read wrong answers aloud") but a wrong answer is still seen by seven others. |
| L1 `explore1`, L4 `explore1`, L5, L7, L8, L9, L10 | LOW | Lost: Scratch tasks need a starter project or handout; none exists in the repo (`find . -name "*.sb3"` returns nothing; `fixes_p6.md` item 7 and 15 say "NOT done"). |
| L7 wb Start here | LOW, MID | Lost / rushed: no low-floor entry; formula and angle sum are the taught method; 336 words. |
| L8 wb Start here (451 words), L9 (429), L10 (380) | LOW | Reading load, even with the Python corner greyed. |
| L1, L2, L5, L6, L8 Start here Q-N choice point | all | Fine, but the Think harder and Go further slides are labelled 40-72, the same minutes as ws1/ws2, so a child who chooses them has no check-together slot while the tutor teaches the main pages. |
| L10 showcase | LOW | Exposed: presenting is expected of everyone; the options (screenshot, plan-only) are in the guide, not on the child's page. |
| L3 Q4 (e)(f) | LOW | Unscaffolded double negatives. |

### 2.3 Heatmap, current (mean of the six)

| Lesson | LOW | MID | HIGH | Lesson mean |
|---|---|---|---|---|
| 1 | 3.00 | 4.17 | 4.00 | 3.72 |
| 2 | 3.00 | 4.00 | 4.17 | 3.72 |
| 3 | 3.67 | 4.17 | 4.00 | 3.94 |
| 4 | 3.00 | 4.00 | 4.33 | 3.78 |
| 5 | 3.33 | 4.17 | 4.33 | 3.94 |
| 6 | 3.33 | 4.33 | 4.50 | 4.06 |
| 7 | **2.67** | 3.67 | 4.50 | 3.61 |
| 8 | 3.17 | 4.17 | 4.50 | 3.94 |
| 9 | 3.67 | 4.17 | 3.83 | 3.89 |
| 10 | 2.83 | 3.67 | 4.50 | 3.67 |
| **Level** | **3.17** | **4.05** | **4.27** | 3.83 |

---

## 3. Phase 1 (blind): Part 2, the diagnostic

Current rule, from `diag/build_diag.py` (page 3 of the child PDF, `outputs/diagnostics/Math_Inquirers_Level6_Placement_Check.pdf`): **Main questions (6) decide**: 4-6 join Level 6; 2-3 "a short chat with a tutor and the free taster" (Level 6 with a little support; if warm-up is 2 or less, Level 5 "may be more comfortable"); 0-1 "we suggest Ages 10-12 (Level 5)". The 4 warm-up items decide nothing except that hint; the 2 Brain stretchers are unscored flags and, for Level 6, point nowhere (no level above).

**Questions (answers re-derived and all 12 correct in the script).**

| # | Item | Skill and school year (my belief) | Fair at 11-13? |
|---|---|---|---|
| W1 | every factor of 24 | factor pairs, P4-P5; all 8 needed | yes; all-or-nothing marking is harsh |
| W2 | 6/36 simplest form | P4-P5 (Level 5 L2) | yes |
| W3 | triangle 52 + 63 | angle sum, P4-P5 (Level 5 L8) | yes |
| W4 | read a loop, n = 17 | loop reading, not taught in Level 5 (coding starts in Level 6) | yes in prose, but not "from the level below"; the key says "not a mark against the child" while it is one of the four warm-up marks |
| M5 | doubles then +5, out 31 | work backwards, P5-P6 | yes |
| M6 | primes between 30 and 50 | prime defined in the item; scan and test 49 | yes |
| M7 | -4 +9 -12 | negatives across zero | yes (context) |
| M8 | NOT green, 4R 3B 5G | probability defined as "3 out of 12"; simplest form | yes |
| M9 | average of 5 is 12, find the fifth | average, P5-P6 | yes ("mean" is now "average") |
| M10 | 10 o'clock + 17 hours | clock wrap | yes |
| S11 | 50th term of 4, 7, 10, 13 | Lesson 1 skill, explanation asked | good discriminator |
| S12 | 3-digit even numbers from 1-4 | Lesson 5 skill | good discriminator |

The scored items still map one-to-one to lessons 1-8 (S11 L1, M6 L2, M7 L3, M5 L4, S12 L5, M8 L6, M10 L8, M9 L9); the difference from before is that each is now self-contained, so a "no" means "had not seen it" less often.

Six pretend children on the current rule (rates in `reaudit_p6.py`, `PROF2`; P(join) / P(chat) / P(down)):

| Child | OLD 8-item rule on today's questions (P suggested Level 5) | CURRENT rule: join / chat / down | Right outcome | Verdict now |
|---|---|---|---|---|
| Strong for age (12) | 0.84 join, 0.01 | 0.98 / 0.02 / 0.00 | join Level 6 | right; no level above exists |
| Typical for age (12) | 0.11 join, **0.43** | 0.54 / 0.42 / 0.04 (L5 down or hinted 0.09) | join Level 6 | right in a plain sense, but 42% are told to book a chat |
| Weak for age (12) | 0.00 join, 0.99 | 0.05 / 0.47 / 0.48 (L5 down or hinted 0.85) | Level 6 with support, or taster first | defensible; chat band is the right idea |
| Younger but strong (11) | 0.49 join, 0.14 | 0.81 / 0.19 / 0.01 | join Level 6 | right (warm-up items are no longer P6 topics) |
| Older but weak (13) | 0.01 join, 0.90 | 0.20 / 0.60 / 0.20 (L5 down or hinted 0.58) | Level 6 with support | wrong 58% of the time: Level 5 is "Ages 10-12" and the page does not mention the age mismatch |
| Guesser / rusher (capable) | 0.05 join, 0.77 | 0.27 / 0.58 / 0.15 (L5 down or hinted 0.45) | join Level 6 | still mis-read 45% of the time; no "check your answers" prompt and the key's "common error" column is the careless slip |
| Pure guesser | 0.00, 1.00 | 0.00 / 0.02 / 0.98 | not ready | right |

Cut-score noise with six deciding items (true per-item rate p; P(join) / P(chat) / P(down)): p 0.5: 0.34 / 0.55 / 0.11; p 0.6: 0.54 / 0.42 / 0.04; p 0.7: 0.74 / 0.25 / 0.01; p 0.8: 0.90 / 0.10 / 0.00. One question still moves the recommendation, but a wrong band now costs a chat, not a move down, except at 0-1.

Wording: "friendly check, not a test", a "not learnt yet" tick box on every question, the stretchers described as "meant to be tricky, most children will not finish them", "Found it hard? ... says nothing about how clever your child is", "You make the final choice ... change level free of charge before lesson 1", no word "failure". Faults: the "Skills covered" list (Primes, Negative numbers, Probability ...) is still printed on the parent page next to the score with no "ideas you will meet" framing; the key still says "for example 2.05 and $2.05" (copied from another level); the header "Open to a year either side" remains; the 0-1 row offers only "Level 5".

---

## 4. Phase 2 (compare)

### 4.1 Rubric per lesson: before / earlier "after" claim / now

| L | Before | Claimed after | Now | Per-criterion deltas, now vs before (name +/-) |
|---|---|---|---|---|
| 1 Code the Pattern | 18 | 20 | **20** | Ladder +1, Posing +1, Metacognition +1, Beyond -1 |
| 2 Prime Hunters | 15 | 17 | **19** | Ladder +1, Posing +2, Metacognition +1 |
| 3 Below Zero | 13 | 16 | **18** | LFHC +1, Ladder +1, Posing +2, Metacognition +1 |
| 4 Algebra Machines | 19 | 19 | **20** | Metacognition +1 |
| 5 Every Possible Way | 18 | 18 | **20** | Posing +1, Metacognition +1 |
| 6 Fair or Unfair? | 16 | 18 | **20** | Generalisation +1, Ladder +1, Posing +1, Metacognition +1 |
| 7 Turtle Geometry | 16 | 18 | **19** | Ladder +1, Posing +1, Metacognition +1 |
| 8 Secret Codes | 15 | 17 | **21** | Generalisation +1, Justification +1, Ladder +1, Posing +2, Metacognition +1 |
| 9 Data Detectives | 18 | 20 | **22** | Generalisation +1, Ladder +1, Posing +1, Metacognition +1 |
| 10 Showcase | 20 | 20 | **21** | Generalisation +1 |
| **Level mean** | **16.8** | **18.3** | **20.0** | |

Criterion means before -> now: Ladder 1.3 -> 2.0, Posing 0.9 -> 2.0, Metacognition 1.1 -> 2.0, Generalisation 1.4 -> 1.8, LFHC 1.9 -> 2.0, Justification 1.8 -> 1.9, Beyond 1.5 -> 1.4; unchanged: Depth 1.0, Multiple paths 1.5, Inquiry 2.0, Complexity 1.4, Pacing 1.0.

Reading: the gain over the earlier claim (+1.7) comes from the two later passes (the Investigation and what-if items, and Looking back), which the 18.3 estimate pre-dated. The three gaps the original audit named as "still open" are now: metacognition closed (1 -> 2), pacing unchanged (1), beyond-syllabus unchanged (I score 1 in L1, L2, L3, L4, L6 and L7, 2 in the other four). Depth over speed (all 1) is also unchanged.

### 4.2 Journey: heatmap before vs now, and the six dimensions

| Lesson | LOW before -> now | MID before -> now | HIGH before -> now |
|---|---|---|---|
| 1 | 2.67 -> 3.00 | 3.67 -> 4.17 | 3.83 -> 4.00 |
| 2 | 2.50 -> 3.00 | 3.50 -> 4.00 | 4.00 -> 4.17 |
| 3 | 3.33 -> 3.67 | 4.17 -> 4.17 | 3.83 -> 4.00 |
| 4 | 2.50 -> 3.00 | 3.67 -> 4.00 | 4.00 -> 4.33 |
| 5 | 3.00 -> 3.33 | 4.00 -> 4.17 | 4.17 -> 4.33 |
| 6 | 3.00 -> 3.33 | 4.33 -> 4.33 | 4.33 -> 4.50 |
| 7 | 2.17 -> 2.67 | 3.50 -> 3.67 | 4.33 -> 4.50 |
| 8 | 3.00 -> 3.17 | 4.17 -> 4.17 | 4.50 -> 4.50 |
| 9 | 3.33 -> 3.67 | 4.17 -> 4.17 | 3.33 -> 3.83 |
| 10 | 2.33 -> 2.83 | 3.50 -> 3.67 | 4.17 -> 4.50 |
| **Mean** | **2.78 -> 3.17** | **3.87 -> 4.05** | **4.05 -> 4.27** |

Six dimensions, level mean (P / D / F / C / M / S):

| Persona | Before | Now |
|---|---|---|
| LOW | 3.3 / 2.2 / 3.4 / 2.4 / 3.0 / 2.4 | 3.9 / 2.4 / 3.4 / 3.0 / 3.0 / 3.3 |
| MIDDLE | 4.2 / 3.4 / 4.3 / 3.5 / 4.1 / 3.7 | 4.8 / 3.4 / 4.3 / 3.9 / 4.0 / 3.9 |
| HIGH | 4.9 / 3.1 / 4.4 / 4.0 / 4.3 / 3.6 | 5.0 / 3.4 / 4.5 / 4.0 / 4.7 / 4.0 |

What moved and what did not: LOW gains are in confidence (+0.6), social/online (+0.9) and participation (+0.6), which match removed mechanisms (printed fast-track criterion, "for strong thinkers" label, race wording, cold-called relay, public tally, the PSLE phrase, the "you you" typo, the reflection box moved to a page every child reaches). **LOW difficulty fit hardly moved (2.2 -> 2.4) and LOW motivation and fun did not move (3.0, 3.4).** HIGH gains are in motivation (+0.4: Go further from minute 12, Investigation, showcase rounds) and social (+0.4); HIGH fit moved only 3.1 -> 3.4 because the 25-35 teach block is unchanged. The weakest cell is still LOW in Lesson 7 (2.17 -> 2.67); the five weakest are now LOW L7, LOW L10, then LOW L1, L2 and L4 at 3.00. The strongest are HIGH L6, L7, L8 and L10 (4.50) and MID L6 (4.33).

### 4.3 Tier compliance before vs now

| Basis | Before | Claimed after | Now |
|---|---|---|---|
| Question bank (230 items) | 78.7% (181/230, "49 violations") | 100% | **97.2%** (223.5/230) |
| 289 items, earlier lenient worksheet reading | 83.0% | 100% | **95.7%** |
| 289 items, strict worksheet reading | not measured (worksheet counted 59/59) | | **90.8%** |
| Printed Start-here pages alone, strict | not measured | | **66%** (39/59) |

The earlier claim of 100% does not hold: five bank items are single-step Challenge items or Core-level items sitting in Challenge (L1 X1, L2 X1, L3 X3, X4, L10 X4) and three Core items still use unglossed code notation (L1 C5, L4 C6, L7 C2). L1 (83%) and L10 (88% strict) are at or below their original figure on the strict basis.

### 4.4 Diagnostic: did the earlier findings get fixed?

| Earlier finding | Status | Evidence |
|---|---|---|
| Scored items are a pre-test of the lessons ("exposure, not readiness") | **Largely fixed** | M6 defines prime, M8 defines probability and gives 3/12, M9 says "average", S11 is the Lesson 1 skill with an explanation asked; warm-up now tests factors, simplifying, angle sum and reading a loop. |
| Warm-up not from the level below; W4 speed was P6 content | **Mostly fixed** | W4 is gone; W1-W3 are P4-P5 and match Level 5 topics; the new W4 (loop) is a Level 6 coding readiness item, not a Level 5 topic. |
| Typical child sent down about half the time | **Fixed** | Same questions and rates: OLD rule sends 43% of typical children to Level 5; CURRENT sends 4% down, 9% down or hinted. Cost: 42% get "book a chat". |
| Younger-strong child mis-placed (1 in 5) | **Fixed** | 0.14 -> 0.03 on today's items. |
| Rusher placed as weak | **Not fixed** | 0.77 -> 0.45 hinted/down; nothing tells the child to check, and the key's "common error" column lists exactly the careless slips. |
| Older weak child offered an out-of-age level | **Not fixed** | 0.58 down or hinted; "Ages 10-12" is the only alternative on the page. |
| Noisy cut scores / warm-up should decide | **Not done** | `fixpass_p6.md` recorded "warm-up (4) decides" and put the table in `p6.json` `notes.placement`, then listed the build changes as "not made". The later unified build (`ab5b2e1`) made the 6 main questions decide for every level and ignores `notes.placement`, `mainNote`, `guideBox`, `topicsTitle`, `easyLine`, `keyFix`, `timeNote`, `childHeader`. Fewer deciding items (6 instead of 8), softened by a middle "chat" band. |
| Discouraging wording ("failure", "Not yet?") | **Fixed** | Replaced by "Found it hard? That is useful to know, and it says nothing about how clever your child is." |
| Answers in the child's PDF | **Fixed** | Separate `Math_Inquirers_Level6_Tutor_Key.pdf`. |
| Skills list read as a list of gaps; "$2.05" example; "a year either side" header | **Not fixed** | Still on the PDFs. |
| `docs/levels_and_placement.md` (70% / 40-69% / under 40%) disagrees with the shipped rule (4-6 / 2-3 / 0-1 of the main six, warm-up only a hint) | **New inconsistency** | Both exist. |

**Verdict now: mostly yes** (strong, typical, younger-strong and guesser children land where they should; weak, older-weak and rusher children are handled by a chat band that the page offers but does not explain for age or carelessness). Before: mostly no.

### 4.5 Regressions and unfixed items (claimed fixed in a log but not true, or worse than before)

**Regressions (worse than a previous state):**
1. **Looking back lost "what I would try next".** `close_gaps_p6.md` shipped three prompts ("hardest part", "I got unstuck by", "Next time I will try"); the fix pass replaced them with "did well / hardest part / what helped", which is kinder and safer but drops the one forward-looking element of a Polya look-back.
2. **Diagnostic: only 6 questions decide**, down from 8, and warm-up (the better readiness signal) decides nothing. Mitigated by the chat band, but the log's claim ("warm-up decides") is false in the shipped PDF.
3. **Tier compliance in L1 and L10 is at or below the original on the strict basis** (83% and 88% vs 83% and 90%): the Start-here pages are more teaching-dependent than the bank.
4. **Lesson 10 timing is now inconsistent in print:** deck `showcase` 62-85, `exit` 86-88, `reflect` 88-90 and "2 minutes 30 seconds each"; the tutor guide plan says "showcase 62 to 87 (3 minutes each plus a 20-second switch)" and "exit and certificates 87 to 90". Eight children at 3 min 20 s is 26.7 minutes in a 25-minute slot, the exact problem the earlier review flagged.

**Claimed in a log but not delivered or not true:**
5. **Starter `.sb3` projects and a pre-lesson Scratch handout** (`fixes_p6.md` items 7 and 15 "NOT done"; SPEC still says a 10-minute video or handout "is sent beforehand"): nothing in the repo; 7 of 10 lessons have a Scratch Explore.
6. **"100% tier compliance after the fixes"** (`gifted_p6.md`, `gifted_fixes_p6.md`): 97.2% on the bank, 90.8% strict overall (4.3).
7. **Check slide is only partly de-risked:** `close_gaps_p6.md` invited a fast-track child by private chat; `fixpass_p6.md` correctly removed that (safeguarding rule) and made the sneak-peek unmarked, but papers are still held to the camera for everyone at the same moment, so the "pre-test" feel remains for LOW.
8. **Diagnostic build changes** listed in `fixpass_p6.md` (headers, placement table from `notes`, `topicsTitle`, `easyLine`, `keyFix`, `timeNote`) were not made; the unified rule replaced them.
9. **Think harder / Go further slides** are now labelled 40-72, but that is the worksheet window, so a child who chooses them still gets no check-together slot (baseline item 21 closed on paper only).
10. **Naming:** question bank, taster and "What learners get" still say "Ages 11-13 (finishing P6)", while the diagnostics say "For children after the PSLE" and "Level 6".
11. **Stale content:** `diag/content/p6.json` `notes.placement` and `mainNote` describe a rule the PDF does not use.

### 4.6 Improvements that are real (with evidence)

1. **Core is genuinely low floor in the bank.** Tier violations in the bank fell from 49 to 5 full plus 3 partial. Examples in the text now: L2 Core defines prime and lists the primes; L3 Core starts "On a thermometer, 0 degrees C is where water freezes ... Draw a thermometer"; L6 Core "__ out of __"; L7 Core "A full turn on the spot is 360 degrees"; L8 Core shift-by-one code with the alphabet; L9 Core defines median and mode.
2. **Public labelling is gone.** No "Fast track", "for strong thinkers", "advanced", "top group" in the workbook, slides, scripts or guide; guide rule "never say advanced, top group, strong or early finisher"; printed page 1 reads "After question N you may choose: carry on, or try Think harder." Race and points wording is gone from every `warm1` (grep of content, generators, slides finds none); L6 timer removed; L10 relay by volunteers with "pass".
3. **Safe reflection.** "Nobody marks this. You can write pass", "I am still stuck (my tutor will check in during the lesson)", on the Finish page every child reaches; the "you you" typo is fixed.
4. **Problem posing and "what if" are in every lesson** (posing 0.9 -> 2.0): printed Go further tasks, the Investigation with a first step and a model answer, and the `go` slide at minute 12.
5. **Scaffolds for the LOW child where it counts:** L7 vocabulary box, prefilled trace rows, 2-step setup slide, "use your arm"; L4 one-step first row; L6 prefilled difference table rows and a hint for "362 reds"; L2 exit uses 111; L9 hook phrase removed; L3 "no level 0" note; L8 Python corner greyed and optional.
6. **Diagnostic is much fairer** (4.4): self-contained questions, readiness warm-up, "not learnt yet" tick, separate key, no discouraging box.
7. **Content accuracy holds.** I re-derived the 12 diagnostic answers and brute-forced a sample of Challenge answers across L2, L3, L5, L7, L8, L9 and L10 (`spot_checks()` in the script: L3 magic grid and lift, L5 648/252/70/14/28/15, L7 the 13 full turns and 12 repeats, L8 182, Friday/Saturday and shifts 3 and 16, L9 68 and 34, L10 33, 30 and 2027, L2 301 and the lockers). No error found; I did not check every one of the 230 bank answers.

### 4.7 Remaining gaps (in order of weight)

1. **Scratch dependency has no supply** (no starter files, no handout): the Explore and the code questions are the LOW child's hidden prerequisite in 7 lessons.
2. **Lesson 7 Start-here page** is still entirely post-teaching and 336 words; LOW 2.67, MID 3.67 are the lowest cells. Needs a one-step first row (for example "a turtle turns 90 four times: how many degrees?") before the table, and the star formula moved to Think harder.
3. **Pacing/compacting (criterion 11 = 1) and wait time for HIGH:** the 25-35 teach block and in-worksheet teaching slides are for everyone; Think harder and Go further have no check-together slot; Lesson 9 core is PSLE revision (HIGH fit 3).
4. **Diagnostic rule:** make the warm-up decide (the table already written in `p6.json` `notes.placement`), mention age ("Ages 10-12" is not right for a 13-year-old), add "check your answers" for careless children, retitle "Skills covered", fix the key example, and reconcile `docs/levels_and_placement.md`.
5. **Depth over speed and extension (criteria 2 and 12):** five to seven multi-part Start-here items in about 35 minutes in every lesson; six lessons teach lower-secondary procedures early, so "extends thinking beyond the syllabus" is not safe wording for P6.

Also open: Lesson 10 timing mismatch (guide vs deck), five bank items to retier (L1 X1, L2 X1, L3 X3 and X4, L10 X4), and the Start-here items listed as violations in 1.3.

### 4.8 Marketing language that is safe now

Same as the earlier verdict: "enrichment toward secondary maths and coding", "inspired by research-based approaches used in gifted education (low-floor tasks, Polya-style look-back, problem posing)", "open investigations with room to go further", "small groups with differentiated challenge". The question bank, taster and learner pages already say "not an official GEP standard and not affiliated with MOE". Not safe: "not a syllabus pre-teaching course", "extends thinking beyond the syllabus", anything implying identification or outcomes.

---

## 5. Ten-line summary

1. Rubric level mean: before 16.8, earlier claim 18.3, now **20.0** (blind 20.4); 7 of 10 lessons at 20 or more; weakest L3 (18).
2. Journey means: LOW 2.78 -> **3.17**, MIDDLE 3.87 -> **4.05**, HIGH 4.05 -> **4.27**.
3. Tier compliance: 83% -> **95.7%** (lenient) or **90.8%** (strict); question bank 78.7% -> 97.2%; the "100%" claim is not true.
4. Diagnostic: "mostly no" -> **mostly yes**, but the log's "warm-up decides" was never built.
5. Gaps: Scratch supply, L7 Start-here, pacing/HIGH wait, diagnostic rule and wording, depth/extension.
6. Regressions: Looking back lost "next time"; 6-question cut; L10 timing mismatch; L1/L10 strict compliance not above original.
