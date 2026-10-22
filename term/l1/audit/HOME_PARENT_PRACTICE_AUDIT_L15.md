# Home practice, parent summary and online practice audit: Level 1 Term 2 Lesson 15 (Equal Groups)

Role HOME_PARENT_PRACTICE. Files audited: `out/l15/L15_Home_Practice.pdf` (2 pages), `L15_Parent_Summary.pdf` (1 page), `out/l15/practice/` (key `t2l15`, runner version 2, 14 items, 11 templated). Source data `lessons/l15.json`. Read first: owner decisions (Term 2 defaults 1, 7 and 9), `TERM_WIDE_AUDIT.md`, `FIXES2_L06` to `FIXES2_L09`, and the L11 to L14 audits of this role (shared runner and print findings are not repeated unless this lesson makes them worse).

## Verdict: Ready after minor fixes for the printed pieces; the online practice is Needs rework until finding L15-1 is fixed

One High defect in the online runner, reproduced in the browser: after a child presses "Try a similar one" on a templated fill-in-the-boxes item (c1 and c6 here), the page shows the finished sentence ("3 groups of 5 = 15") with no boxes, and "Check" answers "Type a number in every box" for ever. The question is unanswerable and the answer is on screen. The runner file is the same in every lesson L10 to L20 (identical md5), so the defect is shared, but it hits two of the six Start here items of this lesson. The printed home sheet and parent summary are correct and honest; they need a numbering fix and layout care. Everything else in the online practice (typed answers, choices, set answers, pictures) works.

Counts: lesson-specific 1 High, 4 Medium, 7 Low. Shared runner and print items: as L13 and L14 (unchanged).

## Method

- Home sheet and parent summary rendered at 60 and 100 dpi, text extracted, margins measured (home: left 14.0 mm, right 14.0, top 15.3, footer 5.3 mm from the edge; parent: left 15.1, right 16.1), all five home answers solved (12 and 12; No; 15, 15, 15; Yes; 18).
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every item of every tier opened, with screenshots of each at phone width. Console errors: none. Horizontal overflow: none. Requests: `index.html`, `practice.js`, `fonts.css`, four font files and `data/t2l15.json`, all same-origin; no tracking, no cookies, no external host.
- Dynamic variant test: for each of the 10 templated items (c1, c2, c3, c4, c6, t1, t2, t3, t4, g2) a script solved each new variant independently (from the drawn picture for c2, c3, t1 by counting the cookie shapes; from the wording for c4, t3, t4, g2), typed the answer and pressed Check, repeating "Try a similar one" up to 120 times. Pictures versus numbers were also verified statically: c1 (16 variants) has a plates and 7 x a x b shapes for every pair; c2 (12), c3 (9), c6 (9) and t1 (6) all show exactly the numbers in the wording. Result: 0 wrong answers or pictures among c2, c3, c4, t1, t2, t3, t4 and g2; c1 and c6 break on every variant (finding L15-1).
- Typed forms for a number item (c4): `10`, ` 10 `, `010`, `10 sweets`, `10.0` accepted; `ten` and `twelve` get "Please type the answer with number digits, like 54."; `5 x 2`, `5+2` and `10 10` get "Please type just the answer number."; `11` gets "Not yet. Try once more" with the hint; an empty box gets "Type or choose an answer first. It is fine to guess." Kind, neutral, no score or timer.
- Set item g3 ("4 + 4 + 4 + 4 + 4 + 4 = [] x []"): `6, 4`, `4, 6`, `6 4`, `4 x 6`, `6 x 4`, `4,6.` accepted (either order, as owner default 1); `6` ("Those fit. Are there more? Keep looking."), `6, 4, 4` (same message, which is wrong: there is no third number to find) and `24`, `5, 5` ("Not quite yet") refused.
- Choice items: c3, c5 (`4 + 3` refused with "Not quite yet. Have another go."), t2; the options are shuffled.
- Page source: no answer in `index.html` or the DOM; no external URL in `practice.js`. Answers sit in `data/t2l15.json` (shared R9).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 to H3 Start here (3 + 3 + 3 + 3, a story with unequal bags, 5 + 5 + 5 and 3 x 5), H4 Think harder (is 2 x 6 = 6 x 2), H5 Go further (4 tricycles and 3 bikes: 18). Wording plain; no hints in stems; the order is the workbook's. Products within 20. |
| Can a parent help without teaching differently | Yes: counters on plates, "how many in each group?". The sheet does not say what not to teach, and gives only groups-first answers (finding L15-3). |
| Parent summary | 81-word summary (under 90), plain English, no "MOE-aligned", GEP or SASMO claim. "Equal groups and x are Primary 1 work at school; we start from objects and pictures" is honest and correct (MOE p. 31). WhatsApp number and 90 days match `privacy.html`. "Words we used" defines groups of, each, in all and x well. |
| Consistency with lesson | Words, numbers and questions match the guide and deck ("In each", "In all", the x sentence). The final line ("draw a story, use groups and sharing, test a claim") is the term line; "sharing" has not been taught yet. |
| Print | A4, home practice two pages with answers on page 2 (good); parent summary one page. Left margin 14.0 mm: no binding gutter for left-bound sheets; the footer sits 5.3 mm from the bottom edge (inside the unprintable band of many printers). |

## B. Lesson-specific findings

| # | Sev | Where | Evidence | Fix |
|---|---|---|---|---|
| L15-1 | High | Online c1 and c6, every "Try a similar one" variant | `variantOf` runs `fill(t.frame, all)` for templated fill-in items, so `{a} groups of {b} = {c}` becomes "3 groups of 5 = 15" with no placeholders left; `control()` then builds no input boxes. Reproduced in Chromium at 390 and 1280 px: the card shows the full sentence and the picture, "Check" returns "Type a number in every box. It is fine to guess." on every press, and "Next question" never appears (it is shown only once the item is done), so the child is stuck on the card and the answer is on screen. It failed on the first variant after the base item for both c1 and c6 in the script run, and again by hand with a screenshot. The same code is in all lessons L10 to L20, so every templated `fields` item is affected. | In `variantOf`, keep `v.frame` as the raw template (placeholders intact) and fill only `q`, `hint`, `steps`; add a regression test that every variant of a `fields` item renders N inputs. Until fixed, remove the `tpl` from c1 and c6. |
| L15-2 | Medium | Parent summary heading and "Next lesson" | The page is headed "LESSON 5 ... FOR PARENTS" and names "Lesson 16: Skip-Count Tables" next and "The Lesson 16 workbook with its 100 square page". The workbook and deck call the same lessons 5 and 6. A parent matching "Lesson 16" to a sheet headed "Lesson 6" cannot. | One scheme across all family-facing pages. |
| L15-3 | Medium | Home answer page (H1 to H5) and parent page | Answers give one order only (H3 "3 x 5 = 15"; no "5 x 3 is also right"). The parent summary never says that 3 x 4 and 4 x 3 are both fine for a child's own sentence, although the guide and owner default 1 do. A parent who thinks 5 x 3 is wrong will correct a correct answer. | Add to the parent page and the home answers: "Either order is fine: 3 x 5 and 5 x 3 both make 15." |
| L15-4 | Medium | Home sheet H1 and H3 layout | H1 reads "3 + 3 + 3 + 3 = [] [] / 4 groups of 3 = [] []" (second blank drops to the next line, fine). H3 puts three separate blanks on one line: `5 + 5 + 5 = [][]  3 groups of 5 = [][]  3 x 5 = [][]` with only a small gap between the boxes of one blank and the next label, so the ends of the blanks run into "3 groups of 5". H5 uses a short dashed line where the others use boxes. A child cannot always tell which pair of boxes belongs to which equation. Known template limit (FIXES2_L06). | Put each equation on its own line (a), (b), (c); use boxes in H5. |
| L15-5 | Medium | Online g3 text | The question is displayed as "4 + 4 + 4 + 4 + 4 + 4 = [] x []. Type the two numbers with a comma between them." The printed-page blank token `[]` leaks into the screen as two literal square brackets, and the child must type two numbers in one box. `6, 4, 4` also gets "Those fit. Are there more? Keep looking.", which invites a third number that does not exist. | Say "= ___ x ___" or "Write the two numbers", and for a fixed-length set say "Type exactly two numbers". |
| L15-6 | Low | Online item set | None of the 14 items carries an authored slip (`slips` is empty on every item), so the common mistakes in the key (4 + 3 for 4 groups of 3 in c5; 3 + 5 = 8 for 3 groups of 5; "6" for 3 bikes in t3) all get the generic "Not quite yet" (shared R11). | Author slips for c4, c5 and t3. |
| L15-7 | Low | Online t2 | All nine variants swap the same two numbers, so the answer is always "the same"; a child who learns that presses it every time. (It is mathematically always right, so the item is correct but does not discriminate.) | Add variants where the two totals differ (for example 3 bags of 5 against 4 bags of 4). |
| L15-8 | Low | Online t1 steps | Steps read "The second plate has 2, so it needs more." The sentence has no number of cookies needed. | "...so it needs 1 more." with the number filled in. |
| L15-9 | Low | Online c1 and c6 at 390 px | The third box drops below the "=" onto its own line, so "[] groups of [] =" and the answer box look unrelated. | Smaller boxes or allow the frame to wrap at the "=". |
| L15-10 | Low | Online | Nine of the 14 items are text only (c4, c5, t2, t3, t4, g1 to g4): the "pictures render" check passes for the five that have one (c1, c2, c3, c6, t1), and all five render correctly in the base item; the child has no picture for "5 groups of 2" or "6 bikes". | Add a picture to c4 and t3 (plates). |
| L15-11 | Low | Parent summary | No "please do not teach..." line. Parents may hear "multiply" and teach "times tables" or the "multiply by" language that the guide forbids (36:01). | "Please say 'groups of' for the x sign for now; tables come later." |
| L15-12 | Low | Parent summary, hand-off | "Have ready for next lesson: the Lesson 16 workbook with its 100 square page" does not say how or when that workbook reaches the family. | "Your tutor will send it before class" or the actual route. |

## C. Online runner checks (Playwright results)

| Check | Result |
|---|---|
| Opens at 390 and 1280 px | Yes, no horizontal scroll, text 18 px; fields wrap at 390 px (L15-9). |
| Pictures | c1, c2, c3, c6 and t1 render in the base and in every variant I solved except where the item loses its boxes (c1, c6); counts match the numbers in every variant checked. |
| Typed numbers | As above: kind, neutral messages; digits only; units, spaces and leading zeros accepted. |
| Set and ordered answers | g3: either order accepted; wrong counts refused; no ordered-only item in this lesson (the "wrong orders refused" check applies to c6 only through the exact-box rule: `4, 3, 12` for 3 rows of 4 gets "Look again at the boxes with a red edge"; the red-edge cue is the only marker). |
| Multiple-box marking | `3, 4, 13` and `4, 3, 12` (swap) are both refused with red edges on the right boxes and a hint; a blank box gets "Type a number in every box". Works only for the base item (L15-1). |
| Wrong answers | First wrong: "Not yet. Try once more." plus a hint; second wrong shows the answer and the steps. No score, no timer, no streak. |
| Network and privacy | 8 same-origin requests; no tracking; `localStorage` key `mi-practice-t2l15` for progress only. |
| Keyboard | Enter submits in text boxes (code and a typed run); radio items have no Enter handler; focus returns to the first box after render (shared R4). |
| Answer leak | None in `index.html`; answers sit in the data file (shared R9) and, for c1 and c6 variants, on screen (L15-1). |

## D. Home timing and fit

"About 15 minutes": H1 (2 numbers), H2 (one circle), H3 (3 numbers), H4 (counting 12 counters for a Yes) and H5 (a two-step story) is about 10 to 12 minutes for a middle child. Tiers in the same order as the workbook. H2 and H4 reuse class types (S1, T1: the same claim and picture idea) which is good for practice; H5 repeats the G1 bike-and-car idea with new numbers.

## E. What is good

The beyond-P1 statement is not needed and is correctly not made; "Primary 1 work at school" is accurate. Neutral, kind feedback; no timers or scores; the stuck route is the grown-up's WhatsApp photo with the 90-day statement matching the privacy page; the answer-page is separate from the question page; the eight other templated items (c2, c3, c4, t1, t2, t3, t4, g2) marked correctly in every variant the script produced, and their pictures matched their numbers.
