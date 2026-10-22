# Home practice, parent summary and online practice audit: Lesson 11 (Who Is Where?)

Second-round independent audit, role HOME_PARENT_PRACTICE, 22 Oct 2026. Files audited: `term/l1/out/l11/L11_Home_Practice.pdf` (2 pages), `L11_Parent_Summary.pdf` (1 page) and `out/l11/practice/` (key `t2l11`, 10 items). Source: `term/l1/lessons/l11.json`. The workbook and guide are audited separately (`WORKBOOK_AUDIT_L11.md`, `GUIDE_DECK_AUDIT_L11.md`) and not repeated. Audit only: nothing was edited; test scripts are in the auditor scratchpad.

## Verdict: Ready after minor fixes

Score on the 10-criterion, 0 to 2 scale used for the Term 1 pages (no project instrument exists for parent pages): **12/20**.

| # | Criterion | Score | Note |
|---|---|---|---|
| 1 | Home maths correct and worded to the guide | 1 | All five answers right; H1 packs three instructions in one sentence |
| 2 | A parent can help without teaching a different method | 2 | "Touch each toy, say the places"; the page tells parents to wait 10 seconds |
| 3 | Parent summary plain, short, in the word limit | 2 | Summary paragraph 89 words (limit 90, so at the limit); whole page about 500 words in a clear layout |
| 4 | No overclaim; beyond-P1 statement honest | 2 | "Start here is school Primary 1 work; Think harder goes beyond it on purpose"; no MOE, SASMO or GEP claim |
| 5 | Privacy and recording statements consistent with `privacy.html` | 1 | One contradiction about who can see the recording (finding 4) |
| 6 | Print layout (A4, double-sided, left binding, separate answer page) | 1 | Margins fine; answers print on the back of the questions (finding 3); footer 5.8 mm from the edge |
| 7 | Writing and drawing space for the child | 1 | H4 and H5 need working and drawing room, one or two dotted lines given (finding 5) |
| 8 | Online marking correct, including ordered and multi-answer, wrong orders refused | 1 | Correct in all cases tested; ordered marking is stricter than the question (finding 2) |
| 9 | Online child safety and accessibility (no tracking, keyboard, 44 px, pictures render) | 1 | Safe and keyboard-clean; the picture items have no usable alt text (finding 8) |
| 10 | The family can actually reach the online practice | 0 | No link, no URL, no key on any printed page (finding 1) |

Counts for this lesson: 0 High, 5 Medium, 6 Low. No finding is High: every home answer is right, every online variant marks correctly, nothing leaves the origin.

## Home practice: maths, wording, layout

Independently solved: H1 3rd (4th from one end of 6 is 3rd from the other, whichever end the child calls the front, so there is no ambiguity even though home has no door); H2 6 children; H3 4th; H4 7 children (3 + 1 + 3); H5 7th (a line of 9 has the middle at 5th; 2 places behind is 7th). All match the answer page. Tiers are honest: H1 to H3 Start here, H4 Think harder (the both-ends idea, previewed in class), H5 Go further. No contest item is in a Start here question. The sheet asks about 15 minutes, which is right for five items with a drawing.

Wording against the guide: H2 has no answer frame and no unit ("How many children are in front of Kumar?" then a dotted line); H1 is "Put 6 toys in a row. Put a coin on the 4th toy from the front. Then write: ..." which is three instructions in one run-on before the question (rule 1, rule 18); the title prints as "Who Is Where?: practice at home". "From the front" is not defined on the home sheet (no door, no FRONT paper), which is harmless for the answers but is exactly the word the lesson teaches; the parent page defines "front" as "next to the door".

Layout: page 1 is the questions, page 2 is "Answers for grown-ups" on a separate sheet side (good: not on the same page), but on a double-sided print it falls on the back of page 1 (finding 3). Left and right margins 14.0 and 14.5 mm, top 14.2 mm; the footer sits 5.8 mm from the bottom edge on every page, below the usual 6 mm printer margin (Low). The parent page is one page, margins 15 mm, bottom 20 mm.

## Parent summary: what it says

Plain English; it names what was learnt, the big idea, what is school work and what goes beyond, three things to try (toys in a row, real queues, turn the line round), five words, three good questions, a "When your child is stuck" box, the next lesson and its materials. The kit list for Lesson 12 is true (checked against `l12.json`: strips kit page, two colouring pencils, about 20 counters, pencil and paper). Not said: what not to say at home (for example "do not say 'the number is 4th'" or "do not drill 11th and 12th"); there is no "please do not teach a quicker way", only "wait 10 seconds and do not hurry". The page does not mention the online practice at all.

## Online practice: method and results

Served `out/l11/practice/` as a static site and drove it with Playwright 1.56.0 (Chromium 141) at 375 x 667, 320 x 568 (dark mode) and 1280 x 800. Every item of every tier was opened; the authored answer was typed or chosen for all ten (all accepted, `g3` is a self-check with a checklist); every option of the choice item was tried singly (only the right one passes); the runner's standard formats were tried; every template was drawn 70 times and every drawn question was solved by an oracle written from the question text (not from the template): c2 6 of 6 variants, c4 15 of 15, t1 6 of 6, t2 9 of 9, g1 5 of 5, g2 5 of 5, zero mismatches. The two picture templates were checked from the page DOM: c1 (16 variants) and c2 (6 variants) draw the right number of children and put the ring on the right child in all cases (also checked statically against the JSON). Request log, cookies, `localStorage`, console, tab order and Enter-to-check were captured.

| Check | Result |
|---|---|
| Pictures render (c1, c2) | yes, at 320, 375 and 1280 px; figure scales, no overflow, no horizontal scroll at any width or in dark mode |
| Ordered marking (t3 "list the places between 3rd and 7th") | `4,5,6`, `4 5 6`, `4, 5, 6`, `4;5;6`, `4th, 5th, 6th`, `4 , 5 , 6 ` and a trailing comma are accepted; `6,5,4` and `5,4,6` are refused; `4,5`, `4,5,6,7` and the slip `3,4,5,6,7` get specific, kind messages; `four, five, six` and `456` are refused neutrally |
| Number formats (c2 answer 4) | `4`, ` 4 `, `04`, `4.0`, `4.`, `4 children`, `4th` accepted; `four`, `٤`, `4,0`, `1 0`, `4+0` get "Please type the answer with number digits" or "just the answer number" (neutral); `-4` is marked wrong normally; empty gets "Type or choose an answer first. It is fine to guess." |
| Slips | c2: 5 and 6; t1: 10; c3: "4 children in front" all get a named slip message |
| Wrong twice | reveals the answer and the steps ("Let us look at it together") |
| Single-choice (c3) | only the right option passes; empty is refused with a neutral message |
| Network | requests are to `index.html`, `practice.js`, `fonts.css`, three font files and `data/t2l11.json` on the same origin only; no external host in the source |
| Storage | one `localStorage` key `mi-practice-t2l11` with the ids of finished items; no cookies |
| Keyboard | the answer box has focus on load; Enter checks; Tab goes Check, hint, then the page; buttons are at least 44 px |
| Answer leaks | before a check the DOM holds the question only (the steps and the answer are built after a check or after two tries); the data file, as in Term 1, holds all answers and is readable by a curious grown-up, which is acceptable for a no-score practice page |
| Wording and tone | "Not yet. Try once more." and "Let us look at it together." are kind; no timer, no score, no streak |

## Findings

| # | Sev | Where | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | Home practice page 2 last line; parent page; guide section 5 | The home sheet says "More practice online (no timers, no scores): ask your tutor for the practice link." The Parent Summary does not mention the practice at all; the guide gives only the folder `out/l11/practice` and the key `t2l11`. No printed page carries a URL or a QR code. This is Term 1 finding R2, still open for Term 2 and it becomes High if the term starts with no published URL. | One line on the parent page and the home sheet with the URL (or a short link) for this lesson, or an explicit "the tutor sends the link on the lesson day" with the tutor guide telling the tutor how. |
| 2 | Medium | Online t3 | The question reads "List the places of the children between them. Type the numbers with a comma between." and is marked as an ordered list: `6,5,4` and `5,4,6` are refused although they are a correct list. The refusal text is "Those are the right numbers, but check which one goes in each blank", but there are no blanks. A 6-year-old who lists the places in any order is told they are wrong. | Either ask "in order, smallest first" in the question and say so in the refusal ("write them smallest first"), or mark the set unordered. |
| 3 | Medium | Home practice PDF (2 pages) | Page 2 is "Answers for grown-ups". On a double-sided print of the 2-page file the answers are on the back of the questions, and a child turning the sheet over sees every answer. The audit brief asks that the answer page be separate from the questions. | Print the answers on the parent summary page, or add "Print page 2 on its own sheet" to the file, or add a blank back to page 1 in the build. |
| 4 | Medium | Parent summary, "Next lesson" box | The page says both "The recording link is private to your family: please do not share it" and, two sentences later, "your tutor will share a private link with enrolled families." `privacy.html` says recordings are visible to "only the enrolled families of the same group, through a private link". "Private to your family" is not what the notice promises. The same sentence appears on every Term 2 parent page (it is copied from Term 1). | Use the notice's words: "The recording link is private to the families in your child's group: please do not share it." |
| 5 | Medium | Home practice H4, H5 (and H1) | H5 says "Draw a line of 9 children." and gives two dotted lines; H4 asks for "I know because ..." and gives one; H1 asks the child to place a coin and gives one line. There is no drawing box although the sheet's own hint is "use toys in a row, or draw the line" and the guide's stuck advice is to draw. | A drawing box for H4 and H5 and two lines for the "because". |
| 6 | Medium | Online t1 and g1 worked steps | The steps read "4 take away 1 children are in front of Mei, and the same number are behind. Count Mei once: that is 2 times 4 take away 1." (t1 with k = 4, answer 7) and "Half of 7 take away 1 are in front of the middle child." (g1 with n = 7). They are ambiguous: "2 times 4 take away 1" reads as 2 x (4 - 1) = 6 although the answer for k = 4 is 7, and "Half of 13 take away 1" can read as half of 13, take 1. The worked solution contradicts the answer to a child who reads it as written. The template substitution produces the grammar. | Write the steps with numbers computed by the template: "{k-1} children are in front of Mei and {k-1} are behind. {k-1} + 1 + {k-1} = {ans}." and "{n-1} children are left. Half of {n-1} is {(n-1)/2}, so the middle child is {ans|ord}." (derive fields exist). |
| 7 | Low | Online c4, t1, t2, g1, g2 | Six of the ten items are text only although the lesson and the pre-flight say a picture is needed for a 6-year-old (spec R1); only c1 and c2 draw the line. c4 and t2 ("Ali is 3rd and Mei is 9th") are the easiest to draw. | Add a `line_up` picture (the `fig` key already works) to c4 and t2. |
| 8 | Low | Online c1, c2 pictures | The SVG `aria-label` is "6 children in a line, front on the left". It does not say which child is ringed, so a screen-reader user cannot answer c1 or c2. | Make the label say "the 3rd child from the front is ringed" only after a check, or give a different accessible task. |
| 9 | Low | Online c1, c4 | "Type just the number: for 3rd, type 3." trains the confusion the lesson separates (4 and 4th), although the runner already reads "3rd" correctly (`4th` was accepted for c2). | Accept and prefer "3rd": "Type the place, like 3rd." The runner already parses it. |
| 10 | Low | Home practice H1, H2, title | H1 packs three instructions before the answer frame; H2 has no unit frame; the title reads "Who Is Where?: practice at home". | "Put 6 toys in a row. Put a coin on the 4th toy from the front. The coin is on the toy that is ___ from the back."; "There are ___ children in front of Kumar."; "Practice at home: Who Is Where?" |
| 11 | Low | All printed pages | Footer 5.8 mm from the bottom edge. | Raise it to 8 to 10 mm. |

## Summary for the fixer

Fix 1 (the link) and 3 (the answer page) first; both are template or build decisions shared by every lesson. Findings 2 and 6 change online data only and no answer. Finding 4 is one sentence copied across all Term 2 lessons. Findings 7 to 11 are polish. The home sheet and the parent page are otherwise sound and the beyond-P1 statement is exactly what the owner decisions ask for.
