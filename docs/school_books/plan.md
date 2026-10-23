# School early-finisher puzzle books: product and production plan

Status: planning document only (23 Oct 2026). No lesson, tool or website file is changed by this plan. Nothing here is decided until the owner answers section 19.

Sources used: `docs/terms/owner_decisions.md` (all addenda, including 5 to 8 of 22 Oct 2026), `docs/moe/syllabus_by_level.md`, `docs/moe/verification_report.md`, `docs/syllabus_map/`, `docs/books/school_paper_wording_patterns.md`, `docs/sasmo/*_analysis.md` (puzzle TYPE inspiration only), the existing p1..p6 holiday workbooks, `wbstyles/`, `print/make_print_pdfs.py`, `p3/wb_pdf.py`, `docs/printing/quote_request.md`.

---

## 1. What we are building (product definition)

**Name (working):** "Early Finisher Puzzles, Primary N" (N = 1 to 6). Final name is an owner decision (section 19).

**One line:** a book of single-page maths puzzles that a pupil can pick up and do alone when they finish class work early, each puzzle practising a topic the school teaches at that Primary level, each checking itself, each with a topic tag the teacher can read at a glance.

**It is a different product from the home extension workbooks (addenda 5 and 6, 7):**

| | Home extension workbook | School early-finisher book |
|---|---|---|
| Buyer | Parent (shop, by level) | School (teacher, HOD, procurement) |
| Reader | Child with a parent, self-study | Pupil in class, minutes at a time, teacher nearby but busy |
| Content | Holiday-program question types, may go beyond the syllabus | Puzzles on the topics the school teaches at that level, no content beyond the syllabus |
| Voice | Parent/child, Mi branding | School-neutral, teacher-facing front matter, minimal branding |
| Structure | Sections with worked examples, weekly pace | Standalone pages, any order, no pacing |
| Answers | Full answers with short explanations | Teacher key plus built-in self-check on every page |
| Licence | Single family | School photocopy licence / bulk pricing |
| Overlap rule | Question types may overlap; the questions themselves must never be identical to the home book. Enforced by script (section 11). | |

## 2. Audience and how it is used

**Teacher (the buyer).** Expects: no marking; a page she can hand out in ten seconds without explaining; a topic label so she can match the page to what she has just taught; two difficulty levels so she can choose for a strong or a slower early finisher; a key she may never need; a licence that lets her photocopy.

**Pupil.** Finishes the set work early, takes a page from the tray (or is handed one), reads it unaided, works in 5 to 15 minutes, checks it themselves using the built-in check, corrects, and puts it back or shows the teacher a completed check strip. Reading level must be at or below the school-paper level for the year (section 11).

**Classroom patterns we design for:** (a) page tray at the back of the class; (b) the teacher hands a single photocopied page to a pupil; (c) a "puzzle folder" kept for wet-weather or relief-teacher cover; (d) occasional whole-class use at the end of a topic. We do not design for homework, tests, grading or levelling.

**What the teacher does not have to do:** mark, explain instructions, hunt for what is correct. What she may do: spot-check (section 8).

## 3. Format

- **Page size:** A4 portrait, one puzzle per page, printed one side only in the master file so any page can be photocopied alone (no content on the back; the back of a printed copy stays blank). Double-sided master is not offered.
- **Margins:** 15 mm all sides, 20 mm left if the school punches holes; puzzle area must be photocopy-safe in black and white (no meaning carried by colour alone; mono-safe test in QA).
- **Page count per pupil book:** 40 puzzle pages (20 topics x core page and stretch page), plus a 2-page "How to use" and a contents/topic-tag page, 43 pages total. Teacher book: same 43 pages as a reduced thumbnail plus the key and notes, about 24 pages.
- **Why 40:** about one puzzle a fortnight over a 40-week year, with room for choice within each unit; reuses the 40-lessons-per-level rhythm already in `docs/terms`.
- **Digital PDF vs printed:**
  - Digital PDF per level (pupil book + teacher book in one licensed bundle): the main product, because the licence is a photocopy licence. Delivered by download link after payment (same route as soft-copy home books).
  - Printed copies: optional, bound or loose-leaf, ordered through the existing print route; a loose-leaf set suits trays. Offered at higher price (section 14).
  - Each page carries a small footer licence line (section 13) and its page code (e.g. P3-07C).
- **Page independence rule:** a page never refers to another page, to a worked example elsewhere, to a lesson, to Mi or to a class. A needed instruction is printed on the page (3 lines max).

## 4. Series structure per level

- Six books, Primary 1 to Primary 6, each matched to the same-numbered Primary level. P5 and P6 follow the Standard track; the Foundation track adds nothing new (`syllabus_by_level.md`, Foundation section), so no separate Foundation edition.
- Each book: 10 units. Each unit = one MOE topic area for that level. Each unit has 2 sub-topics, each with a core page (C) and a stretch page (S): 4 pages per unit, 40 pages.
- Units follow the syllabus strands for the level (Number and Algebra, Measurement and Geometry, Statistics), in a suggested but not required order that follows the usual school sequence. Order is free; the contents page lists pages by strand.
- **Two tiers only, neutral labels:** "Core" and "Stretch" would be acceptable neutral labels; alternative: a single star and a double star. Default: one star and two stars, with the line "Pages with one star practise the topic as taught. Pages with two stars use the same topic with more steps." No "easy", "hard", "gifted", "challenge". Stretch stays inside the syllabus topic (more steps, bigger numbers within the level's number range, two ideas combined), never contest-extension.
- **Puzzles must practise the school topic, not extend it.** Rule: every puzzle's solution path uses only skills in the syllabus outcome(s) cited on that page (section 6 mapping). The audit checks "could a pupil who has just learned this outcome do each step?" Contest-style items listed in owner decision 6 (digit-sum tests, gaps and posts, chance, cryptarithms, pairing sums, worst-case counting) are excluded outright. The `docs/moe/verification_report.md` section D list (Venn, number machines, probability, parity beyond P2, pigeonhole, etc.) is not used as content, only logic puzzles as a form (logic grids and magic squares are puzzle formats, not topics; the arithmetic inside them is on-syllabus).
- **Syllabus facts that constrain content** (from `syllabus_by_level.md`): no prime numbers, negatives, probability, coordinates, speed; symmetry and nets only from P4; order of operations and brackets only from P5; letters only at P6; no statistics at P5; ratio P6 only; fraction division P6 only; no 2-digit divisor anywhere.

## 5. Puzzle types and which strands they suit

| Puzzle type | Best strands | Notes |
|---|---|---|
| Logic grid (who/what/when) | Measurement (time, length, mass, money), comparison and ordering, fractions | Clues use only topic comparisons ("longer than", "earlier than") |
| Magic square / sum square | Whole numbers (add/subtract, tables), money, fractions (like), decimals | Constant is the check |
| Number riddle ("I am a number...") | Place value, factors/multiples, tables, rounding, odd/even | 3 to 5 clues, unique answer |
| Code-breaker (answers decode to a word) | Everything with computed answers | Principal self-check device |
| Pattern chain / sequence | Number patterns P1 to P4, shape patterns P2 | Missing terms; rule stated in pupil words |
| Path / maze (route of correct answers) | Facts and conversions, equivalent fractions, tables, units | Unique route; wrong turn gets stuck |
| Balance / equation puzzle | Add/subtract, mult/div relationships, P6 simple equations, P5 brackets | Pans or boxes |
| Shape and measurement puzzle | Geometry, area, perimeter, volume, angles | Grid drawing, tile fitting, find missing side |
| Picture-fill / colour-by-answer | Graphs, 2D shapes, P1-P2 number | Answers decide colour; picture is the check |
| Graph detective | Picture/bar/line/pie graphs, average | Complete the graph from clues; totals must match |

## 6. Topic-to-page mapping (draft)

Page counts are core + stretch pages. Each row = one unit, 4 pages (2 sub-topics x C and S) unless a count is shown. Outcome references use the syllabus's own numbering and page numbers from `docs/moe/syllabus_by_level.md`. "Strand" NA = Number and Algebra, MG = Measurement and Geometry, ST = Statistics. Totals are 40 per level. The mapping is a draft to be re-checked by the audit against the syllabus PDF before any page is written.

### Primary 1 (syllabus pp. 31 to 32)

| # | Unit | Syllabus outcomes | Puzzle types | Pages |
|---|---|---|---|---|
| 1 | Counting and numbers to 100 | NA Whole Numbers 1.1 to 1.3 (p. 31) | code-breaker, picture-fill, path | 4 |
| 2 | Comparing and ordering numbers | 1.4, 1.5 | logic grid, path | 4 |
| 3 | Number patterns | 1.6 | pattern chain, code-breaker | 4 |
| 4 | Ordinals (first to tenth) | 1.7 | logic grid (queues) | 4 |
| 5 | Addition and subtraction within 20 and 100 | 2.1 to 2.7 | magic square, balance, number riddle | 6 |
| 6 | Multiplication within 40 and division within 20 | 3.1 to 3.4 | path, riddle, picture-fill | 4 |
| 7 | Money (cents to $1, dollars to $100) | NA Money | logic grid, balance | 4 |
| 8 | Length and time | MG Measurement 1.1 to 1.4, 2.1 to 2.4 (p. 32) | path, logic grid | 4 |
| 9 | 2D shapes and figures | MG Geometry 1.1 to 1.4 | picture-fill, shape fitting | 4 |
| 10 | Picture graphs | ST (p. 32) | graph detective | 2 |
| | | | **Total** | **40** |

(Unit 5 has 6 pages because addition and subtraction carry the most outcomes at P1; unit 10 has 2 pages because the strand has a single outcome.)

### Primary 2 (pp. 33 to 34)

| # | Unit | Outcomes | Puzzle types | Pages |
|---|---|---|---|---|
| 1 | Numbers to 1000, place value, patterns | Whole Numbers 1.x | code-breaker, riddle, pattern chain | 4 |
| 2 | Odd and even | 1.6 | riddle, path | 2 |
| 3 | Add and subtract to 3 digits | algorithms, mental calculation | magic square, balance | 6 |
| 4 | Tables of 2, 3, 4, 5, 10; x and division | multiplication and division | path, riddle, code-breaker | 6 |
| 5 | Fractions: part of a whole, compare, add/subtract like fractions | NA Fractions 1.1 to 2.1 | logic grid, picture-fill, balance | 4 |
| 6 | Money in dollars and cents | NA Money | logic grid, magic square | 4 |
| 7 | Length, mass, volume | MG Measurement | path, logic grid | 4 |
| 8 | Time to the minute | Measurement time | logic grid, path | 4 |
| 9 | Shape patterns and 3D shapes | Geometry 1.1 and 3D | pattern chain, riddle | 4 |
| 10 | Picture graphs with scales | ST (p. 34) | graph detective | 2 |
| | | | **Total** | **40** |

### Primary 3 (pp. 35 to 36)

| # | Unit | Outcomes | Puzzle types | Pages |
|---|---|---|---|---|
| 1 | Numbers to 10 000, place value, patterns | Whole Numbers 1.x | riddle, code-breaker, pattern chain | 4 |
| 2 | Add and subtract to 4 digits, mental calculation | algorithms | magic square, balance | 4 |
| 3 | Tables of 6, 7, 8, 9; mental calculation | multiplication facts | path, code-breaker | 4 |
| 4 | Division with remainder; x and / algorithms | 3.3, 3.4 | riddle, balance | 4 |
| 5 | Fractions: equivalent, simplest form, compare, add/subtract related | Fractions 1.1 to 2.1 | maze (equivalent fractions), logic grid | 6 |
| 6 | Money: add and subtract in decimal notation | NA Money | logic grid, magic square | 2 |
| 7 | Length, mass, volume; compound units; km, ml | MG Measurement | path, code-breaker | 4 |
| 8 | Time: seconds, start/finish/duration, 24-hour clock | Time 2.1 to 2.3 | logic grid, path | 4 |
| 9 | Area and perimeter | Area and Perimeter (p. 36) | shape/tile fitting, riddle | 4 |
| 10 | Angles, perpendicular and parallel; bar graphs | Geometry, ST (p. 36) | shape puzzle, graph detective | 4 |
| | | | **Total** | **40** |

### Primary 4 (pp. 37 to 40)

| # | Unit | Outcomes | Puzzle types | Pages |
|---|---|---|---|---|
| 1 | Numbers to 100 000, rounding, approximation | Whole Numbers 1.1 to 1.6 | riddle, code-breaker | 4 |
| 2 | Factors and multiples | 2.1 to 2.5 (1-digit factors within 100) | riddle, path, logic grid | 4 |
| 3 | Four operations (4 by 1, 3 by 2 digits; division) | 3.1, 3.2 | magic square, balance | 4 |
| 4 | Fractions: mixed numbers, improper fractions, of a set, add/subtract | NA Fractions (p. 37) | maze, balance, logic grid | 6 |
| 5 | Decimals to 3 places; operations | NA Decimals (p. 38) | magic square, path, code-breaker | 6 |
| 6 | Area and perimeter: missing sides, composite figures | MG (p. 39) | shape puzzle | 4 |
| 7 | Angles: notation, measure, draw | MG Geometry (p. 39) | shape puzzle, code-breaker | 2 |
| 8 | Rectangle, square, line symmetry | Geometry (p. 39) | picture-fill, shape puzzle | 4 |
| 9 | Nets and solids | Geometry (p. 39) | shape puzzle, riddle | 2 |
| 10 | Tables, line graphs, pie charts | ST (p. 40) | graph detective | 4 |
| | | | **Total** | **40** |

### Primary 5, Standard (pp. 41 to 42)

| # | Unit | Outcomes | Puzzle types | Pages |
|---|---|---|---|---|
| 1 | Numbers to 10 million; x and / by 10, 100, 1000 | Whole Numbers | code-breaker, path | 2 |
| 2 | Order of operations and brackets | 2.2, 2.3 | balance, magic square | 4 |
| 3 | Fractions and division; fraction as decimal | 1.1, 1.2 | path, logic grid | 4 |
| 4 | Mixed numbers; fraction x whole number and x fraction | 2.1 to 2.5 | balance, maze | 6 |
| 5 | Decimals: x and / by 10, 100, 1000; unit conversion | Decimals 1.1, 1.2 | path, code-breaker | 4 |
| 6 | Percentage: part, of a whole, discount, GST, interest | Percentage 1.x | logic grid, balance | 4 |
| 7 | Rate | Rate | logic grid, riddle | 2 |
| 8 | Area of triangle; composite figures | MG Area (p. 42) | shape puzzle | 4 |
| 9 | Volume of cube and cuboid; litre and cm3 | Volume 2.1 to 2.6 | shape puzzle, riddle | 4 |
| 10 | Angles: line, point, vertically opposite; triangles; parallelogram, rhombus, trapezium | Geometry 1.1 to 1.4 | shape puzzle, code-breaker | 6 |
| | | | **Total** | **40** |

(No Statistics unit at P5: the Standard syllabus has none.)

### Primary 6, Standard (pp. 43 to 44)

| # | Unit | Outcomes | Puzzle types | Pages |
|---|---|---|---|---|
| 1 | Fraction division (by a whole number; by a proper fraction) | Fractions 1.1, 1.2 | maze, balance | 4 |
| 2 | Percentage: find the whole; percentage change | Percentage 1.1, 1.2 | logic grid, balance | 4 |
| 3 | Ratio (whole numbers): equivalent, simplest form, share, missing term, ratio and fraction | Ratio 1.1 to 1.7 | path, balance, riddle | 8 |
| 4 | Algebra: letter notation, simplify (no brackets), substitute, simple equations | Algebra 1.1 to 1.5 | balance, code-breaker, magic square | 6 |
| 5 | Circle: area and circumference; semicircle and quarter circle | MG Area (p. 44) | shape puzzle | 4 |
| 6 | Composite figures | MG Area (p. 44) | shape puzzle | 2 |
| 7 | Volume: missing dimension, cube edge, base area | Volume 2.x | riddle, shape puzzle | 4 |
| 8 | Unknown angles in composite figures | Geometry (p. 44) | shape puzzle, code-breaker | 4 |
| 9 | Average: total, number, mean | ST (p. 44) | graph detective, logic grid | 2 |
| 10 | Mixed revision across P1 to P5 outcomes (those re-met in P6) | spiral | mixed | 2 |
| | | | **Total** | **40** |

Spot-check: every cited outcome exists in the summary; none of the "not in the syllabus anywhere" list is used. P6 unit 10 is optional and may be dropped to 38 pages if the owner prefers no revision page.

**Teacher-facing topic tag on every page:** "Topic: Fractions - equivalent fractions (matches the P3 syllabus topic: Fractions)". The syllabus outcome numbers (e.g. "NA Fractions 1.1") are in the teacher book only; pupil pages show the plain topic name. Mapping stored per page in a data file (section 9) so the contents page and teacher book are generated, not typed.

## 7. Puzzle template catalogue

Each template is a generator with parameters, a verified solver, a difficulty tier setting and a self-check device (section 8). Tier is controlled by parameters, never by a different template.

| ID | Template | Parameters that set core vs stretch | Typical levels |
|---|---|---|---|
| T01 | Logic grid 3x3 / 4x4 | Core: 3 items, 5 clues; Stretch: 4 items, 7 clues | P1 to P6 |
| T02 | Magic square 3x3 (line sums equal) | Core: 3 givens + visible magic number; Stretch: 2 givens, hidden constant | P1 to P6 |
| T03 | Number riddle (3 to 5 clues) | Core: 3 clues; Stretch: 5 clues, range wider | P1 to P4 mainly |
| T04 | Code-breaker (answers to letters) | Core: 6 sums, one-to-one key; Stretch: 8 sums, two-step | P1 to P6 |
| T05 | Pattern chain / sequence | Core: one rule; Stretch: two alternating rules (within level number range) | P1 to P4 |
| T06 | Maze / path of correct answers | Core: 6x6 cells; Stretch: 8x8, decoys | P1 to P6 |
| T07 | Balance / equation | Core: 2 pans, one unknown; Stretch: chained balances | P1 to P6 |
| T08 | Shape and measurement (grid drawing, tile fit, missing side) | Core: integer sides small; Stretch: composite | P3 to P6 |
| T09 | Picture-fill (colour/shade by answer) | Core: 12 cells; Stretch: 20 cells | P1 to P4 |
| T10 | Graph detective | Core: one missing bar; Stretch: totals and two missing values | P1 to P4, P6 |
| T11 | Cross-number (small crossword of numbers) | Core: 5 entries; Stretch: 8 entries | P2 to P6 |
| T12 | Number-chain / domino loop | Core: 6 pieces; Stretch: 8 | P1 to P4 |

Recommended coverage per book: at least 6 different templates, no template more than 8 times, each used at both tiers.

## 8. Self-checking design (owner addendum 8)

**Rule SC-1.** Every puzzle page has at least one built-in check a pupil can use alone, and the check must be printed on the page in plain words in a "Check it" strip (1 to 2 lines). A page without a verified check is not published.

**Rule SC-2.** The check must reveal a wrong answer without revealing the right one (it says "something is off", not "the answer is X"). The pupil is told "If your check does not work, look for the mistake and try again."

**Rule SC-3.** The check must not be a copy of the answers printed upside down on the page (no printed answer key on the page; that defeats the puzzle).

### 8.1 Mechanism catalogue

| Code | Mechanism | How it works | Fits |
|---|---|---|---|
| K1 | Code word | Each answer maps to a letter; the letters spell a word | T04, T06, T11 |
| K2 | Hidden picture | Answers decide which cells to colour; a clear picture appears if all are right | T09, T06 |
| K3 | Check-sum | A stated total (row total, grand total, magic number) must match | T02, T10, T12 |
| K4 | Grid consistency | The answer must satisfy every clue/row/column; contradictions are visible | T01, T11 |
| K5 | Unlock | The answer to puzzle part 1 is needed to read clue 2; a wrong first answer makes clue 2 impossible | T03, T08 |
| K6 | Route closes | The path from Start must reach Finish; a wrong cell dead-ends | T06 |
| K7 | Built-in verification | Reverse operation: "Put your answer back: does it make the two pans equal?" | T07, T03 |
| K8 | Chain closes | Last piece must connect to the first; the loop only closes if all are right | T12, T05 |
| K9 | Measured check | Draw, then measure/count to confirm (e.g. count squares inside, count the perimeter) | T08 |

### 8.2 Choice per puzzle type

| Template | Primary check | Secondary check |
|---|---|---|
| T01 logic grid | K4 (each row and column has exactly one tick) | K1 (final cells spell a short word) |
| T02 magic square | K3 (all lines equal the printed magic number) | none needed |
| T03 number riddle | K5 or K7 (check by testing all clues) | K1 (letter of answer) |
| T04 code-breaker | K1 | K3 optional |
| T05 pattern chain | K8 or K1 | K7 (apply the rule back) |
| T06 maze | K6 | K1 (letters on the route) |
| T07 balance | K7 | K3 |
| T08 shape/measure | K9 | K3 (total area = sum of parts) |
| T09 picture-fill | K2 | none |
| T10 graph detective | K3 (totals given must match) | K4 |
| T11 cross-number | K4 (across and down agree) | K3 |
| T12 chain | K8 | K1 |

### 8.3 Effects on difficulty and layout

- **Difficulty:** a check removes guessing risk: pupils may trial-and-error against the check. Mitigation: wrong-answer decoys that are plausible mistakes (a code word that is a real but wrong word is forbidden; decoy letters yield nonsense, not another word); stretch pages use checks that need a final computation (K3, K7). Self-checks are tuned so that guessing is no faster than doing: tested by the script (below, V4).
- **Layout:** a fixed "Check it" strip at the page foot, boxed, with a small tick icon, identical across the book so pupils learn where to look; reserved 25 mm height. Code-word boxes sit at the foot; hidden pictures use the main area.
- **Reading load:** check wording is 1 sentence of at most 14 words at P1 to P2, 18 at P3 to P4, 24 at P5 to P6.
- **Teacher key:** the key still lists every answer, but each entry also shows "Check result: the code word is ... / the sum should be ...", so a teacher spot-checks a finished page in seconds by looking at the check strip, not the working. Teacher notes say "routine marking is not needed; if you wish to spot-check, look at the check strip".

### 8.4 Verification by script (check design is tested, not trusted)

For every puzzle the generator outputs the puzzle, answers and check data. `verify_puzzles.py` then runs:

- **V1 uniqueness:** an independent exhaustive/solver search finds exactly one solution (section 9).
- **V2 check-correctness:** with the correct answers the check passes (code word spells the intended word; sum matches; picture is the intended one).
- **V3 error detection:** all single-answer errors (every cell replaced by every other plausible value) and a sample of double errors are tested; the check must fail for at least 98% of single errors and 90% of double errors. Cases where the check still passes are logged; if above threshold, the puzzle is redesigned.
- **V4 guess-resistance:** the check cannot be satisfied by a shortcut (e.g. code word guessable from the first three letters: test by simulated guesses with a dictionary; the word must not be inferable from fewer than half the letters).
- **V5 word safety:** every code word is on a child-safe word list, in plain spelling for the school market (British spelling, as in `school_paper_wording_patterns.md`), no ambiguous or offensive words, and a wrong-letter mix does not form another safe word more than 5% of the time.
- **V6 independence:** the check uses only information printed on the page.

## 9. Tooling

New directory proposed (not created now): `school_books/` with:

- `school_books/gen/` one generator module per template (`t01_logic_grid.py`, ...). Each takes a seed, level and tier and returns a puzzle object: {id, level, unit, tier, template, topic_tag, syllabus_refs, prompt_text, data, solution, check}.
- `school_books/solvers/`: an independent solver per template written separately from the generator (different code path): brute-force/constraint-propagation for grids, magic squares, riddles; BFS/DFS counting routes for mazes; expression evaluation for balance and code-breakers; area/perimeter calculators for shapes. The solver counts solutions up to 2; build fails unless exactly 1.
- `school_books/verify_puzzles.py`: runs V1 to V6 (section 8.4), plus:
  - **V7 range check:** every number, every intermediate value and every unit stay inside the level's range from `syllabus_by_level.md` (encoded as `school_books/data/level_limits.json`; for example P3 numbers to 10 000, tables to 9, fraction denominators up to 12).
  - **V8 reading level:** word count per sentence, word list per level, vocabulary against a per-level allowed-word file built from the school-paper wording guide.
  - **V9 non-copy:** compares each puzzle prompt and parameter set against the home-book question bank (`hp/qbank.json`, p1..p6 content) and the private contest drafts; fails on identical numbers + structure or text similarity above a threshold; contest/book problems are never loaded into the repo's public files by this tool, only compared by hash of normalised structure.
  - **V10 coverage:** the mapping table is complete (every unit has its pages, no outcome uncited, no off-syllabus outcome).
- `school_books/render/`: HTML/SVG templates (reusing the Fredoka/Nunito Sans fonts in `fonts/fonts.css`, the navy `#1B2A49` and teal `#1F7A6F` palette of `wbstyles/gen.py` style A "Exercise book", squared-paper background removed for photocopy; keep a plain white page option) rendered to PDF with Playwright as in `p3/wb_pdf.py`. One page = one HTML section; each page validated at A4 with no overflow.
- `school_books/assemble.py`: builds pupil PDF, teacher PDF, topic index and per-page PDFs (so a school can print one page); stamps licence footer and page codes. Reuse `print/make_print_pdfs.py` only for the optional printed edition; the single-sided independent design uses no gutter shift and no blank-back logic (the blank-back handling of cut-out pages is not needed).
- Data: one JSON record per puzzle in `school_books/puzzles/pN/`, deterministic seeds committed so a puzzle can be regenerated and the verification repeated.

Mono-safe test: render at 150 dpi grayscale and check for contrast and that no clue depends on colour only.

## 10. Page layout specification

A4 portrait, 210 x 297 mm.

1. **Header band (22 mm):** page code (e.g. P3-07 *), puzzle title in 1 to 4 words, tier stars; name line and date line on the right ("Name ____"), no class or score box.
2. **Topic tag line (8 mm):** "Topic: Time - finding how long it takes". Plain words only.
3. **Instructions (10 to 22 mm):** at most 3 short lines, one command per sentence, command verbs following the wording guide (Find, Fill in, Circle, Write; no "work out"), numerals for quantities, box for numbers and short line for words; picture first, then the command.
4. **Puzzle area (about 175 mm):** large squares/boxes (min 10 mm for handwritten digits at P1 to P2, 8 mm later); clear working space for P3+ where the template needs it.
5. **Check it strip (25 mm):** see 8.3.
6. **Footer (10 mm):** licence line (section 13) and the publisher line. Tiny, grey, legible when copied.

Style rules: school-neutral voice (no Mi, no "Hello explorer"), colour used lightly (navy line art, one accent) so black-and-white copying works; fonts large enough for the age (P1 to P2 minimum 14 pt body, P3 to P4 12.5 pt, P5 to P6 11.5 pt); no tiny inline hints; names mixed across ethnic backgrounds as in the school papers; spelling British (Singapore school convention, "sweets", "coloured").

## 11. Quality process

**Authoring rules (original puzzles only).**
1. Every puzzle is generated from our own templates with our own parameters; no puzzle starts from a contest, book, past-paper or website problem. The SASMO analyses and the private notes are inspiration for puzzle TYPES only (what thinking moves exist); no number set, scenario or clue wording is carried over.
2. Authors write from the syllabus outcome, not from a source problem. Each puzzle record contains `source_of_idea: "own"`.
3. V9 non-copy check (section 9) and a human spot-check of 10% of pages.
4. Different questions from the home book: V9 compares to `hp/qbank.json` and the p1..p6 workbook content.
5. Honest tiers: stretch = more steps within syllabus, never new content.
6. No hints beyond the Check strip; no references to class lessons.

**Reading level per level (words per sentence, vocabulary).**

| Level | Max words per sentence | Page instruction max | Vocabulary |
|---|---|---|---|
| P1 | 8 | 2 sentences | Picture-led, 1 clue per sentence, numerals only |
| P2 | 10 | 3 sentences | One compound sentence allowed |
| P3 | 12 | 3 to 4 sentences | Measurement and fraction words as in school papers |
| P4 | 14 | 4 sentences | Topic terms from the syllabus |
| P5 | 16 | 4 sentences | Topic terms |
| P6 | 18 | 5 sentences | Topic terms including ratio, equation |

Wording guide reuse: all command verbs, blanks, comparison words (greater/greatest, never "bigger"), "in all" / "How many more", name conventions and answer frames come from `docs/books/school_paper_wording_patterns.md`; items marked there as "not seen in these papers" are used only if the owner accepts them.

**Independent audit.** Separate reviewer (not the author) checks for each level: (a) syllabus mapping vs the PDF summary (every outcome reference); (b) every puzzle solved by hand on a 20% sample; (c) reading level; (d) check design (can a pupil really self-correct); (e) layout at A4 and mono; (f) no copying; (g) no claim that outruns the legal wording (section 12). Findings logged as in `docs/audit/`; fix pass; re-audit of fixes.

**Pupil trial before release (recommended).** 4 to 6 pupils from the target age solve 10 pages unaided; record time, stuck points and whether the check strip was understood. Needs a willing school or tuition class (owner to arrange).

## 12. Legal wording on syllabus alignment

- Allowed, only after the audit passes and the owner reviews the final wording: "Puzzles matched to the topics of the Primary N mathematics syllabus." The syllabus text itself is quoted only in short phrases; our summary stays in our own words.
- Not allowed: "MOE-endorsed", "MOE-approved", "approved by the Ministry of Education", the MOE logo, official crest, "official syllabus workbook", or any wording implying the Ministry or any school has reviewed or recommended the book. Same for GEP and SASMO (existing rule): no contest claims, no "SASMO-style".
- Add on the copyright page: "Not affiliated with or endorsed by the Ministry of Education, Singapore. The mathematics syllabus is published by the Ministry of Education, Singapore."
- The 2021 syllabus is the one verified (footer "Updated: Oct 2025"); say which edition the mapping uses in the teacher book; add a "re-checked on" date; if the ministry publishes a revision, the mapping is re-audited (open item E in the verification report).
- Per owner addendum 7 the exact phrase ("matched to the MOE Primary Mathematics syllabus topics" or the shorter one above) is reviewed before publication. Draft default: "Matched to the topics of the Primary N mathematics syllabus" without the abbreviation MOE in the sales line.
- School names in testimonials or examples only with written permission.

## 13. Licence terms and printable licence wording

Plan: the licence is on the copyright page of both books, in the product page, and as a 1-line footer on each page.

Draft licence (for owner/lawyer review, not legal advice):
- **Single-school photocopy licence:** the purchaser (one school, one campus) may photocopy pages for use by pupils and staff of that school in class and for self-study in school. Not for resale, not for other schools, not for tuition centres or private classes, not for posting online or in a learning portal outside the school's closed system, not for sharing with families beyond the child's own copy (default; see option below).
- Digital file stays with the school; no redistribution; no editing of pages; watermark with licensee name on the PDF footer (default on).
- Licence term: perpetual for the edition bought (option: annual).
- Footer line (every page): "(c) [year] Preciouslyours Pte Ltd. Photocopy licence: [School name] only. Not for resale. Not affiliated with or endorsed by the Ministry of Education, Singapore."
- Invoicing: Preciouslyours Pte Ltd (addendum 5). Entity name and GST status to be confirmed by owner.

## 14. Pricing and licensing options (owner to choose)

All prices are placeholders for the owner to set; none is researched market data. Market comparison is an open task (a quick search of school-supplier prices, 1 hour).

| Option | What the school gets | Notes |
|---|---|---|
| A. Per-level photocopy licence (digital) | Teacher PDF + pupil PDF for one level, one campus | Simplest. Recommended default. Price per level. |
| B. Whole-series licence | All six levels, one campus | Discount versus six single levels (bundle ~ 4 to 5x one level) |
| C. Per-pupil printed sets | Printed pupil books (loose-leaf or bound), quantity bulk tiers (e.g. 10 / 30 / 100) plus one teacher book free per order | Higher price, covers print cost; use print route |
| D. Annual subscription | All levels, updates, re-checked on syllabus revisions | Recurring; more work for the owner |
| E. Teacher pack (single teacher) | One level, personal use, no school licence | Cheap entry for trials |

Recommended default: offer A and B (digital licence) plus C as printed bulk on request; no subscription at launch. Free sample: 4 pages of one level (2 pupil pages with their checks + 1 key page), watermarked, as a download.

Channel: direct quote and invoice to the school (email + PDF), not the existing parent shop; a simple school-facing page on the website with sample, licence summary and a request-a-quote form is a later task (outside this plan).

## 15. Pilot recommendation

**Default pilot: Primary 3.**

Why P3:
- P3 is the middle of the range; the early-finisher need is strongest at P3 and P4 where reading is independent and the syllabus is broad.
- P3 syllabus has the richest puzzle-friendly content that is plainly on syllabus: tables 6 to 9, equivalent fractions, time (seconds, 24-hour), area and perimeter, bar graphs.
- Most plan documents and the SASMO type analysis for G3 exist, so puzzle-type inspiration is already catalogued; the existing p3 holiday workbook gives layout and wording precedent (58 pages in the designed file).
- Proves all templates T01 to T12 except those that start at P4 (nets, symmetry) or later; later levels reuse most generators.
- P1/P2 pupils need picture-heavy art and the lowest reading load (higher design cost); P5/P6 would need many geometry and algebra solvers. P3 is a balanced test.

Alternative: **P2** (lower production risk because of smaller number ranges; weaker evidence of the teacher demand) or **P4** (best demand signal, heavier syllabus). Owner to confirm.

Pilot scope: full P3 book (40 pupil pages + teacher book), full audit, and a trial with 4 to 6 pupils. If the owner wants a cheaper test first: 12-page P3 sampler (3 units) for school outreach. Decision gate after the pilot: proceed to the other levels only if (a) the audit passes, (b) at least 2 schools express interest or trial, (c) owner accepts the price.

## 16. Sample puzzle specs for the pilot level (P3), not full pages

IDs follow P3-unit-page. Every spec lists topic tag, syllabus ref, template, tier, parameters, self-check, and verification the script must pass. Arithmetic in these specs was checked by hand; the generator must reproduce uniqueness by solver.

**Spec A. P3-03C "Table detective" (riddle plus code), core**
- Topic tag: Multiplication tables of 6, 7, 8 and 9. Ref: NA Whole Numbers, Multiplication and Division (p. 35).
- Template: T03 number riddle x 5 + K1 code word.
- Content: 5 riddles. Each says which table the number is in, a range and one digit clue, e.g. "I am in the 8 table. I am more than 40 and less than 70. My ones digit is 4 more than my tens digit." Answer 48. Hand check: multiples of 8 from 41 to 69 are 48, 56, 64; ones minus tens is 4, 1, -2; only 48 qualifies.
- Self-check: each answer is looked up in a printed letter table (a list of 12 numbers with letters); the five letters in order spell a 5-letter word. Wrong answers give letters that do not spell a word (V4/V5 test).
- Parameters: tables from {6, 7, 8, 9}; numbers 20 to 90; no number appears twice; digit clues from {ones minus tens, tens plus ones, odd/even}.
- Tier: Stretch (S) variant: tables 6 to 9 with a two-table clue ("in both the 6 table and 8 table", between 30 and 100) plus one digit clue.
- Verify: V1 each riddle has exactly one answer in range; V2; V3; V7 tables within 6 to 9.

**Spec B. P3-02C "Square of hundreds" (magic square), core**
- Topic tag: Adding and subtracting numbers (hundreds and thousands). Ref: Whole Numbers, addition and subtraction algorithms (p. 35).
- Template: T02 3x3 magic square on the numbers 100, 200, ..., 900 using each exactly once; the magic number printed (1500).
- Content: three squares given; the pupil fills the other six. Hand-checked base square (units of 100): 2 7 6 / 9 5 1 / 4 3 8; with the top row 2, 7, 6 given (200, 700, 600) the rest is forced (script check: 8 magic squares of 1 to 9 exist and the three givens leave exactly one).
- Self-check: K3 (every row, column and the two diagonals must total 1500); the page prints "Check: all eight lines make 1500". Also each of the nine numbers is crossed off a list of 900..100 (K4: each used once).
- Stretch variant: numbers 1 100 to 1 900 (step 200 or different constant), only 2 givens, hidden constant that the pupil first finds by adding a full given row (unlock K5).
- Verify: V1 unique completion under the "each number once" rule; V3 every single wrong entry breaks at least one line sum (true for magic squares, tested).

**Spec C. P3-08C "Who finished when?" (logic grid), core**
- Topic tag: Time: starting time, finishing time and how long. Ref: Measurement, Time 2.1 to 2.3 (p. 36).
- Template: T01 logic grid 3 pupils x 3 start times x 3 durations (all whole minutes, within an hour or two, using 12-hour clock with a.m./p.m.).
- Content: three pupils started a puzzle at 10:15, 10:30, 10:45 a.m. They took 20, 25 and 40 minutes. Clues are comparisons and facts: "Mei finished at 10:55 a.m." "The pupil who took longest did not start last." etc. The solver must show a unique assignment of start time and duration to names; the finishing times are derived and printed in the answer line.
- Self-check: K4 grid consistency plus K1: the three finishing times, written as minutes after 10:00, are used to pick letters from a table spelling a short word; or simpler for core: K4 only, since each row/column of the grid must hold one tick.
- Stretch variant: 4 pupils; start times in 24-hour clock including crossing noon; durations with hours and minutes.
- Verify: V1 unique; V7 time to the minute, duration under 3 hours; V8 clue wording.

**Spec D. P3-05S "Fraction route" (maze), stretch**
- Topic tag: Fractions: equivalent fractions and simplest form. Ref: NA Fractions 1.1 to 1.4 (p. 35).
- Template: T06 8x8 grid of fractions, denominators up to 12.
- Content: "Start at the square marked START. Move to a square next to it (not diagonal). You may only step on a fraction equal to 1/2 [core] or on a fraction equal to the fraction shown in the Start box." Stretch: the rule changes at the halfway box: after the flag, only fractions equal to 3/4 (changing the target is a second step). Exactly one path from Start to Finish (decoys include fractions like 5/12, 6/11, 7/14 that look close).
- Self-check: K6 (route must reach Finish) plus K1: the letters on the path (every 4th cell) spell a word; stepping on a wrong fraction dead-ends or breaks the word.
- Parameters: denominators 2 to 12 (P3 limit); all values within one whole; no mixed numbers (those are P4); fractions not in simplest form allowed as the topic requires.
- Verify: V1 path count is exactly 1 by exhaustive search (simple paths); V3 each single wrong step is detectable (dead end or letter break); V7 denominators at most 12.

## 17. Production cost and time estimate (agent-hours)

Agent-hours are estimates of work for the assistant plus reviewers; one agent-hour = one hour of an agent working. Human (owner) time is listed separately. These are rough planning numbers and will be revised after the pilot.

| Task | Pilot P3 | Each later level | Notes |
|---|---|---|---|
| Framework: shared tooling (generators, solvers, verification, rendering, assembly) | 36 | 0 | One-off |
| Template generators and solvers for the pilot level's used templates (about 9) | 24 | 8 (new templates only) | Most reuse |
| Content authoring + generation + verification of 40 pages | 20 | 20 | Includes self-check tuning |
| Layout/rendering fixes, page QA (A4, mono) | 8 | 6 | |
| Teacher book (front matter, mapping, key, notes) | 6 | 5 | |
| Independent audit (separate agent) | 10 | 8 | Includes hand-solving 20% sample |
| Fix pass + re-audit | 6 | 5 | |
| Legal wording and licence pages, product text | 4 | 1 | Owner/lawyer review separate |
| Project management, reports, sample pack | 4 | 2 | |
| **Total** | **118** | **55** | |

Estimated totals: pilot 118 agent-hours; P1 and P2 about 50 each; P4 to P6 about 60 each (geometry solvers); full series of six about 118 + 5 x 57 = roughly 400 agent-hours. In calendar terms: pilot 2 weeks if run in parallel (generation) and serial (audit); series 8 to 10 weeks with 2 to 3 agents in parallel.

Human time (owner): 1 to 2 hours to decide section 19, 1 to 2 hours for wording/legal review, arranging 1 school trial (about 1 hour), and print supplier quote for the printed edition (reuse `docs/printing/quote_request.md` with a loose-leaf variant).

Cash costs (not agent-hours): printing for printed copies (supplier quote), any stock art licence if images are bought (default: all art is own SVG, so none), legal review of licence wording (owner's choice).

## 18. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Puzzle drifts into contest-extension | Wrong product; breaks addendum 7 | Outcome-citation per page, V7 range check, audit question "could pupil do each step after the topic" |
| Puzzle has two solutions or is unsolvable | Pupil frustration, teacher complaint | Independent solver, exhaustive uniqueness (V1), hand-solve sample in audit |
| Self-check lets pupils guess | Defeats learning | V3/V4 tests, decoys, final computation on stretch |
| Self-check hints too much at the answer | Spoils puzzle | SC-2: check says "off" not "answer is" |
| Copying a contest/book/home problem by accident | Legal and ethical | V9, original generators, source_of_idea field |
| Syllabus revision makes mapping stale | Mislabelled pages | Dated mapping, annual re-check, data-driven tags |
| Alignment claim misread as endorsement | Legal risk | Strict wording (section 12), owner review |
| Demand unproven | Wasted effort | Pilot gate: 2 interested schools before more levels; sampler outreach |
| Licence abuse (sharing PDF) | Revenue loss | School name watermark, licence line on each page, terms |
| Photocopy quality (colour/light grey) | Unusable copies | Mono-safe test, no tints below 25% contrast |
| Reading level too high for the youngest | P1/P2 pupils cannot start alone | Reading table, picture-led instructions, pupil trial |
| Price/market mismatch | No sales | Short market check before pricing |
| Overlap with home book | Owner's addendum 6 breached | V9 comparison to home bank |
| Production load at P4 to P6 geometry | Time overrun | Do P3 pilot first; reuse solvers; accept 38-page P6 |
| Staff time of the owner as invoicer (B2B process) | Admin | Standard quote template and invoice; Preciouslyours Pte Ltd route |

## 19. Decisions needed from the owner (with recommended defaults)

1. **Pilot level.** Recommended default: P3. (Alternatives P2, P4.)
2. **Book size.** Default: 40 puzzle pages per level, single-sided, plus teacher book. (Alternative: 32 pages.)
3. **Tier labels.** Default: one star and two stars, with the neutral sentence in section 4.
4. **Product name and branding.** Default: "Early Finisher Puzzles, Primary N", publisher line Preciouslyours Pte Ltd, a small neutral logo; no Mi on pages; Mi may appear on the teacher-book cover only (owner to say). Alternative: "Math Inquirers" in the title.
5. **Format and delivery.** Default: digital PDF licence first; printed loose-leaf copies on request through the print route.
6. **Licence type.** Default: single-school (one campus) photocopy licence, perpetual, watermarked with the school name. Alternative: annual.
7. **Pricing option.** Default: options A and B (per level; whole series) plus C (printed bulk by quote). The owner sets the amounts; the assistant can research comparable school resources first (yes/no).
8. **Alignment claim wording.** Default: "Matched to the topics of the Primary N mathematics syllabus", with the not-affiliated line (section 12), final wording reviewed by the owner (and the lawyer if the owner wishes) before publication.
9. **Voice and spelling.** Default: school-neutral voice, British/Singapore school spelling, mixed local names.
10. **Self-check strictness.** Default: every page must have a verified check (SC-1); pages that cannot be given one are dropped from the book.
11. **P5/P6.** Default: Standard track only; P6 unit 10 revision optional (keep).
12. **Trial.** Default: run a pupil trial (4 to 6 pupils) before release; the owner arranges the group.
13. **Invoicing and terms.** Default: Preciouslyours Pte Ltd, quote then invoice, payment terms to be set by the owner.
14. **Outreach.** Out of scope for this plan; default: after the pilot passes the audit, produce a 4-page sampler.
15. **Series go/no-go.** Default gate: proceed beyond P3 only after the audit passes and at least 2 schools show interest.
