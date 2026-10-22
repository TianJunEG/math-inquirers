# International syllabus mapping: Ontario, USA (Massachusetts), Australia (Victoria), India

**Verified against MOE syllabus (Oct 2025).** Singapore references in this file (level names follow the Singapore year; P2 as the nearest match to England Year 3; the bar model) were checked: the syllabus itself never names the bar model (it is school practice), and the year mapping is as stated. No change needed. See `docs/moe/verification_report.md`.

Math Inquirers Levels 1-6 (60 lessons) against the primary/elementary mathematics curricula of Ontario (Toronto), the United States (Common Core and the Massachusetts 2017 Framework), Australia (Australian Curriculum v9 and Victorian Curriculum F-10 Version 2.0) and India (NCF-SE 2023 and the new NCERT textbooks). Researched 2026-10-22. Read-only audit: no lesson content was edited.

## 0. How to read this document

**Source discipline.** Every grade placement below is tagged. No tag means I read the primary text for that topic (listed in section 1). A trailing `?` means **[UNVERIFIED]**: inferred from an overview, a chapter title, or general knowledge, and not confirmed in an official expectation. Where I could only reach a secondary source, it is labelled **[SECONDARY]**. Nothing was filled in from memory without a tag.

**What "SAME / EARLIER / LATER / NOT" mean here.** Each program level is a three-year age band. I converted it to school grades using grade = age minus 5 (so Level 1, ages 6-8, is Grades 1-3; Level 6, ages 11-13, is Grades 6-8; Australian Year n follows the same rule, Foundation being age 5 and the same as US Kindergarten; India's Class n likewise, since the NCF-SE text puts Grades 1-2 at ages 6-8). For each lesson I took the grade where its **headline objective** is first taught in that system:
- **SAME** = introduced inside the level's three-grade band;
- **EARLIER** = introduced before the band (the lesson revisits something the child has already met);
- **LATER** = introduced after the band (the lesson is enrichment ahead of school);
- **NOT** = no matching K-8 / Foundation-Year 6 / Class 1-8 topic (or only a fragment);
- **MIXED** = the six "Challenge Day" and "Showcase" lessons, which re-use earlier topics and have no single home.

Because the band is three grades wide, **SAME is the expected result for most lessons**; the useful signals are the LATER, EARLIER and NOT cells and the bracketed stretch notes (for example "add/sub G5" means a part of the lesson goes further than the headline). Grade placement is "first formal introduction", not "mastery". Typical age in a grade is approximate: cut-off dates differ (Ontario and the US start the school year in September, Australia in late January, India typically in April) and children can be nearly a year younger or older than the number suggests [general knowledge, UNVERIFIED for 2026-27 cut-off dates].

**Candour about depth.** The Common Core and Massachusetts PDFs, the ACARA v9 curriculum workbook, the Victorian Curriculum 2.0 document and the NCERT textbook PDFs were downloaded and searched in full. The Ontario curriculum's expectation-level text could **not** be retrieved (the ministry site is a script-driven page and the full policy PDF was not found), so Ontario placements rest on the official ministry grade-by-grade overview plus tags; this is why Ontario (with India) has the most `?` cells. For India I read the NCF-SE 2023 mathematics goals and the NCERT chapter lists for Classes 1-8 and spot-checked chapter text, but did not read every chapter, so topic-level placement inside a book is often `?`.

**Headline findings.**
1. Level and lesson topics fit the four systems' ordinary age sequence well. Across the 54 non-mixed lessons, the headline topic sits inside the age band for 46-50 lessons in every system (Ontario 48, USA 47, Australia 50, India 46; counts in section 3).
2. Real enrichment-ahead (LATER) is concentrated in Levels 4-6 and is system-specific: India's new NCERT sequence puts decimals (Class 7), order of operations (Class 7, `?`), rate/proportion (Class 8) and probability (NCF Secondary) later than the program does; Ontario's overview places factors/multiples late (Grade 7, `?`).
3. Clock arithmetic and Caesar ciphers (Level 6 Lesson 8) are in **none** of the four curricula. Counting principles (6.5) are in none of the three Western K-8 curricula as a topic (the NCF does list simple permutation/combination counting at Class 3-5 level). Venn diagrams and logic grids (1.8) are in none.
4. Coding is mainstream in Ontario (every grade 1-8) and appears as "algorithms" inside Australian mathematics (Years 3-7) and as computational thinking in the NCF; the Common Core has none. See section 8.
5. Gaps in the program's coverage (major school topics without a lesson) are listed per jurisdiction. The biggest shared gaps: coordinate plane and transformations, ratio and proportion, multiplying and dividing fractions and decimals, long multiplication/division algorithms, 3D solids, circles, and charts such as pie graphs.

## 1. Sources consulted

| Jurisdiction | Document, year | URL | Status |
|---|---|---|---|
| Ontario | *The Ontario Curriculum, Grades 1-8: Mathematics, 2020* (replaces the 2005 curriculum; in force September 2020). Strands A Social-Emotional Learning Skills in Mathematics and the Mathematical Processes, B Number, C Algebra (including coding), D Data, E Spatial Sense, F Financial Literacy. | Overview: https://www.ontario.ca/page/math-curriculum-grades-1-8 (page marked published 2020-06-23, "Updated: June 18, 2025"); expectations site: https://www.dcp.edu.gov.on.ca/en/curriculum/elementary-mathematics | Overview page read in full (official). The expectation-level pages are script-rendered and could not be read; strand structure from search excerpts of the official dcp.edu.gov.on.ca pages. Details below the overview are `?`. |
| Ontario, 2025 | No Grades 1-8 mathematics revision found. The June 2025 update note on the ontario.ca page does not say what changed. A 2024 announcement of a new Kindergarten curriculum from 2025 (adding fractions, coding, patterns) was found only in news coverage. | https://www.ontario.ca/page/preparing-students-future | **[SECONDARY]** for the Kindergarten item. Treat "no 2025 revision of Grades 1-8" as **[UNVERIFIED]**, checked by search only. |
| USA | *Common Core State Standards for Mathematics* (2010; PDF as hosted 2023). | https://corestandards.org/wp-content/uploads/2023/09/Math_Standards1.pdf ; overview https://corestandards.org/mathematics-standards/ | Full PDF read (official). |
| USA, Massachusetts | *Massachusetts Curriculum Framework for Mathematics, Grades Pre-K to 12*, June 2017 (Department of Elementary and Secondary Education). CCSS plus Massachusetts additions. | https://www.doe.mass.edu/frameworks/math/2017-06.pdf | Full PDF read (official). |
| Australia | *Australian Curriculum Version 9, Mathematics, Foundation-Year 10* (ACARA): content descriptions and elaborations. Six strands (Number, Algebra, Measurement, Space, Statistics, Probability); four proficiencies (Understanding, Fluency, Reasoning, Problem-solving); processes: mathematical modelling, computational thinking, statistical investigation, probability experiments and simulations. | Structure page https://www.australiancurriculum.edu.au/teacher-resources/understand-this-learning-area/mathematics ; data file https://v9.australiancurriculum.edu.au/content/dam/en/curriculum/ac-version-9/downloads/curriculum-workbook.xlsx | Official ACARA workbook read in full for Foundation-Year 7. (I did not confirm the release date of v9 from the page, which shows only a 2026 copyright notice.) |
| Australia, Victoria | *Victorian Curriculum F-10 Version 2.0, Mathematics* (VCAA, (c) 2023, updated 2025 to add Foundation Levels A-D). "Derived from the Australian Curriculum"; levels Foundation, 1-10, 10A; same six strands. | https://f10.vcaa.vic.edu.au/learning-areas/mathematics/curriculum ; document https://f10.vcaa.vic.edu.au/sites/default/files/2025-02/Mathematics%20%E2%80%93%20Curriculum.docx | Official document read for Foundation-Level 6. It is not identical to AC v9 in sequencing; see section 6. |
| India | *National Curriculum Framework for School Education (NCF-SE) 2023*, NCERT/Ministry of Education (document released August 2023; the file is dated August 2023 on ncert.nic.in). Stages 5+3+3+4: Foundational (ages 3-8), Preparatory (8-11, Grades 3-5), Middle (11-14, Grades 6-8), Secondary (14-18). | https://ncert.nic.in/pdf/NCFSE-2023-August_2023.pdf (a copy also at https://dsel.education.gov.in/sites/default/files/update/ncf_2023.pdf, which failed a TLS check from this environment and was not used) | Full PDF read (official), mathematics goals in Part C section 3.4. |
| India | NCERT mathematics textbooks aligned to NCF: Classes 1-2 *Joyful Mathematics*; Classes 3-5 *Maths Mela*; Classes 6-8 *Ganita Prakash*. | PDFs e.g. https://ncert.nic.in/textbook/pdf/aejm101.pdf (Class 1), bejm101 (Class 2), cemm101 (Class 3), demm101 (Class 4), eemm101 (Class 5), fegp101 (Class 6), gegp101 (Class 7 Part I), hegp101 (Class 8 Part I); front matter e.g. aejm1ps.pdf. | Chapter lists read for all of Classes 1-8 (Class 7 Part II and Class 8 Part II not enumerated); chapter text sampled. Several are "Reprint 2026-27". Note the older NCERT series and state-board books differ [UNVERIFIED]. |

Program documents used: `docs/levels_and_placement.md`, `hp/lessons.js` (Level 1), `p2`-`p6` `content/l1.js`-`l10.js`, and `docs/audit/gifted_p*.md`. Level names follow Singapore primary years but the lessons are enrichment (Core / Think Harder / Challenge; "Notice it. Test it. Explain why.").

## 2. Program levels against school years

| Program level | Ages | Ontario / USA grade | Australia year (Victoria level) | India class (NCF stage) |
|---|---|---|---|---|
| 1 | 6-8 | Grades 1-3 | Years 1-3 (Foundation is age 5) | Classes 1-3 (Foundational ages 6-8 = Classes 1-2; Class 3 begins Preparatory) |
| 2 | 7-9 | Grades 2-4 | Years 2-4 | Classes 2-4 |
| 3 | 8-10 | Grades 3-5 | Years 3-5 | Classes 3-5 (Preparatory) |
| 4 | 9-11 | Grades 4-6 | Years 4-6 | Classes 4-6 |
| 5 | 10-12 | Grades 5-7 | Years 5-7 (Year 7 is secondary in Victoria) | Classes 5-7 |
| 6 | 11-13 | Grades 6-8 | Years 6-8 | Classes 6-8 (Middle) |

Kindergarten/Foundation are age 5 in the US and Australia (as given in the brief); Ontario has Junior and Senior Kindergarten at ages 4-5 [general knowledge, UNVERIFIED]. The India column assumes Class 1 at about age 6, which the NCF-SE text supports (Grades 1 and 2 are the 6-8 years band).

## 3. Summary matrix: 60 lessons by 4 jurisdictions

Cell = label, grade where the headline topic is first taught, `?` if [UNVERIFIED], then a short bracketed note (standard code, or a stretch that comes later). "G" = Grade, "Y" = Australian Year, "Cl" = India Class, "K" = Kindergarten, "F" = Foundation, "MA" = Massachusetts addition, "CCSS" codes such as 2.NBT are Common Core domains. Victoria differs from Australia on a few items; see section 6.

| Lesson | Topic | Ontario (Grade) | USA CCSS/MA (Grade) | Australia / Victoria (Year / Level) | India NCERT (Class) |
|---|---|---|---|---|---|
| L1.1 | Skip counting 2/3/5, add-or-take-away rules | SAME G1? | SAME G2 (2.NBT.2) | SAME Y1 (Y1 A01) | SAME Cl1? |
| L1.2 | Number bonds to 10 and 20, equal sign | SAME G1 (G1 equality) | SAME G1 (K bonds to 10) | SAME Y1 (F bonds to 10) | SAME Cl1 (Cl1 "Making 10") |
| L1.3 | Picture graphs, reading a class vote | SAME G1 | SAME G2 (2.MD.10) | SAME Y1 (Y1 ST02) | SAME Cl2 (Cl2 Data Handling) |
| L1.4 | Repeating and growing patterns | SAME G2 (growing G4) | SAME G3 (shape pat. G4) | SAME Y1 (growing Y2) | SAME Cl1? (Cl4 patterns ch.) |
| L1.5 | Working backwards, number machines | LATER G4 (unknowns G4) | SAME G2 (2.OA.1) | SAME Y3 (Y3 A01) | SAME Cl3? |
| L1.6 | Coin combinations (money) | SAME G2 (coin combos G2) | SAME G2 (MA also G1) | SAME Y3 (Y3 M06) | SAME Cl1 (Cl1 rupee coins) |
| L1.7 | 2D shapes, counting triangles, composing | SAME G1 | SAME G1 (1.G.1-2) | SAME Y1 | SAME Cl2 (Cl2 shapes) |
| L1.8 | Logic, Venn sorting, logic grid | NOT (sorting G1) | NOT (sorting K) | NOT (sorting F) | NOT (puzzles = NCF theme) |
| L1.9 | Length: ruler, units, convert | SAME G2 (metric rel. G4) | SAME G2 (convert G4) | SAME Y3 (informal Y1) | SAME Cl3 (NCF Prep: std units) |
| L1.10 | Challenge Day (mixed puzzles) | MIXED | MIXED | MIXED | MIXED |
| L2.1 | Numbers to 1000, digit cards | SAME G3 (G3 to 1000) | SAME G2 (2.NBT) | SAME Y2 (Y2 N01) | SAME Cl3? (Cl3 Hundreds ch.) |
| L2.2 | Add/subtract within 1000, missing digits | SAME G3? | SAME G2 (2.NBT.7) | SAME Y3 (Y3 N03) | SAME Cl3 (Cl3 Give and Take) |
| L2.3 | Multiplication, division, arrays | SAME G3 (G3 rows/cols) | SAME G3 (arrays G2) | SAME Y2 (Y2 N05) | SAME Cl2 (Cl2 Grouping) |
| L2.4 | Pattern machines, far places, multiples | SAME G4? | SAME G4 (3.OA.9 G3) | SAME Y3 (rules Y6) | SAME Cl4 (Cl4 Patterns) |
| L2.5 | Mystery number machines, 2-step backwards | SAME G4 (G4 unknowns) | SAME G3 (3.OA.8) | SAME Y3 (x/div Y5) | SAME Cl4? |
| L2.6 | Money, change, working backwards | SAME G3 (change G3) | SAME G2 (2.MD.8) | SAME Y3 (Y3 M06) | SAME Cl2? |
| L2.7 | Fractions: unit, compare, add like | SAME G3 (add/sub G5) | SAME G3 (add/sub G4) | SAME Y3 (add/sub Y5) | SAME Cl3? (Cl3 Fair Share) |
| L2.8 | Shape builders: composing, cubes, nets | SAME G3? | EARLIER G1 (vol. G5, nets G6) | SAME Y4 (nets Y5) | SAME Cl4? |
| L2.9 | Mass, volume, length, time to 5 min | SAME G3 | SAME G3 (5-min G2) | SAME Y3 (a.m./p.m. Y4) | SAME Cl3 (Cl3 Filling, Time) |
| L2.10 | Challenge Day (mixed puzzles) | MIXED | MIXED | MIXED | MIXED |
| L3.1 | Numbers to 10 000 | SAME G4 (G4 to 10 000) | SAME G4 (4.NBT) | SAME Y3 (Y3 N01) | SAME Cl4 (Cl4 Thousands) |
| L3.2 | Add/subtract 4-digit, cryptarithms | SAME G4? | SAME G4 (4.NBT.4) | SAME Y4 (Y4 N06) | SAME Cl4? |
| L3.3 | Times tables 6-9, patterns | SAME G4 (to 10x10 G4) | SAME G3 (3.OA.7) | SAME Y4 (Y4 A02) | SAME Cl3 (NCF Prep: to 10x10) |
| L3.4 | Bar-model word problems | SAME G3? | SAME G3 (3.OA.8; 4.OA.2) | SAME Y3 (Y2-Y4 elab.) | SAME Cl3? |
| L3.5 | Division with remainders | SAME G4 (G4 2-3 digit) | SAME G4 (4.NBT.6) | SAME Y5 (Y5 N07) | SAME Cl4? |
| L3.6 | Fraction walls, equivalent fractions | SAME G5? | SAME G3 (add/sub G4-5) | SAME Y4 (add/sub Y5) | SAME Cl5? (Cl5 Fractions) |
| L3.7 | Area and perimeter of figures | SAME G3 (area G3) | SAME G3 (3.MD.5-8) | SAME Y4 (Y4 M02) | SAME Cl5? (Cl6 ch.6 confirmed) |
| L3.8 | Angles, perpendicular, parallel | SAME G4? | SAME G4 (4.MD.5-7, 4.G.1) | SAME Y3 (Y3 M05) | SAME Cl5 (Cl5 Angles as Turns) |
| L3.9 | Compound units, budget, 12/24-hour | SAME G4? (budget G5) | SAME G4 (4.MD.1-2; 24h none) | SAME Y5 (conv. Y6) | SAME Cl5? |
| L3.10 | Challenge Day (bar graph, logic) | MIXED | MIXED | MIXED | MIXED |
| L4.1 | Factors, multiples, factor pairs | LATER G7? (overview G7) | SAME G4 (4.OA.4) | SAME Y5 (Y5 N02) | SAME Cl6 (Cl6 Prime Time) |
| L4.2 | Numbers to 100 000, rounding, estimating | SAME G5 (G5 to 100 000) | SAME G4 (4.NBT.3) | SAME Y4 (Y4 N07) | SAME Cl5? |
| L4.3 | Order of operations, missing signs | SAME G6? | SAME G5 (5.OA.1; 6.EE) | SAME Y6 (Y6 A02) | LATER Cl7? (Cl7 Arith. Expr.) |
| L4.4 | Improper/mixed, fraction of a set, compare | SAME G5? | SAME G4 (4.NF) | SAME Y4 (Y4 N04) | SAME Cl5? |
| L4.5 | Decimals to 3 places, rounding | SAME G4 (G4 intro) | SAME G4 (4.NF.5-7) | SAME Y4 (Y4 N01) | LATER Cl7 (Cl7 ch.3 (new series)) |
| L4.6 | Angles: protractor, clock, compass turns | SAME G6 (protractor G6) | SAME G4 (4.MD.6) | SAME Y5 (Y5 M04) | SAME Cl6 (Cl6 Lines/Angles) |
| L4.7 | Composite area/perimeter | SAME G5? | EARLIER G3 (3.MD.7d) | SAME Y5 (Y5 M02) | SAME Cl6 (Cl6 ch.6) |
| L4.8 | Symmetry and nets | SAME G4? | SAME G4 (nets G6) | SAME Y4 (nets Y5) | SAME Cl4 (Cl4 Symmetry) |
| L4.9 | Line graphs, tables, misleading scales | SAME G5 (broken-line G6) | NOT (5.MD.2 line plot only) | SAME Y5 (Y5 ST02) | SAME Cl6? (NCF Middle) |
| L4.10 | Challenge Day (heuristics) | MIXED | MIXED | MIXED | MIXED |
| L5.1 | Numbers to 10 million, digit riddles | SAME G7 (to 1 billion) | EARLIER G4? (to 1 000 000) | EARLIER Y3? ("beyond 10 000") | SAME Cl7 (Cl7 lakh/crore/million) |
| L5.2 | Fractions and division, divide fraction by whole | SAME G7? | SAME G5 (5.NF.3, 5.NF.7) | SAME Y7? (Y7 N06) | SAME Cl7? (Cl7 ch.8) |
| L5.3 | Fraction word problems, before and after | SAME G6? | SAME G5 (5.NF.6) | SAME Y6? | SAME Cl7? |
| L5.4 | Area of a triangle | SAME G5? | SAME G6 (6.G.1) | SAME Y7 (Y7 M01) | SAME Cl7? (NCF Middle) |
| L5.5 | Volume of cuboids, water tanks | SAME G6? | SAME G5 (5.MD.3-5) | SAME Y7 (Y7 M02) | LATER Cl8? |
| L5.6 | Rate, price per item, work rate | SAME G7? | SAME G6 (6.RP.2-3) | SAME Y7 (Y7 N08 ratio) | LATER Cl8 (Cl8 Proportional) |
| L5.7 | Percentage, discount, GST | SAME G5 (intro G5) | SAME G6 (disc./tax G7) | SAME Y5 (disc. Y6) | SAME Cl7? (NCF Middle) |
| L5.8 | Angle chasing (triangle, parallelogram) | SAME G5? (parallel G8) | SAME G7 (7.G.5; 8.G.5) | SAME Y6 (tri. sum Y7) | SAME Cl7 (Cl7 ch.5, ch.7) |
| L5.9 | Pattern generalisers, nth term in words | SAME G6? | SAME G6 (6.EE) | SAME Y6 (Y6 A01) | SAME Cl6 (Cl6 Patterns ch.1) |
| L5.10 | Challenge Day (strategies) | MIXED | MIXED | MIXED | MIXED |
| L6.1 | Sequences, nth term (+ Scratch loop) | SAME G6? (coding each grade) | SAME G6? | SAME Y6 (Y6 A01, A03) | SAME Cl6 (Cl6 ch.1) |
| L6.2 | Primes, prime factorisation (+ mod code) | SAME G7? | EARLIER G4 (pr. fact. G6) | SAME Y6 (pr. fact. Y7) | SAME Cl6? (Cl6 Prime Time) |
| L6.3 | Negative numbers | SAME G6 (integers G6) | SAME G6 (6.NS.5-7) | SAME Y6 (Y6 N01) | SAME Cl6 (Cl6 ch.10) |
| L6.4 | Algebra machines, letter rules, equations | EARLIER G5 (multi-term G7) | SAME G6 (6.EE.2,7) | SAME Y7 (Y7 A01-03) | SAME Cl7 (Cl7 ch.4) |
| L6.5 | Counting every possible way | NOT (prob. only) | SAME G7 (7.SP.8; perm. HS) | NOT (Y7 single-stage) | EARLIER Cl5 (NCF Prep C-4.2) |
| L6.6 | Probability, 2 dice, fair games, simulation | SAME G6? (complex G8) | SAME G7 (7.SP.5-8) | SAME Y6 (Y6 P01-02) | LATER Cl9 (NCF: Secondary) |
| L6.7 | Turtle geometry, polygon angles | SAME G7? (code G4, G7) | SAME G8? | SAME Y7 (Y7 M05) | SAME Cl8? |
| L6.8 | Clock arithmetic, mod, Caesar cipher | NOT | NOT | NOT | NOT (Cl8 remainders partial) |
| L6.9 | Mean, median, mode, levelling out | SAME G6? (overview: "averages" from G3) | SAME G6 (6.SP.5; MA +mode) | SAME Y7 (Y7 ST01) | SAME Cl7? (NCF Middle C-5.1) |
| L6.10 | Showcase Challenge (maths + code) | MIXED | MIXED | MIXED | MIXED |

### Tally by level and jurisdiction (headline topic vs the level's three-grade band)

| Program level (ages) | Jurisdiction | SAME | EARLIER | LATER | NOT | MIXED |
|---|---|---|---|---|---|---|
| Level 1 (6-8) | Ontario | 7 | 0 | 1 | 1 | 1 |
| Level 1 (6-8) | USA | 8 | 0 | 0 | 1 | 1 |
| Level 1 (6-8) | Australia | 8 | 0 | 0 | 1 | 1 |
| Level 1 (6-8) | India | 8 | 0 | 0 | 1 | 1 |
| Level 2 (7-9) | Ontario | 9 | 0 | 0 | 0 | 1 |
| Level 2 (7-9) | USA | 8 | 1 | 0 | 0 | 1 |
| Level 2 (7-9) | Australia | 9 | 0 | 0 | 0 | 1 |
| Level 2 (7-9) | India | 9 | 0 | 0 | 0 | 1 |
| Level 3 (8-10) | Ontario | 9 | 0 | 0 | 0 | 1 |
| Level 3 (8-10) | USA | 9 | 0 | 0 | 0 | 1 |
| Level 3 (8-10) | Australia | 9 | 0 | 0 | 0 | 1 |
| Level 3 (8-10) | India | 9 | 0 | 0 | 0 | 1 |
| Level 4 (9-11) | Ontario | 8 | 0 | 1 | 0 | 1 |
| Level 4 (9-11) | USA | 7 | 1 | 0 | 1 | 1 |
| Level 4 (9-11) | Australia | 9 | 0 | 0 | 0 | 1 |
| Level 4 (9-11) | India | 7 | 0 | 2 | 0 | 1 |
| Level 5 (10-12) | Ontario | 9 | 0 | 0 | 0 | 1 |
| Level 5 (10-12) | USA | 8 | 1 | 0 | 0 | 1 |
| Level 5 (10-12) | Australia | 8 | 1 | 0 | 0 | 1 |
| Level 5 (10-12) | India | 7 | 0 | 2 | 0 | 1 |
| Level 6 (11-13) | Ontario | 6 | 1 | 0 | 2 | 1 |
| Level 6 (11-13) | USA | 7 | 1 | 0 | 1 | 1 |
| Level 6 (11-13) | Australia | 7 | 0 | 0 | 2 | 1 |
| Level 6 (11-13) | India | 6 | 1 | 1 | 1 | 1 |
| **All 60** | **Ontario** | **48** | **1** | **2** | **3** | **6** |
| **All 60** | **USA** | **47** | **4** | **0** | **3** | **6** |
| **All 60** | **Australia** | **50** | **1** | **0** | **3** | **6** |
| **All 60** | **India** | **46** | **1** | **5** | **2** | **6** |

### Reading the matrix

- The `?` cells are unconfirmed placements: 58 of the 216 placed cells (4 jurisdictions x 54 non-mixed lessons) carry `?`. Ontario (26) and India (26) carry nearly all of them, because only the ministry overview (Ontario) and chapter titles (India) were readable; the US and Australia have 3 each.
- Level 1 Lesson 8 (Logic Lab) is NOT in any curriculum as a topic. Sorting objects into categories is taught (K / F / G1); Venn diagrams, ordering from clues and logic grids are not named in any of the four documents I read.
- Level 6 Lesson 8 (clock arithmetic, mod, Caesar cipher) is NOT in any of the four. Class 8 *Ganita Prakash* "Number Play" works with remainders (the word "remainder when" appears four times) but I did not find clock or cyclic arithmetic there, so I call it partial at best.
- Level 6 Lesson 5 (counting): not a topic in Ontario or Australia (Year 7 has single-stage sample spaces only); US compound-event sample spaces are Grade 7 (7.SP.8) and permutations/combinations are a high-school "(+)" standard; the NCF lists systematic counting and listing of permutations or combinations "in simple situations" in the Preparatory Stage goals (C-4.2), which I mapped to Class 5.
- The six Challenge/Showcase lessons are MIXED; they reuse the Mathematical Practice / proficiency / process language rather than a topic.

## 4. Ontario (Toronto)

### 4.1 Document and structure
Official: *The Ontario Curriculum, Grades 1-8: Mathematics, 2020*; ontario.ca overview https://www.ontario.ca/page/math-curriculum-grades-1-8 and https://www.ontario.ca/page/new-math-curriculum-grades-1-8 (grade-by-grade summary, read in full); expectations at https://www.dcp.edu.gov.on.ca/en/curriculum/elementary-mathematics (not readable here). Six strands (A SEL skills and the mathematical processes; B Number; C Algebra, including coding; D Data; E Spatial Sense; F Financial Literacy). Strand A's social-emotional-learning expectations are taught but, per the ministry, schools were asked from 2021-22 not to assess or report on them [SECONDARY, from search excerpts of dcp.edu.gov.on.ca]. Coding: each grade has one overall and two specific expectations on coding (writing programs, reading and altering code) [SECONDARY: school-board and educator pages; only the per-grade coding sentences below are confirmed on the official overview].

### 4.2 Grade by grade (official overview; ages approximate)

| Grade (age) | Number | Algebra incl. coding | Data | Spatial sense | Financial literacy |
|---|---|---|---|---|---|
| 1 (6) | to 50; fractions via equal sharing | patterns for predictions; both sides of a number sentence equal; code to order a sequence of steps | ask, sort into categories, graph or table | compare length, mass, capacity; calendars; describe shapes | recognise Canadian coins and bills, compare values |
| 2 (7) | to 200; add/subtract problems; fractions via sharing | extend shape and number patterns; adjust add/subtract pairs to be equal; code to move objects on a grid | collect, organise, display, interpret more complex data; likelihood of events | visualise shapes turned or taken apart; simple maps; measure with rulers, timers, clocks | same amount in different ways (coins to $1; loonie, toonie, bills to $100) |
| 3 (8) | to 1000; place-value breakdown; fractions in more than one form; multiplication as rows and columns; facts x2, x5, x10 and division | what repeats in a pattern; equal multiplication/division equations; code with a repeating operation (for example repeated "add 3") | scales on graphs; averages to compare data | 3D objects; measure length, weight, capacity; area of 2D shapes; digital and analog time | change for whole-dollar purchases |
| 4 (9) | to 10 000; intro to decimals; divide 2- and 3-digit by 1-digit; facts 1x1 to 10x10; multi-operation problems | repeating vs growing patterns; find values that make statements true (n + 3 = 10); read and write code for geometric designs | frequency tables; multiple-bar graphs; infographics | properties of rectangles; area; metric unit relationships | ways to pay; value judgements |
| 5 (10) | to 100 000; intro to percentages; add/subtract same-denominator fractions; facts 0x0 to 12x12; multi-operation problems | repeating, growing, shrinking patterns; one-variable equations (3 + x = 24 - 5); code growing patterns | sampling; misleading graphs; experiments for probability | triangles, types, angles; metric length, area, mass, capacity; converting units | e-transfers, cheques; best value; basic budgets; credit and debt |
| 6 (11) | to 1 million; integers; divisibility rules; divide whole numbers by fractions and mixed numbers | patterns growing at a constant rate; expressions and equations with several terms; code to solve optimisation problems (for example greatest area for a given perimeter) | discrete vs continuous data; broken-line graphs; ways to describe probability | four-sided shapes and areas; surface area; metric conversions; protractors | payment methods; goals; interest and fees |
| 7 (12) | to 1 billion; rational numbers; factors and multiples; fractions with equivalent fractions; add/subtract integers | decimal patterns; equations such as 2x + 5 = 3x - 1; code to rotate or resize shapes | circle graphs; misleading graphs; independent vs dependent probability | circle measures; surface area and volume of cylinders etc.; dilations | exchange rates; interest; cost of borrowing |
| 8 (13) | scientific notation; fractions-decimals-percentages interchangeably; squares to 144 and roots; proportion; exponents | integer patterns; s = d/t; equations with integers and decimals; code a best-fit line or curve | scatter plots; complex experiments | right triangles and Pythagorean theorem; unknown angles from intersecting/parallel lines; very large and small units | financial plans; balanced budgets; simple and compound interest |

### 4.3 Notable features
- Coding is a required part of the Algebra strand in every grade 1-8 and is framed as a tool for mathematics (patterns, geometry designs, optimisation, transformations).
- Mandatory financial literacy (Strand F), with Canadian money (loonie, toonie).
- Emphasis on recall of number facts (by Grade 4 or 5: tables to 10x10 or 12x12), as the overview states.
- Strand A: social-emotional learning and the "mathematical processes" (problem solving, reasoning, connecting, communicating, representing, reflecting, selecting tools; the process list is from general knowledge and not verified).

### 4.4 Mapping notes
- Close matches: 1.2 (equal sign, Grade 1), 2.1 (to 1000, Grade 3), 3.1 (to 10 000, Grade 4), 3.3 (tables to 10x10, Grade 4), 3.5 (division, Grade 4), 4.5 (decimals, Grade 4), 5.7 (percent introduced, Grade 5), 6.3 (integers, Grade 6).
- Program ahead of the Ontario overview: 1.5 working backwards with "unknown" statements (Grade 4 in the overview); factors and multiples (4.1) if the overview's Grade 7 placement is right [UNVERIFIED: finer expectations may begin earlier]; 5.1 numbers to 10 million (Grade 7 to 1 billion); 5.2 fraction division (Grade 6-7).
- Ontario Grade 5-6 patterns, expressions and one-variable equations correspond to 5.9 and 6.4, which the matrix labels SAME or EARLIER.

### 4.5 Coverage: Ontario topics with no lesson
Financial literacy beyond money and one budget (3.9): payment methods, interest, exchange rates; coding in Grades 1-5 (the program has no coding before Level 6); transformations and dilations (G7); circle measurement and circle graphs (G7); surface area and volume of cylinders; scatter plots; Pythagorean theorem; exponents and scientific notation (G8); rational numbers and scale proportion (only 5.6 rate); 3D object properties (G3); the Strand A social-emotional skills strand. Telling time is partly covered (2.9, 3.9).

### 4.6 Vocabulary, notation, methods
- "Grade" (JK/SK then Grade 1). Ontario schools use "regrouping" for carrying/borrowing in common usage [general knowledge, UNVERIFIED]; the program's "carry" and "borrow" language should be glossed.
- Canadian money: dollars and cents, loonie ($1) and toonie ($2) are named in the overview; the penny was withdrawn in 2013 and cash totals round to 5 cents [general knowledge, UNVERIFIED]. The program's "fewest notes and coins" (2.6) uses Singapore denominations (check the page); for a Canadian child swap in loonie/toonie.
- Metric units are used in school, but everyday speech in Canada uses imperial for height and weight (feet, pounds) and Fahrenheit for baking [general knowledge, UNVERIFIED].
- "Averages" appear in the Grade 3 overview; formal mean, median, mode grade not confirmed.
- Number-writing: 4-digit numbers in Canada are commonly written 1 000 (space) in English; the program uses a space for thousands (e.g. 10 000) [general knowledge, UNVERIFIED].

### 4.7 Which program levels fit a child in Ontario
By age: Grade 1 (age 6) fits Level 1; Grade 2 fits Level 1 or 2; Grade 3 fits Level 2 or 3; Grade 4 fits Level 3 or 4; Grade 5 fits Level 4 or 5; Grade 6 fits Level 5 or 6; Grades 7-8 fit Level 6. By topic, Level 2 lessons 2.1-2.3 match Grades 3's number and multiplication; Level 3 matches Grade 4 (numbers to 10 000, times tables, division); Level 4's decimals (4.5) and angles with a protractor (4.6) match Grades 4 and 6; Level 5's rate, volume and triangle area (5.4-5.6) are mostly Grade 6-7 content, so a Grade 5 child meets them early (by design). A Grade 6 child will have seen integers and percent at school; Levels 5 and 6 add the reasoning layer. Use the program's own diagnostic; these are cautious indications, not placements.

### 4.8 Coding and Level 6's Scratch bridge
Ontario's coding expectations sit in Strand C and are mathematical (repeating "add 3", geometric designs in Grade 4, optimisation in Grade 6, rotating shapes in Grade 7). Level 6's Scratch strand (loops and variables to test sequences and mod, a turtle that draws polygons, a coin-and-dice simulation, list programs for averages and ciphers) is a close fit with that spirit, and 6.7 (turn angles, polygons) echoes Grade 4 "code for geometric designs" and Grade 7 "rotate shapes". The ministry text I read does not name Scratch or any language, so I cannot say the program matches any specific expectation wording. Levels 1-5 contain no coding.

## 5. United States (Boston / Massachusetts)

### 5.1 Documents
- *Common Core State Standards for Mathematics* (CCSSM), 2010. Eight Standards for Mathematical Practice (SMP): 1 Make sense of problems and persevere in solving them; 2 Reason abstractly and quantitatively; 3 Construct viable arguments and critique the reasoning of others; 4 Model with mathematics; 5 Use appropriate tools strategically; 6 Attend to precision; 7 Look for and make use of structure; 8 Look for and express regularity in repeated reasoning.
- *Massachusetts Curriculum Framework for Mathematics, Pre-K-12, June 2017*: the Common Core as adapted by Massachusetts, which says it includes "both the Common Core State Standards and unique Massachusetts standards and features" (2010 adoption), revised 2016-17 with three key shifts (clarity, coherence, rigor). Unique additions I found: prime factorisation named in the Grade 6 GCF standard ("Use prime factorization to find the greatest common factor...", absent from the CCSS wording I read); money content in Grade 1 (identify U.S. coins and their values, use coin values to solve problems up to 100 cents, cents notation such as 69 cents) and in Grade 2; "mode" named with median and mean in the Grade 6 statistics; and a glossary definition of "standard algorithm" as "one of the conventional algorithms used in the United States based on place value". I did not compare the two documents line by line, so other additions may exist [UNVERIFIED].

### 5.2 Grade by grade (CCSS critical areas, read from the PDF; ages approximate)

| Grade (age) | Critical areas / main content |
|---|---|
| K (5) | Count, represent and compare whole numbers (to 20, with sets of objects); add/subtract within 10 initially with objects; describe shapes and space. |
| 1 (6) | Add/subtract within 20; place value to 100 (tens and ones); linear measurement as iterated units; compose/decompose shapes; tell time to the hour and half hour; organise data in up to three categories. MA adds coin values (see above). |
| 2 (7) | Base-ten notation to 1000; fluency with add/subtract within 100, solve within 1000; standard units (cm and inch); describe and analyse shapes; time to 5 minutes with a.m./p.m.; dollar bills and coins; picture graphs and bar graphs. |
| 3 (8) | Multiplication and division within 100 (all single-digit products from memory by end of grade); fractions, especially unit fractions; arrays and area; 2D shapes; time to the minute, liquid volume and mass; scaled picture/bar graphs; perimeter. |
| 4 (9) | Multi-digit multiplication; division with multi-digit dividends and remainders; place value to 1 000 000; fraction equivalence, add/subtract like denominators, multiply fraction by whole number; decimals as tenths and hundredths; factors, multiples, prime and composite to 100; angles and protractor; lines of symmetry; perpendicular and parallel; metric and customary unit conversions (km/m/cm, kg/g, lb/oz, l/ml, hr/min/sec). |
| 5 (10) | Add/subtract fractions with unlike denominators; multiply fractions; divide unit fractions by whole numbers and the reverse; decimals to hundredths (operations) and place value to thousandths; division with 2-digit divisors; volume of right rectangular prisms; first quadrant coordinates; parentheses in expressions; line plots. |
| 6 (11) | Ratio and rate; divide fractions by fractions; negative numbers and the full rational number system, all four quadrants; expressions, equations and variables (one-step equations); statistical thinking (mean, median, variability); area of triangles and special quadrilaterals, surface area (nets), volume with fractional edges; GCF and LCM (Massachusetts wording uses prime factorisation); percent as a rate; tape diagrams named in 6.RP.3. |
| 7 (12) | Proportional relationships, percent (discounts, taxes, tips); operations with rational numbers; linear equations; scale drawings; circles (area, circumference); angle relationships (supplementary, vertical, adjacent); probability and compound events; sampling. |
| 8 (13) | Linear functions; systems of equations; transformations, congruence, similarity; Pythagorean theorem; exponents, scientific notation; triangle angle sum and exterior angle; scatter plots. |

### 5.3 Notable features
- The eight SMP run through every grade; they are the closest cousin of "Notice it. Test it. Explain why." (SMP 3 and 8 especially), but I would call this a family resemblance, not an alignment.
- Fluency expectations are explicit: add/subtract within 1000 by strategies (G3), fluent multi-digit add/subtract by the standard algorithm (G4), multiplication (G5), division (G6); all single-digit multiplication facts known from memory by end of Grade 3.
- Strong fractions pathway (unit fractions G3 to division of fractions G6); data and probability are light until Grades 6-7.
- Coding: **none** in the Common Core (CCSSM does not mention coding or algorithms as content in K-8). Massachusetts has a separate computer science/digital literacy framework that I did not read [UNVERIFIED].

### 5.4 Mapping notes
- Matches at the same age: 2.2 add/subtract within 1000 (G2), 3.3 tables (G3), 4.1 factors/primes (G4), 4.5 decimals (G4), 4.6 protractor (G4), 5.5 volume (G5), 6.3 negatives (G6), 6.6 probability (G7).
- Earlier in US than in the program: 2.8 (composing shapes G1, though cube counting and nets arrive in G5-G6), 4.7 (composite area G3, 3.MD.7d), 6.2 prime numbers (G4; prime factorisation G6, Massachusetts wording).
- US introduces triangle area (6.G.1) and nets (6.G.4) in Grade 6; the program has them at Levels 5 and 4.
- Not in CCSS: 6.8 modular arithmetic; Venn/logic grids; line graphs as a named elementary topic (the closest are line plots of fractions in G5 and graphing real-world coordinates).

### 5.5 Coverage: US topics with no lesson
Coordinate plane (5.G, 6.NS, 8.EE); ratio and proportional relationships (6.RP, 7.RP); fraction multiplication/division beyond the preview in 5.2; decimal operations (5.NBT, 6.NS); multi-digit multiplication and the standard long-division algorithms; exponents; customary units (inches, feet, pounds, gallons, Fahrenheit); two-dimensional shape classification by hierarchy (G3-G5); circles, surface area, transformations, Pythagorean theorem; money with U.S. coins (the program uses another currency). Time to the minute is touched in Level 2 and Level 3 only.

### 5.6 Vocabulary, notation, methods
- "Grade" and Kindergarten; "regrouping" is the common US word for carrying and borrowing in school, though CCSSM prefers "compose and decompose" and "standard algorithm"; the program should gloss "borrow".
- Customary units: the CCSS teaches inches (G2) and, by Grade 4, ft/in and lb/oz alongside metric. Program pages in metric only will leave a US child without feet, pounds, gallons and Fahrenheit.
- Long division in the US uses the "house" (bracket) layout; multiplication of multi-digit numbers uses the standard algorithm; the Singapore bar model is called a "tape diagram" in US resources [general knowledge, UNVERIFIED; "tape diagrams" are named in CCSS 6.RP.3].
- Money: $ and the cent sign, penny/nickel/dime/quarter; MA writes cents as 69 cents in the standard (confirmed in the Grade 1 money standard). Commas for thousands (10,000), decimal point; the program's space-separated 10 000 will look unusual.
- The CCSS does not name "mode"; Massachusetts does (Grade 6).
- "Order of operations" is formal in Grade 6 (6.EE); parentheses appear in Grade 5.

### 5.7 Which program levels fit a child in Massachusetts
By age: Kindergarten (5) is below the program; Grade 1 fits Level 1; Grade 2 Level 1 or 2; Grade 3 Level 2 or 3; Grade 4 Level 3 or 4; Grade 5 Level 4 or 5; Grade 6 Level 5 or 6; Grades 7-8 Level 6. By topic, Grade 3's multiplication/division, unit fractions, area and perimeter match Levels 2 and 3 (2.3, 2.7, 3.3, 3.7); Grade 4's multi-digit work and fractions match Levels 3 and 4; Level 5's rate and percent (5.6, 5.7) precede Grade 6 ratio and Grade 7 percent in the US. A child who is strong in the US system and arrives in Grade 4 or 5 would be comfortable with Levels 3-4 content on the topics above, but would lack the program's metric-only unit practice if they are used to customary units.

### 5.8 Coding and Level 6's Scratch bridge
The Common Core has no coding strand; Level 6 is therefore additional to the mathematics standards. The mathematics it uses (sequences, primes, negatives, algebra, counting, probability simulation, angles, averages) sits at Grades 4-8 in CCSS. A US family should hear Level 6 described as a computing bridge for maths, not as part of Common Core.

## 6. Australia (Melbourne / Victoria)

### 6.1 Documents
- *Australian Curriculum Version 9 Mathematics (F-10)*, ACARA: content descriptions with elaborations; achievement standards per year level; six strands (Number, Algebra, Measurement, Space, Statistics, Probability) and four proficiencies (Understanding, Fluency, Reasoning, Problem-solving), plus processes (mathematical modelling, computational thinking, statistical investigation, probability experiments and simulations).
- *Victorian Curriculum F-10 Version 2.0 Mathematics*, VCAA (c) 2023, updated 2025 to add Foundation Levels A-D. "Derived from the Australian Curriculum", with Victorian elaborations and some changes of placement. Victoria's primary school is Foundation to Year 6; Year 7 is in secondary school [general knowledge, UNVERIFIED].

### 6.2 Year by year (AC v9 content descriptions; ages approximate; Foundation age 5)

| Year (age) | Number and Algebra | Measurement and Space | Statistics and Probability |
|---|---|---|---|
| F (5) | numbers to at least 20, subitising to 5, part-part-whole to 10, equal sharing; repeating patterns | compare length, capacity, mass, duration; days; sort and name shapes; position | collect, sort and compare data |
| 1 (6) | to at least 120; partition; add/subtract within 20; skip counting by 2, 5, 10; repeating patterns; money in simple transactions | informal units for length, years/months/weeks/days/hours; classify familiar shapes; directions | categorical data, one-to-one displays |
| 2 (7) | to at least 1000; halves, quarters, eighths; one-digit multiply/divide (arrays); additive patterns; addition facts to 20, doubles for twos | calendar, analog time to quarter hour, turns; classify shapes by sides, "parallel"; position | surveys, graphs from software |
| 3 (8) | numbers "beyond 10 000"; unit fractions (1/2, 1/3, 1/4, 1/5, 1/10); add/subtract 2-3 digit; multiply/divide with arrays; inverse operations; facts 3, 4, 5, 10; algorithms (steps and decisions) | metric units, time to the minute; angles as turn compared with right angles; money (dollars and cents); 3D objects; 2D representations | categorical and discrete data, guided investigations; **Probability begins**: likely/unlikely, repeated chance experiments |
| 4 (9) | tenths and hundredths; odd/even; equivalent fractions; count by fractions incl. mixed numerals; x, / by 10; facts to 10x10; algorithms with multiplication; estimation | unmarked units; perimeter and area; am/pm and durations; angle names (acute, obtuse, reflex); composite shapes; grid references; line and rotational symmetry | many-to-one displays; chance order by likelihood |
| 5 (10) | decimals beyond 2 places; factors, multiples, divisibility; compare mixed numerals; percentages (100% = whole); add/subtract related denominators; multi-digit multiplication and division with remainders; algorithms for factors/multiples | metric choice; perimeter and area of irregular shapes; 12- and 24-hour; protractor; nets; coordinates; translations, reflections, rotations | line graphs over time; equally likely outcomes |
| 6 (11) | integers; prime, composite, square numbers; fractions on a number line; add/subtract decimals and fractions; percent, fraction and decimal of a quantity incl. discounts; rules for growing patterns; brackets and combined operations; algorithms with rules | metric conversions; area formula of a rectangle; timetables; angles on a straight line, at a point, vertically opposite; cross-sections; four-quadrant plane; tessellations | compare data in the media; probability on a 0-1 scale; simulations with digital tools |
| 7 (12) | square roots; prime factorisation (exponent notation); ratios; integer add/subtract; rational numbers; algebra: variables, expressions, one-variable linear equations; tables of values | area of triangles and parallelograms; volume of prisms; pi and circles; parallel lines; angle sum of a triangle; classify polygons | range, median, mean, mode; stem-and-leaf; sample space for single-stage events |

### 6.3 Notable features
- Proficiencies (Understanding, Fluency, Reasoning, Problem-solving) are built into the content descriptions in Version 2.0 rather than sitting beside them, and problem solving and reasoning are explicit.
- Algorithms are inside the mathematics from Year 3 ("follow and create algorithms involving a sequence of steps and decisions" 3N07, 4N09, 5N10, 6A03, 7SP04), including in Year 6 "writing a simple program to generate a sequence of numbers" (elaboration to AC9M6A03) and a robot-programming idea in AC9M3SP02 and AC9M6SP04 elaborations.
- Elaborations repeatedly mention bar models (Years 2-5) and Aboriginal and Torres Strait Islander contexts.
- Probability starts at Year 3; money appears in Years 1-3; Measurement and Space are separate strands.

### 6.4 Where Victoria differs from AC v9 (read in the VCAA document)
- Odd and even numbers are a Level 3 content description in Victoria (VC2M3N01) and Year 4 in AC v9 (AC9M4N02).
- Level 3: unit fractions "and their multiples" and "combine fractions with the same denominator to complete the whole" (VC2M3N03), and money is in Number (VC2M3N07), not Measurement.
- Level 4: number sequences of multiples of 3, 4, 6, 7, 8, 9 (VC2M4N02), and "calculation of change to the nearest 5 cents" (VC2M4N08), with an elaboration that "not all countries use dollars and cents; for example, India uses rupees".
- Level 5: algorithms with "branching and repetition (iteration)" (VC2M5N10).
- Level 6: prime, composite, square **and triangular** numbers (VC2M6N02). I did not find a VC2M6P01 in the document (AC9M6P01 "probabilities lie on numerical scales 0-1" is not listed for Level 6 in the list I extracted, though the reason is not checked). I did not compare the two documents line by line; these differences were noticed while reading, so others may exist. The matrix uses AC v9 grades; the odd/even and Level 3 fraction points are the main Victorian shifts I found.

### 6.5 Mapping notes
- Early matches: 1.2 and 1.4 (patterns Y1), 2.1 (to 1000, Y2), 2.3 (arrays, Y2), 3.1 (numbers beyond 10 000, Y3), 3.8 (angles, Y3).
- Program lessons that are ahead of Australian placement: 3.5 division with remainders (Y5 "interpret any remainder"), 3.9 compound unit conversion (Y6), 4.1 factors (Y5), 5.4 triangle area (Y7), 5.5 volume (Y7), 5.6 rate/ratio (Y7), 6.4 algebra (Y7).
- Australia has one placement the program does earlier: numbers to 10 million (5.1) have no stated upper bound in AC v9.
- Australian primary has no counting-principles, no modular arithmetic.

### 6.6 Coverage: Australian topics with no lesson
Coordinates and grid references (Y4 SP02, Y5 SP02, Y6 SP02); transformations and tessellations (Y5-Y6); 3D objects and cross-sections (Y3, Y6); calendar and time-zone/timetables (Y6 timetables, partly 2.9, 3.9); chance language and early probability Y3-Y5 (the program jumps to 6.6); statistical investigation processes (Y3-Y7); multiplication/division of decimals by powers of ten (Y6); rounding in money to 5 cents; fraction and decimal links before Year 6 (partly 4.5).

### 6.7 Vocabulary, notation, methods
- "Year" (Foundation/Prep, then Year 1; Victoria uses "Level" in the curriculum and "Prep" colloquially [general knowledge, UNVERIFIED]); "Foundation" = age 5.
- AC v9 teaches partitioning and "regroup and rename"; "borrowing" is not the curriculum word. Australian schools prefer mental strategies and "place value to partition, rearrange and regroup" before the written algorithm.
- Dollars and cents with "c", change to the nearest 5 cents (VC2M4N08). The program's 2.6 and 3.9 money pages are in another currency.
- Number writing: AC v9 says "naming and writing conventions for numerals beyond 10 000" (3N01) and Victoria elaborates the digit-group spacing ("sets of 3 digits"); the program's space-separated 10 000 matches Australian/SI practice.
- Metric throughout (including temperature in Celsius); the Singapore bar model is used in Victorian elaborations.
- Time: 12- and 24-hour with a.m./p.m. in Year 4-5; school year runs late January to December, so an Australian child in Year 3 in term 4 is a different age/stage from an Ontario Grade 3 child in October.

### 6.8 Which program levels fit a child in Victoria
By age: Foundation (5) is below the program; Year 1 fits Level 1; Year 2 Level 1 or 2; Year 3 Level 2 or 3; Year 4 Level 3 or 4; Year 5 Level 4 or 5; Year 6 Level 5 or 6; Year 7 Level 6. By topic, the program mostly sits on or slightly ahead of Australian placement, with Levels 5 and 6 close to Years 6-7 in content; a Year 5-6 child has met percent and integers at school. Probability and algorithms are strong in the Australian curriculum and are matched by Level 6.

### 6.9 Coding and Level 6's Scratch bridge
The best fit among the four. AC v9 mathematics itself includes algorithms (3N07, 4N09, 5N10, 6A03, 7SP04), explicitly mentioning flow charts, spreadsheets and, in Year 6, writing a simple program; a separate Digital Technologies learning area exists [general knowledge, UNVERIFIED: not read here]. Level 6's Scratch tasks (sequences, primes/mod, negative numbers, function machines, counting loops, simulations, polygon turtle, ciphers, list averages) are comparable in kind. The curriculum text names no language.

## 7. India (NCERT / NCF-SE 2023)

### 7.1 Documents
- *National Curriculum Framework for School Education 2023* (NCF-SE), https://ncert.nic.in/pdf/NCFSE-2023-August_2023.pdf. 5+3+3+4 design: Foundational (3-8), Preparatory (8-11), Middle (11-14), Secondary (14-18). Mathematics goals in Part C section 3.4 (curricular goals CG and competencies C) by stage.
- NCERT textbooks (reprints 2026-27): *Joyful Mathematics* Class 1 and 2; *Maths Mela* Class 3, 4, 5; *Ganita Prakash* Class 6, Class 7 (Parts I and II), Class 8 (Part I seen). Classes 4 and 5 books use "Grade", the Class 1-3 books use "Class". The older NCERT *Math-Magic* series is replaced by these [UNVERIFIED for every state board].
- NCF-SE emphasis (text read): the Foundational Stage key focus is "foundational numeracy: understanding, and adding and subtracting with Indian numerals; basic shapes and measurement using non-standard tools; early mathematical thinking through play". The Preparatory Stage builds "conceptual understanding of numbers, the four basic operations, shapes and spatial sense, measurement (standard tools and units), and data handling" with "procedural fluency and mathematical and computational thinking". The Middle Stage "moves towards abstracting" and introduces algebra. The curriculum stresses joy, reasoning, puzzles, computational thinking and the history of Indian mathematics (zero and place value, Aryabhata, Brahmagupta, Baudhayana-Pythagoras theorem, Virahanka numbers).

### 7.2 Class by class

| Class (stage, age) | NCERT book and chapters (titles read) | Main topics |
|---|---|---|
| 1 (Foundational, 6) | *Joyful Mathematics* 13 chapters: Finding the Furry Cat; What is Long? What is Round?; Mango Treat; Making 10; How Many?; Vegetable Farm; Lina's Family; Fun with Numbers; Utsav; How Do I Spend My Day?; How Many Times?; How Much Can We Spend?; So Many Toys | counting, comparison, bonds to 10, early addition/subtraction, shapes, rupee coins, time of day |
| 2 (Foundational, 7) | *Joyful Mathematics* 11 chapters: A Day at the Beach; Shapes Around Us; Fun with Numbers; Shadow Story; Playing with Lines; Decoration for Festival; Rani's Gift; Grouping and Sharing; Which Season Is It?; Fun at the Fair; Data Handling | numbers, shapes, lines, grouping and sharing (multiplication/division ideas), data handling |
| 3 (Preparatory, 8) | *Maths Mela* 14 chapters: What's in a Name?; Toy Joy; Double Century; Vacation with My Nani Maa; Fun with Shapes; House of Hundreds I; Raksha Bandhan; Fair Share; House of Hundreds II; Fun at Class Party; Filling and Lifting; Give and Take; Time Goes On; The Surajkund Fair | numbers to 999, 3-digit add/subtract, fair share (fractions/division), capacity, calendar and time |
| 4 (Preparatory, 9) | *Maths Mela* 14 chapters: Shapes Around Us; Hide and Seek; Patterns Around Us; Thousands Around Us; Sharing and Measuring; Measuring Length; The Cleanest Village; Weigh It, Pour It; Equal Groups; Elephants, Tigers, and Leopards; Fun with Symmetry; Ticking Clocks and Turning Calendar; The Transport Museum; Data Handling | thousands, patterns, parts and wholes, length/weight/capacity, equal groups, symmetry, clocks, data |
| 5 (Preparatory, 10) | *Maths Mela* 15 chapters: We the Travellers I; Fractions; Angles as Turns; We the Travellers II; Far and Near; The Dairy Farm; Shapes and Patterns; Weight and Capacity; Coconut Farm; Symmetrical Designs; Grandmother's Quilt; Racing Seconds; Animal Jumps; Maps and Locations; Data Through Pictures | numbers (10,000s), fractions, angles as turns, multiplication/division, area/perimeter ideas, time, maps, data |
| 6 (Middle, 11) | *Ganita Prakash* Grade 6, 10 chapters: Patterns in Mathematics; Lines and Angles; Number Play; Data Handling and Presentation; Prime Time; Perimeter and Area; Fractions; Playing with Constructions; Symmetry; The Other Side of Zero (Integers) | sequences/patterns, angles, number puzzles (Collatz, Kaprekar, palindromes), bar graphs, primes and common factors/multiples, perimeter and area, fractions, constructions, symmetry, integers |
| 7 (Middle, 12) | *Ganita Prakash* Part I (8 chapters): Large Numbers Around Us; Arithmetic Expressions; A Peek Beyond the Point; Expressions Using Letter-Numbers; Parallel and Intersecting Lines; Number Play; A Tale of Three Intersecting Lines; Working with Fractions. Part II not enumerated | lakh/crore and million, expressions, decimals, algebra with letter-numbers, angles, triangles, fraction multiplication |
| 8 (Middle, 13) | *Ganita Prakash* Part I (7 chapters seen): A Square and a Cube; Power Play; A Story of Numbers; Quadrilaterals; Number Play; We Distribute, Yet Things Multiply; Proportional Reasoning-1. Part II not enumerated | squares/cubes, exponents, number story, quadrilaterals, remainders and divisibility, algebra, proportion |

### 7.3 NCF mathematics goals (Preparatory stage), read from the text
CG-1 Numbers (counting numbers and fractions, Indian place value, four operations, tables at least to 10 x 10 "Pahade"); further goals for shapes/spatial sense, measurement (non-standard and standard units, simple conversion such as cm to m, area of rectangle as length times breadth, equal-area shapes with different perimeters), and CG-4 problem solving with procedural fluency "as a step towards developing computational thinking" (puzzles, magic squares, systematic listing of permutations and combinations in simple situations such as forming a committee of two from five, choosing among mental, estimation and paper-pencil methods). CG-5 appreciation of the development of zero and the Indian place value system. Middle stage: large numbers up to 20 digits, scientific notation, integers via Brahmagupta, percentage, algebra (variables, linear equations), geometry and constructions, Baudhayana-Pythagoras, mean-mode-median, bar/histogram/line/pie graphs, CG-8 computational thinking ("decomposition, pattern recognition, data representation, generalisation, abstraction, algorithms"; C-8.1 "programmatic thinking techniques such as iteration, symbolic representation, and logical operations"). Probability (C-6.2) is listed at the Secondary stage.

### 7.4 Notable features
- Home-language and Indian-context story chapters, puzzles, games (NIM), patterns throughout; New series are explicitly play-first (Joyful Mathematics, Maths Mela).
- Strong number-play strand (Collatz, Kaprekar, palindromes in Class 6 "Number Play"), place value and the history of the Indian number system.
- "Large Numbers Around Us" (Class 7) teaches lakh and crore beside million and billion (the chapter table reads 10,00,000 ten lakhs = 1,000,000 one million; 1,00,00,000 one crore = 10,000,000 ten million).
- Fewer separate probability and coding chapters in the textbooks I enumerated; computational thinking is a stated goal.
- Order of topics differs from Western sequences: decimals appear as a Class 7 chapter ("A Peek Beyond the Point") in the new *Ganita Prakash* sequence I read, not in the Class 3-6 chapter titles; ratio and proportion appear in Class 8 Part I. Older NCERT books and state boards (and CBSE schools using other publishers) often differ [UNVERIFIED]. Do not assume a family's child has followed this sequence.

### 7.5 Mapping notes
- Close matches: 1.2 (Class 1 "Making 10"), 2.2 (Class 3 "Give and Take"), 2.9 (Class 3 Filling and Lifting, Time Goes On), 3.8 (Class 5 Angles as Turns), 4.8 (Class 4 Fun with Symmetry), 6.3 (Class 6 integers).
- LATER in India than in the program (enrichment ahead): 4.3 order of operations (Class 7, `?`), 4.5 decimals (Class 7), 5.5 volume (Class 8, `?`), 5.6 rate (Class 8), 6.6 probability (Secondary).
- Program ahead on topics Western curricula teach: 5.1 numbers to 10 million (Class 7).

### 7.6 Coverage: Indian topics with no lesson
Lakh/crore numbering and Indian place-value reading (the program uses Western grouping); Pahade (tables to 10 x 10 in the NCF, partly 3.3); rupee-and-paise money with ₹ (the program's money pages use another currency); constructions with compass and straightedge (Class 6); maps and locations (Class 5); calendars and time (partly 2.9); data handling beyond 1.3, 3.10 and 4.9 (Class 2-6 chapters); history-of-mathematics strand (zero, Aryabhata, Brahmagupta, Sulba-Sutras, Virahanka) is absent; ratio/proportion (Class 8 Part I, only the rate idea in 5.6) and exponents (Class 8).

### 7.7 Vocabulary, notation, methods
- "Class" (Class 1 to 12) in the new NCERT Class 1-3 books; "Grade" in Class 4-8 books and in the NCF; stage names Foundational, Preparatory, Middle, Secondary.
- Number naming: lakh (1,00,000) and crore (1,00,00,000), written with Indian comma grouping (2-2-3 from the right); million and billion appear beside them in Class 7. The program writes 10 000 with a space and has no lakh/crore.
- Currency: rupees and paise, symbol ₹; Class 1 chapter "How Much Can We Spend?" uses coins of 1, 2, 5, 10 rupees.
- "Pahade" for multiplication tables, recited; tables to 10 x 10 are an NCF competency at Preparatory stage.
- Long division in Indian schools is laid out with the divisor on the left and the quotient above the line, the same family as the US bracket [general knowledge, UNVERIFIED].
- Metric throughout; Celsius; 12-hour clock in textbooks.
- India uses "Class" for year and "tables"/"Pahade" for times tables, "sum" for any exercise [general knowledge, UNVERIFIED].

### 7.8 Which program levels fit a child in India
By age: Class 1 (6) Level 1; Class 2 Level 1 or 2; Class 3 Level 2 or 3; Class 4 Level 3 or 4; Class 5 Level 4 or 5; Class 6 Level 5 or 6; Class 7-8 Level 6. By topic, the new NCERT sequence is lighter on abstract operations early (Class 1-2 books are activity-based) and puts decimals, order of operations, ratio and probability later than the program, so a Class 4-6 child may find Level 4-5 lessons on decimals, rate and percent ahead of school (and these are the lessons that need a gentle entry); Level 6's primes, integers, patterns and number play would be well matched to Class 6-7. Indian children in private schools may follow other publishers, so use the diagnostic rather than the class.

### 7.9 Coding and Level 6's Scratch bridge
The NCF names computational thinking (decomposition, pattern recognition, generalisation, abstraction, algorithms) as a goal at Preparatory and Middle stage and "programmatic thinking" with iteration and logical operations at Middle; no textbook coding chapter was seen. Level 6's Scratch lessons fit that stated aim, but the NCF does not mention Scratch.

## 8. Coding strands and Level 6's Scratch bridge: summary

| Jurisdiction | Where coding sits | Relation to Level 6 |
|---|---|---|
| Ontario | Strand C Algebra, grades 1-8, one overall + two specific expectations a year; confirmed examples: sequence steps (G1), move objects on a grid (G2), repeating "add 3" (G3), geometric designs (G4), growing patterns (G5), optimisation (G6), rotate/resize shapes (G7), best-fit line (G8). | Closest in spirit: patterns (6.1), geometry designs (6.7), simulations and data (6.6, 6.9). Levels 1-5 have no coding, so an Ontario child will have had up to five grades of coding the program does not mirror. |
| USA (CCSS / MA) | None in CCSSM. MA has a separate computer science / digital literacy framework not read here. | Level 6 is additive to Common Core. |
| Australia / Victoria | Algorithms (steps and decisions) are content descriptions in maths Years 3-7; Year 6 elaboration mentions writing a simple program; Digital Technologies learning area not read. | Close fit for 6.1 (sequences), 6.2 (factor counting), 6.5 (nested loops), 6.8 (ciphers). |
| India | NCF computational-thinking goals at Prep and Middle stage; no coding textbook chapters seen. | Fits the aim; no Scratch. |

None of the documents I read names Scratch.

## 9. Differences families moving between systems will notice

| Item | Program | Ontario | USA | Australia | India |
|---|---|---|---|---|---|
| School year labels | P1-P6 names, age bands | Grade 1-8, JK/SK | Grade 1-8, K | F, Year 1-6 (Vic: Level) | Class 1-8 |
| Carry / borrow | "carry", "borrow" in pages | "regrouping" [UNVERIFIED] | "regrouping"; CCSS: compose/decompose, standard algorithm | partition, rearrange, "regroup and rename" | "carry" and "borrow" in common use [UNVERIFIED] |
| Long division | check workbook | not read | "house" bracket, standard algorithm Grade 6 | strategies then written method | divisor on left, quotient above |
| Times tables | tables 6-9 at Level 3 | facts 1x1 to 10x10 in G4 | by end of G3 (3.OA.7) | facts to 10x10 in Y4 | tables ("pahade") to 10x10, Prep stage |
| Money | Singapore denominations | $ and cents, loonie, toonie | $ and cents, coins to 100 cents | $ and c, change to nearest 5c | rupees and paise, symbol ₹ |
| Units | metric | metric (imperial in daily life) | customary taught: in, ft, lb, oz | metric only | metric |
| Big numbers | 10 000 with space | commas / spaces | 10,000 with comma | space convention | lakh and crore: 1,00,000; 1,00,00,000 |
| Bar model | "bar model" | not confirmed | "tape diagram" | "bar model" in elaborations | not named |
| Thinking-skill language | "Notice it. Test it. Explain why." | mathematical processes | 8 Standards for Mathematical Practice | 4 proficiencies | reasoning, computational thinking |

## 10. What is safe to claim

**Safe, because it is true of what I read:** the program's six levels follow the ordinary sequence of school years in Ontario, the United States, Australia and India closely enough that most lessons sit within one or two years of where each school system first teaches the topic; its lessons are enrichment that reasons about, rather than pre-teaches, school topics; some lessons (listed above: Levels 4-6) go beyond what these systems cover at that age; and Level 6 adds a Scratch coding bridge that has no counterpart in the US Common Core and is closest in spirit to Ontario's coding strand and the algorithm content of the Australian curriculum. It is fair to say, for example, "a Toronto Grade 3 or 4 child will find Levels 2 and 3 familiar", provided the sentence is framed as a topic comparison with the curriculum named and dated, as in this document.

**Do not claim:** that the program is aligned with, based on, accredited by, approved by or endorsed by the Ontario Ministry of Education, the Common Core State Standards Initiative, the Massachusetts Department of Elementary and Secondary Education, ACARA, the VCAA, NCERT or India's Ministry of Education. Do not use their names or logos as endorsement. Do not say "meets Common Core standards", "covers the Ontario curriculum" or "NCERT-compliant"; it does not cover these curricula (see the coverage gaps) and I have not seen any official statement of equivalence. Do not use the Standards for Mathematical Practice or proficiencies as a claim that the program implements them. Do not claim readiness for a school year, test or grade placement from a level; do not promise that a child will be "ahead" in their school's grade; and say "similar in spirit to" rather than "the same as" for any coding-strand comparison. Describing lessons as "enrichment that goes beyond the school syllabus" is only true topic by topic (see LATER cells), not for the programme as a whole, as the majority of lessons sit at or below the age band's grade range.

**Wording for site copy that is defensible:** "Math Inquirers lessons are enrichment: puzzles and investigations that build reasoning about topics children meet in school, with a coding bridge at Level 6. We compare topics informally with school curricula in several countries; we are not affiliated with, and do not claim alignment with or endorsement by, any ministry, board or the Common Core."

## 11. Caveats and open items

1. Ontario expectation-level text was not retrievable; every Ontario `?` should be checked against the PDF of the 2020 curriculum on ontario.ca before any parent-facing statement. In particular factors/multiples (4.1) and the formal grade of mean/median/mode (6.9) may be earlier than the overview suggests.
2. Indian placements rest on NCERT chapter titles and sampled chapter text; Class 7 Part II and Class 8 Part II chapter lists were not read, so "LATER" for volume, percent and proportion could change. State-board and older NCERT books may differ.
3. The Massachusetts framework was compared with CCSS only by searching for unusual features; additional Massachusetts-specific standards may exist.
4. Victorian Curriculum 2.0 differs from AC v9 in places (section 6.4); the matrix uses AC v9 grades.
5. Grade-to-age conversion is approximate; Southern Hemisphere and Indian school calendars shift when in the year a child is in a given grade.
6. The matrix was built from the headline objective of each lesson, as listed in `hp/lessons.js` and `pN/content/lN.js`. Lessons with several strands (for example 4.4 fractions) carry stretch notes, but a reviewer should read each lesson page before quoting a single cell.
7. No page of this repository was changed and nothing was committed.
