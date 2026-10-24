# Fix pass, Lesson 9 (Draw and Measure): audit finding -> action

Source: `audit/WORKBOOK_AUDIT_L09.md`. Rebuilt 22 Oct 2026; validator 0 FAIL, 1 WARN (model estimate of page 5 at 102%; measured PDF fills 84, 92, 95, 88, 91%, 5 pages).

| # | Sev | Finding | What was done |
|---|---|---|---|
| 1 | Medium | No ruler picture anywhere | True-scale ruler figure added to S4 (Ali and Mei pencils), S6 (Mei's line), T2 (line A from the 2 mark), T3 (two tips between marks) and G2 (snail's way forward). Rounding is decided from the picture, no "closer to" in any stem. |
| 2 | Medium | S7 and T4 were the same rounding task, rounding in Start here | S7 removed from Start here (now 6 questions); rounding lives in Think harder (old T4, now T3, read from a picture). Old T3 (dot on a 13 cm line) dropped to keep page 3 on one page; the subtraction idea is in S2/S5/G1. |
| 3 | Medium | Investigation had no space | Investigation text now says what goes on each of the 4 ruled lines (lines 1 to 3: start and end marks; line 4: "I notice ..."). |
| 4 | Medium | No printed ruler / no fallback | Not done on purpose (owner: families have a ruler, no cut-out). Parent page lists the ruler; tutor_prep asks before the lesson; materials note asks to print at 100% because the ruler pictures are real size. A child with no ruler remains excluded from the drawing items (listed as open). |
| 5 | Low | G2(b) "in all" ambiguous | "The snail has crawled ___ cm in all, counting the way back." |
| 6 | Low | T4(a) two answers in one line, unit wraps | Split into (a) Ali, (b) Mei, (c) how much longer. |
| 7 | Low | S1 first blank copied from the stem | Ask for the end mark only (box); E1 changed the same way. |
| 8 | Low | E1 drawn on spare paper | E1 has a drawing box on page 5; page still fits (91%). |
| 9 | Low | S3 not checkable from the key | Key says a grown-up checks with the pencil; stem now "measure it in whole cm" (no "nearest"); H3 likewise. |
| 10 | Low | Start here too slow with four drawn lines | S2 and S5 each draw one line (the other length is given in words). Start here now 6 questions, page 2 time reduced to 8 minutes. |
| 11 | Low | Mi seems to hold a calculator | Shared asset, not edited; reported. |

Other changes: verify/l09_checks.py updated (picture data read back against the keys, T3 tips are clearly nearer one mark, S1/S2/E1 answers); script and slide notes for pages 1 and 2 rewritten; G3 sets `draw_strokes: 3` (a path of 3 pieces, so the heavy-drawing warning no longer applies); tutor guide strand note and parent summary now say Term 1 goes beyond the school P1 syllabus on purpose (no MOE-aligned claim).

Not changed: Go further balance (G1 stays largely two subtractions; G2 and G3 carry the stretch); online practice c5.
