# Home practice, parent summary and online practice audit: Lesson 12 (Bar Strips: More and Fewer)

Second-round independent audit, role HOME_PARENT_PRACTICE, 22 Oct 2026. Files audited: `term/l1/out/l12/L12_Home_Practice.pdf` (2 pages), `L12_Parent_Summary.pdf` (1 page) and `out/l12/practice/` (key `t2l12`, 10 items). Source: `term/l1/lessons/l12.json`. The workbook and guide are audited separately (`WORKBOOK_AUDIT_L12.md`, `GUIDE_DECK_AUDIT_L12.md`) and not repeated. Audit only: nothing was edited; test scripts are in the auditor scratchpad.

## Verdict: Ready after minor fixes

Score on the 10-criterion, 0 to 2 scale used for the Term 1 pages (no project instrument exists for parent pages): **12/20**.

| # | Criterion | Score | Note |
|---|---|---|---|
| 1 | Home maths correct and worded to the guide | 1 | All five answers right; H2 and H3 have no answer frame or unit |
| 2 | A parent can help without teaching a different method | 2 | "Lay two strips side by side, or draw boxes in two rows, and count the extra boxes"; wait 10 seconds |
| 3 | Parent summary plain, short, in the word limit | 2 | Summary 89 words (limit 90, so at the limit), one page, clear layout |
| 4 | No overclaim; beyond-P1 statement honest | 2 | "Strips (called bar models at school) and the Think harder questions go beyond Primary 1 on purpose"; no MOE, SASMO or GEP claim |
| 5 | Privacy and recording statements consistent with `privacy.html` | 1 | One contradiction about who can see the recording (finding 4) |
| 6 | Print layout (A4, double-sided, left binding, separate answer page) | 1 | Margins fine; answers on the back of the questions; footer 5.8 mm from the edge |
| 7 | Writing and drawing space for the child | 0 | H1 says "Draw a strip for each" and gives one dotted line; no question has a drawing box (finding 2) |
| 8 | Online marking correct (numbers, choice, variants) | 2 | Every authored answer accepted, every variant matched an independent oracle, slips named |
| 9 | Online child safety and accessibility (no tracking, keyboard, 44 px, pictures render) | 1 | Safe and keyboard-clean; in dark mode the figure names and "?" are invisible (finding 5) |
| 10 | The family can actually reach the online practice | 0 | No link, no URL, no key on any printed page (finding 1) |

Counts for this lesson: 0 High, 5 Medium, 6 Low. No finding is High: every home answer is right, every online variant marks correctly, nothing leaves the origin. Finding 1 becomes High if the term starts with no published URL.

## Home practice: maths, wording, layout

Independently solved: H1 5 more pencils (14 - 9); H2 58 marbles (38 + 20); H3 65 stickers (25 + 15 = 40; 25 + 40); H4 12 sweets (30 - 6 = 24; 12 each; Ben 12, Ali 18); H5 7 stickers (gap 14, half). All match the answer page. Tiers are honest: H1 to H3 Start here (S1, S2, S3 types), H4 Think harder (total and difference), H5 Go further (a transfer with the gap shown by a total). The arithmetic is within 70, about the same level as the workbook's Start here, which is above the P1 quiz ceiling (see the workbook audit, finding 1) and has no scaffold on the home sheet either.

Wording: H1 is "Ali has 14 pencils. Mei has 9 pencils. Draw a strip for each. Ali has ___ more pencils than Mei." (good: the command is in the middle but the frame is at the end). H2 ("How many marbles does Kumar have?") and H3 ("How many stickers do they have altogether?") end with a dotted line and no frame or unit (rule 16). H4 asks "Write: I know because ..." with one dotted line. The sheet's own hint is "use paper strips or draw boxes in a row", but there is no space to draw anywhere.

Layout: page 1 is questions, page 2 is "Answers for grown-ups" (separate sheet side, but on a double-sided print it sits on the back of page 1). Left and right margins 14.0 and 14.5 mm, top 14.2 mm; footer 5.8 mm from the bottom edge (below the usual 6 mm printer margin). The parent page margins are 15 mm sides, 13 mm top and 14.7 mm bottom.

## Parent summary: what it says

Plain English; it names what was learnt, the big idea, what is school work and what goes beyond, three things to try (a spoken story drawn as two strips; compare two stacks of coins; make equal with 10 counters and 6), five words, three good questions, a "When your child is stuck" box, the next lesson and its materials. The Lesson 13 materials list is true (checked against `l13.json`: the printed workbook with its kit page of ten-frames and 20 counters cut out, or about 20 small things of two kinds, pencil and paper). "Make equal ... how many should move so both have the same?" with 10 and 6 has the answer 2 (the same transfer idea as T2). Not said: what not to say at home (for example "don't tell your child to always take away"); the page does not mention the online practice.

## Online practice: method and results

Served `out/l12/practice/` as a static site and drove it with Playwright 1.56.0 (Chromium 141) at 375 x 667, 320 x 568 (dark mode) and 1280 x 800. All ten items were opened; the authored answer was typed or chosen for each (all accepted; `g3` is a self-check with a checklist); every option of the choice item was tried singly (only "9 - 5" passes); formats and slips were tried; every template was drawn 80 times and each drawn question was solved by an oracle written from the question text: c1 38 distinct variants, c2 34, c4 20, t1 20, t2 16, t3 16, g1 16, g2 8, zero mismatches. The two picture templates (c1, 48 variants; c2, 36 variants) were checked statically in the data file (the numbers drawn match the numbers in the question; no combination lacks a picture) and from the DOM in the browser. Request log, cookies, `localStorage`, console, the DOM before a check and tab order were captured.

| Check | Result |
|---|---|
| Pictures render (c1, c2) | yes at 320, 375 and 1280 px; scale correctly; no horizontal scroll at any width |
| Ordered and multi-answer items | none in this lesson (no `set`, `multi` or `fields` item); the runner paths for them were tested in the Lesson 11 audit |
| Number formats (c1 answer 4) | `4`, ` 4 `, `04`, `4.0` and `4 stickers` accepted; `four`, `4,0`, `4+0` get neutral "type the answer with number digits" or "just the answer number"; `-4` is marked wrong normally; empty gets "Type or choose an answer first. It is fine to guess." |
| Slips | c1: 20, 12; c2: 8, 7; c4: 14, 4; t1: 20, 24; t2: 12; t3: 70; g1: 26, 19; g2: 30 all get a named message; g2 40 (Mei's number) gets the generic message |
| Variants | the slip messages exist for the base numbers only; a drawn variant gets "Not quite yet. Have another go." and the hint |
| Single choice (c3) | only the right option passes, each wrong option gets a message or the generic one |
| Network | requests are to `index.html`, `practice.js`, `fonts.css`, three font files and `data/t2l12.json`, same origin; no external host in the source |
| Storage | no cookies; `localStorage` key `mi-practice-t2l12` holds finished ids only |
| Keyboard | answer box has focus on load; Enter checks; buttons at least 44 px |
| Answer leaks | before a check the DOM holds the question only (no steps, no "Yes" text); the data file holds the answers, as in Term 1 |
| Tone | "Not yet. Try once more." and "Let us look at it together." are kind; no timer, no score, no streak |

## Findings

| # | Sev | Where | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Home practice page 2 last line; parent page; guide section 5 | "More practice online (no timers, no scores): ask your tutor for the practice link." The Parent Summary does not mention the practice; the guide gives only the folder and the key `t2l12`. No printed page carries a URL or a QR code (Term 1 finding R2, still open). | One line with the URL or short link on the parent page and home sheet, or an explicit "the tutor sends the link on the lesson day" with a tutor-guide step. |
| 2 | Medium | Home practice H1, H4, H5 (and H2, H3) | H1 says "Draw a strip for each." and gives one dotted line. H4 and H5 need working and gives one and two lines. The strips idea cannot be shown without a drawing box, and the sheet's hint says "draw boxes in a row". | A drawing box with a faint grid under H1, H4, H5, and a frame ("Kumar has ___ marbles.", "They have ___ stickers altogether.") for H2 and H3. |
| 3 | Medium | Home practice PDF (2 pages) | Page 2 is "Answers for grown-ups". On a double-sided print of the 2-page file the answers are on the back of the questions. The audit brief asks that the answer page be separate from the questions. | Print the answers on the parent summary page, or add "Print page 2 on its own sheet", or add a blank back to page 1 in the build. |
| 4 | Medium | Parent summary, "Next lesson" box | "The recording link is private to your family: please do not share it." and, two sentences later, "your tutor will share a private link with enrolled families." `privacy.html` says recordings are visible to "only the enrolled families of the same group, through a private link". The same sentence is on every Term 2 parent page (copied from Term 1). | "The recording link is private to the families in your child's group: please do not share it." |
| 5 | Medium | Online c1, c2 figures, dark mode | In `prefers-color-scheme: dark` the figure text ("Ali", "Mei", "Ben", "Kumar", the "?" and the gap bracket) is drawn in the same dark ink as in light mode on a dark card, so the names, the "?" and the bracket are almost invisible (checked in a screenshot at 320 x 568, dark). Only the numbers inside the yellow bars remain. The gap bracket and the "?" are the question. | Give the figure fixed light backing, or use `currentColor` for text and the bracket, and test the SVG in both schemes. |
| 6 | Low | Online t2, g1 (transfer items) and c4, t1, t3, g2 | Six of the nine scored items are text only; the two transfer items (t2, g1) are exactly where a picture helps a 6-year-old most, and the pre-flight (R1) says nine of ten lessons need a picture. On a phone the numbers inside c1 and c2 bars are about 7 px. | Add `bar_model` pictures to t2 and g1; enlarge the figure text for narrow screens. |
| 7 | Low | Online slips | "20 joins the strips. How many more is the gap between them: take away." and "8 takes away." are garbled. | "20 joins the strips. The gap is found by taking away." and "8 is the take-away answer. Kumar has more, so add." |
| 8 | Low | Online g1 worked steps | "40 shared into two equal strips is half of 40 each." and "The top shelf gave away 9 to get there." read awkwardly and number words are template joins. | "Each shelf has {T/2} after the move. The top shelf gave away {m}, so it had {T/2} + {m} = {ans} at first." (derive fields exist). |
| 9 | Low | Online variants | Slip messages exist only for the base question; a drawn variant (the "Try a similar one" button) gets the generic "Not quite yet" for the same slips. | Generate slips from the template (e.g. "{a+b}" joins the strips). |
| 10 | Low | Home practice title and H1 | "Bar Strips: More and Fewer: practice at home" (double colon); H1 sentence order puts the drawing command between two statements and the frame. | "Practice at home: Bar Strips"; "Ali has 14 pencils. Mei has 9 pencils. Draw a strip for each. Ali has ___ more pencils than Mei." (already close; add a box). |
| 11 | Low | All printed pages | Footer 5.8 mm from the bottom edge. | Raise it to 8 to 10 mm. |

## Summary for the fixer

Fix 1 (the link), 2 (drawing space) and 3 (the answer page) first; 1 and 3 are shared with every lesson. Finding 4 is one sentence copied across all Term 2 lessons. Finding 5 is a figure-tool fix and will affect every lesson that draws strips, groups or arrays online. Findings 6 to 11 are polish. The home sheet and the parent page are otherwise sound and the beyond-P1 statement is what the owner decisions ask for.
