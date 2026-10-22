# Self-audit: Level 1 Term 1 Lesson 5 (Make-a-Ten Adding)

Desk audit by the author (a model); no child has used this lesson. Machine checks: `python3 term/l1/tools/validate.py 05` (22 pass, 0 warn, 0 FAIL after the fix pass of 22 Oct 2026). Format follows `AUDIT_L01.md`.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| 1 | Schema valid | PASS | validator |
| 2 | Every answer verified independently | PASS | 422 checks in `verify/l05_checks.py` (counters moved in ten-frames, kit bars regrouped, every make-a-ten pair enumerated, investigation rule tested for all pairs 1 to 9) |
| 3 | Online variants verified | PASS | 525 variants: expression = brute-force oracle = runner JavaScript; page loads in a browser |
| 4 | Timing sums to 90, no part OVER | PASS | script needs 71:32, slow class 84:55; opening 2, explore 16 |
| 5 | Timing realistic | PASS with caveat | modelled, not stopwatch. Workbook script 25:38 of 28; slow class needs 30:36 there but the total stays under 90 |
| 6 | Tiers | PASS | Start here 7 (S1 to S7, 19 min), Think harder 4 (pairs that make ten, 3 or 4 numbers, odd-one-out), Go further 3 (plan's six-number sum, 1 to 9, write a sum to 100). Nothing contest-style at Start here |
| 7 | Neutral labels, nothing named | PASS | validator |
| 8 | Sneak-peek | PASS | Q1 count 12 counters (access), Q2 moving one counter keeps the total (thinking); unmarked; papers to the camera once |
| 9 | No private chat, safeguarding | PASS | no breakout rooms, check-in in the open session |
| 10 | No overclaims | PASS | strand label tutor-only; guide and parent page now say plainly that Term 1 goes beyond the school P1 syllabus on purpose (owner decision 22 Oct 2026); no 'MOE-aligned' claim |
| 11 | Ruler only if the child has one | PASS | none needed |
| 12 | Materials home-findable | PASS | buttons, pasta, clips, paper; kit page used for 28 + 6 (up to 5 bars, 14 squares) |
| 13 | Recording cues | PASS | 11 cues at most 26 words, each with an action |
| 14 | Joining cold | PASS | warm-up: bonds to 10 (ten-frame), next ten (bonds to 20), tens and ones together; needs only counting to 20 |
| 15 | No copied contest text | PASS | validator; problems are original (ideas from the original drafts only) |
| 16 | Layout | PASS | 30 slides, no overflow or Mi overlap reported, all slide types viewed; workbook 6 pages (PDF-measured fill 96, 97, 95, 92, 99, kit 91); home 2; parent 1; guide 18 |
| 17 | Printed answers separate | PASS | key is its own PDF |
| 18 | Reading load | PASS | no child string over 40 words |

Independent audit (WORKBOOK_AUDIT_L05.md), fix pass of 22 Oct 2026. Author's own Instrument A claim of 21 was too high; the auditor scored 17. Honest re-score after the fixes (desk review, no child): low floor high ceiling 2; depth over speed 1 (S3 to S6 and E1, E2 remain calculation); generalise 2; justify 2 (T3 now asks for the reason on lines, G1 b needs reasoning); multiple paths 1; challenge ladder 2 (G1 now has a change-one-number part, so Go further is no longer T4 with more addends); student-led inquiry 1; complexity 1 (one story, T4); problem posing 1 (G3); metacognition 2; pacing 1; extension not acceleration 1 (crossing a ten stays in Start here by owner decision, scaffolded). Total 17/24, same as the auditor's 17 but with the tier and wording faults removed. Tier compliance (strict): S7 (spot the mistake) is on 8 + 6, taught in class, so kept; S6 d is now scaffolded ("47 needs ___ more to make 50"), S6 c is within 40; the sums over 40 left in Start here (S5 35 + 7, S6 d) are scaffolded by blanks that name the next ten. 16 of 17 items clean, one partial (S7).

Open items: never trialled with children; 28 + 6, 35 + 7 and 47 + 6 cross a ten above the school P1 range by owner decision; the exit ticket has no item for objective 4 (the total does not change when counters move; covered in Talk time and the Sneak-peek, exit part is fixed at 3 questions); S4 picture shows 28 only, not the 6 extra ones; template gaps listed in `audit/FIXES_L05.md` (no printable ten-frame kit page, kit bars have no gaps, look-back type size).
