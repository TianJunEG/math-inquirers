# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 27 (Fill the Grid)

Role HOME_PARENT_PRACTICE. Files audited: `out/l27/L27_Home_Practice.pdf` (1 page), `L27_Home_Answers.pdf` (1 page), `L27_Parent_Summary.pdf` (1 page), and `out/l27/practice/` (key `t3l27`, 11 items: 5 Start here, 3 Think harder, 3 Go further; 4 templated, 6 with a drawn picture, 1 self-check). Source: `lessons/l27.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions (Term 2 defaults 7 and 9; the 23 Oct entries), `TERM_WIDE_AUDIT.md`, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md`, and the L24 audit of this role.

## Verdict: Ready after minor fixes

The home maths, the answer page and the parent page are right and plain, and the online practice runs cleanly: every item marks correctly, every picture agrees with its question, all templated variants are right, no external requests, no console errors and no overflow at phone or laptop width. The faults: the home sheet is words only although the lesson is about pictures in a grid (H3 and H4 ask a child to build a 3 by 3 and a 4 by 4 grid from a sentence, with no grid printed), one online item (`g1`) gives wrong reasons in its worked steps, the online practice has no rewind items and its picture alt text says only "a row of picture tiles", and the parent page repeats a term line that does not fit the lesson and has a thin recording statement.

Counts: High 0, Medium 3, Low 7.

## Method

- Home sheet and answer page rendered at 80 dpi and text extracted; all five home answers solved independently: H1 square; H2 the ? is 2; H3 row 2 is 2 3 1 and row 3 is 3 1 2 (the unique completion: the middle box of row 2 cannot be 2, and 3 cannot be last because the last column has a 3); H4 the second box of row 3 is 4 (enumerated over all 4 by 4 Latin squares: row 3 starting with 3, after rows 1 and 2 as given, has two completions, but the second box is 4 in both); H5 count up 46 to 52 is 6 steps. All match the answer sheet; the answers are on a separate page, so a double-sided print never shows them behind the questions.
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened. For each of the 10 non-self-check items a wrong answer and then the right one were typed or chosen. c1 and c2 (choice with a picture): the wrong choice shows the slip line ("The circle is already in the row. Which shape is missing?"), the right choice shows "Yes, that is right" and the steps. c3 (digits in a row, 4 variants of the missing digit), c4 (n by n boxes, n = 3 to 6), c5 (n by n circles, n = 3 to 7), g2 (n by n 3s, n = 5 to 9): 5 to 10 variants each taken by "Try a similar one" (after two wrong answers, which shows the worked steps) and the stated answer checked against an independent computation: 0 mismatches. t1, t2, t3, g1 (pictures): right answers accepted; each picture solved independently (t1 box a is a square; t2 two shapes; t3 not correct; g1 box a is 1, grid unique by enumeration). g3 self-check shows the checking steps. Typed-answer handling on c5: `3`, ` 3 `, `03`, `3.0`, `3 circles` right; `three` "Please type the answer with number digits, like 54."; `3,3` "Please type just the answer number."; empty "Type or choose an answer first. It is fine to guess."; `9` the slip line. The same wrong answer twice gets the "same answer as before" line. No ordered or multi-answer item exists in this lesson, so the "wrong order refused" test does not apply (the runner's ordered logic was exercised in the L24 audit). Keyboard: the first box has focus on load; Enter checks. External requests: none (the page requests only `data/t3l27.json`, `fonts.css` and fonts). Console errors: none. Horizontal overflow: none at either width.
- Pictures: each of the six drawn pictures was checked against its stem: c1 (circle, triangle, ? gives square), c2 (square, ?, circle gives triangle), t1 (triangle at the top right, circle in the centre; box a is top middle, so a square), t2 (circles at top middle and middle left, a in the centre: two shapes could go in), t3 (rows each have one of each; column 1 is circle, triangle, circle), g1 (3 4 1 2 / a ? ? 4 / ? 3 4 1 / ? ? ? 3): all agree with the answers.
- Page source: `index.html` and `practice.js` hold no answers or external URL; the answers sit in `data/t3l27.json`, fetchable by any browser (shared with every lesson).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 and H2 Start here (the missing shape in a row; the missing digit in a column), H3 Think harder (finish a 3 by 3 from one row and one start digit: a real elimination with a unique answer), H4 Go further (4 by 4, one box), H5 earlier practice (Term 1 Lesson 7, count up). Plain wording, no hints in stems, units not needed. Tier labels honest |
| Can a parent help without teaching differently? | Yes. The answer page uses the class words (the row has ... so the box must be ...), says "wait 10 seconds, then suggest drawing it", and the H3 worked answer reasons through the column as the class did |
| Pictures | None on the home sheet. H3 and H4 describe a 3 by 3 and a 4 by 4 grid in sentences ("Row 1 is 1, 2, 3, 4. Row 2 is 2, 1, 4, 3. Row 3 starts with 3. What is the second box of row 3?"): a child has to draw the grid before starting, with no box to draw in; the sheet says "use your tiles or draw it" (finding 1) |
| Answer-line size | Blanks for single answers are short lines; H3 gives two long lines for "Row 2: ___ Row 3: ___": enough for three digits each |
| Parent summary | One page, about 330 words, plain English. "What we did" about 80 words. Words list (row, column, grid, one of each). Do-not-teach line is specific: "Please do not teach a rule such as always start in a corner: the reason for each box is the lesson." The beyond-P1 statement is honest and specific: "Solving a 4 by 4 grid of digits, finding a box from only two clues, and saying how many of each digit a bigger grid holds go past the school Primary 1 syllabus on purpose"; "Finding the missing one in a row is early Primary 1 work." No MOE-aligned, GEP or SASMO claim. "Try at home" suggestions are doable with household items (buttons, coins, pasta). Have-ready box true against `l28.json` (the strip page with 14 strips) |
| Recording statement on the parent page | One sentence only: "Missed a lesson? Every lesson is recorded; your tutor will share a private link with enrolled families." No statement of what is recorded and no "please do not share the link"; `privacy.html` says the tutor and the shared screen are recorded, cameras are not, and the link is only for the enrolled families of the group (finding 5) |
| When your child is stuck | The WhatsApp number appears once with the 90-day retention, consistent with `privacy.html` ("90 days after the program ends, then deleted") |
| Term line | "Your child is learning to give a reason, and to read time and money in real life." sits on a grid lesson: a generic Term 3 line that does not fit (finding 6) |
| Print layout | A4, left margin 14 mm for the bound edge, answers on a separate page, header and footer clear; the home sheet is about 85% full |

## B. Online practice

| Item | Result |
|---|---|
| c1, c2, c3, c4, c5 (Start here) | Correct, pictures right, variants right. c4 asks a counting-boxes question (n by n boxes) at Start here: a multiplication fact (n times n up to 36) with no picture; "3 rows of 3 boxes make 9 boxes" is phrased as repeated counting: fine for 3 and 4, heavy for 6 (36) because there is no picture or array (Low, finding 8) |
| t1, t2, t3 (Think harder) | Correct; t1 and t2 pictures right; t3 right. `easier` buttons point to c1 and c2: right |
| g1 (Go further) | Answer and picture right; **the worked steps are wrong**: "The last box in row 3 has a 4 above it in its column, so row 3 is 2, 3, 4, 1" (row 3 is `? 3 4 1`, its empty box is the first, and the reason is that the row already holds 3, 4 and 1) and "The first column needs 1, so box a is 1" (the column 3, a, 2, ? needs 1 and 4; box a is 1 because its row already has the 4). A child who follows the steps is taught a false argument (finding 2) |
| g2 | Correct for n = 5 to 9; the stem reads "A 8 by 8 grid" for n = 8 ("An 8 by 8"): a grammar slip in one of five variants (Low, finding 9) |
| g3 | Self-check; fine |
| Rewind items | None: "runner rewind items absent" (brief). The preflight plans two online rewind items from lesson 17 (sharing) at the end of the set; nothing is rendered. The home sheet's H5 is the rewind (finding 4) |
| Answers in the page | Static JSON, as for every lesson (Low, shared) |
| Accessibility | All controls are labelled; focus order is tabs, then dots, then the answer box, then Check; radios carry the option text; the picture alt text is "a row of picture tiles" for c1, c2, t1, t2 and t3 and "squares grid 4 by 4" for g1: a screen-reader user cannot solve any picture item (finding 7) |
| Kind feedback | Neutral and short ("Not yet. Try once more.", "Let us look at it together."); no scores, no timers |

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Home sheet H3 and H4 | Both describe a grid in words only; the lesson is about pictures in a grid; the child must draw a 3 by 3 or a 4 by 4 grid first with no drawing area; a parent cannot see what to draw | Print a small empty 3 by 3 with row 1 filled for H3 and a 4 by 4 with two rows filled for H4; keep the answers page |
| 2 | Medium | Online `g1` steps 1 and 3 | The reasons are wrong (the box is in column 1 not "last", the column needs 1 and 4); the answer 1 is right | Step 1: "Row 3 has 3, 4 and 1, so its empty first box is 2." Step 2: "Row 2 is a, ?, ?, 4: the row has a 4, so box a cannot be 4." Step 3: "Column 1 has 3 and 2, so box a is 1 or 4; it is not 4, so it is 1." |
| 3 | Medium | Cross-lesson: `l20.json` `parent.next_materials` | The hand-off into Term 3 still says "print it a week before" and "clock (optional)" (preflight T9); not fixed | Edit before Term 3 starts |
| 4 | Low | Online practice end | No two rewind items from Term 2 Lesson 17 (sharing); the practice is current-lesson only (the Term 1 audit finding F4 repeated) | Add the planned two rewind items to the runner, marked "from earlier" |
| 5 | Low | Parent page, the recording sentence | Only "Every lesson is recorded; your tutor will share a private link with enrolled families"; no statement of what is recorded and no "do not share the link" (as in L11) | Add "The recording has the tutor, the shared screen and any voice that is unmuted. Please do not share the link." |
| 6 | Low | Parent page, term line | "...to read time and money in real life" on a grid lesson | Use "Your child is learning to give a reason for each step." |
| 7 | Low | Online practice, picture alt text | "a row of picture tiles" for every 3 by 3 picture, "squares grid 4 by 4" for g1 | Give each picture an informative label ("row: triangle, circle, empty") |
| 8 | Low | Online c4 | "n by n boxes" up to 6 by 6 with no picture | Show the grid (the `grid` figure exists) or limit n to 3 to 5 |
| 9 | Low | Online g2 | "A 8 by 8 grid": an article slip in one variant | Use "A grid with {n} rows and {n} columns" or a plural guard |
| 10 | Low | Parent try-at-home 1 | "put 9 small things of 3 kinds on a 3 by 3 grid you draw" asks a parent to draw a grid; the kit page's mat is the same grid and is free | "Use mat 1 from your kit page, or draw a 3 by 3 grid" |

Counts: High 0, Medium 3, Low 7.

## What is good

Every printed answer is right and the answer page is separate; the parent page says exactly what not to teach and states the beyond-P1 position honestly; the home sheet includes a Think harder and a Go further item with unique answers; the online practice has no tracking, no external request, no overflow, neutral feedback, a hint then a worked solution, and templated variants that cannot be wrong because the answer is computed (checked: about 30 variants, 0 errors).
