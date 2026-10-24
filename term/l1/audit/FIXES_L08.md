# Fix pass: Lesson 8 (Balance and Swap), 22 Oct 2026

Source: audit/WORKBOOK_AUDIT_L08.md. Rebuilt with `bash term/l1/build.sh 08`: validator 17 pass, 0 warn, 0 FAIL; 6-page workbook (fills 92, 90, 84, 86, 100, 91%), home sheet 2 pages, parent page 1 page; 2612 independent answer checks.

| # | Sev | Finding | What was done |
|---|---|---|---|
| 1 | Medium | S3 ambiguous blank, hint in stem, written reason in Start here | Stem now "Siti writes 6 + 3 = 5 + 9." (a) Is it balanced? Circle Yes or No. (b) Fill in the missing number: 6 + 3 = 5 + []. The "I know because" part was removed (rule 25). Key, script read-out, checks updated. |
| 2 | Medium | G2 missing answer slots | Three rows of [] + 5 = 9 + [] (a to c), then (d) I notice. Key gives example pairs; checks verify each pair and that all three differ. |
| 3 | Medium | Investigation had no writing space | Already fixed by the shared template (4 ruled lines, commit 2379b77); verified on page 5. |
| 4 | Medium | Investigation first step unclear, no key answer | First step is now: which total is not 10, then "the 6 goes up 1. What does the 4 do?". The key gives both answers; checks added. |
| 5 | Medium | No plate or balance picture | NOT FIXED: the shared figure tools have no plate type and I may not edit them. Reported as a template gap. S2 keeps its draw box. |
| 6 | Low | S4 teaching and "across" jargon | Instruction removed: "7 + 5 = 12. Fill in the missing numbers." The rows are plain 6 + [] = 12, 5 + [] = 12, 4 + [] = 12. |
| 7 | Low | Box and line mixed | Boxes now used for every single missing number: S3, S7, T3, T4, G1, G2, G3, home H1 to H3. Lines kept for words. S7 spare line removed. |
| 8 | Low | Circle Yes or No prints no choices | Already fixed by the shared template (words printed); verified. |
| 9 | Low | Page 3 intro names the technique | hint_p3 is now "Use your plates or draw a picture. Then write how you know. Choose any question, in any order." |
| 10 | Low | G3 is S6 with bigger numbers | Added (c): Kumar has 12 in his pocket, how many on his page (33), a reversed unknown. Stem names three children; key, checks, hint, solution updated; one answer line fewer. |
| 11 | Low | Kit page unused by any question | Kept (it is a shared kit type); intro now says it helps S5 and S7 and that the plates are real plates. S7 hint offers the tens bar. A plates kit is a template change: reported. |
| 12 | Low | Mi holds a calculator | Shared asset, not touched. Reported to the owner. |
| 13 | Low | Pages 2 and 4 under-filled | Now 90% and 86% after the G2 and G3 changes. |

Owner decisions of 22 Oct 2026: strong arithmetic kept (S5, S7, E3). The tutor guide strand note and the parent summary now say plainly that Term 1 goes beyond the school Primary 1 syllabus on purpose; no "MOE-aligned" claim. S7 stays in Start here with a two-route hint (find the total first, or move a tens bar); if tutors find it not approachable after class exploration it should move to Think harder. No end-of-term-check or WhatsApp text appears in this lesson.

Tier balance: Start here lost its only written-reason item (S3). Think harder keeps the taught idea in new settings (T1 to T4). Go further gained the reversed unknown (G3c) and three open pairs (G2).
