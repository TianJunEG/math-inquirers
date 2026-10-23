# Primary 3 semester booklets: build report

## PAUSED (23 Oct 2026)

Owner decision SCHOOLBOOKS-WAIT: Primary 3 to 6 school booklets wait until the Primary 2 booklets are audited and schools show interest. Work stopped during the reading phase. Nothing is built.

Done: read the P1 plan, build report, audits (rounds 1 to 3), `school/p1` pipeline (build.py, render.py, validate.py, gen/), plan.md (templates T01-T12, P3 reading load 18 words per sentence), the Primary 3 syllabus pages 35-36 of the PDF, `docs/books/p3_school_paper_patterns.md`.
Not done: `docs/school_books/p3_semester_booklets_plan.md` (gap analysis and page allocation), `school/p3/` (copy of `school/p1`), pages, front matter, keys, validation.

## Where to resume

1. Write the plan: gap analysis and 40-page allocation (S1 = Terms 1-2, S2 = Terms 3-4, 10 one-star and 10 two-star each), in the P1 plan format.
2. `cp -r school/p1 school/p3`; change outcomes.py to the 34 Primary 3 outcome lines below; replace the page modules; fix validate.py P1-only checks (decimal money $3.45 is now allowed, division sign allowed, P1 syllabus section check, 3 colour-by-code pages, P1-specific page numbers).

Primary 3 outcome lines (34, wording from the PDF, pp. 35-36):
Numbers up to 10 000 1.1 counting in hundreds/thousands; 1.2 notation, representations, place values; 1.3 reading and writing in numerals and words; 1.4 comparing and ordering; 1.5 patterns.
Addition and Subtraction 2.1 algorithms (up to 4 digits); 2.2 mental calculation of two 2-digit numbers.
Multiplication and Division 3.1 tables of 6, 7, 8, 9; 3.2 multiplying and dividing within the tables; 3.3 division with remainder; 3.4 algorithms (up to 3 digits by 1 digit); 3.5 mental calculation within the tables.
Fractions: 1.1 equivalent; 1.2 simplest form; 1.3 comparing and ordering unlike fractions (denominators not above 12); 1.4 equivalent fraction given the denominator or numerator; 2.1 add and subtract two related fractions within one whole.
Money 1.1 adding and subtracting money in decimal notation.
Length, Mass and Volume 1.1 measuring length in km and volume in ml; 1.2 compound units; 1.3 converting (km/m, m/cm, kg/g, l/ml). Time 2.1 seconds; 2.2 start, finish or duration; 2.3 24-hour clock.
Area and Perimeter 1.1 concepts; 1.2 area in square units, cm2, m2; 1.3 perimeter of rectilinear figure, rectangle, square; 1.4 area of rectangle and square.
Angles 1.1 concept; 1.2 right angles, greater or smaller than a right angle. Perpendicular and Parallel Lines 2.1 identify; 2.2 draw.
Bar Graphs 1.1 reading and interpreting; 1.2 different scales on the axis.

Expected honest gap notes for the plan (not yet written up): practical measuring (km, ml, seconds, compound units) can only be read from drawn scales (recognition); angle concept is recognition; drawing perpendicular and parallel lines can only be checked through a lettered-grid read-off; mental calculation outcomes cannot be enforced on a page.
