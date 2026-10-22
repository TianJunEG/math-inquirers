# Home practice, parent summary and online practice audit: Level 1 Term 2 Lesson 16 (Skip-Count Tables)

Role HOME_PARENT_PRACTICE. Files audited: `out/l16/L16_Home_Practice.pdf` (2 pages), `L16_Parent_Summary.pdf` (1 page), `out/l16/practice/` (key `t2l16`, runner version 2, 13 items, 9 templated, none with a picture). Source data `lessons/l16.json`. Read first: owner decisions (Term 2 defaults 1, 3, 7 and 9), `TERM_WIDE_AUDIT.md`, `FIXES2_L06` to `FIXES2_L09`, and the L11 to L15 audits of this role (shared runner and print findings are not repeated unless this lesson makes them worse; the Lesson 15 audit records the c1-style defect in templated fill-in-the-box items, which this lesson does not have).

## Verdict: Ready after minor fixes

The home sheet and parent summary are correct and honest (the beyond-P1 statement is exact). The online practice marks correctly: every templated variant I produced (about 70 across 9 items) had the right answer, typed forms are handled kindly, wrong orders are refused. The faults are: a lesson built on a 100 square and a number line has no picture online at all; the ordered-list feedback is misleading; the parent page uses a different lesson number from the workbook; and one template formula is wrong for numbers the lesson itself uses (latent, not yet visible).

Counts: lesson-specific 0 High, 4 Medium, 8 Low. Shared runner and print items: as L13 to L15 (unchanged).

## Method

- Home sheet and parent summary rendered at 60 and 100 dpi, text extracted, margins measured (home: left 14.0 mm, right 14.0, top 15.3, footer 5.3 mm from the edge; parent: left 15.1, right 16.1), all five home answers solved (8 and 12; 10, 20, 30; 30; 10 and 20; 28).
- Online practice served over HTTP and driven in Playwright 1.56 (Chromium) at 390 x 800 and 1280 x 800. Every item of every tier opened, with a phone screenshot of each. Console errors: none. Horizontal overflow: none. Requests: `index.html`, `practice.js`, `fonts.css`, four font files and `data/t2l16.json`, all same-origin; no tracking, no cookies, no external host.
- Dynamic variant test: for each templated item (c1, c2, c3, c4, c6, t1, t2, t4, g1; t3, c5, g2 and g3 are fixed) a script solved each new variant independently from the question text, typed it and pressed Check, repeating "Try a similar one" up to 150 times (14, 8, 9, 11, 9, 7, 3, 6 and 6 distinct variants appeared). 0 wrong answers. The first pass of t1 and t4 failed only because of an error in my own solver; re-run correctly, 0 failures.
- Template formulas re-derived: c1 `a*b` (jumps a of size b, b = 2 or 5, up to 8 x 5 = 40), c2 `a*10` (a from 2 to 9: up to 90), c3 ordered `multiples(k, lim)`, c6 `j` (a jump count; k x j at most 40), t1 `4*n`, t2 `common(2,5,lim)`, t4 `5*j`, g1 `40//b - 40//a`; c4 `((n%5)*(n%5))%3` (finding L16-4).
- Typed forms for a number item (c2): `40`, ` 40 `, `040`, `40 straws`, `40.0` accepted; `forty` gets "Please type the answer with number digits, like 54."; `4 x 10`, `4+10` and ` 4 0` get "Please type just the answer number."; an empty box gets "Type or choose an answer first. It is fine to guess."
- Ordered and set answers: see section C.
- Page source: no answer in `index.html` or the DOM; no external URL in `practice.js`. Answers sit in `data/t2l16.json` (shared R9).

## A. Printed pieces

| Item | Finding |
|---|---|
| Home maths | All five correct. H1 and H2 (blanks in a count in 2s and 5s), H3 (3 bundles of 10 = 30) are Start here; H4 (numbers up to 20 in both the 2s and the 5s: 10 and 20) is Think harder; H5 (2 x 7 = 14, so 4 x 7 = 28) is Go further. Wording plain; stems carry no hints except H5 ("Mei knows 2 x 7 = 14" is the doubling hint, acceptable at Go further). Products within 40 apart from H5's 28. |
| Can a parent help without teaching differently | Yes: the 100 square, a counter, fingers. The sheet does not warn against rote chanting (finding L16-8). |
| Parent summary | 87-word summary (under 90), plain English, no "MOE-aligned", GEP or SASMO claim. The beyond-P1 statement is exact and honest: "The 2, 5 and 10 tables within 40 are Primary 1 work. The 4s (the 2s doubled), the 3s and numbers that are in two tables go past the school Primary 1 syllabus on purpose, always with the 100 square and counters." WhatsApp number and 90 days match `privacy.html`. |
| Consistency with lesson | Words and numbers match the guide and deck. "In both tables: a number we say in two different counts" is a clear gloss. |
| Print | A4, home practice two pages with answers on page 2 (good); parent summary one page. Left margin 14.0 mm: no binding gutter for left-bound sheets; the footer sits 5.3 mm from the bottom edge. |

## B. Lesson-specific findings

| # | Sev | Where | Evidence | Fix |
|---|---|---|---|---|
| L16-1 | Medium | Online, all 13 items | No item has a picture (no `svg` in any item or template). The workbook is built on a 1 to 40 chart, a 100 square, a number line with arcs, a dots grid and number strips; the online practice has plain text for "A frog jumps 5 each time. Where does it land after 3 jumps?" and "How many jumps of 5 does it take to land on 15?". A child without a printed square cannot jump or colour; the "pictures render" check passes trivially. The spec lists the `hundred` and `number_line` figures for practice. | Add a number line with arcs to c1 and c6, a 1 to 40 chart to t2 and g2, and dots to t1. |
| L16-2 | Medium | Online c3 (the only ordered list) | `30, 25, 20, 15, 10, 5` and `10, 5, 15, 20, 25, 30` are refused (correct) but the message is "Those are the right numbers, but check which one goes in each blank." There are no blanks in a count-in-5s list (shared with L14-3). For k = 2 and a limit of 40 the child must type 20 numbers with commas (about 60 keys on a phone). | Message for ordered lists: "These are the right numbers but the order is not right. Count up from the start." Cap the limit at 20 for k = 2. |
| L16-3 | Medium | Parent summary heading and "Next lesson" | The page is headed "LESSON 6 ... FOR PARENTS" and names "Lesson 17: Sharing and Grouping" next; the workbook and slides call the same lessons 6 and 7; the guide mixes "Lesson 6 of 10", "Lesson 16" and "Lesson 15". | One scheme across all family-facing pages. |
| L16-4 | Medium | Online c4 template | The answer rule `((n%5)*(n%5))%3` returns "yes" whenever n mod 5 is 3 (3, 8, 13, 18, 23, 28, 33, 38): checked for 1 to 40 and wrong for exactly those eight numbers. The variant list [10, 12, 15, 20, 21, 25, 27, 30, 34, 35, 40] happens to avoid them, so no child sees a wrong answer today; but 28 and 33 are the very numbers the lesson uses (Explore, Talk time) and are the obvious ones to add. | Use `min(1, n%5)` (0 yes, 1 no). |
| L16-5 | Low | Online c2 | Variants run to 9 x 10 = 90, past the guide's "products to 40 at Start here" and past Primary 1's multiplication limit (within 40); the other Start here items stay at or below 40. Counting in tens to 90 is fine; the "x" wording is the issue. | Limit a to 2 to 4 at Start here; keep 5 to 9 for Think harder. |
| L16-6 | Low | Online slips | Each item carries one authored slip for the base numbers only (for example c4 "Count in 5s: 5, 10, ... 35. Do you say 35?"); the 11 variants get the generic "Not quite yet" (shared R11). | Generate slips from templates. |
| L16-7 | Low | Parent summary, Try at home 3 | "Double it: if 2 x 6 = 12, what is 4 x 6? Show it with 24 counters in rows." The hand-off lists "about 20 counters"; 24 are needed (or drawn dots). | "Show it with dots or 24 buttons." |
| L16-8 | Low | Parent summary | The guide says "do not teach tables by heart; the jumps are the method" but the parent page has no "please do not drill" line; a parent may chant the tables. | "Please count in jumps rather than chanting the table by heart." |
| L16-9 | Low | Home sheet H4 and H5 | H4 and H5 answers use short dashed lines where H1 to H3 use boxes; "and" in H4 wraps onto the second line. Fine to fill in; inconsistent. | Boxes throughout. |
| L16-10 | Low | Parent summary, hand-off | "Have ready for next lesson" omits the workbook; Lesson 17's materials ask for it (the groups mat on page 6 replaces plates). | Add "your workbook". |
| L16-11 | Low | Parent summary, last line | "Your child is learning to draw a story, to use groups and sharing, and to test a claim with an example" is the term line; fine for the term, but "sharing" is not taught until the next lesson. | Use the lesson line. |
| L16-12 | Low | Online t3 | Fixed item: "Which number is in both the 2s and the 5s?" with options 12, 15, 20, 25: only 20 qualifies, and the authored slip for 15 ("odd") is right. It never varies, so "Try a similar one" is absent. | Add a template with 10, 20, 30, 40 against distractors. |

## C. Online runner checks (Playwright results)

| Check | Result |
|---|---|
| Opens at 390 and 1280 px | Yes, no horizontal scroll, text 18 px. |
| Pictures | None exist (L16-1); nothing renders and nothing mismatches. |
| Typed numbers | As above: digits only; units, spaces, leading zeros and `.0` accepted; words, expressions and two numbers get kind, neutral messages. |
| Ordered list (c3) | Accepts `5, 10, 15, 20, 25, 30`, `5 10 15 20 25 30` and `5,10,15,20,25,30.`; refuses `30, 25, 20, 15, 10, 5`, `10, 5, 15, 20, 25, 30` (right numbers, wrong order: misleading message L16-2), `5, 10, 15, 20, 25` ("Those fit. Are there more? Keep looking."), `5, 10, 15, 20, 25, 30, 35` ("Some of these fit, but one does not.") and a letter O for zero (`3O`). Marking is right. |
| Unordered sets (t2, g2) | `10, 20, 30, 40` and `20, 10, 40, 30` accepted for t2; `10, 20, 30` and `5, 10` refused kindly; g2 `20, 40` and `40, 20` accepted, `20` and `20, 40, 10` and `4, 5` refused. Right. |
| Choice items | c4, c5 and t3: the options are shuffled; wrong then right works; every c4 variant correct (the formula problem is latent). |
| Templates | 9 templated items, about 70 distinct variants, 0 wrong answers and every answer reproduced by an independent solver from the question text. |
| Wrong answers | First wrong: "Not yet. Try once more." plus the authored slip or the generic message and the hint; second wrong shows the answer and the steps. No score, no timer, no streak. |
| Network and privacy | 8 same-origin requests; no tracking; `localStorage` key `mi-practice-t2l16` for progress only. |
| Keyboard | Enter submits in text boxes; radio items have no Enter handler; focus returns to the first box after render (shared R4). |
| Answer leak | None in `index.html`; answers sit in the data file (shared R9). |

## D. Home timing and fit

"About 15 minutes": H1 (two blanks), H2 (three), H3 (one), H4 (list the common numbers to 20) and H5 (use a doubling) is about 8 to 11 minutes for a middle child. Tiers are in the same order as the workbook. H4 repeats the sneak-peek puzzle and H5 depends on the doubling idea that the class never teaches (see the guide audit), so H5 is a real challenge for most children; it is correctly Go further.

## E. What is good

The beyond-P1 statement is the clearest in Term 2 so far (names which parts are Primary 2 and Primary 4, says "on purpose", and says "always with the 100 square and counters"). Neutral, kind feedback; no timers or scores; the stuck route is the grown-up's WhatsApp photo with the 90-day statement matching the privacy page; the answer page is separate; the templated items produced no wrong answers or pictures that disagreed with the text.
