# Math Inquirers Level 5 (p5, ages 10-12): RE-AUDIT after the fix passes

Repo /home/claude/math-inquirers was read only and was not modified. Files were not mid-edit when read. Scores are judgement; no children were observed. The weekly dose / email pack was not audited.

## PART 1. Content audit (baseline docs/audit/audit_p5.md, commit 5286a96)

### Answers
Every answer was recomputed in Python (exact Fractions) and by hand: all keys, sneak-peek puzzles, Investigation answers, Think harder, Go further and qbank items. Zero wrong numeric answers. Two apparent FAILs (L3 Q5, L7 GF) were float-comparison artifacts in my test; the exact checks pass (60/100=3/5; 54/(3/5 x 3/4)=120; GST=9).
Brute-force confirmations: L1 riddles unique (7253609, 3594208, 5437209), 231 maximum bracketing; L2 3/4 as three different unit fractions has exactly 3 ways, smallest difference 8/35; L3 8 counter ways; L5 cuboid counts 6/8/9/10/7 for 24/36/48/60/64; L6 cheapest 20 cans $13.64, eggs $9.60, car park $4.80/$9.50, Investigation 5 and 4 ways; L8 8 and 5 isosceles triangles; L9 100th digit is 5; L10 chair order Siti-Mei-Ali-Ben, 60 rectangles, 15 digit-4s.

### Verdict per lesson (before / after)
| Lesson | Before | After |
|---|---|---|
| L1 | minor fix | OK |
| L2 | minor fix (one real defect) | minor fix (P6 skill taught to all, clipped label) |
| L3 | minor fix | OK |
| L4 | OK | OK |
| L5 | minor fix | OK |
| L6 | minor fix | OK |
| L7 | needs rework | minor fix (optional P6 slides have no real time) |
| L8 | minor fix | OK |
| L9 | OK | OK |
| L10 | minor fix | OK |
Counts: before OK 2 / minor 7 / rework 1; after OK 8 / minor 2 / rework 0.

### Baseline 20 issues
Fixed 17, partly 2, not fixed 0 (one more counted in the 17 as folded). Fixed: #1 timetable (page 2 now 14 min, check 4), #2 L2 teachpattern spoiler (now 1/7-1/8 example), #3 five pages per lesson (57 total), #4 L7 P6 items moved to Think harder and labelled, #6-#11, #13-#20.
Partly:
- #5 L2 fraction/whole number: Core is clean and Q1(d) removed, but still taught on teach1/try1 to everyone with a note-level label, and the unlabelled warm-up quick question 4/5 / 2 remains.
- #12 figure-less Think harder/Go further: only a generic "Draw a big, neat diagram" line added. Still no figures: L4 GF Q6/Q7, L5 GF Q7, L8 TH Q3/Q4, L8 GF Q5/Q6.

### New or remaining problems (with fix)
1. Reading load up about 36% on workbook pages 1-2 (same counter: mean about 357 to about 484 words; L3 538, L5 572, L6 579). Cause: more Start here hints, "Page 2 plan" lines (35 words), choice box (20 words). Fix: trim the boilerplate to one line.
2. L2 workbook p.8 Q1(c) figure label clipped ("one child's share is sh..."). Fix: shorten to "short by".
3. L10 deck order is exit, end (88-90 goodbye), reflect (86-88): goodbye precedes the reflection. The L10 title note repeats "In this last lesson the 88 to 90 slot is certificates." twice. Fix: reorder slides, delete the duplicate sentence.
4. L7 optional P6 slides teachchange and teachdeal sit in the 72-76 check slot, so P6 teaching has no time. Fix: move to a take-home note or cut.
5. Shared outputs still carry old labels: outputs/designed/Math_Inquirers_P5_What_Learners_Get.pdf ("Challenge for strong thinkers", "Challenge Screening Set", "Readiness tracker"); p5/Math_Inquirers_P5_Weekly_Dose_of_Thinking_Math.pdf; outputs/designed/Math_Inquirers_P5_Question_Bank.pdf ("gifted-education-type problems", Core/Think Harder/Challenge); outputs/schemes P5 Scheme of Work. Workbook says "Go further". Guide says ages 11-12, question bank says 10-12. Fix: align wording and age band.
6. "I am still stuck (my tutor will check in with me)" promises a check-in that cannot happen in-session (reflection 86-88, stamp 88-90; nothing follows in L10). Fix: define when it happens (open session next lesson start; never a private message).
7. Sneak-peek is tight (2 puzzles, privacy mechanics, reveal, debrief in 3 minutes, worst in L1, L5, L7). L1 slide offers "all hold paper to the camera together", which is effectively public. Puzzle 2 still hard for LOW in L1 (brackets), L2, L5 (tank rise), L8.
8. Think harder header "Draw a big, neat diagram first and label every length or angle" prints on every lesson, including L1, L2, L3, L6, L7, L9, L10 where nothing is labelled. Fix: make it per-lesson.
9. Slide-only Think harder/Go further items differ from the printed pages (documented in notes).
10. Breakout pairs have no adult; with 4 rooms and one tutor each gets about 3 minutes. Guide's "send photo through the approved channel" should say via the parent.
11. Warm-up quick questions untaught and heavy for LOW: L2 (2/5 x 3/4, 4/5 / 2), L3 (3/4 of a number is 27; 1/3 of 3/4).
12. L1 page 1 still ends with the 6-clue riddle wall; L8 Q2 compulsory three shapes on page 1 and Reasons A-F strip only on page 2 though page 1 Q1(d), Q2 need it.
13. Tier slips in Think harder (Core level): L2 TH Q1, Q4; L4 TH Q1; L7 TH Q3, Q4. Duplicates: L6 TH Q4 repeats page-2 gym structure; L2 TH Q3 vs Investigation (a); L9 TH Q4 vs Investigation (a)(b).

## PART 2. Gifted-style rubric (12 criteria x 0/1/2, 24 max)
| Lesson | As found | After gifted fixes | Now |
|---|---|---|---|
| L1 | 13 | 15 | 19 |
| L2 | 14 | 16 | 18 |
| L3 | 15 | 16 | 19 |
| L4 | 16 | 17 | 19 |
| L5 | 16 | 18 | 20 |
| L6 | 17 | 18 | 21 |
| L7 | 15 | 17 | 20 |
| L8 | 15 | 17 | 19 |
| L9 | 16 | 18 | 20 |
| L10 | 18 | 19 | 21 |
| Mean | 15.5 | 17.1 | 19.6 |
All ten lessons improved. Bands: 20+ in L5, L6, L7, L9, L10 (5 lessons); the rest in 12-19; none under 12.
Per criterion: C1, C3, C4, C6 = 2 everywhere. C2 and C11 = 1 everywhere (no scheduled 10+ minute think time; first 37 minutes lockstep; sneak-peek deliberately not used to skip). C5 = 2 in L6, L9, L10. C7 = 2 in L10 only. C8 = 2 in L5, L6, L7. C9 = 2 except L2 = 1 (make-up-your-own items still bank-only). C10 = 2 everywhere (lenient: identical 2-minute box, "Next time I will try" dropped). C12 = 2 everywhere, though L2 and L7 still carry flagged P6 previews.
Sensitivity: scoring C9 and C10 as 1 drops the mean to about 17.6 and no lesson reaches 20.
Remaining gaps and fixes: add a scheduled 10-minute open think slot for HIGH (C2/C11); restore "Next time I will try" (C10); add a make-up-your-own item to L2 Investigation (C9).

## PART 3. Student journey (Participate / Fit / Fun / Confidence / Motivation / Social-online; Fit converted fitq = 5 - 2|f-3| for means)
After scores (P,F,Fun,C,M,S):
| L | LOW | MIDDLE | HIGH |
|---|---|---|---|
| 1 | 4,2,3,4,3,4 | 4,3,4,4,4,4 | 5,4,4,4,4,4 |
| 2 | 4,2,3,3,3,4 | 4,3,4,4,4,4 | 4,4,4,4,4,4 |
| 3 | 3,2,3,3,3,3 | 4,3,3,4,3,4 | 4,3,4,4,4,4 |
| 4 | 4,3,4,4,4,4 | 5,3,5,4,4,4 | 4,4,4,4,4,4 |
| 5 | 4,2,4,3,3,3 | 4,3,5,4,4,4 | 5,4,4,4,4,4 |
| 6 | 4,2,3,3,3,3 | 4,3,4,4,4,4 | 5,4,4,4,4,4 |
| 7 | 4,3,4,4,4,4 | 5,3,5,4,5,4 | 5,4,4,4,5,4 |
| 8 | 4,2,3,4,3,4 | 4,3,4,4,4,4 | 4,4,5,5,4,4 |
| 9 | 4,3,4,4,4,4 | 4,3,4,4,4,4 | 5,4,5,5,5,4 |
| 10 | 4,3,4,4,4,4 | 4,3,5,4,4,4 | 4,3,5,4,5,4 |
(L10 LOW social 3 per heat.py: 4,3,4,4,4,3.)

Heatmap means, before > after (delta):
| L | LOW | MIDDLE | HIGH | Lesson |
|---|---|---|---|---|
| 1 | 3.00>3.50 (+0.50) | 4.17>4.17 (0) | 3.50>4.00 (+0.50) | 3.56>3.89 |
| 2 | 2.67>3.33 (+0.66) | 4.00>4.17 (+0.17) | 3.67>3.83 (+0.16) | 3.44>3.78 |
| 3 | 2.00>3.00 (+1.00) | 3.17>3.83 (+0.66) | 4.00>4.17 (+0.17) | 3.06>3.67 |
| 4 | 3.50>4.17 (+0.67) | 4.50>4.50 (0) | 3.67>3.83 (+0.16) | 3.89>4.17 |
| 5 | 3.00>3.33 (+0.33) | 4.17>4.33 (+0.16) | 3.83>4.00 (+0.17) | 3.67>3.89 |
| 6 | 2.17>3.17 (+1.00) | 3.67>4.17 (+0.50) | 3.83>4.00 (+0.17) | 3.22>3.78 |
| 7 | 3.50>4.17 (+0.67) | 4.67>4.67 (0) | 3.83>4.17 (+0.34) | 4.00>4.33 |
| 8 | 2.83>3.50 (+0.67) | 4.00>4.17 (+0.17) | 4.00>4.17 (+0.17) | 3.61>3.94 |
| 9 | 3.33>4.17 (+0.84) | 4.17>4.17 (0) | 4.33>4.50 (+0.17) | 3.94>4.28 |
| 10 | 3.00>4.00 (+1.00) | 4.17>4.33 (+0.16) | 4.33>4.50 (+0.17) | 3.83>4.28 |
Persona means: LOW 2.90 > 3.63 (+0.73); MIDDLE 4.07 > 4.25 (+0.18); HIGH 3.90 > 4.12 (+0.22); overall 3.62 > 4.00. No cell dropped.

Five weakest cells now and exact fix:
1. L3 LOW 3.00. Q2: add "Start here: draw the AFTER bars: Siti 3 boxes, Mei 4 boxes. 7 boxes are 84 stickers. One box = ____." Q3(b): add "Start here: the total stays 80. Ali 3 parts, Ben 5 parts. One part = ____." Warm-up: replace "3/4 of a number is 27" and "1/3 of 3/4" with "1/4 of 36" and "Half of 1/2".
2. L6 LOW 3.17. Q2: add "Shop B: $2.92 = 292 cents. 292 / 4 = ____ c." Shorten Q5 stem. Mark Q3(c)(d) "(try this one if you like)".
3. L2 LOW 3.33. Warm-up: replace 2/5 x 3/4 and 4/5 / 2 with "Which is bigger, 1/2 or 3/5?" and "1/4 of 12". Q2(b): add "9/20 - 1/4: write 1/4 as twentieths: ___/20". Shorten clipped figure label.
4. L5 LOW 3.33. Q2: add starter "1x1x36, 1x2x18, 1x3x___, 1x4x___, 1x6x___; then shortest edge 2". Mark Q2(b) optional, allow a calculator for 50x30x18. Replace sneak-peek puzzle 2 (tank rise) with "A box has a base 5 cubes by 4 cubes. How many layers hold 60 cubes?"
5. L1 LOW and L8 LOW 3.50 (tie). L1: mark Q3 "(try this one if you like)"; make the choose line per-lesson ("After question 2"). L8: mark Q2(b) rhombus optional; print the Reasons A-F strip on page 1 too.
Strongest: L7 MIDDLE 4.67, L4 MIDDLE 4.50, L9 HIGH and L10 HIGH 4.50 (tie).

Level-wide patterns:
- LOW now has a guaranteed win in the first 10 workbook minutes in 10 of 10 lessons (baseline 8 of 10; L3 and L10 fixed). Page 1 still ends with a wall in L1 (Q3) and L8 (Q2).
- HIGH low-demand time is about 20 of 90 minutes (baseline about 25). The Go further what-if is open from minute 9, but the first 37 minutes are not compacted. HIGH Fit is still weak.
- Social improved: private answers, volunteers first, pass, no cold-calling. Safeguarding model holds (no private tutor-to-child messages); the "still stuck" tick is the exception that needs a defined open-session follow-up.
- "Think harder" and "Go further" remain mildly sorting labels.
- Added reading load (Part 1 item 1) is the main newly introduced cost, and it falls hardest on LOW.

## 10-line summary
1. Content audit verdicts before: OK 2 / minor fix 7 / rework 1.
2. Content audit verdicts after: OK 8 / minor fix 2 (L2, L7) / rework 0.
3. Baseline 20 issues: 17 fixed, 2 partly (#5, #12), 0 not fixed. Zero wrong answers anywhere.
4. Gifted mean before 15.5 (post-gifted-fixes 17.1), now 19.6; 5 lessons at 20+; none under 12.
5. Journey LOW 2.90 > 3.63 (+0.73).
6. Journey MIDDLE 4.07 > 4.25 (+0.18).
7. Journey HIGH 3.90 > 4.12 (+0.22); overall 3.62 > 4.00.
8. Weakest: L3 LOW 3.00, L6 LOW 3.17, L2 LOW 3.33, L5 LOW 3.33.
9. New problems: reading load +36%, L2 clipped label, L10 slide order, L7 P6 time, stale Challenge wording in outputs, undefined "still stuck" follow-up.
10. Repo untouched; report at this path.
