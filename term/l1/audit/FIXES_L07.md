# Fixes for Lesson 7 after the independent workbook audit

Source: `audit/WORKBOOK_AUDIT_L07.md`. Files changed: `lessons/l07.json`, `verify/l07_checks.py`, `AUDIT_L07.md`, `out/l07/`.

| # | Sev | Finding | What was done |
|---|---|---|---|
| 1 | Medium | Investigation has no writing space | Template now prints 4 lines (commit 2379b77). Task reduced to two subtractions of each kind plus the frame "Counting up is quicker when ___." so it fits the 4 lines. |
| 2 | Medium | 2-digit minus 2-digit in Start here (S3, S4, S5, S7, E1) | Kept by owner decision (22 Oct). Scaffolded: S3 is the printed worked step (a, b), S4 now has the 46 bars-and-squares picture, S5 has a drawing box and "draw a bar for each ten and a square for each one" (draw_strokes 14, no warning), S1 picture kept. Tutor-guide strand note and parent summary now say Term 1 goes beyond the school P1 syllabus on purpose, no MOE-aligned claim, and a child who cannot reach S3/S4/S7 after class goes to Think harder. Start here time cut from 20 to 19 minutes (S4, S6). |
| 3 | Medium | T1/T2 over-scaffolded, T4 no space, column-swap slip missing | T1: printed blanks removed, number line 30 to 70 with 38 and 62 marked, one answer slot plus a line. T2: single "83 - 77 = ___" with 2 lines (child chooses the method). T4: 2 lines. Column-swap mistake added to the key for T1, T2, T4. Answers in checks/key updated (T1 val 24, T2 val 6). |
| 4 | Medium | S6(c) say-why in Start here; "Check her tens" | (c) removed; stem is now "Kumar says 59 - 20 = 57." with Yes/No and the answer. Name changed (see 14). |
| 5 | Low | G1 has three jobs in one stem; choice inside text | Stem "Fill in the blanks. Circle the quicker way for each."; choices printed as take away / count up; separate "I know because ___." with 2 lines. |
| 6 | Low | S1 picture smaller than the kit pieces | Not fixed: the bundle picture size is in the shared template (`tools/svg.py`). Report to template owner. |
| 7 | Low | Missing full stops | Added to S1(a), S7, T1, T3, T4 frames. |
| 8 | Low | Odd wording S7, T3 | S7 "21 children are sitting." (online c4 and template too); T3 "Find how many more stickers Ben has than Ali now." (online t3 and template too). Wording avoids 7-word overlaps with the school-paper catalogue. |
| 9 | Low | Investigation "quicker" is a rule, not checkable | Frame "Counting up is quicker when ___." added. |
| 10 | Low | 100 eggs not buildable on the kit page | G2 hint now says to draw a number line from 64 to 100. |
| 11 | Low | Look-back print small, "still stuck" under Next time | Not fixed: look-back block is template. Report. |
| 12 | Low | Key heading orphaned at foot of page 1 | Not fixed: key layout is template. Report. |
| 13 | Low | Mi holds a calculator | Not fixed: owner asset. Report to the owner. |
| 14 | Low | Siti is again the wrong-answer child; Yes/No vs Right/Wrong across lessons | S6 now uses Kumar (script, slide note, key, solution updated). Circle wording across lessons left to a cross-lesson pass. |
| 15 | Low | Intro says "write how you know" but no lines | T1, T2, T4 now have lines; T3 already had one. |

Also: a long online-practice step string shortened to clear a reading-load warning. Not changed: E3 (quicker-way choice in the exit ticket) stays because it tests objective 4.
