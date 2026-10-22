# MOE syllabus alignment audit: Levels 4, 5 and 6 (Ages 9-11, 10-12, 11-13)

Date: 2026-10-22. Scope: p4, p5, p6 lesson content (`content/l1.js` to `l10.js`: topic, objective, question bank Core / Think Harder / Challenge, printed workbook), `p4-p6/SPEC.md`, `docs/levels_and_placement.md`, `docs/gifted_research.md` section 3, `docs/audit/gifted_p4-p6.md`, and the public sign-up page. Read-only on content; nothing was edited.

**Read this first: the official syllabus text itself could not be opened.** Every attempt to download the MOE PDF (moe.gov.sg and school-hosted copies, via curl and via the fetch tool) returned 404 or an empty page, and the SEAB site returned 403. So the MOE learning outcomes below are NOT quoted from the official document. Per the instruction not to guess from memory, each year-level classification is labelled with where it came from: **[MOE-PAGE]** an official MOE page I did fetch, **[SECONDARY]** a tuition or school page, or search-engine extracts of the MOE PDF, and **[UNVERIFIED]** where I found nothing. Treat all ON-LEVEL / BELOW / ABOVE calls as provisional until someone with the PDF re-checks the 3 to 4 pages that matter (P4 to P6 content tables). Section 6 lists exactly what to check.

---

## 1. Which syllabus document, version, date, URL

| Item | What I found | Status |
|---|---|---|
| Document | "Mathematics Syllabus, Primary One to Six" (the 2021 syllabus; MOE's own title in search listings; the user-supplied name "Primary Mathematics Teaching and Learning Syllabus" is the older formal title) | Title seen in search results only |
| Latest version I could identify | Search listing of `https://www.moe.gov.sg/-/media/files/primary/2021-primary-mathematics-syllabus-p1-to-p6-updated-dec-2024.pdf` (file name says "updated Dec 2024"). Older copies: `.../2021-primary-mathematics-syllabus-p1-to-p6.pdf` (footnote says "updated December 2023") and `.../mathematics_syllabus_primary_1_to_6.pdf` | **[UNVERIFIED]**: the URLs appear in search results but every fetch gave 404 or empty |
| Implementation | 2021 syllabus began with the Primary 1 cohort of 2021; P5 from 2025; P6 from 2026. 2026 is the first PSLE on the 2021 syllabus. Footnote quoted by search extract of the MOE PDF: "The 2021 mathematics syllabus will be applicable to Primary 5 from 2025 and Primary 6 from 2026 onwards." | Extract of MOE PDF via search; **[SECONDARY]** for the PSLE statement |
| MOE syllabus landing page | `https://www.moe.gov.sg/primary/curriculum/syllabus` loaded (shows "Last Updated: 14 Aug 2026") but the Mathematics download links are script-rendered and did not appear in the HTML I could read | **[MOE-PAGE]**, no newer revision visible |
| SEAB PSLE Mathematics syllabus page | Not reachable (403). A search of seab.gov.sg returned only the iPSLE page | **[UNVERIFIED]** whether a newer SEAB syllabus document exists |
| Newer revision than Dec 2024? | None found. Nothing I read mentions a 2025 or 2026 revision. I cannot rule one out | **[UNVERIFIED]** |

**Content facts used (all second-hand; the first two are search-engine extracts of the MOE PDF, the rest are tuition or school pages):**

- P6 Ratio: notation a:b and a:b:c for whole numbers, equivalent ratios, dividing a quantity in a given ratio. P6 Average: "relationship between average, total value and number of data". [extract of MOE PDF, **[UNVERIFIED]** by me]
- Changes in the 2021 syllabus [SECONDARY: The Learning Lab, Ancourage Academy; both agree]: P4 gains Pie Charts and Nets (moved down from P6); P4 loses the 12/24-hour clock (to P3) and "turns and the 8-point compass"; P5 loses Average and Ratio (both move to P6); P6 loses Speed (reported as moved to Secondary 1, or dropped; sources differ, and a Bartley Secondary exam list puts "Rate and Speed" in Sec 2); P6 algebra (letter as unknown, simplify simple linear expressions, substitute, solve simple linear equations) now without the "in simple context" restriction on equations.
- Topic lists by year [SECONDARY: deepthink.sg, partial]. P4: numbers to 100 000, factors and multiples, four operations, fractions, decimals, angles, rectangles and squares, area and perimeter, nets, symmetry, tables and line graphs, pie charts. P5: numbers to 10 million, four operations of whole numbers, fraction and division, four operations of fractions, decimals, rate, percentage, area of triangle, volume, angles, properties of triangle, properties of parallelogram / rhombus / trapezium. P6: fractions, ratio, percentage, algebra, angles in geometric figures, circles, volume of cube and cuboid, average.
- Secondary 1 [SECONDARY: school content outlines from Yishun Sec 2025 and Bartley Sec; not the MOE syllabus]: primes, square and cube roots, HCF / LCM, negative numbers, rational numbers, approximation, basic algebraic concepts and notation, ratio, percentage, area and perimeter, angles. Linear equations, expansion and factorisation appear at Sec 2.
- Coding in primary [SECONDARY: IMDA page via search, schools]: Code for Fun is run by IMDA with MOE for primary schools: about 10 hours for upper primary on computational thinking and coding (debugging, events, loops, variables, functions, conditionals) and an intro to AI. School pages say block-based tools such as Scratch are used in upper primary, within the National Digital Literacy Programme. I could not open the IMDA page, and found no moe.gov.sg page stating a Scratch requirement. **[UNVERIFIED]**.
- Mathematical processes and heuristics (reasoning, communication, applications, modelling; heuristics such as draw a model, make a list, work backwards, make suppositions, guess and check): I could not read the framework text. **[UNVERIFIED]**. I make no claims below about exact MOE wording of the processes.

**How well the "one school's scheme of work" basis checks out.** The SPEC files say the topic lists come from the Tampines North Primary 2026 P4 and P5 schemes of work (P6 has no school source). That is a reasonable proxy: a 2026 P4 and P5 school scheme is on the 2021 syllabus, and the P4/P5 lesson topics match the secondary-sourced MOE topic lists almost one for one. But it fails on three points I can see: (a) P4 SPEC lists the 8-point compass, which sources say was removed from the 2021 P4 syllabus; (b) P4 has no pie chart (moved to P4); (c) the P6 SPEC says children know "ratio, rate and speed ... average", but speed is no longer a P6 topic, and the P5 SPEC says percentage increase and decrease is "known" in one line and "P6" in the next. So: broadly consistent for P4 and P5 topic names, not verified, and a few details are stale or inconsistent. For P6 there is no external basis; the level is a deliberately off-syllabus bridge, which is fine if described that way.

---

## 2. Lesson-by-lesson alignment

Legend: ON = on-level (topic in that year's list); BELOW = met in an earlier year; ABOVE = met in a later year (stated); NOT = not found in the primary or Secondary 1 sources I could see. Every call is **[SECONDARY]** or **[UNVERIFIED]** as noted. "Outcome" is a short paraphrase of the topic-list entry, not a quotation of MOE wording.

### Level 4 (Ages 9-11) vs P4

| L | Lesson topic | MOE year | Class | Relevant topic entry / note |
|---|---|---|---|---|
| 1 | Factors and multiples (common factors / multiples) | P4 | ON | "Factors and multiples" [SECONDARY]. Exactly-3-factors, locker problem, "5 does not divide 36 so stop at pairs" are extension of the same topic. |
| 2 | Numbers to 100 000, rounding, estimating | P4 | ON | "Numbers to 100 000". Rounding to 10 / 100 / 1000 as a P4 outcome: **[UNVERIFIED]** (may be P3). Palindromes, digit-card puzzles: extension. |
| 3 | Four operations, order of operations, bar model "times as many" | P4 (order of operations and brackets: **[UNVERIFIED]** whether P4 or P3/P5) | ON | "Four operations of whole numbers". Letters a, b, c, d used as unknowns in Think Harder 7 and Challenge 4: see section 3. |
| 4 | Fractions: improper / mixed, fraction of a set, unlike denominators | P4 | ON, with 2 ABOVE items | "Fractions (I) and (II)". Adding unlike fractions (1/3 + 1/4) is Challenge 2, 5, 6, 7: probably P5 (see section 3). |
| 5 | Decimals to 3 places, order, round, money and mass | P4 | ON | "Decimals; four operations of decimals". Rounding to 2 dp and "closest to" riddles are extension. |
| 6 | Angles: protractor, clock hands, compass turns, unknown angles in squares / rectangles | P4 (angles); 8-point compass **removed from 2021 P4** | ON for protractor and unknown angles; **NOT IN 2021 SYLLABUS** for compass turns (Core 3, 4; Think Harder 1, 4, 5, 7; Challenge 3, 6; Workbook Q4, Q6) | Clock-hand angles (30 per number, 6 per minute): not a listed outcome, a context for angle measure. |
| 7 | Area and perimeter of composite rectilinear figures | P4 | ON | "Rectangles and squares; area and perimeter" |
| 8 | Symmetry and nets | P4 (nets moved down from P6 in 2021) | ON | "Nets; symmetry" [SECONDARY]. If a child's school is on the 2021 syllabus, nets are new in P4, so this is a good fit. |
| 9 | Tables and line graphs | P4 | ON | "Tables and line graphs". **Pie charts** (P4 in 2021) are not covered anywhere: gap (section 4). Misleading-scale graphs: extension. |
| 10 | Mixed heuristics (guess and check, supposition, working backwards, logic) | Heuristics across P1-P6 | Process, not a content topic. Not a syllabus topic | Heads-and-legs and "age in 6 years is 4 times" type problems are PSLE-style; fine as enrichment. |

### Level 5 (Ages 10-12) vs P5

| L | Lesson topic | MOE year | Class | Note |
|---|---|---|---|---|
| 1 | Numbers to 10 million, order of operations, estimating | P5 (numbers to 10 million); order of operations is BELOW (P4) | ON, part BELOW | Brackets in Think Harder and Challenge are revision of P4 skill, used as puzzles. |
| 2 | Fractions: fraction and division, four operations, fraction of remainder | P5 | ON; with 2 items possibly ABOVE (P6) | Think Harder 6 "(Preview of P6)" dividing a proper fraction by a whole number: whether this is P5 or P6 in the 2021 syllabus **[UNVERIFIED]** (P5 "four operations of fractions" is listed [SECONDARY], so the P6 label may be wrong). Challenge 2 (product 1/2 x 2/3 x ... x 99/100, fraction x fraction) and Challenge 7 (telescoping unit fractions): fraction x fraction is likely P6; **[UNVERIFIED]**. |
| 3 | Fraction word problems, before-and-after | P5 (word problems, with model drawing) | ON | Uses units / bar model, which is the standard approach. "3/5 as many as" is a fraction comparison; no ratio notation used (correct for P5 under 2021). |
| 4 | Area of triangle | P5 | ON | 1/2 x base x height; height outside the triangle: consistent with "area of triangle" (**[UNVERIFIED]** that obtuse-triangle heights are in the P5 outcome). Challenge 4 (areas of triangle ADF vs FCE) is competition geometry. |
| 5 | Volume of cuboid, litres and cm3, tank problems, painted cubes | P5 (volume); the 2021 P6 list also shows "volume of cube and cuboid" | ON, tank-rise problems possibly P6 | **[UNVERIFIED]** which of "water rises when an object sinks", "pour between tanks" is P5 or P6. Painted-cubes and "three face areas give volume" (Challenge 7) are enrichment, NOT in syllabus. |
| 6 | Rate (per unit, rate tables, buys, taps and printers together) | P5 | ON | "Rate" [SECONDARY]. Speed is correctly avoided. "Working together" (Challenge 1, 9) and charge rules are enrichment applications. |
| 7 | Percentage: of a quantity, discount, GST | P5 (percentage); finding whole from percentage, % increase / decrease, GST possibly P6 | ON for Core; Think Harder 1, Challenge 2, 3, 4 (increase / decrease, find the original) ABOVE (P6) per the lesson's own SPEC | **[UNVERIFIED]** which year MOE puts discount, GST and % change. The SPEC contradicts itself (line 23 says "increase and decrease" are known; line 24 says they are P6). |
| 8 | Angles; triangle, parallelogram, rhombus, trapezium | P5 | ON | "Angles; properties of triangles; parallelogram, rhombus and trapezium". Angle sum of quadrilateral (Core 6) not confirmed in outcome list **[UNVERIFIED]**. |
| 9 | Patterns and number sense; heads and legs, supposition | No "patterns" topic in the P5 list I saw | NOT (as a topic); heuristics | Rule "3 x figure number + 1" in words is sensible: no letters, as MOE reserves algebra letters for P6. Sum of odd numbers, squares in a grid, digit counting: competition enrichment. |
| 10 | Mixed strategies / logic grids | Heuristics | Process, not a content topic | Fine. |

### Level 6 (Ages 11-13, after PSLE) vs P6 and Secondary 1

| L | Lesson topic | MOE year | Class | Note |
|---|---|---|---|---|
| 1 | Sequences and the nth term (+ Scratch loop / variable) | nth-term formulas not in P6; Sec 1 number patterns **[UNVERIFIED]** | ABOVE (secondary), year **[UNVERIFIED]** | Finding terms of a "number pattern" by rule is a primary heuristic ("look for a pattern"). Geometric sequence (Challenge 5) and rule "6n - 4" go beyond it. |
| 2 | Primes, factors, prime factorisation (+ mod, loops) | Sec 1 (primes, HCF / LCM) [SECONDARY: Yishun outline] | ABOVE (Sec 1) | The SPEC itself says "met directly in lower-secondary maths". Goldbach, twin primes, 1001 = 7 x 11 x 13: extension. |
| 3 | Negative numbers | Sec 1 [SECONDARY] | ABOVE (Sec 1) | Not a primary topic [UNVERIFIED]. |
| 4 | Expressions and equations (function machines) | P6 algebra (letter as unknown, simplify, substitute, simple linear equations) [SECONDARY]; "3(n + 2)" and unknown on both sides: Sec 1 / Sec 2 | ON-level P6 (this is revision of what a PSLE child has just met), with some items ABOVE | See section 3: Challenge 1, 2, 5, 6, 8; Think Harder 3. |
| 5 | Counting (multiplication rule, handshakes, routes, nested loops) | Primary: "make a systematic list" heuristic only | NOT IN SYLLABUS | Permutations / combinations appear much later in mainstream school maths **[UNVERIFIED]** where. |
| 6 | Probability (fractions, two dice, fair games, simulation) | Not in primary; secondary year **[UNVERIFIED]** | ABOVE (secondary) | I found no primary probability topic. |
| 7 | Angles in polygons; turtle geometry; star polygons | P6 "angles in geometric figures" is the nearest; interior-angle sum of polygons is secondary **[UNVERIFIED]** | ABOVE for polygon angle sum and stars; NOT IN SYLLABUS for stars | Stars (turn = 360 x times round / points) are enrichment. |
| 8 | Clock (modular) arithmetic, Caesar cipher | Not in primary or Sec 1 sources | NOT IN SYLLABUS | Enrichment (the SPEC says so). |
| 9 | Averages and data (mean; median, mode) | P6 average (total = average x number of data) [extract of MOE PDF]; median / mode: not in the P6 list | Mean: ON P6 (BELOW for a post-PSLE child); median and mode: ABOVE (secondary) **[UNVERIFIED]** year | MOE P6 word is "average" (see section 3). |
| 10 | Mixed maths and code | n/a | Mix | See above. |

**Coding bridge.** The Scratch work (variables, loops, if, lists, turtle pen) matches the concepts listed for Code for Fun in upper primary [SECONDARY]. No lesson depends on a stated MOE coding syllabus, and I found none for mathematics. Describing it as "a maths and coding bridge" is accurate and needs no MOE reference. Do not say it follows MOE computational thinking or Code for Fun.

---

## 3. Vocabulary, notation and method mismatches

Item references: C1-C6 = Core, T1-T8+ = Think Harder (bank "stretch"), CH1-CH9 = Challenge, WB Qn = printed workbook question, in order of the bank. Rewordings are suggestions; each needs a check against the school-facing MOE wording once the PDF is open.

### Level 4

| Where | Issue | Suggested rewording |
|---|---|---|
| L3 T7 `a + b x c - d (a, b, c and d are the four numbers...)`; L3 CH4 `a x a - a = 30. What is the number a?` | Algebra letters as unknowns; P6 is where letters appear [SECONDARY]; P4 SPEC bans "algebra letters". | T7: "Use each of 2, 3, 4 and 5 once in [ ] + [ ] x [ ] - [ ] to make the biggest answer." CH4: "The same number goes in all three boxes: [ ] x [ ] - [ ] = 30. What is the number?" |
| L5 T1 `Find ALL the digits that the letter A can be: 3.A5 < 3.42` | Letter as a placeholder. | "Find ALL the digits that can go in the box: 3.[ ]5 < 3.42" |
| L4 CH2 (1/3 and 1/4 of money), CH5 (1/4 red, 1/3 blue), CH6 (1/3 and 1/4 of marbles), CH7 (1/2 and 1/3 sweets) | Combining unlike, unrelated fractions: adding fractions with unrelated denominators is likely P5 (P4 deals with related fractions) **[UNVERIFIED]**. A bar model can solve each, so they work as puzzles, but the objective says only comparison. | Either keep and label "uses a bar model, no fraction addition needed", or swap to related denominators (e.g. 1/3 and 1/6, 1/4 and 1/2). |
| L4 T6 `3 m cut into pieces each 1/4 m long` | Division by a fraction is a later-year operation; solvable by counting quarters. | "How many quarter-metre pieces make 3 m? Count the quarters." |
| L6 whole lesson, objective "turn on the 8-point compass (45 steps)"; C3, C4, T1, T4, T5, T7, CH3, CH6; WB Q4, Q6 | 8-point compass and "turns" removed from 2021 P4 [SECONDARY]. SPEC cites it as a school-scheme topic. | Keep as a game ("compass robot") but say "not part of the current P4 syllabus"; or reword to "quarter-turn and half-turn clockwise / anticlockwise from a starting direction." Check against the PDF before changing. |
| L6 WB Q2 `angle notation: AOB means the angle at O between OA and OB` (written with the angle sign) | Introduces angle sign notation. MOE angle notation at P4 vs P5 is **[UNVERIFIED]**. The lesson explains it in-page, which is safe either way. | No change needed. |
| L8 / L9 | No pie charts, though pie charts are now P4. | See gaps (section 4). |
| Bar models | L3 and L4 use bar models for "times as many", fractions and money; this matches the Singapore model method [SECONDARY, general]. | No change. |

### Level 5

| Where | Issue | Suggested rewording |
|---|---|---|
| L2 T6 label "(Preview of P6) A rope 3/4 m long is cut into 3 equal pieces" | Possibly mislabelled: P5 "four operations of fractions" may already include dividing a proper fraction by a whole number **[UNVERIFIED]**. Also SPEC line 23 says the same. | Hold until PDF check. If P5 covers it, drop "(Preview of P6)". If not, keep the label. |
| L2 CH2 `1/2 x 2/3 x 3/4 ... x 99/100`; CH7 `1/6 + 1/12 + 1/20 + ...` | Fraction x fraction is likely P6. | Label "(P6 preview)" or add the first three terms as a shown pattern. |
| L7 T1, CH2-CH4 (percentage increase / decrease, find the original after a discount) | Probably P6 per the lesson's own SPEC; SPEC also lists these as "known". | Make SPEC line 23 consistent with line 24, and keep a "(P6 preview)" tag on the printed Think Harder item. |
| L8 hint, WB Q2: "In a trapezium, the angles between the parallel sides add to 180" and "neighbours add to 180" | Fine as a property of trapezium and parallelogram, but "neighbours" is not MOE vocabulary that I can confirm; "angles between parallel lines" is Sec 1 language. | "In a parallelogram, two angles next to each other (adjacent angles) add up to 180. In a trapezium, the two angles on the same side between the parallel sides add up to 180." Check against school wording. |
| L8 uses "angle BOC", "angle B = 108" in words | MOE uses angle notation; whether the angle sign is introduced at P4 or P5 is **[UNVERIFIED]**. The worksheet uses words, which is safe. | Optional: "angle BOC (also written with the angle sign)". |
| L9 rule written as `number of sticks = 3 x figure number + 1` | Good: words, no letter. Matches "algebra with letters starts P6". | Keep. The P6 workbook then writes `sticks = __ x n + __`, which is a clean step up. |
| L10 and L9 "supposition" (heads and legs) | Make-a-supposition is a standard PSLE heuristic; I could not confirm it as listed MOE wording. **[UNVERIFIED]** | No change. |
| Ratio, average, speed | Not used anywhere (checked by search). Good: matches 2021 (ratio and average moved to P6, speed gone). | None. |

### Level 6

| Where | Issue | Suggested rewording |
|---|---|---|
| L9 all items: "mean" | MOE P6 term is "average" (relationship of average, total, number of data) [extract of MOE PDF]. A child who has just done PSLE will say "average". | First use: "Find the mean (also called the average) of 3, 5, 7 and 9." Add to the lesson key idea: "total = average x number of values". |
| L9 median / mode (C5, CH4, WB Q4) | Not in the primary list I could see; these are secondary. The items define both in-line, which is right. | Add "(you may meet these in secondary school)". |
| L7 "inside angle" and "turn" | MOE secondary vocabulary is "interior angle" and "exterior angle" **[UNVERIFIED]** year. | First use: "The turn is called the exterior angle. The angle inside the shape is called the interior angle." Keep "turn" and "inside" afterwards. |
| L7 key facts "sum of inside angles of a regular polygon" | Secondary topic. | Keep as enrichment; label "(secondary school maths)". |
| L4 `3(n + 2)` (CH6), `OUT = 3n + 2`, "Mei is n years old... in 12 years" (CH8), "Which IN gives the same OUT on both machines" (CH5), "same number out: x3 - 4" (CH1), `(n + 6) x 4 = 60` (T7) | P6 algebra covers a letter for an unknown, simple expressions, substituting and simple linear equations; brackets with a letter and unknowns on both sides are Sec 1 / Sec 2 [SECONDARY]. `3n` (juxtaposition for 3 x n) is standard MOE notation. | Keep, but add "(secondary school style)" to CH1, CH5, CH6 and CH8. Write `3 x n` once before `3n`. |
| L1 "nth term", `6n - 4` | Not a primary phrase; primary says "number pattern". | First use: "A sequence (number pattern) follows a rule. The nth term is the rule for the n-th number." |
| L3 notation `4 - (-6)`, `-3 - (-4)` | Secondary notation; defined in-lesson with a number line. | OK. |
| L6 "probability", "fair game" | Fine. MOE secondary notation P(A) is not used, which is safe. | None. |
| L8 `mod`, `n % d` (WB Python corner), `(letter + shift) mod 26` | Not in MOE primary or Sec 1. | Fine: say "clock arithmetic (the remainder)". |
| P6 SPEC line 23 "Children know ... rate and speed" | Speed is not a 2021 P6 topic [SECONDARY]. | Edit SPEC to "rate" only, or "speed (if the school still teaches it)". |

---

## 4. Coverage gaps (MOE outcomes that no lesson touches)

Based on the secondary-sourced topic lists. Check against the PDF.

| Level | Topics in the year's list not touched | Does it matter for an enrichment programme? |
|---|---|---|
| P4 | Pie charts (new to P4 in 2021); adding / subtracting related fractions as a skill (L4 only compares and converts); multiplication and division of decimals by a whole number as a taught skill (L5 uses it only in items); perpendicular and parallel lines, properties of rectangles and squares as a topic (only inside L7); time (24-hour clock, now P3); money and measures; multiplying 4 digits by 2 digits and dividing by 1 digit as taught skills (only inside L3 items) | No for a "complements the school syllabus" programme: it states it is enrichment. Yes for the page wording: "covers P4 topics" overclaims coverage (see section 5). Pie charts are the one clear gap in a topic the program otherwise covers, because the P4 data lesson stops at line graphs. |
| P5 | Decimals (four operations): in the SPEC "children know" list but no lesson; whole-number multiplication and division beyond estimation; data / statistics (none listed for P5 in the sources I saw, **[UNVERIFIED]**); properties of parallelogram / rhombus / trapezium covered in L8 ✓; ratio and average (moved to P6, correctly absent); percentage as a standalone skill is covered only partly (L7 jumps to discount and GST quickly) | No, for the same reason. The page wording matters more than the gap. |
| P6 | Ratio (none); percentage (none); fractions (÷ fraction); circles (area / circumference); volume of cuboid and cube in P6 form; angles in geometric figures (L7 touches polygons only); pie charts; the full PSLE problem-solving set. Touched: algebra (L4) and average (L9) only | The gap is large by design: Level 6 is post-PSLE and says it is a bridge. But the label "P6" in `docs/levels_and_placement.md` ("Primary 6, after PSLE") and the Level 6 age band mean a parent could think it revises P6 maths. It does not. |

---

## 5. Honesty of wording and suggested safe wording

**What the current text says (and how it checks):**

- `docs/levels_and_placement.md` and the sign-up page: "Ages 9-11 (covers P4 topics)" and "Ages 10-12 (covers P5 topics)". From the audit above: the lesson TOPICS are P4 and P5 topics, but they are a selection of those topics, not full coverage, and four P4 outcomes and several P5 ones are untouched. "Covers P4 topics" can be read as "covers the P4 syllabus". Suggested replacement: "**Ages 9-11: topics from the Primary 4 school year, with puzzles that go further**". Equivalent for 10-12.
- Level 6: "maths + coding bridge, after PSLE": accurate. Do not call it "P6 maths"; the placement table's "Typical school year: Primary 6" column is fine, but the level name and the two phrases below should keep "after PSLE".
- Sign-up page: "Not affiliated with MOE or the Gifted Education Programme" and "Is it linked to MOE or the GEP? No...": consistent with `docs/gifted_research.md` section 3 and with what I found: no official MOE source endorses or defines this programme.
- Per-level SPECs say "tagged to the P4 / P5 syllabus": fine as an internal note; do not publish "tagged to the MOE syllabus".

**Safe wording (supported by what I found):**

- "Topics chosen to complement the school syllabus: each lesson takes a Primary 4 / 5 topic and explores it through puzzles and reasoning." (P4, P5)
- "Maths for the months after the PSLE: ideas you will meet in lower secondary (negative numbers, primes, simple equations) plus counting, probability and coding in Scratch." (P6; matches the SPEC's own "enrichment toward secondary maths and coding".)
- "Inspired by the model-drawing and heuristic methods used in Singapore primary maths" (the bar model and heuristics are in the lessons; I could not verify the MOE wording of the processes, so avoid "follows the MOE mathematical processes").
- "Independent; not run by or affiliated with MOE."

**Do not say:**

- "aligned to the MOE syllabus", "MOE-approved", "follows the MOE curriculum", "prepares for PSLE / Secondary 1", "covers the P4 / P5 / P6 syllabus", "GEP-style" or "GEP preparation" (I verified none of these and several are false: ratio, percentage, circles, fraction division are untouched at P6 and the lessons use secondary topics early).
- "Computational thinking aligned to MOE / Code for Fun" (not verified).

---

## 6. What I could not verify

1. The MOE PDF itself (every URL 404 or empty; SEAB 403). All learning-outcome quotations are paraphrases of secondary sources or of search-engine extracts. A person with the PDF should check, at minimum:
   - P4: is the 8-point compass absent; are pie charts present; rounding to 10 / 100 / 1000 (which year); order of operations with brackets (which year); angle notation (which year); are common factors / multiples P4.
   - P5: dividing a proper fraction by a whole number (P5 or P6); fraction x fraction (P5 or P6); percentage discount, GST, percentage change and "find the whole" (P5 or P6); is the water-level-rise in a tank P5 or P6; angle sum of a quadrilateral.
   - P6: the exact algebra outcomes and the exact word "average"; whether primes or negative numbers appear anywhere before Sec 1.
2. Whether a revision newer than "updated December 2024" exists. The MOE landing page was "Last Updated: 14 Aug 2026" but I could not read its Mathematics links.
3. The Secondary 1 syllabus itself (MOE). My Sec 1 calls rest on two schools' content outlines and a search summary; "Sec 1 vs Sec 2" for probability, number-pattern formulas, polygon angle sum, and median / mode is unknown. Permutation / combination year is unknown.
4. The statement of the mathematical processes (reasoning, communication, applications, modelling) and the list of heuristics. I cannot say MOE's wording; no claim in this report depends on it.
5. Any MOE page on computational thinking / Scratch. I only saw IMDA Code for Fun and school pages in search results; the IMDA page itself did not load.
6. Whether Speed moved to Sec 1 or Sec 2 or was dropped (sources conflict).
7. The Level 4 to 6 workbook figures (diagrams) were not inspected, only text and captions.
8. Student outcomes: this is a topic and wording check, not a measure of whether children find the lessons fit the school year.
