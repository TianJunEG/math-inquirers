# Verification report: MOE syllabus (Oct 2025) against our placements

Date: 2026-10-22. Source: "Mathematics Syllabus, Primary One to Six" (2021 syllabus, footer "Updated: Oct 2025", 50 pages), supplied by the owner and read in full. Page numbers are PDF pages. Structured summary: `docs/moe/syllabus_by_level.md`.

Checked: `docs/audit/moe_alignment_p1_p3.md`, `moe_alignment_p4_p6.md`, `intl_mapping_*` (Singapore references), `docs/audit/journey_p6.md`, the Singapore rows (`docs/syllabus_map/add_singapore.py`, `intl_rows.json`), the tier rows (`build_tier_rows.py`, `tier_rows.json`), the static page `website/syllabus/` and `website/dist/syllabus/`, and all six term plans `docs/terms/level_N_year_plan.md`. Lesson content files were not edited, and neither were the per-level `SPEC.md` files: the SPEC lines flagged in the table (P4 SPEC compass; P5 SPEC "percentage increase and decrease known" vs "P6"; P6 SPEC "rate and speed") still need a one-line owner edit.

**Headline.** 38 wrong or imprecise claims corrected (table A), about two dozen provisional flags confirmed as written (table B). The P1 to P3 audit was already accurate (two corrections). The provisional work was P4 to P6, where the biggest errors were: order of operations is **P5, not P4**; adding unlike fractions (up to two denominators) is **P4, not P5**; fraction x fraction is **P5, not P6**; **speed is in no primary year**; and **P5 has no Statistics strand**.

## A. Corrections (old claim, verified claim)

| # | Where | Old | New | Page |
|---|---|---|---|---|
| 1 | P4-P6 audit L4 lesson 3; L5 lesson 1; SG row 4.3 and 5.1; tier row L4; L3 plan lesson 32; L4 plan 1.2; L5 plan lesson 1 | Order of operations and brackets met in P4 (or "P3/P4/P5, unverified") | **P5** (Whole Numbers, Four Operations 2.2, 2.3). Level 4 lesson 3 is a P5 preview. SG row 4.3 changed SAME to LATER | 41 |
| 2 | P4-P6 audit L4 lesson 4 and section 3; tier row L4; SG row 4.4; L4 plan 2.4 and section 3 | Adding unrelated fractions (1/3 + 1/4) "probably P5", needs swapping | **P4** (Fractions 3.1: denominators up to 12, at most two different). Four Challenge items are on-level; swap advice withdrawn | 37 |
| 3 | P4-P6 audit L5 lesson 2; tier row L5; SG row 5.2; L5 plan lessons 3; L6 plan lesson 11 | Fraction x fraction "likely P6" | **P5** (Fractions, Four Operations 2.2 to 2.5) | 41 |
| 4 | L6 plan lesson 11 | Division by a fraction "P5/P6 [to verify]" | **P6** (dividing a proper fraction by a whole number 1.1; a whole number or proper fraction by a proper fraction 1.2); improper or mixed divisors not listed | 43 |
| 5 | L4 plan 2.6 | Add/subtract mixed numbers in P4 | **P5** (Fractions 2.1). P4 has mixed numbers and improper fractions only | 37, 41 |
| 6 | L4 plan 2.7 | Unit conversion with decimals "[UNVERIFIED P4]" | Decimal-form unit conversion is **P5** (Decimals 1.2); compound-unit conversion is P3 | 36, 41 |
| 7 | L4 plan 3.2; P4-P6 audit L4 lesson 6 | Angles on a line and around a point "edge of P4/P5"; unknown angles in squares and rectangles on-level | **P5** (Angles 1.1 to 1.4). P4 is notation, measuring, drawing only. Lesson 6 unknown-angle items are ABOVE (P5) | 39, 42 |
| 8 | P4-P6 audit L5 lesson 5; L5 plan lesson 12; L6 plan lesson 15 | Tank problems "P5 or P6 [UNVERIFIED]" | Liquid volume in a tank and l/ml to cm3 are **P5**; height from volume and base area (water level after pouring) is **P6** | 42, 44 |
| 9 | L6 plan lesson 15 | "Surface area (P6)" | **Not in the primary syllabus** | all |
| 10 | P4-P6 audit L5 lesson 8; L5 plan lesson 28 | Angle sum of a quadrilateral "[UNVERIFIED]/[check]" | **Not in the primary syllabus**; only the triangle sum (2.2) is | 42 |
| 11 | L5 plan lesson 14 | Parallelogram and trapezium area "[check]" | **Not in the primary syllabus** (only triangle area; circles at P6) | 42, 44 |
| 12 | L5 plan lesson 29 | Symmetry a "P6 preview" | **P4** (Line Symmetry 3.1 to 3.3), so a spiral. Diagonal properties are excluded at P4; tiling not in syllabus | 39 |
| 13 | L2 plan Term 3 lesson 6 | Fold symmetry "Beyond MOE" | **P4 preview** | 39 |
| 14 | P4-P6 audit section 3 and 4; journey_p6.md; L6 plan lesson 13; P6 SPEC line 23; L5 audit lesson 6 | Speed "P6 content" / "moved to Sec 1 or dropped (sources conflict)" | The word **speed appears nowhere** in the primary syllabus. Rate is P5 | 41 |
| 15 | journey_p6.md warm-up W2 | Discount is a P6 topic | **P5** (Percentage 1.4: discount, GST, annual interest). The "wrong 1 time in 5" figure is overstated | 41 |
| 16 | P4-P6 audit L5 lesson 7; L5 plan lesson 21 | Discount, GST, % change all "P5 or P6, unconfirmed" | Discount, GST, interest **P5**; find the whole, % increase/decrease **P6** | 41, 43 |
| 17 | P4-P6 audit section 4 (P5 and P6 rows); L5 plan coverage; L6 plan coverage | Statistics at P5 "[UNVERIFIED]"; pie charts listed as a P6 gap | **No Statistics strand in P5 Standard**; pie charts are **P4**; average P6 only | 40, 44 |
| 18 | P4-P6 audit section 4 (P4 row) | Perpendicular/parallel lines and 24-hour clock as P4 gaps | Both are **P3** | 36 |
| 19 | L5 plan gap (a), open question 3; P5 SPEC "known" line | Ratio taught in some P5 schemes; percentage change "known" | Ratio is **P6 only** (1.1 to 1.7, whole numbers only); % change P6 | 43 |
| 20 | L5 plan gap (b); lesson 2 | Long division by a 2-digit number is drilled, P5 written methods | **No 2-digit divisor in any primary year**; P4 stops at 4 digits by 1 digit and 3 by 2 for multiplication; P5 adds only x and / by 10, 100, 1000 | 37, 41 |
| 21 | L4 plan 2.1 | "2-digit x 3-4 digit" | P4 limit is 4 by 1 and 3 by 2; 2 by 4 goes beyond | 37 |
| 22 | P1-P3 audit L3 lesson 6 (Stretch s8) | "1/2 + 1/4 + 1/8" ABOVE (P4) | **NOT IN**: P4 allows at most two different denominators and no later year relaxes it | 37 |
| 23 | P1-P3 audit L1 lesson 7, M10 | "Diagonal" ABOVE (P4) | **NOT IN**: P4 says "excluding diagonal properties" | 39 |
| 24 | L3 plan lesson 26 | "Before-after / unchanged difference ABOVE, P4-P5 [UNVERIFIED]" | Not a syllabus outcome (method not named); arithmetic P3 to P4 | 13, 35, 37 |
| 25 | L3 plan lesson 25 | "Bar model times as many ABOVE, P4" | x and / word-problem arithmetic is P3; bar-model method not named | 35 |
| 26 | L3 plan lesson 7 | Area of rectilinear figures at P3 | Only perimeter of rectilinear figures and area of rectangle/square at P3; composite area P4 | 36, 39 |
| 27 | L3 plan lesson 32 and gap (e) | Brackets "ABOVE, P4" | **P5** (same as #1) | 41 |
| 28 | L1 plan lessons 20, 1, 2 | Tables 6 to 8 "beyond P1"; common multiples and letters "beyond P1" | Tables 6 to 9 are **P3**; common multiples **P4**; letters **P6** (precision, no wrong placement) | 35, 37, 43 |
| 29 | P4-P6 audit L6 lesson 4; L6 plan lessons 4, 19, 20 | Brackets with letters "Sec 1/2 [SECONDARY]" | P6 Algebra 1.3 says "excluding brackets"; both-sides equations not stated | 43 |
| 30 | L6 plan lesson 25 | HCF and LCM "Sec 1 [to verify]" | Common factors and multiples are **P4**; the HCF/LCM names and prime factorisation are not in primary | 37 |
| 31 | L6 plan coverage table | Decimals "Gap: no decimal lesson" | P6 Standard has **no decimals strand**; not a P6 gap | 43 to 44 |
| 32 | L6 plan lesson 24 | Powers and roots "Sec 1" | Only the root signs for a side from an area or an edge from a volume are P6 (2.5); powers not named | 44 |
| 33 | P4-P6 audit section 1 | Latest version "Dec 2024, unreadable" | The **Oct 2025** PDF; roll-out footnote confirms P6 on the 2021 syllabus from 2026 | 30 |
| 34 | Singapore rows (add_singapore.py, intl_rows.json) | 13 rows carried "not fully confirmed" tags; row 4.3 SAME | Only 3 remain (6.1, 6.6, 6.7: secondary year not read); 4.3 LATER; 26 notes reworded (e.g. 5.4, 5.5, 5.6, 5.7, 5.8) | various |
| 35 | Tier rows L3 to L6 (build_tier_rows.py, tier_rows.json) | L3 "three-term fractions" as NEW; L4 AHEAD = unrelated-denominator fractions; L5 "may already be P5" wording; L6 years unconfirmed | Reworded: three-term fractions moved to AHEAD; L4 AHEAD = order of operations and letters; L5 AHEAD includes water level and P6 percentage items; L6 brackets excluded | 37, 41, 43 |
| 36 | Static page (build_static.py to website/syllabus and dist) | "some placements could not be confirmed"; "years partly unconfirmed" | Singapore now checked against the text; only 3 secondary placements unconfirmed; other places unchanged | n/a |
| 37 | L4 plan 3.7; P4-P6 audit L4 lesson 1 | Cube stacks/views as P4 nets topic; locker/exactly-3-factors treated as on-topic | Unit-cube building is P5; views not named; the P4 factor outcome is limited to 1-digit factors within 100 | 37, 42 |
| 38 | L6 plan lessons 16, 17 | Angles between parallel lines "P6 and Sec 1"; rotational symmetry "Hong Kong P6" | Line/point/vertically opposite angles P5, composite figures P6; parallel-line angles, rotation, tessellation not in primary | 42, 44 |

## B. Provisional flags confirmed as written (no change in meaning)

Compass turns not in 2021 P4 (confirmed, no turns outcome in any year); pie charts P4 (p. 40); nets P4 (p. 39); rounding to 10/100/1000 P4 (p. 37); sign for approximately P4; angle notation P4 (p. 39); 24-hour clock P3 (p. 36); factors and multiples P4 (p. 37); fraction of a set P4 (p. 37); improper and mixed numbers P4 (p. 37); decimals to 3 places P4 (p. 38); rate P5 (p. 41); area of triangle P5 (p. 42); percentage P5 (p. 41); angles, triangle and quadrilateral families P5 (p. 42); algebra letters P6 (p. 43); average P6 (p. 44); ratio P6 (p. 43); P6 circles (p. 44); primes, negatives, probability, coordinates, median/mode absent from primary (confirmed); bar model not named (p. 13); pentagon/hexagon not named; fraction division by a whole number is P6 so "(Preview of P6)" on L5 lesson 2 is right; the P1 to P3 outcome tables.

## C. What the syllabus says that our programme misses or only touches

Holiday programme (Levels 1 to 6), by outcome:

- **P1** (pp. 31 to 32): place value and number words (1.2, 1.3), comparing numbers (1.5), ordinal symbols to 10th (1.7), adding and subtracting within 100 and algorithms (2.5, 2.6), mental calculation (2.7), multiplication within 40 and division within 20 (3.3, 3.4), all of Time (2.1 to 2.4), drawing a line to the nearest cm (1.4), half and quarter circles and copying on a grid. (The P1 term plan closes these in Terms 2 to 4.)
- **P2** (pp. 33 to 34): number words, mental calculation, using the division sign as a topic, telling time to the minute and converting hours to minutes, patterns by size/colour/orientation, the sphere, classifying all five 3D shapes, reading picture graphs with scales as a dedicated topic.
- **P3** (pp. 35 to 36): counting in hundreds and thousands, number words, mental calculation of two 2-digit numbers, 3-digit by 1-digit algorithms, simplest form, km, seconds (none), bar graphs with different scales (one item).
- **P4** (pp. 37 to 40): **pie charts**; fraction add/subtract (up to two denominators) as a skill; decimal x and / by a 1-digit number, decimal quotients, accuracy rounding; 3-by-2 and 4-by-1 algorithms; nets of prisms and pyramids and drawing 2D representations; drawing rectangles and squares.
- **P5** (pp. 41 to 42): decimal x / by 10, 100, 1000 and decimal-form unit conversion; mixed number add/subtract and mixed x whole; annual interest; unit-cube building and isometric grid drawing; litre to cm3.
- **P6** (pp. 43 to 44): fraction division (one lesson in the term plan, none in the holiday course); ratio; percentage change and find-the-whole; circles; inverse volume problems; unknown angles in composite figures; average (mean only). Algebra covered.

Term plans: Level 1 plan covers every P1 strand. Level 2 plan covers P2. Level 3 plan covers P3 (thin on seconds and perpendicular/parallel). Level 4 plan misses decimal quotients and accuracy rounding, 3-by-2 written multiplication as a taught skill, prism/pyramid nets, rectangle/square drawing, fractions-decimals conversion (Decimals 1.3, 1.4); pie charts one lesson. Level 5 plan misses annual interest, isometric grid drawing, mixed-number operations as a taught skill. Level 6 plan: one lesson each on the big P6 topics (ratio, percentage, fraction division, circles, volume).

## D. What we teach that is not in the syllabus (enrichment or preview)

Not in any primary year (enrichment): Venn diagrams, logic grids, sorting from clues, growing patterns with a rule, triangular numbers, number machines, magic squares/triangles and cryptarithms, "how many ways" counting and handshakes, probability, pentagon/hexagon/octagon names, non-standard units, clock-hand angles, compass turns (removed), quadrilateral and polygon angle sums, parallelogram/trapezium area, surface area, painted cubes, tessellation and rotation, parity and pigeonhole, modular arithmetic and ciphers, primes and prime factorisation, negative numbers, nth-term formulas, powers, binary, scale factors, inequalities, coordinates, linear graphs, median and mode, scatter plots, speed and distance-time graphs, Scratch and Python coding.

Preview of a later primary year (stated in each lesson table): common multiples (P4) in Levels 1 to 3; picture graph scales (P2) in Level 1; remainders (P3), odd/even (P2), fraction of a set (P4), equivalent fractions (P3), nets (P4), finding start times (P3) in Level 2; fractions in a bar, composite area, symmetry, factors and multiples (P4) in Level 3; order of operations (P5), unknown angles (P5), mixed-number add/subtract (P5), decimal unit conversion (P5), angles on a line (P5) in Level 4; fraction division, percentage change, find the whole, average, tank levels, letters (all P6) in Level 5; Level 6 is wholly past the primary syllabus apart from algebra and average.

## E. Not resolved

- Secondary 1 and 2 years for primes, negatives, probability, polygon angle sums, nth term, median/mode (the primary syllabus has none; the secondary years come from school outlines).
- Whether MOE textbooks name the bar model, number bond, heuristics (the PDF does not).
- School conventions (time layout, remainder layout, cents symbol).
- Whether an obtuse-triangle height is part of P5 Area of Triangle 1.1 (not spelled out).
- Whether a revision newer than Oct 2025 exists.

## F. Dashboards

See the final line of the session report: artifact status for 'Syllabus fit for parents', 'Syllabus map by level' and 'tier map' is recorded in `docs/syllabus_map/README.md`.
