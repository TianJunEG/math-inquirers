# Independent workbook audit: Level 1 Term 1 Lesson 9 (Draw and Measure)

Auditor: independent model review (desk review, no child observed). Read: `L09_Workbook.pdf` (5 pages) and `L09_Workbook_Answer_Key.pdf` (3 pages), every page rendered and viewed, text extracted, `lessons/l09.json` for tiers, minutes, materials. Every question was solved independently; arithmetic re-checked in Python. The author's self-audit (`AUDIT_L09.md`, 17/24) was read afterwards. Nothing was edited.

Instruments (as `docs/audit/reaudit_p1.md`): A = gifted-style rubric 12 x 0-2, max 24; tier compliance (strict); B = student journey, three personas x six scores 1-5, shown as mean (max 5).

## Verdict: Ready after minor fixes

Maths is correct and the lesson sits well inside P1 length. The workbook is let down by having no picture of a ruler anywhere, no fallback for a child without a ruler, and an Investigation with no writing space.

| Instrument | Score |
|---|---|
| A, gifted-style rubric | 17 / 24 (author: 17) |
| Tier compliance (14 printed S/T/G items) | 12 / 14 = 86% strict (S7, T4 partial) |
| B, journey mean (LOW / MIDDLE / HIGH) | 3.7 / 4.2 / 3.7 |
| Maths | 0 wrong, 0 unanswerable; 1 mildly ambiguous (G2b) |

Instrument A by criterion: 1 low floor/high ceiling 2; 2 depth over speed 1; 3 generalise 2 (does the start mark matter); 4 justify 1 (reasons only in Investigation); 5 multiple paths 1; 6 ladder 2; 7 student-led 1; 8 complexity/context 1; 9 problem posing 1 (G3 open); 10 metacognition 2; 11 pacing/compacting 1; 12 extension not acceleration 2.

Instrument B (one line each): LOW 3.7: drawing and measuring with a real ruler is concrete and fun, but starting at the 0 mark and 4 drawn lines in Start here are slow for a child still learning to hold the ruler. MIDDLE 4.2: best-fitting lesson of the three. HIGH 3.7: T2, G1 and G2 stretch; G3 is a good open task.

## A. Maths

All answers correct: S1 0 and 7; S2 9 cm, 5 cm longer; S3 open; S4 13, 9, 4 longer; S5 8 cm; S6 No, 7 cm; S7 15; T1 12; T2 7 cm, ends at 9; T3 8 cm; T4 16, 19, 3 longer; G1 C = 11 (B = 11, A + B = 19); G2 mark 8, crawled 14 cm (9 forward + 5 back); G3 any three different whole numbers summing to 20; E1 0 and 6; E2 9; E3 7; sneak-peek 3 cm and 8 cm. Open answers S3 and G3 are marked correctly as open. No picture/text mismatch can arise (there are no pictures, finding 1).

## B. Syllabus fit

Drawing and measuring to the nearest cm is P1 (Measurement 1.1 to 1.4). Lines not starting at 0 (T2), bent paths (T1) and the snail with back-tracking (G2) are enrichment and correctly sit at Think harder / Go further, not in Start here. Nothing is beyond P1 in the Start here pages except the rounding wording of S7 (finding 2).

## C. Tier check

- S1 to S6: compliant (ruler, drawing and subtraction by counting on).
- S7 (partial): "To the nearest cm" is the rounding skill; WORDING_GUIDE rule 25 keeps rounding to T/G. It is P1 syllabus content, but it is the lesson's new idea and is not approachable untaught.
- T4 (partial): same skill as S7 (tip closer to the next mark) with bigger numbers plus a difference: not a "new setting".
- T1 to T3: correct (new setting: path, start mark at 2, dot on a line).
- G1 to G3: mastery plus extension (three-piece ribbon, snail, open path). Correct, though G1 is largely two subtractions.
- No contest-style move in Start here.

## D. Numbered findings

| # | Sev | Page / Q | Evidence | Suggested fix |
|---|---|---|---|---|
| 1 | Medium | S4, S7, T2, T4, G2 (pp 2 to 4) | No page shows a ruler. Every "mark", "tip between 14 and 15" and "start at the 2 mark" is described in words, and S7/T4 even give the answer to the rounding ("It is closer to the 15 mark"). The skill the lesson teaches (reading where the end falls) is never practised on paper, and school papers always print a ruler strip. | Print a ruler strip with a pencil or spoon in S4, S7, T2, T4, G2; remove "closer to" from the stems and let the child decide. |
| 2 | Medium | p2 S7 vs p3 T4 | S7 (Start here) and T4 (Think harder) are the same task (read a tip between two marks, choose the nearer, then compare) with larger numbers. Rounding to the nearest mark is flagged to Think harder by rule 25. | Move S7 to Think harder, replace it in Start here with an exact-mark reading from a picture; make T4 different (two pencils where one starts at 2, then compare). |
| 3 | Medium | p5 Investigation | "Try 3 more start marks. Each time, draw a line 6 cm long and write where it ends. What do you notice? Start with: I notice ..." has no lines, table or boxes: three drawings and a sentence with nowhere to put them. | Add a three-row table (start mark / end mark) and two lines for "I notice". |
| 4 | Medium | materials, whole workbook | A ruler is required for every page, but `workbook.kits` is empty, so no printed ruler exists. The year plan says a printed ruler on the kit page when the child has none. A family without a 15 cm ruler cannot do S1 to S6 or the check Q9. Safe to miss: true, but a child present with no ruler is excluded. | Add a kit page with a printed cm ruler strip and the same 10 cm print-at-100% bar used on the check sheet. |
| 5 | Low | p4 G2 (b) | "In all, the snail has crawled ___ cm." Two readings (whole way 14, or distance from the start 4); key says 14 and names the trap. For a 7-year-old the phrase "in all" is not obviously the total path. | "How far has the snail crawled in all, counting the way back?" or ask (b) as "forwards ___ cm, back ___ cm, in all ___ cm". |
| 6 | Low | p3 T4 (a) | Layout: "Ali's pencil is ___ cm and Mei's pencil is ___ \n cm long." The unit wraps to the next line and two answers share one sentence (rule 18: one question per part). | Split into (a) Ali's, (b) Mei's, (c) how much longer. |
| 7 | Low | p1 S1 | The stem says "Start at the 0 mark", then asks "The line starts at the ___ mark and ends at the ___ mark." The first blank is copied from the stem; the child can fill it with no reading of the ruler. | Ask for the end mark only, or remove "Start at the 0 mark" from the stem and keep it in the tutor script. |
| 8 | Low | p5 E1 | The Exit ticket asks for a line "on your spare paper" while the other exit answers are on the sheet; the sneak-peek/exit procedure is "hold your paper to the camera once", so the drawing and the blanks are on two different papers. | Give a small drawing box on the sheet under E1. |
| 9 | Low | p1 S3 | Open task (guess then measure the child's own pencil); key gives "within about 3 cm" and "17 to 19 cm", which a grown-up cannot check without the pencil, and S3 is the only Start here question not checkable from the key. | Fine as an open item; add "a grown-up checks with the pencil" in the key. |
| 10 | Low | p1 to p4 | Time: Start here modelled at 18 minutes with four drawn lines, one object measurement and two answer-based comparisons. A child who is still finding the 0 mark takes longer per line than the 2 to 3 minutes modelled. | Reduce S2/S5 to one drawn line each (give the first line printed), keep the comparison. |
| 11 | Low | all workbooks | Mi appears to hold a calculator (AUTHORING says never show it). Shared asset. | Owner to check. |

## E. Layout and usability (6-year-old)

Drawing boxes are 170 mm wide and about 20 to 27 mm high, wide enough for a 13 cm line (T3) and a 15 cm ruler; the S2 box has to hold two lines (4 and 9 cm) under each other in a box 20 mm high, which is tight for a child with a thick pencil. Printing: because several boxes hold measured lines, a "print at 100%" note and a 10 cm bar would make the printed box dependable, as the check sheet already does; the workbook itself has neither. Nothing is cut off; every page starts with an instruction line; page 4 is about 25% empty.

## F. Pedagogy

Progression S1 (draw) to S7 (nearest) is logical; Think harder is a real change of setting. The exit ticket (E1 to E3: draw from 0, compare two ends, line starting at 3) matches the objectives; E3 uses the start-at-another-mark idea that the page treats as Think harder. Misconceptions (starting at the edge, counting 0 as one, adding instead of subtracting) are in the key for every question.

## G. Safeguarding and inclusion

Plastic or wooden rulers only, no metal edge, no sharp objects (stated in the materials). Labels neutral; names mixed (Ali, Mei, Siti, Ben); no ranking; look-back may be passed. The only inclusion gap is the no-ruler case (finding 4). Pass otherwise.

## H. Consistency with other lessons

Commands match L08 and L10. The dashed-line answer blank is used for all "___ cm" answers (correct under rule 16). Yes/No has no printed buttons (see L08 finding 8). Mascot corner use matches.
