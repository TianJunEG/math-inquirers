# Independent re-audit: Math Inquirers Level 2 (Primary 2, ages 7-9)

Date 2026-10-22. READ-ONLY on content (only this file and `docs/audit/reaudit_p2.py` were written). Desk review by a model: no real children, no pilot data, no timing of a live lesson.

Process followed to limit anchoring:
- **Phase 1 (blind).** Scored the CURRENT material on instrument A (12-criterion gifted rubric, `docs/gifted_research.md` section 2, tier principle from `gifted_brief_template.txt` STEP 2) and instrument B (three personas x six scores, `journey_brief_template.txt` PART 1 and 2) before opening any earlier audit file. The Phase 1 numbers were written into `docs/audit/reaudit_p2.py` (the `NOW_A`, `NOW_B`, `TIER` blocks) before the baselines were opened; the BASE block at the bottom of that file was typed in afterwards.
- **Phase 2 (compare).** Then opened `gifted_p2.md`, `gifted_fixes_p2.md`, `journey_p2.md`, `fixpass_p2.md`, `close_gaps_p2.md`, `fixes_p2.md`, and `journey_p2.py` (to reuse its six diagnostic profiles).
- One deliberate post-Phase-2 note: the baseline called "the standard swap table again" a wrong-tier Challenge item. Applying that yardstick to my own Phase 1 list adds two items (L3 Challenge 7, L6 Challenge 8). I report the blind figure first and the adjusted figure second; nothing else was changed after reading the baselines.

Material read (real current text): `p2/content/l1..l10.js`, `p2/data.js`, `p2/gaps.json`, `p2/workbook_html.js`, `p2/guide.js`; rebuilt PDFs `p2/Math_Inquirers_P2_Student_Workbook_Designed.pdf` (64 pages, text-extracted), `P2_Tutor_Guide.pdf` (83), `P2_Weekly_Dose` (24), `outputs/designed/Math_Inquirers_P2_Question_Bank.pdf` (27), Free Taster (5), Weekly Email Pack (12); all 10 decks `split/p2l1..p2l10/project` (every slide's text and notes, 291 slides); `diag/content/p2.json`, `diag/build_diag.py`, `outputs/diagnostics/Math_Inquirers_Level2_Placement_Check.pdf` and `..._Tutor_Key.pdf`. I also brute-forced 84 answers (digit/coin/array/grid/jug/logic counts, magic-triangle totals, staircase ways): all agree with the printed keys. No answer errors found; no box/shape glyphs remain in any P2 PDF text.

---

## PART 1 - PHASE 1 (BLIND) SCORES OF THE CURRENT MATERIAL

### 1A. Gifted-style rubric (0/1/2 x 12), current

| L | Title | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Total /24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Digit Detectives | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | **19** |
| 2 | Missing Digit Mysteries | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | **20** |
| 3 | Legs, Wheels and Arrays | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | **19** |
| 4 | Pattern Machines | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | **19** |
| 5 | Mystery Number Machines | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | **20** |
| 6 | Market Day | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | **19** |
| 7 | Fair Shares | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | **18** |
| 8 | Shape Builders | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | **18** |
| 9 | Measure Masters | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | **19** |
| 10 | Challenge Day | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | **20** |
| | **Mean** | 2.0 | 1.0 | 1.6 | 1.9 | 1.3 | 2.0 | 1.9 | 1.4 | 1.1 | 2.0 | 1.0 | 1.9 | **19.1** |

Bands used in the brief (20-24 depth-oriented / 12-19 enrichment-flavoured with gaps / <12 drill with a label): L2, L5, L10 sit in the top band at exactly 20; the other seven are 18-19. (The baseline used its own cut, 19+ = "gifted-style"; see strictness notes.)

One-line evidence per criterion (level-wide, then lesson exceptions):

| Criterion | Evidence in the current text | Lesson exceptions |
|---|---|---|
| C1 low floor / high ceiling (2 all) | Every lesson: a concrete explore (slides `*-explore1`), a named "Explore: go further" what-if slide from minute 8 (`*-goexp`), an Investigation with an "Easy first step" line and a model answer with "Look for" (gaps.json). | L10 explore is four closed station cards (`p2l10-card1..4`); kept at 2 because the coin what-if (`goexp`) and Staircase investigation are open with named ranges. |
| C2 depth over speed (1 all) | Each worksheet page is 3 multi-part questions in 12-14 minutes (ws1 36-50, ws2 57-69), preceded by 5-9 teach/try slides. The Investigation is "any time or at home" and has no minutes in the 90-minute plan. Only explore (8-20) and talk (72-80) are unhurried. | none |
| C3 generalisation (2/1) | 2: L1 (Think Harder 4 Mei's swap claim, Q3b "why fewer", mirror-number (c)), L2 (odd+odd always even; add 100 to a magic square), L3 (every swap adds the same legs; tables meet), L4 (3 counting patterns, "exactly one"), L5 (magic trick always n; order matters), L10 (Staircase pattern, bank C1 "write a rule, does it always work"). | 1: L6-L9 (listing and "no more ways" but no rule asked). |
| C4 justification (2/1) | Named-child claims to test (Ali/Mei/Ravi) in workbook and talk slides, "explain why" in each Investigation (c), "show how you know" (L9 header). | L6 = 1 (only Q4a "Explain" and the "no $20 note" talk). |
| C5 multiple paths (2/1) | Mostly teacher-shown second method. | 2: L2 (compare vs compute for "="; undo vs guess-and-check; warm2 "count on or take away?"), L6 (count-on change vs subtract; fewest vs list), L10 (draw/list/table, "when is a table better?"). |
| C6 ladder (2 all) | Banners Start here / Think harder / Go further / Investigation, choice after Q3, go-further from minute 8, no one waiting; residual wrong-tier items are 1-3 per lesson (see 1C). | none |
| C7 student-led (2/1) | Predict, pairs, "do NOT tell the method yet" (explore notes), volunteers-first, sentence starters, "pass" on every talk slide. | L10 = 1 (5 minutes of cards, then about 16 minutes of tutor-led "how to start" worked examples). |
| C8 complexity (2/1) | Mostly a thin story coating (stickers, cakes, Mei and Ali). | 2: L3 (two interacting counts), L6 (budgets, change, "is there enough"), L9 (balances, jug state, timetables), L10 (hawker, logic grid, graph). |
| C9 posing (2/1) | What-if go-further slides and bank Challenge "make up your own" items exist, but no printed child page carries a posing task (the printed Go further pages show bank Challenge 7-9 only). | 2: L5 only (printed Investigation (c) "make your own trick that always returns the start" plus exit-ticket extension). |
| C10 metacognition (2 all) | A printed "Looking back" box on the "Before you go" page of all 10 lessons: Something I did well / The hardest part was / What helped me (two lesson-specific strategy ticks, "I asked for help", "I am still stuck (my tutor will check in...)"), "You may pass on any line", 2 timed minutes (87-89). Missing: "next time I will try". | none |
| C11 pacing (1 all) | A private sneak-peek (min 1-4), a choice after Q3 and go-further slides, but the sneak-peek tests UNTAUGHT ideas so it cannot let anyone skip mastered material; teaching blocks 20-32 and 52-57 and both check-together slides are for everyone. | none |
| C12 extension not acceleration (2/1) | Grade-level numbers, structure (listing, parity, multiples, bars). | L3 = 1 (sharing with leftovers = division with remainder, which the lesson's own notes call a P3 topic). |

### 1B. Tier compliance (current): Core / Think Harder / Challenge

Principle: Core = a child who has not been taught it can start and usually finish (objects, drawing, counting, guess-and-check, level-below skills; no unexplained notation); Think Harder = the lesson's idea in a new setting; Challenge = mastery plus extension. Printed workbook: core pages Q1-Q6 (Start here), Think Harder = bank Think Harder 1-4, Go further = bank Challenge 7-9 (numbered 5-7). Counted by the item's main body (a multi-part question is judged by what a child must do to start and mostly finish it).

| Set | Items | Violations | Compliant |
|---|---|---|---|
| Printed core-page questions (L1-L10) | 56 | 5 | 91% |
| Bank Core | 60 | 4 | 93% |
| Bank Think Harder (includes the 40 printed) | 87 | 2 | 98% |
| Bank Challenge (includes the 30 printed Go further) | 90 | 7 | 92% |
| Slide "Think harder" items (3 per deck; NOT the printed ones) | 30 | 1 | 97% |
| **All** | **323** | **19** | **94.1%** (blind) / **93.5%** after adding the 2 swap-table repeats |

Violations (blind list), with reason:

| Item | Reason |
|---|---|
| L1 core Q1 (b, c) | 15 tens and "830 = 7 hundreds + 13 tens" need the regrouping taught at min 20-24; no concrete scaffold on the page |
| L2 core Q5 | magic triangle: large trial space; the corner insight is only taught on slide `p2l2-teachtri` (hint "try 110 and 120 as corners" helps but the floor stays high) |
| L3 core Q1 and bank Core C5 | asks for 2 x and 2 / sentences: notation the lesson teaches |
| L9 core Q3 | six-step 3 l/5 l jug search; needs the state-table method (first two rows are given) |
| L9 core Q5 | clock hands + a.m./p.m. + elapsed time stacked in one item |
| L6 bank Core C1 | "$2.75" notation convention is what the lesson teaches |
| L8 bank Core C6 | recall of the word "cylinder" |
| L9 bank Core C5 | a.m./p.m. convention, unexplained |
| L1 Think Harder S4; L2 Think Harder S8 | Challenge-level (conjecture/counterexample; new "total = sum/3" insight) |
| L2 slide Think harder item 3 | 456 + 99 with the trick given: Core-level |
| L4 Challenge C1 | lights every 3 s / 5 s = re-skin of Core Q6 (both say) |
| L7 Challenge C4, C8, C9 | list of 3 pairs / fold a strip three times / half of a half: one step. C8 and C9 are printed Go further Q6 and Q7 |
| L8 Challenge C5, C9 | steps of cubes 9+6+3 repeats Think Harder S1; opposite faces of a dice is one-step recall (printed Go further Q7) |
| L10 Challenge C6 | 3/10 + 4/10 left, then x 5 cm: one step plus units |
| (adjusted) L3 Challenge C7, L6 Challenge C8 | trikes/cars 30 wheels and 5c/20c 8 things $1: "swap table again"; both printed Go further |

"Flat" Think Harder items (comply with the principle, but are a Core item with new numbers, so the ladder does not rise): 24 in the bank, **17 of the 40 printed Think Harder items** (L1 S1, S3; L2 S2, S3, S4; L3 S2, S3; L4 S2, S3; L5 S2; L6 S2; L7 S2, S3; L8 S2; L9 S1; L10 S2, S4). If these are counted as failures, compliance is **86%**.

Printed Go further (30 items): 27 genuine extension and 3 weak by the blind pass (L7 Q6, Q7; L8 Q7); after the swap-table adjustment 25 genuine and 5 weak (also L3 Q5 and L6 Q6).

### 1C. Student journey, current (P participate, D difficulty fit, F fun, C confidence, M motivation, S social/online; 1-5)

| L | LOW (P,D,F,C,M,S = mean) | MIDDLE | HIGH |
|---|---|---|---|
| 1 | 4,3,4,3,3,4 = 3.50 | 5,4,4,4,4,4 = 4.17 | 5,3,4,4,4,4 = 4.00 |
| 2 | 4,2,3,2,3,3 = 2.83 | 4,3,3,4,4,4 = 3.67 | 5,3,4,4,4,4 = 4.00 |
| 3 | 5,3,4,4,3,4 = 3.83 | 5,4,4,4,4,4 = 4.17 | 5,3,4,4,4,4 = 4.00 |
| 4 | 4,3,4,3,3,4 = 3.50 | 5,4,4,4,4,4 = 4.17 | 5,3,4,4,4,4 = 4.00 |
| 5 | 4,2,4,3,3,4 = 3.33 | 4,3,4,4,4,4 = 3.83 | 5,3,5,4,4,4 = 4.17 |
| 6 | 4,3,5,3,4,4 = 3.83 | 5,4,5,4,4,4 = 4.33 | 5,3,4,4,4,4 = 4.00 |
| 7 | 5,3,3,3,3,4 = 3.50 | 5,4,4,4,4,4 = 4.17 | 4,2,3,4,3,4 = 3.33 |
| 8 | 5,3,5,3,3,4 = 3.83 | 5,4,5,4,4,4 = 4.33 | 5,3,5,4,4,4 = 4.17 |
| 9 | 3,2,3,2,3,3 = 2.67 | 4,3,4,3,4,4 = 3.67 | 5,3,4,4,4,4 = 4.00 |
| 10 | 3,2,3,2,3,3 = 2.67 | 4,3,4,3,4,4 = 3.67 | 5,4,4,4,5,4 = 4.33 |
| **Mean** | **3.35** | **4.02** | **4.00** |

Evidence (slide/page/item):

- **L1 LOW.** Sneak-peek Q1 (3 hundreds, 2 tens, 5 ones, "draw them if you like", `p2l1-precheck`) is a minute-one win; digit-card explore and swap-the-digits brain break are concrete. Loses ground at core Q1b/c (15 tens; 830 = 7 h + 13 t, taught only at min 20-24) and alone on page 2 Q4-Q6 (chart pieces, 602 -> 598 crossing, a 3-clue riddle) in 12 minutes. "Biggest number wins" (`warm1`) is a small public win/lose. **MID.** Cards 3,5,8 then "how do you know you have them all" (`explore2`) is a real discovery; Q3b "why do 0,5,9 make fewer?" is the right stretch. **HIGH.** Go-further slide (4th card) from minute 8, mirror-number Investigation, Go further Q5-Q7 (381; 120 threes) give a ceiling; still sits through 20-32 place-value teaching and two check-together slides; only job offered is the `teachzero` volunteer.
- **L2 LOW.** Partners-to-999 explore is carry-free and the sneak-peek ladder (Q1 3[]2 + 416 = 788) is a win. Then carries/borrows: core Q1b-c, Q2, solo page-2 Q5 magic triangle and Q6 total-and-difference with bars (bars are not taught until L5); `warm1` "shout it out" partners to 1000 is a chorus. **MID.** "Was there a carry?" (`teach1`) is the right struggle; Q4 magic square satisfying. **HIGH.** Odd/even Investigation (test 5 pairs, explain with counters) and Go further AB7 + 4CD = 1000 (10 ways) are the best tasks; waits through `teachsq/teachtri/teachtwo` (52-57).
- **L3 LOW.** Counting legs/wheels (`warm1`) and counters for hens/goats are concrete; Q3 gives "start with all hens, swap one at a time". Strain: Q1b writes two division sentences, Q4/Q5 leftovers (a P3 idea) and four solo word problems on page 2. **MID.** "Swap 2 hens for 1 goat and the legs stay 16" (`explore2`); talk "can the leftover be 4 or more?" is excellent. **HIGH.** "Where tables meet" Investigation, Think Harder 1 (17 wheels, all ways), Go further Mr Lim; Q1-Q2 trivial; nine teach/try slides.
- **L4 LOW.** Clap-clap-stomp (`warm1`) and the cube train are physical; Q1 shows places 1-10 and the tip "draw a line after the LAST shape of each group". Q1c place 41, Q2b/c ("10th H" = place 40; Ts in 30 letters) need skip-counting by 4; Q3 bead string is wordy. **MID.** "Groups end at times-table numbers" (`explore2`, `teach1`) is a clean discovery. **HIGH.** "Three counting patterns" Investigation, Go further Q5 (predict, list to 100, why) and Q6 towers.
- **L5 LOW.** Guess-my-machine (`warm1`), sneak-peek Q1 ("adds 7, OUT 12") and the IN/OUT/undo strip on page 1 are wins. Strain: Q1 four two-step undo machines, Q5d "what must Ali put IN...", Q3/Q4 bars (a half) done solo. **MID.** "Undo the LAST step first" (`we1`, socks-and-shoes); Q5 "does order matter?" surprises. **HIGH.** Build-a-machine explore, "magic trick" Investigation including "make your own", Go further Q6 (three passes) and Q7.
- **L6 LOW.** Play money (kit pages 62-63), the shop (`warm1`) and the $10 toy stall are the most concrete in the level; sneak-peek Q1 (50 + 20 + 10) is a win. Q1 ($18.75, $76 with fewest pieces) and the 8-row Q2 table are heavy; solo page 2 is four cents-arithmetic problems in 12 minutes. **MID.** "Most of the biggest first, one fewer each time" (`we1`), Q2 seven ways, Q4b all pairs. **HIGH.** "Most coins" Investigation, Go further Q7 (15 amounts); core Q3 change is one-step.
- **L7 LOW.** Fair/not fair thumbs (`warm1`), folding strips and sneak-peek Q1 (fold in 2) are safe. "Fold a strip into 3 equal parts" can fail visibly; Q3c names the 1/6 > 1/4 error on a fictional child (good); Q6 (1/4 vs 3/8 with bars) is hard; slash (slides) vs stacked (workbook) fractions. **MID.** Equal-parts check (`teach1`), bars (`we2/we3`), cake story Q5. **HIGH.** Core is familiar; Think Harder 2-3 are core re-skins; Go further Q6 (fold thrice) and Q7 (half of a half) are one-step; only the strips Investigation (can thirds cover a half?) and bank-only Challenge 1-2 have a ceiling.
- **L8 LOW.** Name-the-solid (`warm1`), cutting circles, folding nets A-D (Q4) are hands-on; Q1 count-and-tick is a win. Q2 (every square by size in a 4x4 grid, triangles on a line) and Q3 (hidden cubes) are visual-spatial with a table scaffold; needs nets cut out beforehand ("give 2 minutes to cut"), circles, about 12 cubes. **MID.** "Cubes cannot float" layer counting (`teachcube`); nets. **HIGH.** Squares joined edge to edge (2 and 5 shapes), Go further 5x5 grid = 55, pyramid = 30.
- **L9 LOW.** Four topics (balance, jugs, ribbons, clocks) and the heaviest page 2: Q3 six-step jug table, Q4b 5 cm overlap, Q5 clocks A and B with a.m./p.m. and "hour hand almost on the 5", then a duration, solo in 12 minutes; needs a home-made coat-hanger balance (`explore1`). Wins: sneak-peek Q1 (one pour with two cups), Q1a (apple = 200 g). **MID.** Swap-on-a-balance (`teach1`, `we1`) is strong; page 2 solo still long. **HIGH.** Weights Investigation (only {1,2,3} and {1,2,4}), Go further Q5 (3 l and 7 l jugs), Q6 scales.
- **L10 LOW.** Mixed topics and new puzzle types: Q4 4x4 logic grid (tick/cross, taught only at 52-55), Q1 picture graph with key 5, Q5 fractions, Q6 growth table. Relay is now by volunteers with "pass", but the station cards say "Read the card aloud", the title is "Challenge Day", and the exit is "No talking, no helping" (80-85). Wins: sneak-peek Q1 (draw shapes), Q2 digit cards, Q3 table with row 1 filled. **MID.** "Draw it, list it, make a table" (`teach1`) is a useful frame; stations and "teach it in two sentences" good; page 2 solo covers three new types. **HIGH.** Staircase Investigation (1, 2, 3, 5, 8, 13), Go further Q6 coin logic and Q7 hawker ($21 to $28), bank C2 "remove a clue": the best ceiling in the level.

Moments that would make a child feel lost, rushed, left out or wait (current):
1. L9 and L2 page 2 (57-69, solo) hold the hardest items for the LOW child; no peer, one tutor visit.
2. L10 `warm1` relay ("choose a friend who has not had a turn") can leave the last child waiting to be picked; `explore1` "Read the card aloud" exposes a slow reader; `exit` "No talking, no helping" is the only test-like moment in the level.
3. L1 `warm1` "Biggest number wins" and L5 explore (one partner "secretly" chooses, the other "solves") can cast a weak child as always the solver.
4. Materials: digit cards (L1/L10), play money (L6), fraction strips (L7), nets and circles (L8), coat-hanger balance and jugs (L9) must be cut/made at home; the child without them loses minutes at the start.
5. HIGH child: about 35-40 of 90 minutes are whole-group listening (teach 20-32, 52-57, check-together 50-52 and 69-72, quick questions); the go-further slide and the choice after Q3 remove the "stranded alone" problem but not the listening.
6. Vocabulary and notation: array, leftover (L3); IN/OUT/undo (L5); semicircle, cuboid, net (L8); a.m./p.m., level balance, overlap (L9); slash vs stacked fractions (L7).
7. Reading load: printed core pages average about 330 words (my count includes figure labels; the baseline's method may differ, so +/-10%) with 3-4 line problems (L3 Q3, L5 Q3-Q4, L9 Q4-Q5, L10 Q3, Q5).
8. Slide Think harder shows three items that are NOT on the child's printed Think Harder page in all 10 lessons (for example L1 slide: "all three digits the same", printed: cards 1, 5, 8); the tutor notes cite the printed numbering.

Guaranteed LOW win in the first 10 worksheet minutes: yes in 10 of 10 lessons (L1 Q1a, L2 Q1a, L3 Q1/Q2, L4 Q1a, L5 Q1a, L6 Q1, L7 Q1, L8 Q1, L9 Q1a, L10 Q1a), and now also a private win at minute 1-4 via the sneak-peek Q1.

### 1D. Diagnostic check, current (4 warm-up + 6 main + 2 stretch, 30 minutes)

**Placement rule actually built** (`diag/build_diag.py`, printed on the PDF): main 6 only. 4-6 join (add "if the stretchers also went well (1 or more) you could try Level 3"); 2-3 "a chat with a tutor and the free taster... Level 2 with a little support suits many children here; if the warm-up is 2 or less, Level 1 may be more comfortable"; 0-1 "We suggest Ages 6-8 (Level 1)". Stretch not scored. **`diag/content/p2.json` carries a different, unused rule** (`scoring`: 5-6 / 3-4 / 0-2, level-up only at main 6/6 + warm-up 4/4 + both stretchers) plus `parent`, `tutorKey` (tie-break, prerequisites, header), `childNote`. None of those is rendered; `build_diag.py` ignores them.

(a) True skill demand:

| # | Question | Skill and fairness |
|---|---|---|
| 1 | 10 more than 64 | P1 place value; fair, very easy |
| 2 | order 58, 85, 49 | P1 comparing; no 50% guess now (3 numbers); fair |
| 3 | 16 - 9 | P1 bridging; fair |
| 4 | 45 + 30 | P1/early P2; fair |
| 5 | 10th shape, group of 4 | P2; drawing 10 shapes works, so low floor; fair (Lesson 4 skill) |
| 6 | 5? + 27 = 81 | P2 missing digit with regrouping; "5?" with "the ? hides one digit" is clear but not a typeset box; fair |
| 7 | 2 layers x 3 rows x 4 cubes | P2/P3 (tables 3, 4; layers); reading load; fair (L3/L8 skill) |
| 8 | 3:50 p.m. + 25 min | P2 time to 5 min, crosses the hour; the hardest main item for a P1-finished child |
| 9 | $1.20 + $0.85 | P2 money; 205 cents regroup; fair with P2 teaching |
| 10 | 3/4 of a pizza | P2; fair, easy |
| 11 | double, add 3, get 17 | P3/enrichment, reverse two-step; guess-and-check allowed |
| 12 | pets logic | P2/P3 logic; fair as a stretch |

All four warm-up items are genuinely Primary 1 (level below). Coverage of the ten lessons by the main six: L2 (Q6), L3/L8 (Q7), L4 (Q5), L6 (Q9), L7 (Q10), L9 (Q8 time). L1/L5/L10 appear only through warm-up or stretch. No item asks the child to explain, list "all", or persist, which is what the lessons demand.

(b) Six profiles (per-question success rates are MY assumptions, listed in `reaudit_p2.py` `PROFILES`; expected warm-up / main shown):

| Profile | E[warm] / E[main] | Built rule: join / chat / down | p2.json rule (not built): join / support / down | Right level? |
|---|---|---|---|---|
| A strong for age (8y) | 3.9 / 5.4 | 99 / 1 / 0 | 89 / 11 / 0 | Join is right. The "try Level 3" prompt appears whenever any stretch is solved |
| B typical for age (8y) | 3.7 / 4.4 | 81 / 19 / 0 | 49 / 47 / 4 | Join is right; the 19% get a friendly chat |
| C weak for age (8y) | 2.7 / 2.2 | 12 / 60 / 28 | 2 / 36 / 62 | Level 1 or support is right: 12% told "join" with no caveat |
| D younger strong (6-7y, P1 done) | 3.9 / 3.0 | 34 / 58 / 8 | 9 / 60 / 31 | Chat or Level 1 is right (L3/L6/L7/L9 assume taught tables, decimal money, fractions, time): 34% told "join" |
| E older weak (9y) | 3.0 / 3.5 | 51 / 44 / 5 | 20 / 60 / 20 | Support needed: 51% told "join" |
| F rusher / guesser (8y) | 3.8 / 3.2 | 40 / 52 / 7 | 13 / 59 / 28 | Level 2 with the tie-break is right; the tie-break ("under 12 minutes, ask them to check two answers") is in the JSON only, not printed |

(c) Cut-score noise on 6 main items (constant per-question success p): p = 0.3 -> join 7 / chat 51 / down 42; 0.45 -> 26 / 58 / 16; 0.6 -> 54 / 41 / 4; 0.7 -> 74 / 24 / 1; 0.8 -> 90 / 10 / 0; 0.9 -> 98 / 2 / 0. SD of a 6-item score is about 1.1 marks and each band is only 2-3 marks wide, so a single sitting cannot separate neighbouring levels; a child at p = 0.45 still hears "join" one time in four. The design leans on the wide middle "chat" band to absorb that.

(d) Wording: no "failure", "Not yet?" or "expect some support"; "Found it hard? That is useful to know, and it says nothing about how clever your child is" is kind (though "how clever" invites comparison); "tick not learnt yet" is positive; "Try your best, or skip it", "You make the final choice", free to change before lesson 1; the tutor key is a separate 2-page PDF. Still discouraging or wrong: a 9-year-old with 0-1 is told "We suggest Ages 6-8 (Level 1)" (the age-9 sentence exists only in unused `parent.down`); the "Level 3" prompt fires at main 4/6 plus one stretch; the stretch instruction "These last two are tricky on purpose, so it is fine to skip them" is printed inside question 11's text and again as the section tip; "Open to a year either side" with "Covers Primary 2 topics" is clear but the Tutor Guide calls the level "children finishing Primary 2 (ages 8 to 9)".

(e) Recommended changes (exact text):
1. Make the built rule and `p2.json` agree. If keeping 4/2 cuts, delete the stretch trigger from the 4-6 row and replace the last sentence by: "Level-up check: only if all 6 main questions, all 4 warm-up questions and both brain stretchers are right."
2. Render `tutorKey.tieBreak` and `tutorKey.prereq` on the key PDF: "Borderline (4 of the 6 main marks): ask your child to explain main questions 6, 8 and 9 aloud. If they can say why, use the higher band. If a child finishes in under 12 minutes, ask them to check two answers before you mark." and "Main questions 7, 8, 9 and 10 (cube stacks and arrays, time, money, fractions) are topics taught in school. Missing two or more means Lessons 3, 6, 7, 8 and 9 will need extra care, even if the main score is 5 or 6."
3. 0-1 row, add: "If your child is 9 or older, ask us: you do not have to choose a level by age."
4. Question 6: typeset "5 [box] + 27 = 81. Which digit goes in the box?"
5. Drop the duplicate "These last two are tricky on purpose..." from the text of question 11 (the section tip says it).

---

## PART 2 - PHASE 2: COMPARISON WITH THE BASELINES

Baselines: instrument A original = `gifted_p2.md` (state before `gifted_fixes_p2.md`); earlier claimed "after" = the table in `gifted_fixes_p2.md`. Instrument B baseline = `journey_p2.md`, which reviewed the state AFTER the close-the-gaps additions (warm-up check, fast-track box, Q8, reflection) and BEFORE the student-journey fix pass. So the B "before" already includes some new material; the A "before" does not.

### (1) Rubric per lesson: original / earlier-claimed after / now

| L | Before | Claimed after | Now | Now - before | Now - claimed | Per-criterion delta now vs before (C1..C12) |
|---|---|---|---|---|---|---|
| 1 | 12 | 16 | 19 | +7 | +3 | 0 0 +1 +1 0 +1 0 +1 +1 +2 0 0 |
| 2 | 13 | 17 | 20 | +7 | +3 | +1 0 +1 0 +1 +1 0 +1 0 +2 0 0 |
| 3 | 12 | 17 | 19 | +7 | +2 | 0 0 +1 +1 0 +1 0 +1 +1 +2 0 0 |
| 4 | 15 | 18 | 19 | +4 | +1 | 0 0 0 +1 0 +1 0 0 0 +2 0 0 |
| 5 | 14 | 17 | 20 | +6 | +3 | +1 0 +1 +1 0 0 0 0 +1 +2 0 0 |
| 6 | 13 | 17 | 19 | +6 | +2 | 0 0 0 0 +1 +1 +1 0 +1 +2 0 0 |
| 7 | 14 | 17 | 18 | +4 | +1 | 0 0 0 0 0 0 0 0 +1 +2 0 +1 |
| 8 | 11 | 14 | 18 | +7 | +4 | 0 0 0 +1 0 +1 +1 0 +1 +2 0 +1 |
| 9 | 15 | 18 | 19 | +4 | +1 | 0 0 0 +1 0 0 0 +1 0 +2 0 0 |
| 10 | 14 | 16 | 20 | +6 | +4 | +1 0 +1 +1 0 +1 -1 +1 0 +2 0 0 |
| **Mean** | **13.3** | **16.7** | **19.1** | **+5.8** | **+2.4** | |

(The fix log's L10 row lists three increments but states 16; I used the stated 16. The original L1-L10 per-criterion rows were read from the rubric tables in `gifted_p2.md`.)

Criterion means:

| Criterion | Before | Claimed (log increments) | Now |
|---|---|---|---|
| C1 low floor / high ceiling | 1.7 | 1.7 | 2.0 |
| C2 depth over speed | 1.0 | 1.0 | 1.0 |
| C3 generalisation | 1.1 | 1.9 | 1.6 |
| C4 justification | 1.2 | 1.2 | 1.9 |
| C5 multiple paths | 1.1 | 1.1 | 1.3 |
| C6 ladder | 1.3 | 2.0 | 2.0 |
| C7 student-led | 1.8 | 1.8 | 1.9 |
| C8 complexity | 0.9 | 0.9 | 1.4 |
| C9 posing | 0.5 | 1.5 | 1.1 |
| C10 metacognition | 0.0 | 1.0 | 2.0 |
| C11 pacing flexibility | 1.0 | 1.0 | 1.0 |
| C12 extension not acceleration | 1.7 | 1.7 | 1.9 |

Reading: the gain over the claim (+2.4) comes from C10 (the later "Looking back" box is a fuller design than the "Look back" line the log counted), C4 and C8 (Investigations and named-child claims, partly my more generous scoring), and C1. The claim was NOT met for C9 (1.1 vs 1.5: posing items exist only in the Question Bank) and C3 (1.6 vs 1.9: only 6 of 10 lessons ask for a rule or "always?"). C2 and C11 are unchanged at 1.0: "depth over speed" and pacing flexibility are the same structural gaps the baseline named.

### (2) Journey heatmap (mean of six) and dimension means, before vs now

| Lesson | LOW before | LOW now | MID before | MID now | HIGH before | HIGH now | Lesson mean before | now |
|---|---|---|---|---|---|---|---|---|
| L1 | 3.33 | 3.50 (+0.17) | 4.17 | 4.17 (0.00) | 3.00 | 4.00 (+1.00) | 3.50 | 3.89 |
| L2 | 2.75 | 2.83 (+0.08) | 3.58 | 3.67 (+0.09) | 4.17 | 4.00 (-0.17) | 3.50 | 3.50 |
| L3 | 3.33 | 3.83 (+0.50) | 4.17 | 4.17 (0.00) | 3.83 | 4.00 (+0.17) | 3.78 | 4.00 |
| L4 | 3.42 | 3.50 (+0.08) | 4.17 | 4.17 (0.00) | 3.83 | 4.00 (+0.17) | 3.81 | 3.89 |
| L5 | 2.83 | 3.33 (+0.50) | 3.75 | 3.83 (+0.08) | 4.17 | 4.17 (0.00) | 3.58 | 3.78 |
| L6 | 3.75 | 3.83 (+0.08) | 4.42 | 4.33 (-0.09) | 4.00 | 4.00 (0.00) | 4.06 | 4.06 |
| L7 | 3.58 | 3.50 (-0.08) | 4.25 | 4.17 (-0.08) | 3.58 | 3.33 (-0.25) | 3.80 | 3.67 |
| L8 | 3.17 | 3.83 (+0.66) | 4.00 | 4.33 (+0.33) | 4.08 | 4.17 (+0.09) | 3.75 | 4.11 |
| L9 | 2.58 | 2.67 (+0.09) | 3.50 | 3.67 (+0.17) | 4.08 | 4.00 (-0.08) | 3.39 | 3.44 |
| L10 | 3.25 | 2.67 (-0.58) | 4.08 | 3.67 (-0.41) | 4.17 | 4.33 (+0.16) | 3.83 | 3.56 |
| **Persona mean** | **3.20** | **3.35** | **4.01** | **4.02** | **3.89** | **4.00** | **3.70** | **3.79** |

Dimension means (all lessons):

| Persona | participate | fit | fun | confidence | motivation | social/online |
|---|---|---|---|---|---|---|
| LOW before | 3.65 | 2.45 | 3.75 | 3.10 | 3.05 | 3.20 |
| LOW now | 4.10 (+0.45) | 2.60 (+0.15) | 3.80 (+0.05) | 2.80 (-0.30) | 3.10 (+0.05) | 3.70 (+0.50) |
| MIDDLE before | 4.60 | 3.40 | 4.30 | 3.70 | 4.05 | 4.00 |
| MIDDLE now | 4.60 (0.00) | 3.60 (+0.20) | 4.10 (-0.20) | 3.80 (+0.10) | 4.00 (-0.05) | 4.00 (0.00) |
| HIGH before | 4.90 | 3.15 | 4.20 | 3.85 | 3.95 | 3.30 |
| HIGH now | 4.90 (0.00) | 3.00 (-0.15) | 4.10 (-0.10) | 4.00 (+0.15) | 4.00 (+0.05) | 4.00 (+0.70) |

Interpretation: the real, content-backed movements are LOW participation (+0.45: the sneak-peek ladder replaces the cold warm-up check), LOW social (+0.50: boards face down, answers private, volunteers and "pass", relay by volunteers) and HIGH social (+0.70: the printed FAST TRACK gate and the breakout split are gone, replaced by a whole-group choice and a go-further slide at minute 8; L1 HIGH 3.00 -> 4.00 as the zero-trap gate and the "last on the page" Investigation are gone). The LOW difficulty-fit column barely moves (2.45 -> 2.60): the page-2 solo block and the stacked topics are untouched. LOW confidence -0.30 and L10 LOW/MID -0.4 to -0.6 are scoring-strictness gaps, not content regressions: I found no change that makes L10 harder (the relay is by volunteers and the card text is now on the slide, both improvements), and the 3s the baseline gave on confidence I gave as 2-3 where page 2 is solo.

Weakest five cells now: L9 LOW 2.67, L10 LOW 2.67, L2 LOW 2.83, L5 LOW 3.33, L7 HIGH 3.33. Baseline weakest five: L9 LOW 2.58, L2 LOW 2.75, L5 LOW 2.83, L1 HIGH 3.00, L8 LOW 3.17. Fixes now (exact):
- L9 LOW: keep core page 2 to Q3 and Q4a; move Q4b and Q5 to Think Harder; replace Q5 by "Clock A shows the time Ali eats breakfast. Write the time with a.m. or p.m."
- L10 LOW: change "Read the card aloud" to "Your tutor will read the card aloud"; delete "No talking, no helping" and say "Work on your own for a few minutes. You may ask if you are stuck."; print clue 1's marks already filled in the Q4 grid; keep "Challenge Day" for the certificate only and title the worksheet "Mixed puzzles".
- L2 LOW: print 110 and 120 already in two corner circles of Q5(a); print a half-drawn two-bar model for Q6 (as L5 Q3 does).
- L5 LOW: move Q5d ("What must Ali put IN to get the same OUT as Mei?") to Think Harder.
- L7 HIGH: replace Go further Q6 and Q7 by bank Challenge 1 ("Three children share a cake cut into 10 equal pieces, each a different number...") and Challenge 2 ("I am a fraction with 1 on top. I am smaller than 1/4 but bigger than 1/7...").

Three strongest cells now: L6 MID 4.33, L8 MID 4.33, L10 HIGH 4.33.

### (3) Tier compliance, before vs now

| Measure | Baseline (as found) | Earlier claim | Now (blind) | Now (adjusted) | Now (Think Harder re-skins counted as failures) |
|---|---|---|---|---|---|
| Items checked | 317 | | 323 | 323 | 323 |
| Compliant | 272 (86%) | 100% | 304 (94.1%) | 302 (93.5%) | 278 (86.1%) |
| Challenge items in the wrong tier | 28 of 90 | 0 | 7 of 90 | 9 of 90 | |
| Think Harder items Core-level | 8 | 0 | 0 (+1 slide item) | 0 | 24 re-skins |
| Core-page questions with no entry point | 8 | 0 | 5 (2 carried over: L2 Q5, L9 Q3; 3 judged differently: L1 Q1, L3 Q1, L9 Q5) | 5 | |

Real gain: Challenge went from 69% to 92% in the right tier, and every Core-level Think Harder item was replaced. The claim of 100% is not met. And the strict figure (86%) equals the baseline: about 40% of the printed Think Harder items are Core items with new numbers, so the ladder is flat between Start here and Think harder in most lessons.

### (4) Diagnostic: did the earlier findings get fixed?

| Baseline finding | Now | Verdict |
|---|---|---|
| Noisy cut scores (8-item total, bands 1-2 marks wide) | Main 6 decide; stretch is not scored; bands 4-6 / 2-3 / 0-1; middle band is a conversation not a verdict. Noise itself is not smaller (SD about 1.1 on 6 items). On the baseline's own six profiles re-run on the built rule: typical 8-year-old "sent down" 12% -> 0% | Partly fixed (error cost lower, precision not better) |
| Discouraging wording ("Not yet?", "failure", "expect some support", answer key in the child's file) | "Not yet?" and "failure" gone; "Found it hard? ... says nothing about how clever your child is"; key is a separate PDF; "Try your best, or skip it"; "not learnt yet" box on every question | Fixed, except the 9-year-old told "Ages 6-8" and the "clever" comparison phrase |
| Younger-strong and older-weak children mis-placed; hasty child sent down | Re-run on the baseline's rates, old rule -> built rule: younger strong: join+support 55 / join 22 / down 22 -> chat 43 / join 54 / down 3 (38% also get the "try Level 3" prompt); older weak: down 67 / support 31 / join 2 -> chat 56 / join 35 / down 9; weak 8-year-old: down 95 -> down 37, chat 56, join 7; rusher: down 94 -> chat 57, down 35, join 7 | Typical and rusher children are no longer wrongly sent down; younger-strong and older-weak children are now MORE likely to hear "join" (worse). Not fixed |
| 4 of 10 lessons not sampled | Pattern (Q5) and time (Q8) items added; cube stack (Q7) | Mostly fixed (L1, L5, L10 only via warm-up/stretch) |
| 50% guess on W2; undefined "5_" notation | Three-number ordering; "5? ... the ? hides one digit" (not a typeset box) | Fixed / partly |
| Tie-break, prerequisites, "tricky on purpose" note | In `p2.json` only; the note is inside question 11's text | Not rendered (tie-break, prerequisites) / partly |

Re-run of the six profiles on the current rule (my rates, 1D b): A 99% join; B 81% join / 19% chat; C 12 / 60 / 28; D 34 / 58 / 8; E 51 / 44 / 5; F 40 / 52 / 7 (join / chat / down). **Diagnostic verdict: before "mostly"; now "mostly" for typical and strong children, "weaker" for the two profiles the baseline said the lessons hurt (younger strong, older weak), because the built rule is more lenient than the spec the fix pass wrote (`p2.json` 5-6 / 3-4 / 0-2) and than `docs/levels_and_placement.md` (70% = enrol, 40-69% = support or one level down, under 40% = one level down: 4/6 is 67% and 2/6 is 33%).**

### (5) Regressions and fixes claimed but not (fully) present

Regressions (worse than baseline, or new defects):
1. **Diagnostic leniency / spec drift.** Built rule 4-6 / 2-3 / 0-1 vs intended 5-6 / 3-4 / 0-2 in `p2.json`; a weak child hears "join" 12% (was about 5%), younger-strong 34%, older-weak 51%. `fixpass_p2.md` listed "Build changes needed in diag/build_diag.py (not made)"; commit `ab5b2e1` later built a different "unified" rule and left `scoring`, `parent`, `tutorKey`, `childNote` dead.
2. **Level-up prompt** shown at main 4/6 plus one stretch ("you could try the Ages 8-10 (Level 3) check"); the spec says only 6/6 + 4/4 + 2/2. About 38% of the younger-strong profile would see it.
3. **Safeguarding contradiction introduced by the fix pass.** `fixpass_p2.md` says "NO private chat to children anywhere" and `guide.js:188` says "No private messages to children", yet the sneak-peek SAY line printed in all 10 lesson scripts says "...to your tutor only, or send it in private chat" (`gaps.json` `common.preSay`), and the routine table says "by private chat" (warm-up row) and "Quiet children can be invited by private chat beforehand" (talk-time row) (Tutor Guide pp. 3 and each lesson).
4. **Cost.** Student workbook 52 -> 64 pages, tutor guide 63 -> 83, Question Bank 21 -> 27; the fix pass admits the "+1 page per lesson" cap was exceeded.

Claimed fixed, not (fully) fixed:
5. `gifted_fixes_p2.md` "Tier compliance 100%": 94% (blind) / 93.5%; printed Go further still has 3-5 weak items (L7 Q6 fold thrice, Q7 half of a half; L8 Q7 dice faces; also L3 Q5 and L6 Q6 on the adjusted count).
6. "One problem-posing prompt added to the Challenge tier of every lesson": true only in the Question Bank PDF; none of the 10 printed Go further pages and none of the Weekly Dose first slots carries one (they were moved to the middle of the list on purpose). So the C9 credit (+1 to +2 per lesson) is mostly unreachable by the child.
7. Core-page scaffolds: L1 Q6, L2 Q2, L4 Q3, L9 Q1 now have a usable entry point; L3 Q7 and L6 Q5b were moved to Think Harder; **L2 Q5 and L9 Q3 still have a high floor** despite the added hints.
8. Slide Think harder items differ from the printed Think Harder page in every deck (baseline already carried "3 slide Stretch items"); the tutor notes quote the printed numbering, so tutor and child see different lists.
9. `fixpass_p2.md` / slide notes: "Looking back... small box on the last core page (every child reaches it)". In print it is on its own "Before you go: Investigation and Looking back" page after page 2. Also L10: slide label `reflect` says 87-89 but its note and the guide say 85-87 (then 87-90 for certificates).
10. Diagnostic items from the fix pass not rendered: tie-break for borderline/fast finishers, prerequisite line, typeset box for "5?", the "Want a gentler start?" card, the age-9 sentence.
11. Reading load: the baseline asked for it to be cut; core pages now average about 330 words by my count (baseline 291 by its count), with added hint lines.
12. HIGH wait time and LOW solo page 2 (12 minutes) are unchanged; the baseline's "give HIGH a job in the mini-lesson" was done only in L1 (`teachzero`).

### (6) Improvements that are real (with evidence)
1. **Metacognition 0 -> 2 in all ten lessons.** Printed "Looking back" box: "Something I did well", "The hardest part was ...", lesson-specific "What helped me" ticks, "I asked for help", "I am still stuck (my tutor will check in during the session)", "You may pass on any line" (workbook, e.g. pp. 6, 12, 17), timed 87-89 (`*-reflect`).
2. **No public labels.** The FAST TRACK box is gone; every lesson header carries "START HERE. After question 3 you may choose: carry on, or try Think harder."; banners Start here / Think harder / Go further / Investigation; the scripts say never announce who is on which page. Evidence: HIGH social 3.30 -> 4.00; L1 HIGH 3.00 -> 4.00.
3. **Cold warm-up check replaced by a sneak-peek ladder.** Q1 is an access question with objects/drawing/counting and a stated first win, Q2 the thinking question; answers private, "I do not know" welcome, nobody marked (`*-precheck`, `gaps.json`). LOW participation 3.65 -> 4.10.
4. **Challenge tier rebuilt.** 28 wrong-tier Challenge items -> 7; real extension tasks now printed, for example L2 AB7 + 4CD = 1000 (10 ways, verified), L4 towers "29? 50? 100?" (tower 10, tower 17, none), L10 hawker "$21 to $28, can 7 dishes cost $30?", L5 "Ben gives Ali 5 marbles... why is it not 5?" (verified).
5. **Ten Investigations, all verified.** Mirror numbers (10 from 200-299; 90 in 100-999), odd/even, where tables meet (15, 30, 45), three counting patterns, magic trick, most coins (85c and 95c need 4), fraction strips, squares edge to edge (1, 1, 2, 5), weights ({1,2,3}, {1,2,4}), staircase (1, 2, 3, 5, 8, 13). Each has an "Easy first step" line and a model answer with "Look for".
6. **Go-further slide from minute 8** so no one waits in the explore (`*-goexp`).
7. **Talk-time safeguards**: volunteers first, pass allowed, no tallies, no cold-calling; L10 relay now by volunteers.
8. **Materials fallbacks**: real money (L6), sugar cubes or drawn layers (L8), ruler balanced on a pencil (L9) in the Tutor Guide.
9. **Diagnostic**: three-number ordering, pattern and time items, stretch unscored, separate tutor key, supportive page wording, "not learnt yet" box.
10. **Accuracy**: 84 independent brute-force checks agree with the printed keys.

### (7) Where the two audits differ in strictness (do not over-read the deltas)
- Both are single-pass model desk reviews with no children; the two reviewers are the same kind of reader, so shared blind spots are likely. Differences of one point in a cell are inside the noise.
- Rubric bands: the baseline called 19+ "gifted-style"; the brief's bands put 20-24 as depth-oriented. By the baseline's cut, nine of ten lessons now score gifted-style; by the brief's cut only three (L2, L5, L10) do, and each by one point.
- I scored C4 (1.9 vs 1.2) and C8 (1.4 vs 0.9) more generously: I credit the printed Investigation prompts and named-child claims, and I gave 2 for multi-variable tasks where the baseline gave 2 only for L6. Applying the baseline's yardstick would remove about 0.3-0.5 from each, so about 0.7 of the +5.8 is scoring difference. I scored C10 = 2 although "what I will try next" was removed; the baseline's yardstick (Polya-style look-back) would arguably give 2 for a box that records strategy and difficulty.
- Items are judged by the main body of each multi-part question (the baseline judged "by its hardest part"), so I am more lenient on Core pages (I accepted L2 Q3d, L4 Q2c) and stricter on re-skinned Think Harder items, which the baseline did not count as failures.
- The investigations and Looking back are optional or outside the timed 90 minutes; I gave full credit where the text offers them, which a stricter scorer could cut for "unscheduled" (C2 stays at 1).
- Journey: the baseline allowed half-points, mine are integers; baseline B reviewed the state after the close-gaps additions, so some of the fixes (neutral choice, sneak-peek) are measured against a state that already had a fast-track box, not against the original lesson; my confidence column is 0.3 lower for LOW and my L10 LOW/MID are 0.4-0.6 lower despite no content getting worse.
- Both used per-question success rates the reviewers assumed; the like-for-like diagnostic re-run (baseline's own rates, old rule versus built rule) is the cleanest comparison, and it shows the leniency drift.

---

## Summary table of headline numbers

| Measure | Before | Claimed after | Now |
|---|---|---|---|
| Level mean rubric /24 | 13.3 | 16.7 | 19.1 |
| Journey mean LOW / MIDDLE / HIGH | 3.20 / 4.01 / 3.89 | not claimed | 3.35 / 4.02 / 4.00 |
| Tier compliance | 86% | 100% | 94% (86% strict) |
| Diagnostic | mostly | n/a | mostly (typical, strong); worse for younger-strong and older-weak |
