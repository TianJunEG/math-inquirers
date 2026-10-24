# Fixes for Lesson 4 after the independent workbook audit

Audit: `audit/WORKBOOK_AUDIT_L04.md` (READY AFTER MINOR FIXES). Fix pass of 22 Oct 2026. Maths and answers are unchanged except G3 (new part d) and G1 (a shown end number, same blanks 8 and 36).

| # | Sev | Finding | What I did |
|---|---|---|---|
| 1 | Medium | Workbook printed 7 pages, orphan S2 tab, thin pages | Already fixed by the shared template (commit 2379b77). Rebuilt: 6 pages, fill 98%, 91%, 96%, 90%, 91%, 84% (kit page). Self-audit corrected. |
| 2 | Medium | Investigation had no writing space | Template now prints 4 ruled lines; checked on the PDF. Nothing to change in the lesson. |
| 3 | Medium | G3 (c) no slot, (d) two commands and nowhere to try blocks | G3 is now a to e: (a), (b) sums; (c) Circle Yes or No: are the two totals the same; (d) a printed second block 52, 53, 62, 63 with two blanks (115 and 115); (e) Circle Yes or No, then write why on 2 lines. Checks added in verify/l04_checks.py. |
| 4 | Medium | S6(b) and E3 "I know because" had no room; reasons not for Start here or exit | S6 keeps circle plus "She should have said ___." (no written reason). E3 is Circle Yes or No only. Reasons stay in T1, T2, G1(b), G3(e), the talk and the tutor questions. Key, script, slide notes and mistakes lists updated. |
| 5 | Medium | T3 method order in the stem; G2 gives away the trick; S4 reveals count | T3: stem "Find the next two numbers", part (a) is a frame for the gaps. G2: "Look at this list: ... and so on." with no hint about two patterns (kept in the tutor hint). S4: "The different last digits are ___ ..." (the five blanks remain as the Start here scaffold). Script line for Q4 matches. |
| 6 | Medium | Page references wrong | True again at 6 pages (key says pages 3, 4, 5 for Think harder, Go further, Investigation and exit; the kit is page 6; materials say page 6). Checked on the built key and parent page. |
| 7 | Low | No pointer to the 100 square on pages 4 and 6 | Page 3 intro now says "(the kit page)"; E2 says "on your 100 square". Page 5 Investigation already says "kit page". |
| 8 | Low | G1 thin, G1/G2/T3 alike | G1 no longer tells the rule: the child finds it from 2, 6, ___, 14, 22, ___, 58 and checks it at the end of the chain. G3 now has a test block. Counts stay S6, T4, G3. |
| 9 | Low | Missing full stops, "a" not "(a)", mixed units | Full stops added on all answer frames; E2 and the online home items now say "down 1 row" and "right 1 square". The "(a)" bracket label is printed by the shared template: listed, not edited. |
| 10 | Low | Look-back crowded, small type | Template (b_print look-back box). Not edited. |
| 11 | Low | S1/S2 cells small, 14 mm blanks | Page 1 is 98% full so the squares cannot grow; blank width is a template matter. Not changed. |
| 12 | Low | E1/E2 repeat the sneak-peek | Left as a before-and-after on purpose; E3 is now a circle (finding 4). |
| 13 | Low | None needed | None. |

Owner decisions (22 Oct 2026): the tutor guide strand note and the parent summary now say plainly that Term 1 goes beyond the school Primary 1 syllabus on purpose (no MOE-aligned wording). Every Start here item is approachable with the 100 square and counters; beyond-P1 ideas (growing gap, sum of two, interleaved, counting in 3s) are at Think harder, Go further and the Investigation only. The end-of-term check and photo return belong to Lesson 10.

Template or tool items not fixed here: bracketed (a)/(b) part labels, Look-back layout and type size, narrow blank width, the "Watch for" list punctuation in the key.
