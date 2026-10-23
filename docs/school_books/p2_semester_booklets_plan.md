# Primary 2 early-finisher puzzles: two semester booklets (plan)

Date: 23 Oct 2026. Model: `docs/school_books/p1_semester_booklets_plan.md` and the P1 build report and three audit rounds. Pipeline: `school/p2/` (copied from `school/p1/`; P1 untouched). Build progress and weak points: `docs/school_books/p2_semester_booklets_build_report.md`.

## 0. Decisions this plan follows

Owner decisions (`docs/terms/owner_decisions.md`): two booklets, **Semester 1** (typical school Terms 1 and 2) and **Semester 2** (Terms 3 and 4), 20 pupil pages each, 10 one-star and 10 two-star, self-checking, pure black and white, no Mi. Teacher notes say that schools vary. Footer codes print both numbers (for example `S1-07 (P2-17)`: seventh page of the booklet, page 17 of the 40 in build order). Original problems only; coins and notes are original art "inspired by", with cents; no MOE logo or claims, no price; the not-affiliated sentence only on the licence page; `(c) 2026 Preciouslyours Pte Ltd` on pupil footers with a `School (write name): ____` line; cover publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers"; annual licence (one school year, renewable), wording DRAFT for a lawyer; registered office 66 Tannery Ln, Singapore 347805; contact pypteltd@gmail.com; DRAFT stamps on cover, licence, teacher notes and both keys; keys read "Key page n of N" with outcome tags in the PDF's own wording and small solved pictures.

Sources read: the syllabus PDF pages 33 and 34 (Primary 2; wording copied, kept in `docs/school_books/p2_outcome_wording.md`), `docs/school_books/plan.md` (templates, reading load: P2 = at most 10 words a sentence, 3 sentences, check wording one sentence of at most 14 words), `p2_school_paper_patterns.md` and `p2_non_routine_catalogue.md` (question TYPES only, no text copied), `coin_reproduction_check.md`, `school/colour_by_code/README.md`, and every audit lesson from the P1 booklets (carried into section 5).

## 1. Gap analysis: the 30 Primary 2 outcome lines against what early-finisher pages can do

The PDF has 30 numbered lines (counting each of fractions 1.1 to 1.3 and 2.1, and the three-bullet lines, as one line). An early-finisher page is a single printed page with a built-in check, so some verbs of the syllabus can only be practised in part. "Full" means the page asks the pupil to do what the line says; "Part" means a printed substitute is used.

| Outcome (PDF wording, short) | Pages | Coverage |
|---|---|---|
| Whole Numbers 1.1 counting in tens/hundreds | P2-11, P2-38 | Full |
| Whole Numbers 1.2 number notation, representations and place values (hundreds, tens, one... | P2-01, P2-10, P2-17, P2-38 | Full |
| Whole Numbers 1.3 reading and writing numbers in numerals and in words | P2-09, P2-38 | Part: reading and matching words and numerals; the pupil writes numerals, not number words (a written word cannot be checked) |
| Whole Numbers 1.4 comparing and ordering numbers | P2-10, P2-17, P2-38 | Full |
| Whole Numbers 1.5 patterns in number sequences | P2-11 | Full |
| Whole Numbers 1.6 odd and even numbers | P2-10, P2-12, P2-17 | Full |
| Addition and Subtraction 2.1 addition and subtraction algorithms (up to 3 digits) | P2-02, P2-13, P2-18 | Full |
| Addition and Subtraction 2.2 mental calculation involving addition and subtraction of a 3-digit num... | P2-03, P2-18 | Full |
| Multiplication and Division 3.1 multiplication tables of 2, 3, 4, 5 and 10 | P2-04, P2-14, P2-20, P2-39 | Full |
| Multiplication and Division 3.2 use of ÷ | P2-05, P2-14, P2-19, P2-39 | Full |
| Multiplication and Division 3.3 relationship between multiplication and division | P2-19, P2-20, P2-39 | Full |
| Multiplication and Division 3.4 multiplying and dividing within the multiplication tables | P2-04, P2-05, P2-19, P2-20, P2-39 | Full |
| Multiplication and Division 3.5 mental calculation involving multiplication and division within multip... | P2-14, P2-20, P2-39 | Full |
| Fractions 1.1 fraction as part of a whole | P2-15 | Full |
| Fractions 1.2 notation and representations of fractions | P2-15, P2-21 | Full |
| Fractions 1.3 comparing and ordering fractions with denominators of given fractions ... | P2-21 | Full |
| Fractions 2.1 adding and subtracting like fractions within one whole with denominato... | P2-22 | Full |
| Money 1.1 counting amount of money in dollars and cents | P2-06, P2-24 | Full (pictured coins and notes) |
| Money 1.2 reading and writing money in decimal notation | P2-06, P2-16, P2-23, P2-24 | Full |
| Money 1.3 comparing two or three amounts of money | P2-23 | Full |
| Money 1.4 converting an amount of money in decimal notation to cents only, and v... | P2-16 | Full |
| Length, Mass and Volume 1.1 measuring (length in metres; mass in kilograms/grams; volume of liquid... | P2-08, P2-25, P2-26, P2-28 | Part: reading pictured scales, tapes and containers; a printed page cannot hold a real instrument |
| Length, Mass and Volume 1.2 using appropriate units of measurement and their abbreviations m, g, k... | P2-08, P2-25, P2-26, P2-27 | Full |
| Length, Mass and Volume 1.3 comparing and ordering (lengths; masses; volumes) | P2-28 | Full (one unit at a time: kg to g and m to cm conversions are Primary 3) |
| Time 2.1 telling time to the minute | P2-07, P2-29, P2-31, P2-40 | Full |
| Time 2.2 measuring time in hours and minutes | P2-29, P2-31, P2-40 | Full |
| Time 2.3 converting time in hours and minutes to minutes only, and vice versa | P2-30, P2-31, P2-40 | Full |
| 2D Shapes 1.1 making/completing patterns with 2D shapes according to one or two of t... | P2-32, P2-33 | Part: completing patterns by choosing the next shape; the pupil's own drawn pattern cannot be checked |
| 3D Shapes 2.1 identifying, naming, describing and classifying 3D shapes (cube, cuboi... | P2-34, P2-35 | Full by picture (cube, cuboid, cone, cylinder, sphere); no real solids to handle |
| Picture Graphs with Scales 1.1 reading and interpreting data from picture graphs with scales | P2-36, P2-37 | Full (picture graphs with keys of 2, 5 and 10) |

**Not covered, or only in part (for the owner):** writing number words by hand (WN 1.3), taking a real measurement or building a real pattern or solid (ME 1.1, GE 1.1, GE 2.1), and anything that needs the pupil to draw. These are the verbs a printed self-checking page cannot see; the teacher notes say so. **Excluded as above Primary 2** (and never used): decimals beyond dollars-and-cents notation, adding or subtracting decimal money (Primary 3), conversions kg to g, m to cm, ℓ to mℓ, tables of 6 to 9, division with remainder, equivalent fractions, unlike fractions, mixed numbers, bar graphs, tally charts as a taught skill, 24-hour time, angles, area and perimeter.

## 2. The 40-page allocation

Typical order, schools vary. Singapore schools teach Primary 2 in different orders (see `p2_school_paper_patterns.md`, section 2: numbers and add/subtract in Term 1, multiplication and division with length and graphs in Term 2, money, mass, volume and shapes in Term 3, fractions, time and a review in Term 4). The split below is a decision for the booklets, not a claim about any school: Semester 1 holds number, the four operations and fractions; Semester 2 holds money, measurement, time, shapes and graphs. Fractions sit in Semester 1 although some schools teach them in Term 4; the teacher notes say to hand out any page when its topic has been taught.

Page ids P2-01 to P2-40 are in build order; "Pos" is the position in the booklet. Mechanics (from plan.md section 8.1): K1 code word, K3 total, K4 grid/logic, K6 route, K7 answer put back, K8 loop closes, K9 measured, TF true/false letters, CBC colour by code. Stars: 1 or 2; two-star never means a new topic, only two steps or two clues.

### 2a. Semester 1 (Terms 1 and 2): 10 one-star, 10 two-star

| Pos | Page | Title | Outcomes | Stars | Mechanic |
|---|---|---|---|---|---|
| S1-01 | P2-01 | Hundreds, Tens, Ones | Whole Numbers 1.2 | 1 | K1 code word |
| S1-02 | P2-38 | Colour the Rocket | Whole Numbers 1.1, Whole Numbers 1.2, Whole Numbers 1.3, Whole Numbers 1.4 | 1 | colour by code, tally and matching parts |
| S1-03 | P2-09 | Words and Numbers | Whole Numbers 1.3 | 1 | K6 route closes at FINISH |
| S1-04 | P2-12 | Odd or Even | Whole Numbers 1.6 | 1 | K6 route closes at FINISH |
| S1-05 | P2-10 | Digit Cards | Whole Numbers 1.2, Whole Numbers 1.4, Whole Numbers 1.6 | 2 | K1 code word |
| S1-06 | P2-11 | Number Patterns | Whole Numbers 1.1, Whole Numbers 1.5 | 2 | K1 code word |
| S1-07 | P2-17 | Mystery Numbers | Whole Numbers 1.2, Whole Numbers 1.4, Whole Numbers 1.6 | 2 | K1 code word |
| S1-08 | P2-02 | Column Sums | Addition and Subtraction 2.1 | 1 | K1 code word |
| S1-09 | P2-03 | Mental Jumps | Addition and Subtraction 2.2 | 1 | K6 route closes at FINISH |
| S1-10 | P2-13 | Missing Digits | Addition and Subtraction 2.1 | 2 | K1 code word |
| S1-11 | P2-18 | Story Sums to 1000 | Addition and Subtraction 2.1, Addition and Subtraction 2.2 | 2 | K1 code word |
| S1-12 | P2-04 | Equal Groups | Multiplication and Division 3.1, Multiplication and Division 3.4 | 1 | K1 code word |
| S1-13 | P2-05 | Share It Out | Multiplication and Division 3.2, Multiplication and Division 3.4 | 1 | K1 code word |
| S1-14 | P2-14 | Times Table Maze | Multiplication and Division 3.1, Multiplication and Division 3.2, Multiplication and Division 3.5 | 1 | K6 route closes at FINISH |
| S1-15 | P2-19 | Fact Families | Multiplication and Division 3.2, Multiplication and Division 3.3, Multiplication and Division 3.4 | 2 | K8 loop closes |
| S1-16 | P2-20 | True or False Tables | Multiplication and Division 3.1, Multiplication and Division 3.3, Multiplication and Division 3.4, Multiplication and Division 3.5 | 2 | K1 letters spell a word |
| S1-17 | P2-39 | Colour the House | Multiplication and Division 3.1, Multiplication and Division 3.2, Multiplication and Division 3.3, Multiplication and Division 3.4, Multiplication and Division 3.5 | 2 | colour by code, tally and matching parts |
| S1-18 | P2-15 | Parts of a Whole | Fractions 1.1, Fractions 1.2 | 1 | K1 code word |
| S1-19 | P2-21 | Fraction Order | Fractions 1.2, Fractions 1.3 | 2 | K1 letters spell a word |
| S1-20 | P2-22 | Fraction Sums | Fractions 2.1 | 2 | K1 code word |

### 2b. Semester 2 (Terms 3 and 4): 10 one-star, 10 two-star

| Pos | Page | Title | Outcomes | Stars | Mechanic |
|---|---|---|---|---|---|
| S2-01 | P2-06 | Dollars and Cents | Money 1.1, Money 1.2 | 1 | K1 code word |
| S2-02 | P2-16 | Writing Money | Money 1.2, Money 1.4 | 2 | K1 code word |
| S2-03 | P2-23 | Which Costs More? | Money 1.2, Money 1.3 | 2 | K1 letters spell a word |
| S2-04 | P2-24 | Purse Match | Money 1.1, Money 1.2 | 2 | K1 letters spell a word |
| S2-05 | P2-08 | Metres | Length, Mass and Volume 1.1, Length, Mass and Volume 1.2 | 1 | K1 code word |
| S2-06 | P2-25 | Kilograms and Grams | Length, Mass and Volume 1.1, Length, Mass and Volume 1.2 | 1 | K1 code word |
| S2-07 | P2-26 | Litres | Length, Mass and Volume 1.1, Length, Mass and Volume 1.2 | 1 | K1 code word |
| S2-08 | P2-27 | Which Unit? | Length, Mass and Volume 1.2 | 1 | K1 letters spell a word |
| S2-09 | P2-28 | Order the Measures | Length, Mass and Volume 1.1, Length, Mass and Volume 1.3 | 2 | K1 letters spell a word |
| S2-10 | P2-07 | Time to the Minute | Time 2.1 | 1 | K1 code word |
| S2-11 | P2-30 | Hours and Minutes | Time 2.3 | 1 | K1 code word |
| S2-12 | P2-29 | Time Taken | Time 2.1, Time 2.2 | 2 | K1 code word |
| S2-13 | P2-31 | Time Detective | Time 2.1, Time 2.2, Time 2.3 | 2 | K1 code word |
| S2-14 | P2-32 | Shape Patterns | 2D Shapes 1.1 | 1 | K1 letters spell a word |
| S2-15 | P2-33 | Pattern Rules | 2D Shapes 1.1 | 2 | K1 letters spell a word |
| S2-16 | P2-34 | Meet the Solids | 3D Shapes 2.1 | 1 | K1 letters spell a word |
| S2-17 | P2-35 | Solid Sort | 3D Shapes 2.1 | 2 | K3 total 15 + K1 code word |
| S2-18 | P2-36 | Picture Graph Scales | Picture Graphs with Scales 1.1 | 1 | K1 code word |
| S2-19 | P2-37 | Graph Detective Two | Picture Graphs with Scales 1.1 | 2 | K1 code word |
| S2-20 | P2-40 | Colour the Butterfly | Time 2.1, Time 2.2, Time 2.3 | 2 | colour by code, tally and matching parts |

(Regenerated from the built pages after the audit-fix build; titles, outcomes and mechanics are those in `school/p2/gen/`.)

## 3. Ranges and wording

Numbers to 1000 (answers 100 to 999 where the topic is 3-digit); tables 2, 3, 4, 5, 10 only (products to 50); ÷ with the sign written; fractions denominators 2 to 12, shaded-part pictures; money in $ and ¢ with decimal notation ($3.45, 345¢), no adding of decimal money; time to the minute (digital 3:47, hands), durations in h and min; m, kg, g, ℓ; pictures of 3D solids; picture-graph keys of 2, 5 and 10. Instruction sentences at most 10 words and at most 3 lines; clue sentences at most 10 words; check strip one or two short sentences. Money is written 50¢ and $2.50; times as 3:47 with am and pm without full stops. Original names and numbers: nothing copied from school papers or contest text.

## 4. Mechanics for self-checking (the answer must be shown wrong, not shown right)

Same as P1: every answer feeds a letter or a closing rule; wrong values give no letter or a decoy letter; the letters of each code word have exactly one arrangement that is a word, tested against about 129 000 words, so no wrong placement spells a word and no single slip spells a word.

## 5. Lessons carried from the three P1 audit rounds

Objects the pupil counts are at least 8 mm in both directions (measured at 300 dpi); code tables are one row of at most eight or nine boxes with room round every letter; every code word has exactly one real-word arrangement and no single wrong letter in any slot spells a word; answer checks reject at least 95% of single wrong answers and of wrong arrangements (enumerated for every page); a blank box is named in the teacher notes as invisible to the check; the page must survive a 1-bit copy; answers unique; a decoration must not look like a mark the check talks about; pages whose drawn answer cannot be seen say so in the notes; front matter, footers and keys agree on the code, the star mix and the page counts; hand-solve from the rendered image.

## 6. Verification per page

Generator with a seed; an independent solver that reads the printed text or drawing (not the generator's data); wrong-answer enumeration (validate.py); the word test; a key entry; a viewed render and a 1-bit photocopy simulation; at least 60% of the pages solved by hand from the render (the build report lists them).
