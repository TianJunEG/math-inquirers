# Primary 2 early-finisher puzzles: two semester booklets (plan)

Date: 23 Oct 2026. Model: `docs/school_books/p1_semester_booklets_plan.md` and the P1 build report and three audit rounds. Pipeline: `school/p2/` (copied from `school/p1/`; P1 untouched). Build progress and weak points: `docs/school_books/p2_semester_booklets_build_report.md`.

## 0. Decisions this plan follows

Owner decisions (`docs/terms/owner_decisions.md`): two booklets, **Semester 1** (typical school Terms 1 and 2) and **Semester 2** (Terms 3 and 4), 20 pupil pages each, 10 one-star and 10 two-star, self-checking, pure black and white, no Mi. Teacher notes say that schools vary. Footer codes print both numbers (for example `S1-07 (P2-17)`: seventh page of the booklet, page 17 of the 40 in build order). Original problems only; coins and notes are original art "inspired by", with cents; no MOE logo or claims, no price; the not-affiliated sentence only on the licence page; `(c) 2026 Preciouslyours Pte Ltd` on pupil footers with a `School (write name): ____` line; cover publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers"; annual licence (one school year, renewable), wording DRAFT for a lawyer; registered office 66 Tannery Ln, Singapore 347805; contact pypteltd@gmail.com; DRAFT stamps on cover, licence, teacher notes and both keys; keys read "Key page n of N" with outcome tags in the PDF's own wording and small solved pictures.

Sources read: the syllabus PDF pages 33 and 34 (Primary 2; wording copied, kept in `docs/school_books/p2_outcome_wording.md`), `docs/school_books/plan.md` (templates, reading load: P2 = at most 10 words a sentence, 3 sentences, check wording one sentence of at most 14 words), `p2_school_paper_patterns.md` and `p2_non_routine_catalogue.md` (question TYPES only, no text copied), `coin_reproduction_check.md`, `school/colour_by_code/README.md`, and every audit lesson from the P1 booklets (carried into section 5).

## 1. Gap analysis: the 30 Primary 2 outcome lines against what early-finisher pages can do

The PDF has 30 numbered lines (counting each of fractions 1.1 to 1.3 and 2.1, and the three-bullet lines, as one line). An early-finisher page is a single printed page with a built-in check, so some verbs of the syllabus can only be practised in part. "Full" means the page asks the pupil to do what the line says; "Part" means a printed substitute is used.

| Outcome (PDF wording, short) | Pages | Coverage |
|---|---|---|
| WN 1.1 counting in tens/hundreds | P2-11, P2-02(cbc P2-38) | Full |
| WN 1.2 notation, representations, place values (hundreds, tens, ones) | P2-01, P2-10, P2-17, P2-38 | Full (place-value discs, digit value, regrouped forms) |
| WN 1.3 reading and writing numbers in numerals and in words | P2-09, P2-17 | Part: reading and matching words and numerals; the pupil writes numerals, not number words (a written word cannot be checked) |
| WN 1.4 comparing and ordering numbers | P2-10, P2-17 | Full |
| WN 1.5 patterns in number sequences | P2-11 | Full |
| WN 1.6 odd and even numbers | P2-12, P2-17 | Full |
| AS 2.1 algorithms (up to 3 digits) | P2-02, P2-13, P2-18 | Full (with and without renaming) |
| AS 2.2 mental calculation, 3-digit number and ones/tens/hundreds | P2-03, P2-18 | Full |
| MD 3.1 tables of 2, 3, 4, 5, 10 | P2-04, P2-14, P2-20, P2-39 | Full |
| MD 3.2 use of ÷ | P2-05, P2-19, P2-20 | Full |
| MD 3.3 relationship between x and ÷ | P2-19 | Full |
| MD 3.4 multiplying and dividing within the tables | P2-04, P2-05, P2-20, P2-39 | Full |
| MD 3.5 mental calculation within the tables | P2-14, P2-20 | Full |
| FR 1.1 fraction as part of a whole | P2-15 | Full |
| FR 1.2 notation and representations of fractions | P2-15, P2-21 | Full |
| FR 1.3 comparing and ordering (unit fractions, like fractions) | P2-21 | Full (denominators up to 12) |
| FR 2.1 adding and subtracting like fractions within one whole | P2-22 | Full |
| MO 1.1 counting money in dollars and cents | P2-06, P2-24 | Full (pictured coins and notes) |
| MO 1.2 reading and writing money in decimal notation | P2-06, P2-16 | Full |
| MO 1.3 comparing two or three amounts | P2-23 | Full |
| MO 1.4 converting decimal notation to cents only, and back | P2-16 | Full |
| ME 1.1 measuring: length in m, mass in kg/g, volume in litres | P2-08, P2-25, P2-26 | Part: reading pictured scales and containers; the pupil cannot handle a real instrument on a printed page |
| ME 1.2 appropriate units and abbreviations m, g, kg, ℓ | P2-27, P2-08, P2-25, P2-26 | Full |
| ME 1.3 comparing and ordering lengths, masses, volumes | P2-28 | Full (one unit at a time: kg to g and m to cm conversions are Primary 3) |
| TI 2.1 telling time to the minute | P2-07, P2-31(cbc P2-40) | Full |
| TI 2.2 measuring time in hours and minutes | P2-29, P2-31 | Full |
| TI 2.3 converting hours and minutes to minutes, and back | P2-30 | Full |
| GE 1.1 making/completing patterns with 2D shapes by attributes | P2-32, P2-33 | Part: completing and choosing; the pupil's own drawn pattern cannot be checked, so patterns are completed by picking the lettered next shapes |
| GE 2.1 identifying, naming, describing, classifying 3D shapes | P2-34, P2-35 | Full by picture (cube, cuboid, cone, cylinder, sphere); no real solids to handle |
| ST 1.1 picture graphs with scales | P2-36, P2-37 | Full (scales 2, 5 and 10) |

**Not covered, or only in part (for the owner):** writing number words by hand (WN 1.3), taking a real measurement or building a real pattern or solid (ME 1.1, GE 1.1, GE 2.1), and anything that needs the pupil to draw. These are the verbs a printed self-checking page cannot see; the teacher notes say so. **Excluded as above Primary 2** (and never used): decimals beyond dollars-and-cents notation, adding or subtracting decimal money (Primary 3), conversions kg to g, m to cm, ℓ to mℓ, tables of 6 to 9, division with remainder, equivalent fractions, unlike fractions, mixed numbers, bar graphs, tally charts as a taught skill, 24-hour time, angles, area and perimeter.

## 2. The 40-page allocation

Typical order, schools vary. Singapore schools teach Primary 2 in different orders (see `p2_school_paper_patterns.md`, section 2: numbers and add/subtract in Term 1, multiplication and division with length and graphs in Term 2, money, mass, volume and shapes in Term 3, fractions, time and a review in Term 4). The split below is a decision for the booklets, not a claim about any school: Semester 1 holds number, the four operations and fractions; Semester 2 holds money, measurement, time, shapes and graphs. Fractions sit in Semester 1 although some schools teach them in Term 4; the teacher notes say to hand out any page when its topic has been taught.

Page ids P2-01 to P2-40 are in build order; "Pos" is the position in the booklet. Mechanics (from plan.md section 8.1): K1 code word, K3 total, K4 grid/logic, K6 route, K7 answer put back, K8 loop closes, K9 measured, TF true/false letters, CBC colour by code. Stars: 1 or 2; two-star never means a new topic, only two steps or two clues.

### 2a. Semester 1 (Terms 1 and 2): 10 one-star, 10 two-star

| Pos | Page | Title | Outcomes | Stars | Mechanic |
|---|---|---|---|---|---|
| S1-01 | P2-01 | Hundreds, Tens, Ones | WN 1.2 | 1 | K1 code word; place-value discs in a chart, one question about the value of a digit |
| S1-02 | P2-38 | Colour the Rocket (CBC) | WN 1.1 to 1.3 (bank-dependent) | 1 | colour by code, tally and matching parts |
| S1-03 | P2-09 | Words and Numbers | WN 1.3 | 1 | K6 route: number words and numerals that match |
| S1-04 | P2-12 | Odd or Even | WN 1.6 | 1 | K6 route over odd or even numbers |
| S1-05 | P2-10 | Digit Cards | WN 1.2, 1.4 | 2 | K1 code word: greatest, smallest and in-between numbers from three digit cards |
| S1-06 | P2-11 | Number Patterns | WN 1.1, 1.5 | 2 | K1 code word: missing terms, steps of 2, 3, 5, 10, 100 |
| S1-07 | P2-17 | Mystery Numbers | WN 1.2, 1.3, 1.4, 1.6 | 2 | K1 code word + clue test, 3-digit riddles |
| S1-08 | P2-02 | Column Sums | AS 2.1 | 1 | K1 code word: vertical sums, up to 3 digits |
| S1-09 | P2-03 | Mental Jumps | AS 2.2 | 1 | K6 route: 3-digit number plus or minus ones, tens, hundreds |
| S1-10 | P2-13 | Missing Digits | AS 2.1 | 2 | K1 code word: the missing digits of vertical sums |
| S1-11 | P2-18 | Story Sums to 1000 | AS 2.1, 2.2 | 2 | K1 code word: two-step stories (problem solving) |
| S1-12 | P2-04 | Equal Groups | MD 3.1, 3.4 | 1 | K1 code word: groups and arrays, tables of 2, 5, 10 |
| S1-13 | P2-05 | Share It Out | MD 3.2, 3.4 | 1 | K1 code word: sharing and grouping stories with ÷ |
| S1-14 | P2-14 | Times Table Maze | MD 3.1, 3.5 | 1 | K6 route over correct facts from tables of 2, 3, 4, 5, 10 |
| S1-15 | P2-19 | Fact Families | MD 3.3, 3.2 | 2 | K8 loop closes: x and ÷ facts linked round a loop |
| S1-16 | P2-20 | True or False Tables | MD 3.1, 3.4, 3.5 | 2 | TF letters spell a word |
| S1-17 | P2-39 | Colour the Castle (CBC) | MD 3.1, 3.4 | 2 | colour by code, tables and ÷ |
| S1-18 | P2-15 | Parts of a Whole | FR 1.1, 1.2 | 1 | K1 code word from shaded fractions |
| S1-19 | P2-21 | Fraction Order | FR 1.2, 1.3 | 2 | K1 letters of the fractions, smallest first |
| S1-20 | P2-22 | Fraction Sums | FR 2.1 | 2 | K1 code word: like fractions within one whole |

### 2b. Semester 2 (Terms 3 and 4): 10 one-star, 10 two-star

| Pos | Page | Title | Outcomes | Stars | Mechanic |
|---|---|---|---|---|---|
| S2-01 | P2-06 | Dollars and Cents | MO 1.1, 1.2 | 1 | K1 code word: pictured coins and notes, $ amounts written in decimal notation |
| S2-02 | P2-16 | Writing Money | MO 1.2, 1.4 | 2 | K1 code word: decimal notation to cents and back |
| S2-03 | P2-23 | Which Costs More? | MO 1.3 | 2 | K1 letters in order of price (two and three amounts) |
| S2-04 | P2-24 | Purse Match | MO 1.1 | 2 | K1 letters: which purse holds which amount |
| S2-05 | P2-08 | Metres | ME 1.1, 1.2 | 1 | K1 code word: reading a pictured metre scale |
| S2-06 | P2-25 | Kilograms and Grams | ME 1.1, 1.2 | 1 | K1 code word: reading pictured scales |
| S2-07 | P2-26 | Litres | ME 1.1, 1.2 | 1 | K1 code word: reading pictured containers |
| S2-08 | P2-27 | Which Unit? | ME 1.2 | 1 | TF letters of the sensible unit spell a word |
| S2-09 | P2-28 | Order the Measures | ME 1.3 | 2 | K1 letters of the longest, heaviest, fullest |
| S2-10 | P2-07 | Time to the Minute | TI 2.1 | 1 | K1 code word from clock faces |
| S2-11 | P2-30 | Hours and Minutes | TI 2.3 | 1 | K1 code word: conversions |
| S2-12 | P2-29 | How Long Did It Take? | TI 2.1, 2.2 | 2 | K1 code word: start and end clock times |
| S2-13 | P2-31 | Time Detective | TI 2.1, 2.2, 2.3 | 2 | K1 code word: a timetable (problem solving) |
| S2-14 | P2-32 | Shape Patterns | GE 1.1 | 1 | K1 letters of the shape that comes next |
| S2-15 | P2-33 | Pattern Rules | GE 1.1 | 2 | K1 letters: two attributes change together |
| S2-16 | P2-34 | Meet the Solids | GE 2.1 | 1 | K1 letters of the name of each solid |
| S2-17 | P2-35 | Solid Sort | GE 2.1 | 2 | K3 totals in a sorting table |
| S2-18 | P2-36 | Picture Graph Scales | ST 1.1 | 1 | K1 code word from a scaled picture graph |
| S2-19 | P2-37 | Graph Detective Two | ST 1.1 | 2 | K3 totals and a second sum |
| S2-20 | P2-40 | Colour the Boat (CBC) | TI 2.1, ME 1.1 (bank-dependent) | 2 | colour by code, tally |

(Final page titles, outcomes and mechanics are those in `school/p2/gen/` and in the build report; this table was written before the build and the report records every difference.)

## 3. Ranges and wording

Numbers to 1000 (answers 100 to 999 where the topic is 3-digit); tables 2, 3, 4, 5, 10 only (products to 50); ÷ with the sign written; fractions denominators 2 to 12, shaded-part pictures; money in $ and ¢ with decimal notation ($3.45, 345¢), no adding of decimal money; time to the minute (digital 3:47, hands), durations in h and min; m, kg, g, ℓ; pictures of 3D solids; picture-graph keys of 2, 5 and 10. Instruction sentences at most 10 words and at most 3 lines; clue sentences at most 10 words; check strip one or two short sentences. Money is written 50¢ and $2.50; times as 3:47 with am and pm without full stops. Original names and numbers: nothing copied from school papers or contest text.

## 4. Mechanics for self-checking (the answer must be shown wrong, not shown right)

Same as P1: every answer feeds a letter or a closing rule; wrong values give no letter or a decoy letter; the letters of each code word have exactly one arrangement that is a word, tested against about 129 000 words, so no wrong placement spells a word and no single slip spells a word.

## 5. Lessons carried from the three P1 audit rounds

Objects the pupil counts are at least 8 mm in both directions (measured at 300 dpi); code tables are one row of at most eight or nine boxes with room round every letter; every code word has exactly one real-word arrangement and no single wrong letter in any slot spells a word; answer checks reject at least 95% of single wrong answers and of wrong arrangements (enumerated for every page); a blank box is named in the teacher notes as invisible to the check; the page must survive a 1-bit copy; answers unique; a decoration must not look like a mark the check talks about; pages whose drawn answer cannot be seen say so in the notes; front matter, footers and keys agree on the code, the star mix and the page counts; hand-solve from the rendered image.

## 6. Verification per page

Generator with a seed; an independent solver that reads the printed text or drawing (not the generator's data); wrong-answer enumeration (validate.py); the word test; a key entry; a viewed render and a 1-bit photocopy simulation; at least 60% of the pages solved by hand from the render (the build report lists them).
