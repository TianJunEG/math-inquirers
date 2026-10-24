# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 28 (Make a Table)

Role HOME_PARENT_PRACTICE. Files audited: `out/l28/L28_Home_Practice.pdf` (1 page), `L28_Home_Answers.pdf` (1 page), `L28_Parent_Summary.pdf` (1 page), and `out/l28/practice/` (key `t3l28`, 11 items: 5 Start here, 3 Think harder, 3 Go further; 8 templated, 3 with a drawn picture (c1 and c2 redrawn for each variant)). Source: `lessons/l28.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions (Term 2 defaults 7 and 9; the 23 Oct entries), `TERM_WIDE_AUDIT.md`, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md`, and the L24 audit of this role.

## Verdict: Ready after minor fixes

The home maths, the answer page and the parent page are right and plain, and the online practice runs cleanly: every item marks correctly, every templated variant shown is right (about 60 variants read and checked against the formulas), every picture has exactly the number of sticks its question says (checked line by line in all nine pictures), there are no external requests and no overflow at phone or laptop width. The faults are small: the stick pictures merge into lines so the sticks cannot be counted from the picture, the home sheet has no pictures and one parent activity (the cup and sugar table) gives no numbers, the online practice has no rewind items, picture alt text is minimal, and the parent page has a thin recording statement and a term line that does not fit.

Counts: High 0, Medium 2, Low 7.

## Method

- Home sheet and answer page rendered at 80 dpi and text extracted; all five home answers solved independently: H1 5 pencils a box: 15 and 20; H2 2 pens to 3 pencils: 8 pens go with 12 pencils; H3 15 triangles need 31 sticks (2n + 1); H4 40 sticks make 13 squares (3n + 1 = 40, n = 13: brute-forced for n up to 100); H5 27 + 16 = 43, so the box is 34. All match the answer sheet; the answers are on a separate page, so a double-sided print never shows them behind the questions.
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened. For each item a wrong answer and then the right one were typed or chosen. Templated items (c1, c2, c3, c5, t1, t3, g1, g2: 8 families) were varied by "Try a similar one" after two wrong answers (which shows the worked steps): 14 distinct c3 variants, 15 c5 variants, 5 to 7 variants for each other family, the answer in each "The answer is ..." compared with an independent computation (2n + 1, 3n + 1, p times k, s + 3e, (t - 1) / 2, (t - 1) / 3): 0 mismatches. Typed-answer handling on c1: `9`, `9 sticks`, `09` right; `nine` "Please type the answer with number digits, like 54."; `9.5` "Not yet. Try once more."; empty "Type or choose an answer first. It is fine to guess."; the slip line for 12 ("The triangles share sticks. Each new triangle adds only 2."). The same wrong answer twice gets the "same answer as before" line. No ordered or multi-answer item exists in this lesson, so the "wrong order refused" test does not apply. Keyboard: the first box has focus on load; Enter checks. External requests: none. Console errors: none. Horizontal overflow: none at either width.
- Pictures: the three picture families (c1 triangles n = 2 to 6, c2 squares n = 2 to 5, c4 four triangles) were checked by counting the line elements in each SVG: 5, 7, 9, 11, 13 for triangles and 7, 10, 13, 16 for squares, equal to 2n + 1 and 3n + 1, and each picture's label gives the same n as the stem. The pictures are right but the sticks merge (finding 1).
- Page source: `index.html` and `practice.js` hold no answers or external URL; the answers sit in `data/t3l28.json`, fetchable by any browser (shared with every lesson).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 and H2 Start here (an equal-groups table; a two-row ratio table with new numbers), H3 Think harder (the 15th triangle row by "double and add 1"), H4 Go further (working back from 40 sticks), H5 earlier practice (Term 1 Lesson 8: 27 + 16 = box + 9). Plain wording; no hints in stems; units on the line (pencils, sticks, squares). The H4 worked answer says "So there are 12 and 1 more squares: 13", awkward (Low, finding 7) |
| Can a parent help without teaching differently? | Yes. The answer page uses the class words (each box adds 5, double and add 1, take away the first square) and says "wait 10 seconds, then suggest drawing it" |
| Pictures | None on the home sheet; the three growing-pattern questions describe the sticks in words ("3 sticks for 1 triangle, 5 sticks for 2 triangles ...") and a drawing is optional (finding 4) |
| Parent summary | One page, about 330 words, plain English. Words list (table, picture, more each time, rule). Do-not-teach line is specific: "Please do not teach letters for a rule: we say it in words." The beyond-P1 statement is honest and specific: "Finding the 10th, 20th and 100th picture of a growing stick pattern, and working back from a total number of sticks, go past the school Primary 1 syllabus on purpose"; "Completing a table of equal groups is Primary 1 work." No MOE-aligned, GEP or SASMO claim. Have-ready box true against `l29.json` (the mistake-card page, 8 cards, the mat is not cut); it also tells families to keep the paper strips, which no later lesson needs (Low, finding 5) |
| "Try at home" | (1) "Make a table: 1 cup, 2 cups, 3 cups of water, with spoons of sugar for each. Ask: what is the next number?" gives no sugar numbers and no rule, so a parent cannot know what to ask (Medium, finding 2); (2) "Stick game: build triangles in a row with 14 paper strips or straws, never matches or toothpicks": safe and clear; (3) "Ask: how do you know? How many more each time?" |
| Recording statement on the parent page | The same one sentence as every Term 3 page: "Every lesson is recorded; your tutor will share a private link with enrolled families." No statement of what is recorded and no "do not share the link" (L11 had both) (finding 6) |
| When your child is stuck | The WhatsApp number appears once with the 90-day retention, consistent with `privacy.html` ("90 days after the program ends, then deleted") |
| Term line | "Your child is learning to give a reason, and to read time and money in real life." sits on a table lesson: a generic Term 3 line that does not fit (finding 8) |
| Print layout | A4, left margin 14 mm for the bound edge, answers on a separate page, header and footer clear; the home sheet is about 80% full with room for the answers lines |

## B. Online practice

| Item | Result |
|---|---|
| c1, c2 (sticks in n triangles and n squares) | Correct, pictures right, variants right; the picture shows the sticks as merged lines, so the picture cannot be counted stick by stick (finding 1) |
| c3 (pages in k days) | Correct for p = 2 to 6, k = 3 to 5; the worked steps read "Each day adds p pages. Count on k times." Wording and plurals fine |
| c4 (how many more sticks each new triangle needs) | Correct; picture of four triangles right |
| c5 (next number after s, s + e, s + 2e) | Correct for every variant shown (the formula s + 3e covers all 16 combinations of s and e from 2 to 5) |
| t1 (10 to 20 triangles), t3 (squares), g1, g2 (work back) | Correct for every variant; g1 (t = 9, 15, 21, 31, 41, 51) and g2 (t = 10, 13, 16, 22, 31, 37, 40) only offer totals that fit exactly, so "with none left over" is always true |
| t2 | Static "Can exactly 16 sticks make a row of triangles? Yes/No": No; correct; the steps use "odd" and "even" without a reminder (Low) |
| g3 | Static: 100 triangles need 201: correct; the same as workbook G1(a), so a child who has done the page sees it again (Low) |
| Rewind items | None: "runner rewind items absent" (brief). The preflight plans two online rewind items from lesson 18 (times stories) at the end of the set; nothing is rendered. The home sheet's H5 is the rewind (finding 3) |
| Answers in the page | Static JSON, as for every lesson (Low, shared) |
| Accessibility | All controls are labelled; focus order is tabs, then dots, then the answer box, then Check; radios carry the option text; the stick pictures have a label with the count ("4 triangles made of sticks") which gives the question's own number but not the answer: acceptable; the picture is otherwise unreadable to a screen reader (Low) |
| Kind feedback | Neutral and short ("Not yet. Try once more.", "Let us look at it together."); no scores, no timers |

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Online c1, c2, c4 pictures (and workbook S1, deck) | The `stick_pattern` figure draws collinear sticks with round caps in one colour so two sticks in a row look like one long line; the sticks cannot be counted separately from the picture even though every picture has the right number of lines | Draw each stick as a separate bar with a small gap or alternating tone; the same fix as the workbook (L28 finding 1) |
| 2 | Medium | Parent page, try-at-home 1 | "Make a table: 1 cup, 2 cups, 3 cups of water, with spoons of sugar for each. Ask: what is the next number?" gives no numbers and no rule (how many spoons per cup?) | "Put 2 spoons of sugar in each cup. Make a table: 1 cup 2 spoons, 2 cups 4 spoons, 3 cups ... Ask: how many spoons for 5 cups?" |
| 3 | Low | Online practice end | No two rewind items from Term 2 Lesson 18 (times stories); the practice is current-lesson only (Term 1 audit finding F4 repeated) | Add the planned two rewind items marked "from earlier" |
| 4 | Low | Home sheet H3, H4 | The sheet has no pictures although the lesson is about sticks; H3 and H4 describe the pattern in words only; a child who has not kept the strips must draw to check | Add a three-stick-triangle picture for H3 and a three-square picture for H4, once the figure is fixed (finding 1) |
| 5 | Low | Parent page, have-ready box | "Keep the paper strips in their envelope": no later lesson uses them | "The paper strips are not needed again" |
| 6 | Low | Parent page, recording sentence | Only "Every lesson is recorded; your tutor will share a private link with enrolled families"; no statement of what is recorded and no "do not share the link" | Add "The recording has the tutor, the shared screen and any voice that is unmuted. Please do not share the link." |
| 7 | Low | Home answers H4 | "So there are 12 and 1 more squares: 13." | "The first square and 12 more make 13 squares." |
| 8 | Low | Parent page, term line | "...to read time and money in real life" on a table lesson | "Your child is learning to give a reason for each step." |
| 9 | Low | Cross-lesson: `l20.json` `parent.next_materials` | The hand-off into Term 3 still says "print it a week before" and "clock (optional)" (preflight T9); not fixed | Edit before Term 3 starts |

Counts: High 0, Medium 2, Low 7.

## What is good

Every printed answer is right and the answer page is separate; the parent page says exactly what not to teach (letters) and states the beyond-P1 position honestly; the home sheet includes a Think harder and a Go further item with unique answers; the online practice has no tracking, no external request, no overflow, neutral feedback, a hint then a worked solution, and templated variants that cannot be wrong because the answer is computed (about 60 variants read, 0 errors); its "work back" families only use totals that fit exactly.
