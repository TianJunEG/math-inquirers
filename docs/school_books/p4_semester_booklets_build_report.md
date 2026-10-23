# Primary 4 semester booklets: build report

Branch `claude/great-fermi-1hv4vc`. Pipeline `school/p4`; plan `docs/school_books/p4_semester_booklets_plan.md`; outcome wording `docs/school_books/p4_outcome_wording.md`.

## What was built

Two booklets, 40 pupil pages (P4-01 to P4-40), 20 each (Semester 1 = Terms 1 and 2, Semester 2 = Terms 3 and 4), 10 one-star and 10 two-star in each. Outputs in `school/p4/out/`: `P4_S1_Puzzles.pdf`, `P4_S2_Puzzles.pdf` (20 pages each), `P4_S?_FrontMatter.pdf` (5 pages: cover, licence, two pages of teacher notes, contents with coverage), `P4_S?_Answer_Key.pdf`, `P4_S?_Complete_Pack.pdf`, `verification.json`, `validation_report.txt`.

Front matter: DRAFT stamps on the cover, licence, teacher notes and key; the publisher line "Preciouslyours Pte Ltd, trading as Math Inquirers"; the registered office and contact email as in the P2 front matter; an annual licence whose wording a lawyer must approve; the teacher notes say schools vary and "Pictures are not actual size."; the only Ministry wording is the fact "The mathematics syllabus is published by the Ministry of Education, Singapore." on the licence page, and the sentence "Not affiliated with or endorsed by the Ministry of Education, Singapore." on the cover only. `python3 build.py --final` removes the DRAFT stamps.

The syllabus PDF (in the owner's uploads) was read for the Primary 4 pages only (printed pages 37 to 40). The wording of the 42 outcome lines is copied from it. Bullets under a line are joined with commas and semicolons. Nothing else from the PDF is quoted.

## Page table

| Page | Title | Stars | Outcomes | Mechanism |
|---|---|---|---|---|
| S1-01 (P4-01) | Place Value | 1 | NU1.1, 1.2 | code word |
| S1-02 (P4-02) | Words and Numerals | 1 | NU1.2 | matching, letters spell a word |
| S1-03 (P4-03) | Number Patterns | 2 | NU1.4 | code word |
| S1-04 (P4-04) | Round It | 1 | NU1.5, 1.6 | route: true statements with ≈ |
| S1-05 (P4-05) | Colour the Bus | 2 | NU1.1 to 1.5 | colour by code |
| S1-06 (P4-06) | Factor or Not? | 1 | FM2.1, 2.2, 2.4 | lettered Yes or No |
| S1-07 (P4-07) | Multiples Maze | 1 | FM2.1, 2.4 | route |
| S1-08 (P4-08) | Common Factors | 2 | FM2.1, 2.3 | code word |
| S1-09 (P4-09) | Number Riddles | 2 | FM2.1 to 2.5 | code word |
| S1-10 (P4-10) | Long Multiplication | 1 | FO3.1 | code word |
| S1-11 (P4-11) | Colour the Lorry | 2 | FO3.1, 3.2 | colour by code |
| S1-12 (P4-12) | Division | 2 | FO3.2 | code word |
| S1-13 (P4-13) | Number Ring | 2 | FO3.1, 3.2 | loop |
| S1-14 (P4-14) | Mixed or Improper | 1 | MI1.1 | code word |
| S1-15 (P4-15) | Fraction Number Line | 1 | MI1.1 | lettered choices |
| S1-16 (P4-16) | Fraction of a Set | 1 | FS2.1 | code word |
| S1-17 (P4-17) | Fraction Sums | 2 | FA3.1, MI1.1 | code word |
| S1-18 (P4-18) | Name the Angle | 1 | AN1.1 | lettered choices |
| S1-19 (P4-19) | Protractor Readings | 2 | AN1.2 | code word |
| S1-20 (P4-20) | Fraction Stories | 2 | FS2.1, FA3.1 | code word |
| S2-01 (P4-21) | Decimal Place Value | 1 | DP1.1 | code word |
| S2-02 (P4-22) | Order the Decimals | 2 | DP1.2 | ordering |
| S2-03 (P4-23) | Decimal Match | 1 | DP1.3, 1.4 | matching |
| S2-04 (P4-24) | Rounding Decimals | 1 | DP1.5 | lettered choices |
| S2-05 (P4-25) | Magic Decimals | 2 | DA2.1 | magic square totals |
| S2-06 (P4-26) | Decimal Shares | 2 | DM3.1 to 3.3 | code word |
| S2-07 (P4-27) | Missing Sides | 1 | AP1.1, 1.2 | code word |
| S2-08 (P4-28) | L-Shapes | 1 | AP1.3 | code word |
| S2-09 (P4-29) | Match the Figures | 2 | AP1.3 | matching |
| S2-10 (P4-30) | Joined Shapes | 2 | AP1.1 to 1.3 | code word |
| S2-11 (P4-31) | Shape Facts | 1 | RS2.1 | lettered True or False |
| S2-12 (P4-32) | Complete the Corner | 2 | RS2.1, 2.2 | lettered points |
| S2-13 (P4-33) | Mirror Lines | 1 | LS3.1, 3.2 | lettered Yes or No |
| S2-14 (P4-34) | Complete the Figure | 2 | LS3.1, 3.3 | code word from counts |
| S2-15 (P4-35) | Name the Solid | 1 | NT4.1 | lettered choices |
| S2-16 (P4-36) | Which Net? | 2 | NT4.3, 4.4 | lettered choices |
| S2-17 (P4-37) | Complete the Table | 1 | ST1.1, 1.2 | totals and code word |
| S2-18 (P4-38) | Line Graph Detective | 1 | ST1.2 | code word |
| S2-19 (P4-39) | Pie Chart | 2 | ST1.2, FS2.1 | code word |
| S2-20 (P4-40) | Colour the Ferry | 2 | DP1.2, 1.4, 1.5, DA2.1, DM3.1, 3.2 | colour by code |

Coverage: 40 of the 42 outcome lines have a page. Two are honest gaps, AN1.3 (drawing an angle of given size) and NT4.2 (drawing 2D representations of solids): a pencil drawing cannot be checked by a strip printed on the page. RS2.2 (drawing rectangles and squares) and LS3.3 (completing a symmetric figure) are covered in part: the pupil chooses the fourth corner, or shades and then counts squares, but the drawing itself is never seen. The front matter lists the two gaps.

## Validation

`python3 validate.py` on the final build: 736 checks, 0 failed (`out/validation_report.txt`). It covers: every page's generator checks (independent solver, one answer, word test), the wrong-answer enumeration (every single change of one answer and every wrong arrangement; the share rejected was 100% on every page, the threshold is 95%), tier mix 10 and 10, page codes, the reading level (14 words, 4 sentences), black and white only, stroke widths, answer boxes of at least 12 mm, fonts embedded, page sizes, front matter wording (DRAFT, email, address, publisher line, no Ministry wording other than the two allowed sentences), the footer with a 68-character school name, layout in a browser (overflow, clipping, margins, fill, minimum text size 8 pt), the colour-page labels, and a 1-bit render at 150 dpi (ink loss and flat grey).

The validate script was adapted from P2: 42 outcome lines, the 14-word limit, three colour pages (P4-05, P4-11, P4-40), no coin checks, and the two documented gaps. The ink-loss limit for the answer key was raised from 35% to 38%: the key pages measure 34 to 35% because the key is small text and the loss is anti-aliasing, not content.

## Hand-solved from the rendered image (final builds)

All 40 pages were solved by hand from the rendered image of the final build, without looking at the key, and compared with the key afterwards: 33 code-word pages gave the word in the key (HUNGRY, BACKUP, CREAMY, TEACUP, FROZEN, PEANUT, FRUITY, SHRIMP, FIGURE, FABRIC, WALRUS, BANDIT, CURFEW, CAMPUS, POLICE, STUDIO, WIZARD, DONKEY, COBALT, FAMILY, FRIDGE, WALNUT, CRAFTY, CANOPY, BOTANY, TURKEY, WOMBAT, FATHOM, DEVOUR, BOUNTY, FLIGHT, COUSIN, SHADOW), and the 7 pages without a word (P4-04 and P4-07 routes of 11 and 8 boxes, P4-13 ring closing on 179, P4-25 magic square, and the three colour pages P4-05, P4-11, P4-40 with their colour counts and twin marks) came out as the key says. Pages changed after a first solve (S1-19, S2-06, 07, 10 to 17, 20) were solved again from the final image. Every page was also viewed as an image in normal render, and the pages with figures, graphs, dot grids, nets, protractors and colour pictures as a 1-bit photocopy simulation at 100 dpi.

Hand-solving found real faults that no generator check had caught:

- P4-37 Complete the Table: the key listed the six missing numbers cells first, then row totals, then column totals, but the page said "row by row". The independent solver used the same order, so every check passed and the word was wrong for any pupil who followed the instruction. Fixed: the order is now reading order in the generator and in the solver, and the word is FLIGHT.
- P4-31 Shape Facts: "A square has 2 equal sides" and "A square has 4 pairs of equal sides" are arguable. Replaced by "Only two sides of a square are equal", "All four sides of a square are equal", and "pairs of equal sides" only for rectangles.
- P4-19 Protractor Readings: the arm lay over printed numbers and the inner numbers collided near the centre. Now no angle is a multiple of 20 or within 30 degrees of the base, and the inner scale has numbers only at 40, 60, 120 and 140.
- P4-40: a part read "1 × 5 ="; the bank now never makes a multiplication by 1.
- Layout: P4-27 (units outside the card), P4-35 and P4-36 (figures over the names), P4-33 (dashed line over the caption, figure over the number), P4-34 (axis numbers clipped), P4-14 (bars past the margin), P4-22 (page too empty), P4-38 (check strip pushed down), P4-18 (the small letter a sat on the middle arm).

## Weak points (honest list)

1. P4-19: a protractor drawn on the page can only be read to about 2 degrees by eye at photocopy size. All angles are multiples of 5 and the code table steps are at least 5 apart, so a reading out by 5 is caught; a reading out by 2 or 3 would be rounded by the pupil. The arm is thick and the printed numbers are small (3 mm). A real protractor on a real angle is not covered.
2. P4-18 items 5 and 6: the marked angle spans a middle arm (angle a covers two smaller angles). The arc is one unbroken arc and the letter a sits on the left or right of it, but a pupil may still think a refers to only one part. The decoy names are the smaller angles, so the check catches it.
3. P4-32 dot grids: dots 1.1 mm across at 5.2 mm spacing. They survive a 1-bit copy but look light on a worn copier.
4. P4-34 grid lines: some rows look heavier than others in a low-resolution raster because of anti-aliasing; the PDF itself has equal lines.
5. P4-36: the nets are scaled to fit the card, so line weight differs between nets.
6. The colour pages P4-05, P4-11 and P4-40 are abstract pictures (a bus, a lorry, a ferry) whose answer boxes are 9 mm (the P2 template and the shared library), below the 12 mm rule of the other pages. The check strip counts colours; a pupil without crayons writes Y, R, B, G or O.
7. Code words: the pupil's word is checked against about 241 000 words; very rare words may count as a word. A wrong set of letters can still, rarely, spell a word with two wrong answers at once; only one wrong answer at a time and every wrong arrangement were tested.
8. Lettered-choice pages have only two or three options per row, so a pupil can guess. The word test makes any wrong set fail to spell a word, but it cannot tell a careful pupil from a lucky one.
9. Multiplication and division in columns (FO3.1, FO3.2) are checked only by the answer, not by the working.
10. The sign ≈ and the angle sign are drawn as pictures (the fonts lack them), so they cannot be searched or copied as text.
11. The reading level is within the P4 limit of 14 words but some stories (P4-20, P4-30) are two sentences of 12 to 14 words; weaker readers will need help.

## Similarity check

Run against every file in `docs/books/private_*` and `docs/sasmo/private_*` (43 files, about 21 700 text units; gitignored, not copied anywhere). The check script is not committed. Method: (a) every 7-word run of all page text (body, instructions, strip, key, teacher note) against every 7-word run of the private text; (b) for every question card, any private unit that shares at least two numbers (11 or more, or a decimal) and at least three non-generic words; (c) a manual look at structure.

- First run: 9 shared 7-word runs, on P4-20 ("spent 3/8 of her money on a book and", "how many litres of water are in"), P4-29 (a run of figure labels, "cm 3 cm 10 cm 7 cm"), P4-31 and P4-33 (teacher-note phrases). All were reworded or reseeded. Final run: 0 shared 7-word runs.
- Scenario with the same numbers: 2 automatic hits, both false (a code table and a pattern list, not a question). No page repeats a private question with its numbers. P4-29 once had the same four side lengths as a private rectilinear figure and was reseeded.
- Structure: the item types are the textbook kinds named in the syllabus (place value chart, factors, long multiplication, fraction of a set, area of composite figures and so on). No page copies a private entry's combination of scenario, numbers and question; the stories were written fresh and several (tank, savings, path round a garden) were checked against the private text for wording only.
- The check is an automated word and number match. It cannot judge that two differently worded questions are the same idea; a human reviewer of the private notes could still flag a topic overlap.

## Decisions for the owner

1. Licence wording, title and the Ministry sentence stay DRAFT until the owner and a lawyer approve them (`build.py --final` removes the stamps).
2. Gaps: should AN1.3 and NT4.2 get pages anyway (drawing an angle with a protractor; drawing a cube on isometric dots), with a teacher check by overlay or by a second pupil? No printed self-check exists for a drawing.
3. Colour pages: keep the three colour pictures as abstract shapes, or commission recognisable art? Keep the 9 mm answer boxes on them?
4. Whether the booklet should print the protractor with numbers at every 20 degrees (as now, thin) or at every 10 (clearer, more cluttered).
5. The split of Primary 4 into Semester 1 (whole numbers, factors and multiples, four operations, fractions, angles) and Semester 2 (decimals, area and perimeter, rectangle and square, symmetry, solids, data) follows the typical order only; schools vary and the teacher notes say so.
6. One-star and two-star: the two-star pages combine two steps or two clues. Confirm that this reading of the star rule is what the owner wants at Primary 4.

## Uncertain

- No external reviewer has seen the pages; the hand-solve is by the builder. A fresh pupil-level solve and a teacher read-through are still needed, in particular for P4-18, P4-19, P4-34 and P4-36.
- The similarity check cannot rule out that a private source has a topic overlap in a different wording.
- Pages were not photocopied on a real copier; the 1-bit simulation at 100 and 150 dpi stands in for it.
