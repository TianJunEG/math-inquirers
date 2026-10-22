# Fixes for the independent workbook audit, Lesson 1 (22 Oct 2026)

| # | Sev | Finding | What I did |
|---|---|---|---|
| 1 | Medium | S2 and S7 need 35 and 66 strokes | Quick draw taught: one long line per bundle of ten, one short line per single stick. Added to the page 1 hint, S2 and S7 hints, solution, key, tutor stuck line. S2 about 8 strokes, S7 about 12 (draw_strokes set). Both draw warnings gone. S7 still one shared box (template has one draw box); text says "Ali's sticks, then Mei's sticks". |
| 2 | Medium | "Circle Yes or No" and T4 print nothing | Already fixed by the template (commit 2379b77): S6a prints Yes / No. T4 now has `choices` and prints its three options on one row; wording "Circle one. Then show how you know." |
| 3 | Medium | T3 "even" is P2 and undefined | Clue now "My tens digit is more than 3." Answer 46 unchanged and unique. Updated T3 hint and solution, online t3 and its slip, the make-your-own puzzle (example now 73), and verify/l01_checks.py. |
| 4 | Medium | Investigation has no writing area | Template now prints 4 ruled lines (verified on page 5). A 6-row table is a template feature: left to the owner. |
| 5 | Low | G1 no command, blank starts with a name | (a) "Circle the child who has more sticks." with Ben / Siti printed; (b) "That child has ___ more sticks." |
| 6 | Low | G3 three questions in one stem | Stem "Write 30 in different ways, like 3 tens and 0 ones." then (a) write the ways on the lines, (b) "There are ___ ways." 5 lines. |
| 7 | Low | straws / sticks / pencils | S5 now says sticks. G2 keeps pencils (boxes of 10, a different context on purpose). |
| 8 | Low | key orphan heading | Template problem (keep-with-next). Not edited; listed. |
| 9 | Low | kit page spacing and empty right quarter | Template problem. Not edited; listed. |
| 10 | Low | hint says write how you know on all | Page 3 hint now: "T4 asks you to show how you know." |
| 11 | Low | G1 and T4 same idea, little extension | G1 rebuilt: Ben 6 tens 14 ones (74), Siti 5 tens 29 ones (79): two bundles opened, then the gap (5). Answers, key, checks updated. Online g1 left as it was. |
| 12 | Low | Siti is the mistaken child again | S6 now Kumar (script, slide notes, key updated). |

Owner decisions (22 Oct): parent summary, tutor guide strand note and tutor prep now say Term 1 goes beyond the school Primary 1 syllabus on purpose; no MOE-aligned claim anywhere. Lesson 1 content itself is within numbers to 100, so no tier move was needed; Start here items are explored with bundles and the kit.

Result: validator 22 pass, 0 WARN, 0 FAIL; workbook 6 pages, fills 93/91/97/85/98/89%.
