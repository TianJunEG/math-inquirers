# Re-audit: Math Inquirers Level 3 (p3, ages 8-10) after the fix passes

Read-only audit. Repo /home/claude/math-inquirers untouched. p3 files were unchanged since 08:34 during the audit (not mid-edit). Sources: p3/content/l1..l10.js, p3/gifted.json, p3/workbook_html.js, split/p3l1..10, p3 workbook PDF (58 pp), guide, weekly. Known shared-file limit: the Weekly Dose PDF still uses the heading "Challenge".

Same methods and scales as the baselines. Scores are my judgement from the current slides, scripts and workbook; the journey scores are estimates of a simulated child, not observed data.

## 1. Content audit (baseline audit_p3.md)

### 1.1 Answers
344 Python checks (digits, cryptarithms, remainders, fractions, polyominoes, money, timetables, graphs, logic): every answer in keys, qbanks, workbook figures and slide notes is correct. 5 check failures were artifacts of my checks (double-counted rotations, tuple order, table-1 included in a "all ten last digits" list, 22 cm impossible by parity, L9 22 vs 15 ways: the lesson's 15 is right under its own rules). No wrong answer anywhere.

### 1.2 Verdicts per lesson

| Lesson | Before | After | Change | Reason now |
|---|---|---|---|---|
| L1 Number Sleuths | minor fix | OK | improved | Q5(b)/Q6 stretch moved, if-time marks added. Only the garbled ws1ans note remains (typo). |
| L2 Cryptarithm Crackers | minor fix | minor fix | same | Q6 fixed, but workbook p8 Q1(a) (3[]47 + 25[]8 = []025, two carries, three blanks) comes before the worked-supported Q1(b) and is a hard first item. Swap (a) and (b). |
| L3 Times Table Treasure | minor fix | minor fix | same | Q2(a) and Q5 table fixed. Page 2 now has only Q5 as non-star (Q4/Q6 starred), so a child who stops at the stars gets almost no page-2 practice. |
| L4 Model Makers | needs rework | minor fix | improved | Q5/Q6 replaced by P4-level items. Go further Q1 (c0) and sneak-peek puzzle 2 are still P4/P5 level. |
| L5 Remainder Riddles | OK | OK | same | Wording fixed. Reading load ~372 words on pages 1-2 is heavy for a LOW reader. |
| L6 Fraction Walls | OK | OK | same | Ambiguous digits item and stray "coin lesson" fixed. |
| L7 Area Architects | minor fix | minor fix | same | Table rows fixed. Sneak-peek puzzle uses area/perimeter before they are defined. |
| L8 Angle and Line Detectives | minor fix | minor fix | same | Diagonal Q5(c) fixed. Q5(c) hint now gives the answer away. |
| L9 Measure and Money Masters | needs rework | minor fix | improved | Cut to ~12 core of 17 parts, still heavy. p43 Q1(e)/(f) text spills outside the answer card. "5:15 p.m.." typo. |
| L10 Challenge Day | minor fix | minor fix | same | Breakout version of the stations works, but there is no List card slide; logic clue wording fixed. Exit notes still mention a favourite-lesson line. |

Counts: before 2 needs rework / 6 minor fix / 2 OK. After 0 needs rework / 7 minor fix / 3 OK.

### 1.3 The 25 baseline findings
Numbers follow the order of audit_p3.md.
- Fixed (19): 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23.
- Partly fixed (4): 1 (L4 Go further Q1/c0 still P5), 2 (L9 still 17 parts, ~12 core), 4 (L10: breakout vs shared card works, but no List card slide), 13.
- Not fixed (2): 24, 25.

### 1.4 New problems introduced or exposed (exact place, fix)
1. Minutes 67-70, every lesson: Think harder, Go further and the Investigation all sit in a 3-minute slot with four slides. The Investigation has no slide, no time and no debrief. Fix: give the Investigation its own slot (move talk to 72-80) or make it take-home with a next-week share.
2. Look back (min 86-88): promises "still stuck" is seen by the tutor, but the tutor cannot see a paper page; the "hand signal" is public. Fix: say it is for the child; tutor reads it in the next lesson, or drop the promise. No public labels.
3. Safeguarding: "show only to the tutor on camera" is not private in a group video call, and the tutor guide also says "send a photo through the approved channel", which contradicts the no-private-messages rule. Fix: show to the whole group on a count of three, or show the tutor in the group call; delete the photo line.
4. L8 Q5(c) hint gives the answer.
5. L9 p43 Q1(e)/(f) spill outside the answer card; "5:15 p.m.." typo.
6. L10 exit notes still mention the favourite-lesson line.
7. L1 ws1ans garbled note.
8. "After question 3 choose" (page 1 to page 2 routing) lets a middle child skip core page-2 practice. Fix: "do Q4 and Q5 first, then choose".
9. Pairs work unsupervised in breakout rooms until the check at ~minute 52 (page 1 at 42). Fix: tutor visits each room by minute 47.
10. L3 page 2 has only Q5 non-star.
11. Reading load unchanged: L5 ~372 words, L8 up to ~254 words on a page. Fix: read-aloud step or shorter stems for L5 Q3 and L8 Q5.
12. L7 sneak-peek puzzle uses area/perimeter before they are taught; L2 Q1(a) hard first item (see 1.2); L4 sneak puzzle 2 and the Go further slide are P4/P5.

## 2. Gifted-style rubric (baseline gifted_p3.md; 12 criteria x 0/1/2, max 24)

What moved: criterion 1 stays 2 and criterion 2 stays 1 everywhere. Criterion 6 (challenge ladder) is 2 in all lessons now. Criterion 9 (posing) is 2 where an Investigation plus a printed posing item exist (most lessons). Criterion 10 (reflection) is raised to 2 on the strength of the Look back page (strategy, what was hard), but it is borderline: there is no "what next", and the tutor never sees the reflection. Criterion 11 (pacing/compacting) stays 1: sneak-peek and Go further from minute 10 help, but the sequence is still lockstep. Criterion 7 (debrief/discussion) is held back by the Investigation having no debrief. I did not give any lesson 20 because of that.

| L | Lesson | Before | Projected in baseline "after rework" | Now | Delta vs before | Band |
|---|---|---|---|---|---|---|
| 1 | Number Sleuths | 16 | 18 | 19 | +3 | 12-19 |
| 2 | Cryptarithm Crackers | 15 | 17 | 18 | +3 | 12-19 |
| 3 | Times Table Treasure | 17 | 19 | 19 | +2 | 12-19 |
| 4 | Model Makers | 16 | 18 | 19 | +3 | 12-19 |
| 5 | Remainder Riddles | 16 | 18 | 19 | +3 | 12-19 |
| 6 | Fraction Walls | 15 | 17 | 18 | +3 | 12-19 |
| 7 | Area Architects | 17 | 19 | 19 | +2 | 12-19 |
| 8 | Angle and Line Detectives | 14 | 16 | 17 | +3 | 12-19 |
| 9 | Measure and Money Masters | 15 | 17 | 18 | +3 | 12-19 |
| 10 | Challenge Day | 16 | 18 | 19 | +3 | 12-19 |
| | Mean | 15.7 | 17.7 | 18.5 | +2.8 | partly |

Every lesson improved; none dropped. The level stays "enrichment-flavoured with gaps". To reach the 20+ band: give the Investigation a slot and a debrief (criteria 7, 11); add a "what will I try next" line to Look back and let the tutor read it (10); add a second solution path to the mini-lesson (2, 5).

## 3. Student journey (baseline journey_p3.md; P, F, U, C, M, S each 1-5; mean of six)

Cell format: before -> after (delta).

| Lesson | LOW | MIDDLE | HIGH |
|---|---|---|---|
| L1 Number Sleuths | 3.33 -> 4.00 (+0.67) | 4.17 -> 4.17 (0.00) | 4.00 -> 4.17 (+0.17) |
| L2 Cryptarithm Crackers | 2.67 -> 3.17 (+0.50) | 3.67 -> 4.00 (+0.33) | 4.50 -> 4.50 (0.00) |
| L3 Times Table Treasure | 2.33 -> 3.17 (+0.84) | 3.67 -> 4.17 (+0.50) | 4.67 -> 4.67 (0.00) |
| L4 Model Makers | 3.33 -> 3.50 (+0.17) | 4.17 -> 4.17 (0.00) | 4.00 -> 4.17 (+0.17) |
| L5 Remainder Riddles | 2.67 -> 3.33 (+0.66) | 3.83 -> 4.17 (+0.34) | 4.33 -> 4.50 (+0.17) |
| L6 Fraction Walls | 3.17 -> 3.67 (+0.50) | 4.17 -> 4.17 (0.00) | 4.00 -> 4.17 (+0.17) |
| L7 Area Architects | 3.17 -> 3.33 (+0.16) | 4.00 -> 4.17 (+0.17) | 4.33 -> 4.50 (+0.17) |
| L8 Angle and Line Detectives | 2.83 -> 3.50 (+0.67) | 3.83 -> 4.00 (+0.17) | 4.50 -> 4.50 (0.00) |
| L9 Measure and Money Masters | 2.17 -> 2.83 (+0.66) | 3.33 -> 3.83 (+0.50) | 4.50 -> 4.50 (0.00) |
| L10 Challenge Day | 3.67 -> 3.67 (0.00) | 4.50 -> 4.50 (0.00) | 4.00 -> 4.17 (+0.17) |
| Persona mean | 2.93 -> 3.42 (+0.49) | 3.93 -> 4.13 (+0.20) | 4.28 -> 4.38 (+0.10) |

No cell dropped. Dimension strings (P F U C M S) behind the cells:
LOW: L1 543444, L2 423334, L3 423334, L4 433344, L5 433334, L6 434434, L7 433334, L8 434334, L9 332333, L10 434443.
MIDDLE: L1 544444, L2 444444, L3 544444, L4 544444, L5 544444, L6 544444, L7 544444, L8 444444, L9 434444, L10 545454.
HIGH: L1 544444, L2 545454, L3 545554, L4 544444, L5 545454, L6 544444, L7 545454, L8 545454, L9 545454, L10 544444.

Why LOW rose: sneak-peek puzzles are an access point (P, U up); no public labels and the talk-time pass help S and C; stars and scaffolds cut F problems. Why HIGH rose only a little: Go further is available from minute 10, but the Investigation has no audience or debrief, and mini-lesson and check slides still sit below their level (F stays 4, not 5). MIDDLE gains most where page 1 was previously a stretch (L2, L3, L5, L9).

Weakest cells now: L9 LOW 2.83 (17 parts, spill on p43, money decimals); L2 LOW 3.17 (Q1(a) first item); L3 LOW 3.17 (page 2 only Q5 non-star, table recall); L7 LOW 3.33 (sneak vocabulary); L5 LOW 3.33 (reading load).
Strongest: L3 HIGH 4.67; L2, L5, L7, L8, L9 HIGH 4.5; L10 MIDDLE 4.5.

Level-wide patterns: (a) the 3-minute 67-70 crush hurts HIGH and MIDDLE most; (b) the Look back promise, if false, costs LOW trust; (c) unsupervised pairs until minute 52 put LOW at social risk; (d) reading load is the largest unfixed LOW barrier in L5, L8, L9; (e) the P5-level Go further items cost HIGH nothing but should not be shown to everyone on a shared slide.

## 4. Priority fixes
1. Remove the "photo through approved channel" and the "tutor on camera" privacy claim (safeguarding contradiction).
2. Give the Investigation a slot and debrief; reallocate minutes 67-80.
3. Make Look back honest about who reads it.
4. L9: cut to 12 parts, fix p43 spill and the typo.
5. L2: swap Q1(a)/(b). L8: strip the Q5(c) hint. L3: unstar one page-2 question. L7: define area/perimeter or change the sneak puzzle. L4: swap Go further Q1.
6. Tutor visits each breakout pair by minute 47.

## 10-line summary
1. Audit-1 verdicts before: 2 needs rework / 6 minor fix / 2 OK.
2. Audit-1 verdicts after: 0 needs rework / 7 minor fix / 3 OK (L4, L9 improved; L1 to OK).
3. 25 baseline findings: 19 fixed, 4 partly, 2 not fixed.
4. All answers correct (344 checks); no wrong answers.
5. Gifted mean before 15.7, after 18.5 (all 10 lessons up, band still 12-19).
6. Journey LOW mean 2.93 -> 3.42.
7. Journey MIDDLE mean 3.93 -> 4.13.
8. Journey HIGH mean 4.28 -> 4.38; no cell dropped.
9. Top new problems: Investigation has no slot or debrief; privacy claims not true in group video; Look back unseen by tutor.
10. Weakest cell L9 LOW 2.83; strongest L3 HIGH 4.67.
