# Math Inquirers Level 1 (p1, ages 6-8): RE-AUDIT after fix passes

Date 2026-10-22. Repo read-only. Built decks, workbook and guide were rebuilt 08:26-08:27, qbank.json 08:11, lessons.js 08:16; no mid-edit changes seen. Workbook is now 58 pages (was 48).
Method: every answer recomputed in Python (verify_p1.py, 184 checks, 0 wrong answers); decks, workbook PDF text and pages, guide and scripts read in full; same scales as the baselines.

## 10-line summary
1. Audit 1 verdicts, before -> after: OK 1 -> 5 (L1, L2, L4, L8, L10); minor fix 6 -> 5 (L3, L5, L6, L7, L9); needs rework 3 -> 0.
2. Audit 1 baseline findings (31 distinct): 26 fixed, 5 partly (#7, #10, #27/P-2, #29/P-5, P-3), 0 not fixed; about 13 new problems (N1-N13, none a wrong answer).
3. Numbers: no wrong answer anywhere in the lessons, workbook or bank (184 checks).
4. Gifted rubric (0-24): mean 13.3 -> 17.8 (+4.5); the baseline's own rework projection was 15.8, so +2.0 over target. All lessons still in the 12-19 band, none reaches 20.
5. Gifted per lesson now: L1 17, L2 18, L3 18, L4 19, L5 17, L6 19, L7 17, L8 19, L9 17, L10 17.
6. Journey LOW mean 3.02 -> 3.40 (+0.38); biggest gain L6 1.83 -> 3.17.
7. Journey MIDDLE mean 3.80 -> 3.95 (+0.15).
8. Journey HIGH mean 3.78 -> 4.05 (+0.27); HIGH still waits about 28-30 of 90 minutes.
9. Top regressions/new: "After question 3 you may choose" sits on a page that ends at Q2 in L4-L9 (N1); stale T-labels and keys in L6/L1/L10 slides (N2, N3, N8); stale Question Bank PDF/DOCX and Scheme of Work (N4, N5); L9 Q4 uses 2 erasers while teaching 1 clip = 3 erasers (N6).
10. Do not call it "gifted": criteria 5 (multiple methods), 7 (student-led), 10 (look-back lacks "what I'd try next"), 11 (compacting) are still weak everywhere.

---

## Part 1. Content audit (baseline docs/audit/audit_p1.md)

### Verdict per lesson
| Lesson | Before | After | Reason |
|---|---|---|---|
| L1 | minor fix | OK | 0-50 strip in kit, Q4 up to 30, stale-key issue is cosmetic (N3) |
| L2 | minor fix | OK | corner sets verified ({1,2,3},{1,3,5},{2,4,6},{4,5,6}; 13 impossible); N7 is a note mismatch |
| L3 | minor fix | minor fix | keys of 3, tally, half-pictures remain (#10); C1 ambiguity (N12) |
| L4 | OK | OK | pattern circle/triangle/square verified |
| L5 | minor fix | minor fix | two-step check replaced, Q3 split; N1 choice line |
| L6 | needs rework | minor fix | cents-only warm-up, 25c worked example, dollars to T5; stale T-labels (N2) |
| L7 | needs rework | minor fix | exit asks "hexagon" (N11), T3 duplicates talk time |
| L8 | minor fix | OK | pre-printed crosses, Q5/Q6 optional; N13 is minor |
| L9 | minor fix | minor fix | N6 clip/eraser mismatch |
| L10 | needs rework | OK | relay replaced; graph dog 4, cat 7, fish 3, bird 5 (answers 2, 19, cat+fish); ribbon two ways verified; N8 key wording |

Counts: OK 1 -> 5, minor 6 -> 5, rework 3 -> 0.

### Verified specifics
L6: 45c with exactly 3 coins is only 20+20+5; 35c exactly 3 coins only 20+10+5; 45c exactly 4 coins only 20+10+10+5; $12 sets 5+5+2 and 10+1+1. L10 T3 has two sets; S5 ribbon two ways. L3 C7 exactly two graphs. L7 house is 8 shapes. L9 ribbons A7 B5 C9. The single "fail" in my script was a tuple-shape artefact, not content.

### Baseline findings status
- Fixed (26): #1-6, 8, 9, 11-26, 28, P-6. Includes page-2 window now 58-68 in all ten lessons, L6 cents-first, L8 pre-printed crosses, L1 strip, L5 bars taught before page 1, L10 relay replaced, "No.?" bug gone, Fast Track box replaced by a neutral line, Investigation moved onto a page every child reaches.
- Partly (5):
  - #7 shape names: Q2 table, Q3c and the exit still use pentagon/hexagon/octagon vocabulary. Fix: limit to names in the syllabus list or print the names on the slide.
  - #10 L3: keys of 3, tally and half-pictures remain. Fix: keep one new idea per page; move half-pictures to Go further.
  - #27/P-2 movement break: only a 1-minute stand-up at 68. Fix: add a 1-minute stretch at about 55 in lessons with long solo pages.
  - #29/P-5: slide Think harder items still differ from workbook T1-T4. Fix: regenerate slide items from the workbook list.
  - P-3 reading/writing load: improved but the Look-back (about 50 words plus 12 tick boxes in 2 minutes) is heavy. Fix: reduce to 4 ticks and one sentence stem.
- Not fixed: 0.

### New problems and regressions (exact location and fix)
- N1 (all lessons, workbook page 1): "After question 3 you may choose: carry on, or try Think harder." is printed on page 1, but in L4-L9 page 1 ends at Q2 (pp 18, 23, 28, 33, 38, 43), so the choice lands on solo page 2 and the line is wrong. Fix: "When you finish this page you may choose...".
- N2 (L6 slides): l6-key says T2 (should be T1); l6-teachexact says T2 (should be T1); l6-ws2ans note says T3 (should be T2).
- N3 (L1): lessons.js Think harder slide key says "2) 6" but the slide item is "22 -> 20".
- N4: outputs/designed/Math_Inquirers_P1_Question_Bank.pdf/.docx (and hp/ copy) built 07:50, before qbank.json edits at 08:11; L1 S4 reads "Start at 50 take away 7" in the PDF, L6 S4 differs. Rebuild. Also hp/qbank.py is stale; re-running it would undo tier fixes. Delete or mark.
- N5: outputs/schemes/Math_Inquirers_P1_Scheme_of_Work.pdf (07:32) is stale: L6 objective says "pay in dollars with notes up to $100", L6 exit "40c exactly three coins", L7 exit "3 by 3 grid"; lessons.js now has L6 "30c with 20,10,5" and L7 "6 sides -> hexagon". Rebuild.
- N6 (L9): mini-lesson teaches 1 clip = 3 erasers; Q4 uses 2 erasers. Fix: change Q4 to 3 or add a 2-eraser worked step.
- N7 (L2 teachpage2): teaches "big numbers in corners" for target 12, but the worksheet is target 9/10 (small numbers in corners). Fix: match the example to the worksheet.
- N8 (L10 l10-key): "Q5b counting only the 3 small triangles" should say 2.
- N9 (about 21 mini-lesson "Your turn" slides): still say whiteboards held up together, inconsistent with the sneak-peek rule of no public board. Fix: "show your tutor" wording.
- N10 (Look-back): promises "I am still stuck (my tutor will come and help)" but the guide defers it to the next lesson; online the tutor cannot see the tick. Fix: say "your tutor will look at this after class".
- N11 (L7): exit asks for "hexagon" (beyond syllabus); T3 duplicates the talk-time question. Fix: ask "how many sides", change T3.
- N12 (L3 C1): "24 voted; apple 6; orange 6 more than banana" does not say there are only three fruits. Fix: state it.
- N13 (L8): riddles and odd-one-out are taught (slides 54-58) for the optional Q5/Q6.
- Minor: L3 title-slide note says "thumbs and chat" while other slides say "no typing"; l3-explore1 shows Pear but the workbook has Watermelon; online sneak-peek option "everyone holds paper to camera at the same moment" exposes answers in gallery view; the guide's "take a photo and send it through the approved channel" does not say who sends it (safeguarding clarity: say the tutor sends it, never the child privately).

Mandatory teaching slides per lesson (mini + pre-page): L1 7, L2 8, L3 8, L4 6, L5 9, L6 4, L7 7, L8 9, L9 10, L10 9. L9 at 10 is heavy for ages 6-8 in 10 minutes.

---

## Part 2. Gifted rubric (24 max; criteria 1-12)

Criteria scores 0/1/2 from visible design features.
| Lesson | Before | After | Delta | Baseline projection |
|---|---|---|---|---|
| L1 | 15 | 17 | +2 | 17 |
| L2 | 15 | 18 | +3 | 17 |
| L3 | 13 | 18 | +5 | 16 |
| L4 | 12 | 19 | +7 | 15 |
| L5 | 12 | 17 | +5 | 15 |
| L6 | 13 | 19 | +6 | 15 |
| L7 | 15 | 17 | +2 | 17 |
| L8 | 13 | 19 | +6 | 16 |
| L9 | 11 | 17 | +6 | 14 |
| L10 | 14 | 17 | +3 | 16 |
| Mean | 13.3 | 17.8 | +4.5 | 15.8 |

Across the level: C1, C3, C6, C9 = 2 everywhere. C2 = 2 for L4, L6, L8 else 1. C4 = 1 for L1, L7, L10 else 2. C5 = 1 everywhere (one method per task). C7 = 2 only L10 (card choice and report-back). C8 = 2 only L3. C10 = 1 everywhere (look-back lacks "what I would do differently / try next"). C11 = 1 everywhere (all teaching mandatory, no compacting). C12 as baseline.

Tier check of printed Think harder and Go further items: about 6 mild repeats of 72 (L4 T4, L5 T4, L6 T4, L7 T3, L9 T3), about 92 percent compliant. Not comparable with the baseline's 73 percent, which covered all bank items.

Remaining gaps and fixes: C5 add one "another way?" prompt per Q3; C7 let a child lead one talk-time item in every lesson; C10 add "Next time I will..." to the Look-back; C11 mark slides "skip if page 1 is done" for confident groups. Still not "gifted": it is enrichment with good choice, not acceleration.

---

## Part 3. Student journey (1-5; P, D, F, C, M, S)

Cell means (exact, from Python), before -> after.
| Lesson | LOW | MIDDLE | HIGH |
|---|---|---|---|
| L1 | 2.83 -> 3.17 (+0.34) | 3.83 -> 4.00 (+0.17) | 3.33 -> 3.83 (+0.50) |
| L2 | 3.00 -> 3.17 (+0.17) | 3.67 -> 3.83 (+0.16) | 3.33 -> 3.83 (+0.50) |
| L3 | 4.17 -> 4.17 (0) | 4.33 -> 4.33 (0) | 3.67 -> 4.00 (+0.33) |
| L4 | 3.50 -> 3.67 (+0.17) | 4.17 -> 4.17 (0) | 3.17 -> 3.83 (+0.66) |
| L5 | 2.83 -> 3.33 (+0.50) | 3.83 -> 4.00 (+0.17) | 3.83 -> 3.83 (0) |
| L6 | 1.83 -> 3.17 (+1.34) | 2.83 -> 3.50 (+0.67) | 4.17 -> 4.33 (+0.16) |
| L7 | 3.33 -> 3.50 (+0.17) | 4.17 -> 4.17 (0) | 4.00 -> 4.17 (+0.17) |
| L8 | 2.67 -> 3.17 (+0.50) | 3.67 -> 3.83 (+0.16) | 4.17 -> 4.33 (+0.16) |
| L9 | 3.17 -> 3.33 (+0.16) | 3.83 -> 3.83 (0) | 3.83 -> 4.00 (+0.17) |
| L10 | 2.83 -> 3.33 (+0.50) | 3.67 -> 3.83 (+0.16) | 4.33 -> 4.33 (0) |
| Mean | 3.02 -> 3.40 (+0.38) | 3.80 -> 3.95 (+0.15) | 3.78 -> 4.05 (+0.27) |

Representative score vectors (P D F C M S): L1 LOW 4 3 3 3 3 3; L6 LOW 4 3 3 3 3 3; L6 HIGH 5 3 5 4 5 4; L3 MID 5 4 5 4 4 4; L8 HIGH 5 3 5 4 5 4. D (dignity/pace-of-reading) is 3 almost everywhere: the lowest-scoring dimension.

What drove gains: cents-only L6 warm-up and 25c worked example (LOW +1.34); every lesson now has a guaranteed LOW win in the first 10 worksheet minutes (10 of 10, was 7 of 10); sneak-peek puzzles replace the warm-up check; Investigation placed on a page every child reaches; neutral choice line replaces Fast Track box; L8 pre-printed crosses and optional Q5/Q6; L10 relay replaced.

No dropped cells. Weakest cells now: LOW at 3.17 in L1, L2, L6, L8. Unchanged: L3 LOW/MID, L10 HIGH, L5 HIGH, L4/L7/L9 MID.

Remaining journey problems and fixes:
- HIGH still waits about 28-30 of 90 minutes (warm-up, 25-35 mini-lesson, 52-58 teaching bursts, talk time, exit). Fix: make mini-lesson "Your turn" slides skippable and give HIGH a parallel task during teaching bursts.
- LOW at 3.17 in L1, L2, L6, L8: reading load and Look-back length (P-3). Fix as above.
- N1 choice line misplacement breaks the sense of control (C) for L4-L9 solo page.
- N10 unmet promise of help harms safety/belonging (S) for LOW.
- N9 whiteboards shown together re-introduces public comparison for LOW.

---

## Notes for memory (session cannot write memory)
- p1 re-audit done 2026-10-22: audit-1 OK 5 / minor 5 / rework 0; gifted mean 17.8; journey LOW 3.40, MID 3.95, HIGH 4.05.
- Do not regenerate hp/qbank.py (stale; undoes tier fixes). Rebuild Question Bank PDF/DOCX and Scheme of Work from current qbank.json and lessons.js.
- Fix N1 first; it is a one-line change that affects six lessons.
