# Independent audit: term-time pre-flights for Levels 2 to 5

Audited: `docs/terms/l2_preflight.md`, `l3_preflight.md`, `l4_preflight.md`, `l5_preflight.md` (branch `claude/great-fermi-1hv4vc`, 23 Oct 2026). Report only; nothing in the audited files was changed.

Checked against: `docs/terms/owner_decisions.md`, `level_{2..5}_year_plan.md`, `docs/books/p{2..5}_*`, `docs/moe/syllabus_by_level.md`, `docs/schedule/term_2027_t1_availability.md`, the holiday content `p2/content` to `p5/content` (l1.js to l10.js; the task named `levels/` and `hp/`, but `levels/` holds build scripts and `hp/` is Level 1/P1), and `term/l1/tools` (`figs2.py`, `figs3.py`, `svg.py`, `validate.py`, `b_quest.py`, `b_guide.py`).

## 1. Method and headline result

| Check | Result |
|---|---|
| Lessons 1 to 40 present in each file | 40/40 in all four; each lesson has a named Beyond item at Think harder or Go further; lessons 10, 20, 30, 40 carry Mi's Challenge Quest; no end-of-term check anywhere (L5 headline 2 and L4 headline 5 retire the plan's check) |
| Appendix scripts (L3, L4, L5) extracted and run | L3 `178 checks, 178 passed`; L4 `TOTAL checks: 273 failed: 0`; L5 `265 checks, 265 passed`. Every check id quoted in the prose exists in the script (L3 178/178, L4 252/252, L5 250/250 ids matched) |
| L2 appendix script | None exists. L2 says its checks were "a scratch script, not committed" (section 0, section 12). Its "verified" claims cannot be reproduced from the file (finding M4) |
| Independent recomputation (my own code, not the appendix) | Roughly 80 quoted items for L2, 110 for L3, 120 for L4 and 100 for L5 (all of the Quest gate answers, the cut-piece and hour totals, uniqueness claims, brute-force counts, plus hand-derived worked examples). **No arithmetic error found.** Examples re-run: L2 five 7-coin ways to make 110 cents, the 495 trick (891 numbers, at most 6 steps), the number ring (8 rings, 1 with the given start), 275 stacks (6 to 14), tilted squares 6/20/50, the L-garden (1 L-partition, 7 any); L3 jug moves 2/6/8, the 9-circle triangle totals 17/19/20/21/23, 24 from 2,3,5,8 and every target 1 to 10, clock angles (11 of 24), 1 008 four-different-digit numbers; L4 cube nets 11 of 35, staircase opposites, 64/80/142 dates, 2 178, letter sums; L5 Pick, 48 triangles of area 3, 14 bracketings with 9 values, folded corner 25 and 71, 7/11 jugs in 14 moves, Petersen 120 colourings, Frobenius 27/25/36, liar puzzle |
| Time budgets | Standard skeleton sums to 90 in L3 and L5; **L4 sums to 88** (finding H3). Quest-lesson skeleton (2+6+4+10+9+4+20+25+4+2+4) sums to 90 in all four and puts the Quest at minutes 35 to 55 |
| Kit tables | Every row has supplied >= max used. Cut totals recomputed: L2 263 (T 77/57/81/48), L3 271 (45/55/71/100), L4 52 (23/0/23/6), L5 146 (29/12/59/46); per-book splits also correct |
| Hour tables | Row sums, term sums and totals correct: L2 299.3 (+30 = about 330; template 125/109), L3 299.0 (+41 = 340; 150/133), L4 305.0 (+30 = 335; 136/118), L5 349 (+42 = 391; 193/141/84) |
| Type-by-lesson matrices | L3, L4 match their lesson specs and counts; small mismatches in L3 and L5 (finding L6) |
| L3 claim that `level_3_year_plan.md` lines 274 to 395 are Level 5 text | **True.** The section cites `p5_non_routine_catalogue.md`, "2279 questions in 166 Primary 5 papers", GST at 9 percent, and lessons "Shifting Places", "Factor Finders", "Tank Tales", "Percent Sense". The file has 394 lines, so "395" is off by one. The L2, L4 and L5 plans cite their own level's catalogue (checked) |
| Plan titles vs pre-flight titles | All 40 titles match in all four levels |

Verdict: the numbers are sound. The weaknesses are (a) holiday items and owner-decision-6 items that survive in Start here and in the Quest gates, (b) one timing slip, (c) cross-level duplicates, and (d) a number of self-contradictions and stale statements. Details follow.

## 2. High

### H1. Holiday items reused in term lessons, in places the registers say must not be reused
Owner decision 22 Oct (Term 1 is new lessons; no holiday question reused). Each of these is confirmed against the holiday text.

| Where | Term item | Holiday item | Register status |
|---|---|---|---|
| L2 sec 1 Lesson 6 Start here ("[n/d] of the pizza is left", 6 slices, 4 eaten) | pizza 6 slices, 4 eaten | `p2` H7 core 6: "A pizza is cut into 6 equal slices. 4 slices are eaten. What fraction is left?" (answer 2/6) | Not in the L6 "Do not reuse" list in sec 13 (it lists "Ali pizza halves" only) |
| L3 Lesson 13 Start here (2) and L3 sec 8.2 Quest gate 3 | 9 cm by 4 cm rectangle, perimeter 26 cm, area 36 cm2 | `p3` H7 core 1: "9 cm long and 4 cm wide ... perimeter" = 26 cm | L3 sec 3 says H7 is "the largest overlap in the year" and bars its items; this one is not listed |
| L3 Lesson 15 Think harder (1) | which of the letters H, A, M, L, E, T have both a parallel and a perpendicular pair | `p3` H8 exit: "Which letters have BOTH a pair of parallel lines and a pair of perpendicular lines" and key "E and H: both; T and L: perpendicular only" | The register bars "letters E and H" yet the item uses H, E, L, T |
| L5 Lesson 7 Think harder (2) | triangle area 54 cm2, height 9 cm, find the base (12 cm) | `p5` H4 challenge 9: triangle ABC area 54, BD 4, DC 8 (base 12, height 9) | Register bars "triangle ABC of area 54 with BD = 4 and DC = 8" |
| L5 Lesson 23 Think harder (2) and Go further 3 | "40% on shoes, 30% of the rest on a bag" | `p5` H7 stretch 6: "40% on shoes and 50% of the rest on a bag" | Register bars "40% then 50% of the rest" |
| L5 Lesson 10 Think harder (2) | 2/5 on a book, then $18, $24 left | `p5` H10 exit: 1/2 on a ticket, $5 on a snack, $7 left (same structure); L5 Lesson 36 drops the same structure for exactly this reason | L10 register row says "New: ... a fraction then a fixed amount" |
| L5 sec 8.2 Quest gate 2 (Lesson 12) | box 5 cm by 4 cm by 3 cm, 60 cm3 | `p5` H5 core 4 "a 5 x 4 x 3 box" | Barred in Lesson 12 and sec 3 (allowed only in the Remember spiral) |

Fix: replace the items; add the missing entries to the registers; run the TL2/M15/N1 holiday-copy check before the first audit (all four documents already specify it).

### H2. Contest-style items placed at Start here (owner decision 6; Start here is "approachable")
Decision 6 lists digit-sum tests, gaps and posts, chance, ratio notation, cryptarithms, pairing sums and worst-case counting as Think harder, never Start here. Each document restates this rule, then breaks it.

- **L2 Lesson 10 Start here**: posts every 5 m along 20 m (5 posts), queue "4th from the front of 15 is 12th from the back", "how many cuts make 4 pieces" are gaps-and-posts items. The same item is **Quest Term 1 gate 8** (sec 6). L2's own Risk 2 names this kind of slip.
- **L2 sec 6 Year Quest gate 1**: "is blue likely, unlikely or certain" at "Start here level", while Lesson 31 says likely/unlikely are Think harder only (decision 6).
- **L3 Lesson 5 Start here (3)**: six-number pairing sum (76+28+24+12+88+72) although its own strand says pairing is "NOT IN"; **Quest T1 gate 2** (64 + 29 + 36); **Quest T4 gate 1** uses the digit-sum test for 3 ("4725, digits add to 18") while Lesson 31 keeps the test out of Start here.
- **L4 Quest T1 gate 2** (digit-sum test for 9) while Lesson 3 puts digit sums at Think harder.
- **L5 Lesson 2 Start here (4)**: "Is 7 482 a multiple of 3? Of 9? Use the digit sum" (V2.10).
- **L5 sec 8.3 Quest gate 4**: "Pens to pencils are 2 to 3" (ratio statement at Start here level; notation is Think harder by decision 6).
- Not on the decision-6 list but the same "no non-routine item at Start here" rule: L4 Lesson 10 Start here (1) guess-and-check table, L4 Lesson 35 Start here (1), (3), (4) list-all-ways, L5 Lesson 39 Start here (2), (4) counting colourings, L2 Lesson 17 Start here outfit list. L4 sec 13 says "No non-routine item sits at Start here (none does here)": false.

### H3. L4 skeleton does not add to 90
`l4_preflight.md` sec 0.1: "Opening 2, Remember 6, Sneak-peek 4, Explore 14, Mini-lesson 10, Break 4, Workbook 28, Talk 6, Exit 6, Look-back 3, Flex 5 (Opening may be 4 with Explore 12)" = **88**, both variants. `validate.check_timing` fails unless the parts sum to exactly 90. L3 (Explore 16) and L5 (Explore 16) are correct; Level 1 AUTHORING is Opening 4 + Explore 14, or Opening 2 + Explore 16. L2 never lists the standard 11 parts (it says "same as Level 1"), so its non-Quest budget cannot be checked inside the document.

## 3. Medium

- **M1. Quest gates reuse lesson items verbatim**, against each document's own failure-pattern rule 3 ("no Start here or Think harder number is used ... in the Quest"). Examples: L4 T1 gate 6 = Lesson 8 TH(2) (1 245 eggs, 8 to a box, 156) and gate 7 = Lesson 9 SH(2) (14 squares); **L4 T2 gate 8 = Lesson 20's own TH(1)** (180 sweets); L4 T3 gates 1, 5 = Lessons 21 SH(2), 27 SH(1); L4 T4 gates 3, 5, 7 = Lessons 34, 36, 38, 39; L5 T2 gates 1, 3, 5, 6, 7 = Lessons 11, 13, 15, 16, 17 SH items, T3 gates 1, 2, 3, 5, T4 gates 3, 8; L3 T2 gate 3 = Lesson 13 SH(2). Decide once: either Quest items are fresh, or the rule is dropped.
- **M2. Wording conflicts with `validate.py` / `b_quest.py` ban lists.** `BAN_FAMILY` (Quest files) and `QBAN` (every Quest lesson's child text) ban "marked/marks", "score(s)", "out of", "grade(s)": L2 T1 gate 7 ("A scale marked every 100 g"), L3 T1 gate 1 ("marked every 100"), **L5 T3 gate 3 ("18 out of 24 is 75%")**. `BANNED_CHILD` bans "ahead of" and `\bstretch\b`: L5 Lessons 9 (TH 4), 10 (G2) and 34 (TH 1) use "ahead of"; L3 Lesson 13's child-visible puzzle title **"Stretch One Side"** (D20 shows puzzle names to children). Builds would fail.
- **M3. Cross-level duplicates; no cross-level register exists** (L5 sec 14 admits the other levels were not compared; L4 read only the first 130 lines of L3). Confirmed duplicates: (a) "Most and Fewest" 3 by 3 base, front 3,1,2 / side 2,3,1, 6 and 14 and 275 stacks is the same puzzle, same numbers, in **L4 Lesson 27 and L5 Lesson 11** ("Hidden Cubes"), and L2 Lesson 25 is the same with the heights permuted; (b) **L4 Lesson 13 G3 = L5 Lesson 10 TH(1)** (4 times as many, gives 36, then twice as many: 54 and 216); (c) squares in a 3 by 3 grid (14) at L2 L7 TH(2) and L4 L9 Start here (2), and in the Level 3 holiday H10; (d) the "more than, spends, then 3 times as much" decimal chain in L4 L18 G2, L4 L37 G3 and L5 L6 G2 (different numbers, one structure); (e) **inside L3**: Lesson 3 Start here (2) and Lesson 24 Start here (1) are the same item ("Ravi has 7 stickers; Ali has 3 times as many", 21, V3.4).
- **M4. L2 has no committed verification script.** About 100 "verified" claims (sec 0, 12) are unreproducible. I re-derived them all (they are correct), so this is a process gap, not an error. L3 to L5 ship their scripts.
- **M5. Stale scheduling text.** All four say the 90-minute slots are "not re-derived / blocks the launch" (L2 Risk 19, L3 sec 14 and Risk 16, L4 Risk 19, L5 D26). `docs/schedule/term_2027_t1_availability.md` section 7 already has the 90-minute grid with 15-minute buffers (8 slots; Level 2 default Sun 3:45 to 5:15; Level 3 Sun 5:30 to 7:00; Level 4 Thu 5:45 to 7:15; Level 5 Sat 5:15 to 6:45). None of the four mentions the 15-minute between-lesson buffer, and L2/L4 still say the grid has 75-minute slots. The in-lesson 4-minute break is respected everywhere; break length (4 or 5) is an owner decision in L2 (D17) and L4 (D16) only.
- **M6. Tier-honesty slips inside Start here (beyond-syllabus rule: Start here stays school-range).** L4 Lesson 16 Start here (4) adds a mixed number (P5, as the lesson's own strand says; Risk 2 lists this exact slip); L4 Lesson 38 Start here (1) to (4) is all Primary 5 (fraction as division, cuboid layers); L5 Lesson 15 Start here (3), (4) use parallelogram and trapezium area (L5 says "not in the primary syllabus (confirmed)"); L5 Lesson 31 Start here (1) quadrilateral sum 360 (polygon sums not in the syllabus); L5 Lesson 8 Start here (5), (6) need angles on a line and vertically opposite angles, which the syllabus first sets at P5 yet are treated as "recalled" P4 (D9 discloses it; a Term 1 joiner has not met them); L3 Lesson 10 Start here (4) compares prices as 2.40 against "about 2.67" although the lesson says unit prices divide exactly (decimal division is P4).
- **M7. Template effort is counted four times and is unmeasured.** Shared items (fraction renderer, `column`, `bar_model` v2, `balance`, graphs, solids and nets, quest builder, validator, books) appear in each level's total (125 + 150 + 136 + 193). Only L5 nets them (about 84 h own share). Adding the four headline figures overstates the template cost by tens of hours. Per-lesson hours come from one data point (L1 Terms 3 and 4: 172 h for 20 lessons, 8.6 h per lesson); L2 to L4 average 7.5 to 7.6 h per lesson, below that, while L3/L5 cite L1 Quest lessons at 12.5 to 13.5 h and L2/L4 budget them at 11.3 to 12.0. Day counts (8 to 10; 9 to 11) are arithmetically consistent with the hours and plausible, but nothing was measured ("the Level 1 trial has not reported").
- **M8. Tool claims not supported by the code.** L4 sec 0.2 and finding 11 say `bar_model` "caps at 10 cells and 3 bars" (justifying the 6 h F4): `figs2.bar_model` has no such cap (`units.n` and the bar list are unbounded; width scales). L3 Lesson 37 "Figures" says `money` "needs a $100 note", but `figs3.NOTE_SIZE` already contains `$100` (and L2 sec 3.5 says the engine has "$100 notes"); L2's KD page (coins to $1, notes $2/$5/$10/$50) differs from the Level 1 default `play_money` (no $1 coin, 5 notes of $2, 4 of $5), reachable only through the `counts` override.
- **M9. Registers: L2 Lesson 12 "Holiday overlap: NONE (odd and even is not in the holiday course)" is wrong.** Holiday Lesson 3 argues parity twice ("the total is always an even number", hens and goats; 21 is odd), Lesson 5 challenge ("x 2 always even, +1 odd"), Lesson 1 odd-number riddle, Lesson 4 "every even place is blue". Rate MEDIUM-LOW overlap; the quest gate "even + even" and Lesson 29 lean on it.
- **M10. Ambiguous or loosely worded items.** L4 Lesson 36 Start here (2) and L4 Quest T4 gate 5: "A rope is cut in half, then 3 m is cut off one half, and 9 m is left" gives 24 m only if 9 m is the cut half; read as the total left it is 12 m. L4 Lesson 24 Start here (4): "A photo 20 by 15 has a frame 3 cm wide, frame area 246" is right only if the frame is outside the photo (inside gives 174). L4 Lesson 32 G1: "120, 90, 150 and 45 ... add to 360" (the four add to 405; only the first three do). L5 Lesson 17: "Four numbers 4, 9, 5, 6, 6" (five numbers). L5 Lesson 9 G1: "nobody plays neither or both is unknown" (garbled).

## 4. Low

- **L1. Counting slips in prose.** L3 sec 3: "Eleven lessons are Heavy: ... (twenty)" (table says 20, correct). L3 hand-off 36 to 37: "heaviest cut of Term 4 (15 pieces)" but Lesson 34 is 20 and Lessons 33, 36 are 16. L5 headline 9 / Risk 12: "heaviest pages are lesson 28 (21) and lesson 1 (13)" but Lesson 35 is 16. L5 Lesson 10 spec says "Quest Log (3 pages)" but sec 0.1/8/D19 say 4. L3 sec 8.4 "every lesson of the term is visited by exactly one gate" then excludes Lesson 40 (same in L4/L5 for Lesson 10 or 40; harmless).
- **L2. Spec vs table inconsistencies.** L3 Lesson 29: spec "Explore uses 6 clue cards" vs table "max used 10"; L3 Lesson 36: spec 4 cards + 3 signs + 2 bracket pairs vs table "max used 15"; L2 hand-off 9 to 10 "12 counters" vs Lesson 10 "ten counters"; L2 hand-off 11 to 12 omits the 20 counters Lesson 12 uses; L2 Lesson 15 table counts hands only (4) while the spec counts faces too (6); L2 sec 3 has no M16, L5 sec 5.5 has no TL13; L2 and L4 keep a kept page (array mat Lesson 16 -> Lesson 32; fraction wall Lesson 4 -> Lesson 14) across a term break, flagged only in L4.
- **L3. Matrix vs table.** L3 Lesson 18: table has EQ T and EQ G, matrix shows G only. L5 Lesson 18: table has EXP T and EXP G, matrix shows T only; L5 Lesson 33: matrix has CTX, spec Non-routine line does not (4.1 table does).
- **L4. Rewind rule differs by level** (L2: Lessons 5 to 10 rewind n-4; L3: Lessons 1 to 10 rewind a holiday topic; L4: Lessons 6 to 10 n-4, 1 to 5 none; L5: holiday or P4 topic). L4 validator rule N1 "letters allowed only in the lesson 11 letter sums" conflicts with lettered figures in Lessons 7 (A to D), 21 (net letters), 22 (angle names), 30 (towns).
- **L5. Beyond items that are not beyond-syllabus**: L2 Lesson 14 "Share the Gap" (the document itself calls it "ordinary Book 2 school work"), L5 Lesson 37 "Spare Clue", L3 Lessons 2 and 39 (process skills). Rule of 23 Oct asks for a beyond-school item.
- **L6. "Originals only"**: several named puzzles are classics (Locker Parade, Seven Bridges = Koenigsberg with the original bridge counts, Pour and Measure 7 l/11 l, Odd Coin Out, Five-Point Star, 24 game, Petersen colouring, 495 trick, Fibonacci square paradox, handshakes). Only L5 sec 14 warns authors not to present them as invented.
- **L7. Ratio of holiday evidence**: L2 Lesson 3 G1 "Always One Left" (smallest number leaving 1 in 3, 4 and 5) is the same remainder-system type as holiday Mr Lim's sweets; L5 Lesson 26 G3 (prove 1+...+n by pairing) repeats the explanation in holiday H9 challenge 1 (staircase, two copies make a rectangle); L5 Lesson 27 TH(3) (282 digits) and L3 Lesson 34 G1 (192 digits) are the same reverse-page-number question at two levels; L5 Lesson 13 uses the 60 by 40 base (holiday tank 60 by 40 by 50) and a 30 by 20 base in its Quest cave (holiday block in a 30 by 20 tank).
- **L8. Syllabus notes**: L5 sec 14 and L2/L4 rely on `docs/moe/syllabus_by_level.md`, not the PDF (disclosed). L3 plan reference is off by one line (394 lines, not 395).
- **L9. Estimate wording**: L5 headline 12 "141 to 193 hours" and sec 13.3 "193 ... 141 ... about 84 for the Level 5 share alone" read as three different bases; state once which one the owner should budget.

## 5. Holiday overlap: accuracy spot checks (8 lessons per level)

| Level | Lessons checked | Register entries confirmed in holiday text | Misses |
|---|---|---|---|
| L2 | 1, 3, 4, 6, 7, 12, 15, 22 | Digit cards, digit sums 4/5/6, 300 to 399, pages 1 to 120, bicycles, boats of 4, cupcake boxes, Mr Lim, houses 5/9/13, frogs, squares 2x2/4x3/5x5, 5-minute clocks, film 10:40 | L6 pizza (H1), L12 "NONE" |
| L3 | 4, 9, 13, 15, 24, 28, 33, 34 | 35 counters, 58 sweets, 100 people in boats of 9, station clock fast, night train 22:40, 300 and 500 ml cups, handshakes and 3 by 3 squares, digit 5 and pages 1 to 120, pencil box and pens, Mei/mother ages | L13 9 by 4, L15 letters |
| L4 | 3, 10, 12, 16, 21, 22, 23, 31 | Buses 6 and 8, next-door numbers 90/624/783, chickens and rabbits, double and add 7, robot turns 225, area 56 length 8, perimeter 20 largest area, 24 m fencing, 52 54 56 58, chicken-rice queue | none found |
| L5 | 1, 7, 10, 13, 16, 21, 23, 27 | 5 x 4 x 3, 245 volume, 60 x 40 x 50 tank, 36 l in 40 x 30, car parks $1.50/$1.20, two printers sharing 900, candle, bath plug, GST on $20, $109 incl GST, $250 bicycle, 7-digit palindromes, heart 1 000 000 | L7 area 54, L10 structure, L23 shoes, Quest gate 2 |

Counts of holiday question-bank items cited are correct (L2 237, L3 234, L4 239, L5 242: 60 core + 84 to 92 stretch + 90 challenge).

## 6. Kit and hand-off tables vs `term/l1/tools`

Figures and kits named as "existing" were checked in `figs2.py`, `figs3.py`, `svg.py`: all exist (`bundles`, `scatter`, `ten_frame`, `plates`, `number_line`, `hundred`, `seq`, `ruler`, `clock` with `mirror`/`sector`/`digital`, `calendar` with `days`, `shapes2d` with 1/2/4 parts only, `cube_stack` heights 0 to 3, `grid` with one vertical `mirror` column, `network`, `picture_graph`, `table`, `bar_model`, `picture_equation`, kits `base_ten` (tens bars and ones squares), `clock_kit`, `play_money`, `stick_strips` with `n`, etc.). Hard-coded Level 1 items confirmed: `b_guide.py` line 198 footer "Level 1", `validate.py` word bans. Book boundaries (5/10/15/... and Quest Logs in Books 2/4/6/8) and every kit cut in the hand-off tables match the kit tables in all four documents. Gaps: see M8, L2 above.

## 7. Owner-decision lists

Complete for the structural items (holiday policy, previews, instruments, books and payment D11, blocks, break length, cold-join trials, Quest slot and log pages, play-money legality, papers to supply). Defaults are sensible. Gaps:

1. No decision on a cross-level duplicate register (M3) or on whether Quest gate items may repeat lesson items (M1).
2. No decision that the Quest gates must obey `BAN_FAMILY` words (M2).
3. L3 and L5 have no break-length decision (L2 D17, L4 D16 do) and no term price / prorating note (L2 D24, L4 D24 do); Quest Log page count differs by level (3, 3, 4, 4) with no stated reason.
4. L5 D9 default (angle facts "recalled") is the riskiest default: the syllabus first sets them at P5.
5. Slot assignment is not in any decision list; `docs/schedule` section 7 should be cited (M5).

## 8. Suggested order of repair

1. H3 (one line), then M2 and the L5 "out of" and "ahead of" wording.
2. H1 replacements and register additions; add the L2 Lesson 12 correction (M9).
3. H2: move or relabel Start here items and Quest gates; fix the L4 sec 13 check (b).
4. M1/M3 decisions; commit an L2 script; update M5 text in all four files.
