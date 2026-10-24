# Home practice, parent summary and online practice audit: Level 1 Term 3 Lesson 29 (Spot the Mistake)

Role HOME_PARENT_PRACTICE. Files audited: `out/l29/L29_Home_Practice.pdf` (1 page), `L29_Home_Answers.pdf` (1 page), `L29_Parent_Summary.pdf` (1 page, about 460 words with headings), and `out/l29/practice/` (key `t3l29`, 11 items: 5 Start here, 3 Think harder, 3 Go further; 8 templated, 1 with a drawn picture, 1 self-check). Source: `lessons/l29.json`. Read first: `AUDIT2_BRIEF.txt`, `AUDIT_T3_BRIEF.txt`, owner decisions, `TERM_WIDE_AUDIT.md`, `website/privacy.html`, `docs/books/p1_school_paper_patterns.md`, and the L28 audit of this role.

## Verdict: Ready after minor fixes

The home maths, the answer page and the parent page are right and plain; the online practice runs cleanly: every item marks correctly, about 150 templated variants were generated and checked by script against independent formulas (no wrong answer), the one picture (the c5 clock at 4:30) is right, there are no external requests, no console errors and no overflow at phone or laptop width. The faults are small: three online items repeat workbook items, one c3 variant exceeds 100, the practice page says "Level 1 · Lesson 9" with no term, the home sheet's "I know because" blank is only a short line, the parent page omits the carried-ten idea from its beyond statement and gives no "do not teach rounding" line, the recording statement is thin, and there are no online rewind items.

Counts: High 0, Medium 2, Low 7.

## Method

- Home sheet and answer page rendered at 80 dpi and text extracted; all five home answers solved independently: H1 34 + 18 = 52 (so 42 is wrong); H2 3:30 plus half an hour is 4:00; H3 15 - 6 = 9, so $11 is wrong; H4 46 + 38 = 84 (84 - 38 = 46; 74 - 38 = 36); H5 14 - 9 = 5 cm. All match the answer sheet. The answers are on a separate page, so a double-sided print never shows them behind the questions.
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every tier and item opened and screenshotted. Templated items (c1, c2, c3, t1, t2, t3, g1, g2) were varied with "Try a similar one" after two wrong answers: 25 c1, 27 c2, 21 c3, 23 t1, 31 t2, 20 t3, 16 g1 and 6 g2 distinct variants (about 170 in all); each "The answer is ..." or chosen-correct option was compared with an independent computation (a + b; Yes or No from a + b = w; a + b; a - b; too small, about right, too big from the estimate; a + b; m - a - b; a - 29): 0 mismatches. Typed-answer handling on c1: `70`, `70 pencils`, `070` right; `seventy` "Please type the answer with number digits, like 54."; `7.0` "Not yet"; `40 + 30 = 70` "Please type just the answer number."; empty "Type or choose an answer first. It is fine to guess."; `10` the slip line "10 is the gap. To check, add the answer and the number taken away." On g1: `29`, `$29` and `29 dollars` right; `38` the slip "38 only takes away the pen." Choice options are shuffled on every load. No ordered or multi-answer item exists in this lesson, so "wrong order refused" does not apply. Keyboard: the first box has focus on load; Enter checks. External requests: none (only the local json, fonts, script). Console errors: none.
- Pictures: only c5 has a figure (a clock at 4:30, label "starts"); it matches the stem and renders at 390 px. The "Pictures render" check passes: the clock is drawn with hands in the right places.
- Page source: `index.html` and `practice.js` hold no answers or external URL; the answers sit in `data/t3l29.json`, fetchable by any browser (shared with every lesson).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 to H3 Start here (a wrong two-digit sum, a bus time, a money story), H4 Think harder (two children, check by taking away), H5 earlier practice (Term 1 Lesson 9, a length comparison). Plain wording, wrong working always "a child" or "two children", units on the lines. The H1 prompt "I know because ___" has a short underscore that wraps; there is no room for a child to write a reason (finding 4) |
| Can a parent help without teaching differently? | Yes. The answer page uses the class words (a check, the ten was forgotten, the long hand goes round from the 6 to the 12) and says "wait 10 seconds, then suggest drawing it" |
| Pictures | None on the home sheet: H2 describes a bus time in words; a small clock would help but is not needed (Low, finding 5) |
| Parent summary | One page, plain English. Words list (check, add back, wrong step, about, a clue). The "when stuck" line is good: "Please say 'the sum has a mistake', not 'you made a mistake'" and "What do you get if you add it back?" works better than giving the answer. Beyond-P1 statement: "Telling that an answer cannot be right by thinking about how big it must be (an estimate) goes past the school Primary 1 syllabus on purpose": honest, but the carried ten in a column sum (G2) and "taking away one too many" (T1), which the lesson file also marks as beyond, are not mentioned; there is no "please do not teach rounding to the nearest ten" line, although "about" and "estimate" appear (finding 3). No MOE-aligned, GEP or SASMO claim. Have-ready box true against `l30.json` (the Quest Log, 4 pages in the book, a quest partner, the calendar page with 7 day cards cut) |
| "Try at home" | (1) three take-away sums to check by adding back, one wrong on purpose: clear. (2) "Find the wrong step: 45 + 38. Step 1: 45 + 30 = 75. Step 2: 75 + 8 = 85. (Step 2 is wrong: it is 83.)": correct (45 + 38 = 83). (3) "half an hour after half past 4 is 4:60. Can your child say the right time?": correct (5:00); a parent states an impossible time, which is the point. All three work for a parent |
| Recording statement on the parent page | "Every lesson is recorded; your tutor will share a private link with enrolled families." No statement of what is recorded and no "do not share the link", unlike the corrected wording in the guide (finding 6) |
| When your child is stuck | The WhatsApp number appears once with the 90-day retention, consistent with `privacy.html` |
| Term line | "Your child is learning to give a reason, and to read time and money in real life." Fits this lesson reasonably (a wrong time and a wrong total) |
| Numbering | "Level 1 • Term 3 • Lesson 9 • For parents": correct; home sheet "Term 3 • Lesson 9" and the answer page "Answers" header: correct. The next lesson is described as "Calendar Detective, the last lesson of Term 3", not "Lesson 30" |
| Print layout | A4, left margin 14 mm for the bound edge, answers on a separate page, header and footer clear; the home sheet is about 90% full: no room for an extra line without a second page |

## B. Online practice

| Item | Result |
|---|---|
| c1 (add back: n + m) | Correct, templated; variant range a 14 to 32, b 11 to 23 gives sums 25 to 55: fine |
| c2 (is the answer right?) | Correct for every variant; about half "Yes" and half "No" by design |
| c3 (a child forgot the ten) | Correct for all combinations shown; one combination is **57 + 45 = 102 (the child wrote 92)**: a sum above 100 on a Start here item, against "numbers within 100" (finding 2) |
| c4 (which step is wrong, 36 + 28) | Static, correct (step 2); **identical to workbook S3** (finding 1) |
| c5 (film 4:30, half an hour) | Correct; clock figure right; options 4:60, 5:00, 5:30 |
| t1 (Lily 42, 8 more than Ben) | Correct for every variant; plain |
| t2 (is 191 too small, about right, too big) | Correct for every variant (the exact sum counts as "about right", "too small" is 40 below and "too big" 40 above); **the static item is the workbook G1 sum (52 + 39 = 191)**; variants where the exact sum is "about right" (for example 47 + 38 = 85 against tens 50 + 40 = 90) may puzzle a child who sees 85 is less than 90 (Low) |
| t3 (Mei 28, 6 fewer than Aisha) | Correct; **identical to workbook T3** |
| g1 (Lily $50, pen and book, child says $38) | Correct for m 40 or 50, a 8, 12, 14, b 7, 9, 11; money prefix `$`; answers always positive |
| g2 (74 - 29 with the step shown) | Correct for all variants (a - 29); static item is **workbook T1** and inherits its ambiguity: the step "44 - 1 = 43" is shown, and the question asks only "What is the right answer?", so g2 itself is unambiguous |
| g3 (make your own puzzle) | Self-check; steps shown after the child writes; fine |
| Rewind items | None: "runner rewind items absent" (brief). The preflight plans two online rewind items from earlier lessons; nothing is rendered. Home H5 (a length, Term 1 Lesson 9) is the rewind (finding 7) |
| Page header | "Level 1 · Lesson 9 · Check an answer another way and find the wrong step": omits the term, so it reads as Term 1 Lesson 9 (a different lesson exists); the family pages elsewhere say "Term 3 Lesson 9" (finding 8) |
| Accessibility | Controls labelled; the first box has focus; radios carry the option text; the c5 clock has no text alternative saying 4:30 (the stem gives it) (Low) |
| Kind feedback | Neutral and short ("Not yet. Try once more.", "Let us look at it together."); no scores or timers; wrong variants have no slip lines (only the static items do) (Low) |
| Answers in the page | Static JSON, as for every lesson (Low, shared) |

## Findings

| # | Sev | Location | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Online c4, t3, g2, t2 (static) | c4 is workbook S3, t3 is T3, g2 is T1, t2 is G1 (52 + 39 = 191): four of the 11 online items are the workbook items, so a child who did the pages meets them again; the "variant" buttons help but the first view repeats | Write different static items (other numbers, same idea); keep the templates |
| 2 | Medium | Online c3 variants | a = 57 and b = 45 gives a sum of 102 ("The child wrote 57 + 45 = 92"); the rule is numbers within 100 and the item is Start here | Restrict the variable ranges so a + b is at most 99 |
| 3 | Low | Parent summary | The beyond statement names only the estimate; the carried ten in a column sum and "taking away one too many" are beyond too; no "please do not teach rounding" line | Add "spotting the wrong digit in a column sum" to the statement and "Please say about and near; do not teach rounding to the nearest ten" |
| 4 | Low | Home sheet H1 | "I know because ___" is one short line that wraps before Yes and No; no writing space | Put "I know because" on its own line with two dotted lines |
| 5 | Low | Home sheet H2 | A clock time with no picture; fine for most, harder for a child who needs the clock | Add a small 3:30 clock |
| 6 | Low | Parent summary footer | "Every lesson is recorded; your tutor will share a private link with enrolled families." No statement of what is recorded and no "please do not share the link" | Use the corrected wording: "The recording has the tutor, the shared screen and any unmuted voice; children may mute and keep cameras off. Please do not share the link." |
| 7 | Low | Online practice, whole set | No rewind items (known) | Add two items from earlier lessons (a time story and a money story) at the end |
| 8 | Low | Online page subtitle | "Level 1 · Lesson 9" has no term | "Level 1 · Term 3 · Lesson 9" |
| 9 | Low | Online variants | Variants have no slip lines; t2 "about right" cases such as 85 against 90 may confuse | Add a generic slip for each family; for t2 use only exact sums that equal the estimate within 5 or label the middle option "the right answer" |

Counts: High 0, Medium 2, Low 7.
