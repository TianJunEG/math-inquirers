# Lesson timing audit: Math Inquirers Level N=3 (P3, ages 8-10)

Analysis only. Nothing in content, guides, decks, builds or outputs was edited, committed or published. Numbers below are model estimates (a walk-through, not stopwatch timings), with a range. Rebuild every number with `python3 docs/audit/timing_p3.py --md --fix`.

## 1. Verdict

- **None of the 10 lessons fits 90 minutes if the tutor runs the slides and script live online as written.** Central estimate 94.8 to 111.6 min (mean 101.6); range across the optimistic and pessimistic parameter sets 86.4 to 124.5. 10 of 10 lessons are OVER by 2+ min in the central estimate; 5 of 10 are still OVER in the optimistic set. No lesson runs short.
- The overrun is structural, not lesson-specific: the same three parts are over in every lesson (sneak-peek + game + quick questions, +3 to +4 min; the worksheet block, +2 to +13 min; and, in the lessons with a materials-heavy task, Explore) while Talk time is LOOSE in 8 of 10 lessons (about 3 min of dead time) and cannot pay for it.
- Spoken words are not the cause. Tutor speech is about 10 min of a lesson; the rest is waiting (22 min), children's activity (49 min) and online transitions (20 min).

| Lesson | Slides | Script SAY words | Central total | Low-high | vs 90 | Worst parts (central) | After fixes (central) |
|---|---:|---:|---:|---|---:|---|---:|
| 1. Number Sleuths | 29 | 315 | **98.7** | 90.4-109.3 | +8.7 | Worksheet +7.9; Sneak-peek + game + quick Qs +3.8 | 86.9 |
| 2. Cryptarithm Crackers | 28 | 289 | **101.8** | 93.1-113.0 | +11.8 | Worksheet +8.9; Sneak-peek + game + quick Qs +3.7 | 86.3 |
| 3. Times Table Treasure | 28 | 371 | **98.7** | 90.4-109.3 | +8.7 | Sneak-peek + game + quick Qs +3.5; Mini-lesson +3.1 | 86.5 |
| 4. Model Makers | 28 | 304 | **104.2** | 95.1-115.9 | +14.2 | Worksheet +13.0; Sneak-peek + game + quick Qs +3.9 | 89.3 |
| 5. Remainder Riddles | 28 | 296 | **97.3** | 88.9-107.9 | +7.3 | Worksheet +5.2; Sneak-peek + game + quick Qs +3.8 | 88.3 |
| 6. Fraction Walls | 28 | 244 | **105.9** | 96.5-117.8 | +15.9 | Worksheet +10.3; Explore +4.3 | 84.8 |
| 7. Area Architects | 27 | 367 | **100.4** | 91.6-111.7 | +10.4 | Worksheet +5.9; Sneak-peek + game + quick Qs +3.4 | 88.9 |
| 8. Angle and Line Detectives | 27 | 333 | **102.9** | 93.5-114.8 | +12.9 | Worksheet +11.6; Sneak-peek + game + quick Qs +2.9 | 86.9 |
| 9. Measure and Money Masters | 26 | 363 | **94.8** | 86.4-105.6 | +4.8 | Worksheet +3.5; Sneak-peek + game + quick Qs +3.3 | 82.9 |
| 10. Challenge Day | 29 | 307 | **111.6** | 101.5-124.5 | +21.6 | Explore +8.8; Exit + look-back + close +6.2 | 89.2 |

Parts flagged across the level (central, count of lessons): Opening: OK 10; Sneak-peek + game + quick Qs: OVER 10; Explore: OVER 4, TIGHT 2, OK 4; Mini-lesson: OVER 2, TIGHT 4, OK 4; Brain break: OK 10; Worksheet: OVER 10; Talk time: OK 2, LOOSE 8; Exit + look-back + close: OVER 1, TIGHT 2, OK 7.

Size outliers: slide counts run 26 to 29 (L9 smallest, L1 and L10 largest at 29); script SAY words run 244 (L6) to 371 (L3), mean 319, sd 38, so L3, L7 and L9 are about one sd high and nothing is extreme; slide text is highest in L3 (1 899 words against a mean of 1 720). The longest single teaching slides are L7 teach1 (126 words), L3 teachgrid (106) and L5 we1 (104). The tutor guide itself is 81 pages. None of this changes a time estimate by more than 1 min; it is the number of question-and-wait moments and room moves that costs time.

## 2. Where the time goes (all lessons, central)

Average per lesson: speaking 9.8 min, waiting 21.9 min, children's activity 48.6 min, transitions 20.0 min, REC cues 1.3 min. The three biggest sinks against the scripted budget:

1. **The worksheet block (40-70).** It needs 32 to 43 min (mean 37) against 30. Page 1 is scripted as 9 to 12 min but must hold a 2-minute start, two room moves (3 min) and Q1-Q3, which a MID child needs 7.5 to 11 min for, so inside the slide time a LOW child finishes 0.7 to 1.5 of the 3 Start-here items, a MID child 1.2 to 2.8 and a HIGH child 2.0 to 3.0; on page 2 (Q4-Q6, 'if time' items counted) LOW finishes 0.8 to 1.4, MID 1.5 to 2.3 and HIGH 2.5 to 3.0. Between the pages there are 1 to 4 teaching slides that need 1.3 to 8.4 min against 2 to 4 scripted, and each 'check together' slide costs about 2.6 min against 2.
2. **Online transitions and waiting.** About 27 slide changes (11 min at 25 s), four room moves (6 min at 90 s) and 2 min of finding materials and slips of paper add up to about 20 min per lesson; the 10 s + 20 s question rule and hold-ups add 22 min of waiting. The scripted budgets treat most of this as free.
3. **The 2-10 warm-up block.** It needs 11 to 12 min against 8 in every lesson: the fixed sneak-peek puzzles cost about 4.2 min (two 1-minute tries, two camera hold-ups, reading and slide change), the game 3.8 min and 4 or 5 quick questions 2.9 to 3.2 min. Explore is the fourth sink in the lessons with fiddly materials (L6 fractions strips +4.3, L3 circle clocks +3.0, L9 party menu +2.8) and L10 (+8.8).

Fixed items, central: sneak-peek puzzles 4.1 to 4.3 min; look-back 3.8 min (the guide gives it 2); REC cues 8 x 10 s = 1.3 min; L10 certificates 8 x 30 s = 4 min plus about 1 min of volunteers.

## 3. Model and assumptions (keep identical for all levels)

| Item | Value used |
|---|---|
| Tutor speech | 130 words/min including natural pauses; slide narration = 80% of visible slide words; closing/look-back/hook SAY lines counted word by word |
| Read-aloud of questions | 120 words/min (puzzles, quick questions, explore and talk questions, exit ticket; try-it slides 55% of slide words) |
| Group question | 10 s wait + 20 s for one or two answers = 30 s; a teaching slide with an 'Ask' or a question in its notes gets one question, a 'Step n' click gets a 10 s pause |
| Hold-up moment (boards, papers to camera) | 30 s; a whiteboard try-it slide = 60 s work + 30 s hold-up + 15 s feedback |
| Slide change online | 20 / **25** / 30 s (low / central / high); every slide actually shown is counted |
| Room moves, materials | 60 / **90** / 120 s per move to or from breakout rooms; 60 / **75** / 120 s to find materials; 2 min to start a worksheet; talk-time partner-talk round trip 40 / **60** / 90 s |
| REC cue | 10 s at the start of each of the 8 guide parts (the guide has no REC lines yet; see section 4) |
| Group | 8 children (the guide's maximum): 3 s each to greet, 6 s each to glance at an exit ticket, 8 certificates in L10 |
| Activity time | Explore: pair-task minutes judged from the task (6 to 10 min; L10 two 7-minute stations); worksheet: minutes per item judged from the actual workbook text (table below); brain break 2 min movement + 2.5 min water, toilet and settling; game play 3 min; exit work 3 to 3.5 min plus a full 2-minute look-back |
| Activity speed | low / **1.00** / high = x0.85 / x1.0 / x1.2 on the MID-child minutes; LOW child = 1.7 x MID, HIGH child = 0.6 x MID |
| Worksheet geometry | Pairs go to breakout rooms for page 1 (two moves) and to the Explore rooms; page 2 is alone in the main room; 'if time' items (marked in the workbook) are not counted as compulsory |
| Flags (need minus scripted) | OVER >= +2.0; TIGHT +0.75 to +2.0; OK in between; LOOSE <= -3.0 (dead time) |

Sensitivity: if pairs did the worksheet in the main room (no rooms) the worksheet shrinks by 3 min and L1-L9 totals by about 3; if the group is 6, not 8, subtract about 1 min (greeting, ticket scanning). Neither erases the overrun in the central set. Group chat, tech glitches and children who need a repeat are ignored, so real lessons are likelier to run above the estimate than below it.

Workbook minutes per item for a MID child aged 8-10 (core items are multi-part, so 2 to 4.5 min each; Think harder and Go further are 4-6 min each and are not in the timetable; 'if time' items are marked *):

| L | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
|---|---|---|---|---|---|---|
| 1 | 2.5 | 3.5 | 2.5 | 2.5 | 3 | 4* |
| 2 | 3 | 4 | 3 | 3 | 2.5 | 4.5* |
| 3 | 2.5 | 3 | 2 | 4.5* | 4 | 4.5* |
| 4 | 2.5 | 3 | 3 | 3.5 | 3.5 | 3 |
| 5 | 2.5 | 3 | 2 | 3.5 | 3 | 5* |
| 6 | 3.5 | 4 | 2 | 3.5 | 2.5 | 2 |
| 7 | 4 | 4 | 2 | 4 | 3.5 | 3.5* |
| 8 | 3.5 | 3 | 4.5 | 3.5 | 3.5 | 3 |
| 9 | 4 | 2.5 | 2 | 3.5* | 4.5 | 4.5* |
| 10 | 4 | 4.5 | 2.5 | 3 | 3 | 4.5* |

## 4. Things in the guide, decks and workbook that make the clock harder (found while walking through)

- The worksheet slide times do not include the 2-minute start or the room moves: slide ws1 reads '42-52' (L1) or '43-52' (L8) and has to hold both.
- Guide: 'At about minute 52, check in with two or three children for two minutes each' (4-6 tutor minutes) sits on top of the 52-54 'check page 1 together' slide.
- Slides teachmagic (L2) and teachbetween (L10) are labelled 'before worksheet page 2 (Q3)' but Q3 is a page-1 question, so they arrive after the pairs have done it.
- Four optional slides (stretch, challenge, chdiag, chwalk) are all labelled 67-70 (3 min); the workbook Think harder items are 4-6 min each, so the 3-minute 'choose' window cannot contain even one for most children. It works only as an invitation to continue at home.
- L10 Explore: 'two stations, 7 minutes each' (14 min) plus 'at about minute 15 bring the group back together' cannot both be true.
- L3 and L8: the first item on page 2 is an 'if time' item (L3 Q4) or the compulsory work is 10 min for a 7.5-min window (L8); L4 page 2 is three full modelling problems for 6.5 min.
- The look-back is scripted as 2 minutes, which is only the time the children get; the slide change, the 87 words of SAY, one volunteer share and a stuck check-in add about 1.8 min, so the block is about 3.8 min.
- REC: `p3/guide.js` currently says 'Do not record lessons (this is in the tutor agreement)'. If a REC cue is added to the script the recording policy and the tutor agreement need to agree, or the cue should be reworded.
- The decks are not wrong in total slide count; the cost is that every slide change is a waiting moment online.

## 5. Lesson by lesson

### Lesson 1: Number Sleuths

Estimated 98.7 min against 90 (+8.7; range 90.4 to 109.3). 29 slides, 315 SAY words in the script, about 1209 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.4 | 0.4 | 0.0 | 0.0 | 0.17 | **1.0** | -1.0 | OK | 1.0-1.0 |
| Sneak-peek + game + quick Qs | 8 | 1.3 | 4.1 | 5.0 | 1.2 | 0.17 | **11.8** | +3.8 | OVER | 11.6-12.1 |
| Explore | 15 | 0.7 | 2.5 | 6.0 | 5.1 | 0.17 | **14.4** | -0.6 | OK | 12.1-17.5 |
| Mini-lesson | 10 | 2.4 | 3.8 | 2.0 | 2.5 | 0.17 | **10.8** | +0.8 | TIGHT | 10.3-11.3 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.3-5.5 |
| Worksheet | 30 | 2.8 | 7.8 | 19.5 | 7.6 | 0.17 | **37.9** | +7.9 | OVER | 34.0-42.4 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.9** | -3.1 | LOOSE | 6.5-7.5 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.0 | 2.2 | 0.17 | **10.6** | +0.6 | OK | 9.7-12.0 |
| **Lesson total** | 90 | 9.7 | 23.1 | 44.0 | 20.5 | 1.33 | **98.7** | +8.7 | OVER | 90.4-109.3 |

Worksheet block detail (central, minutes): teaching slides before page 1 1.9; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 8.9; check page 1 2.6; teaching slides before page 2 6.9; page 2 alone 6.4; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 10 min on the slide, of which about 5.0 min is real work after the 2-minute start and two room moves; page 2 = 7 min, about 6.5 min of work. MID child needs 8.5 min for Q1-Q3 and 5.5 min for the compulsory part of Q4-Q6 (9.5 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 1.1 + 1.4; MID 1.7 + 2.2; HIGH 2.9 + 3.0. The core pages hold about 25 answer boxes.

**Where the time goes**

- Warm-up block OVER: the two sneak-peek puzzles cost about 4 min (two 1-minute tries, two hold-ups), the Biggest-number game 3.8 min and five quick questions 3.2 min.
- Worksheet OVER (the biggest sink): slide ws1 (42-52) must hold the 2-minute start, two room moves and Q1-Q3, which leaves about 5 min of real work against the 8.5 min a MID child needs (Q2 lists 9 numbers with a repeated 5). The four teaching slides between the pages (teachrename 67 words, teachclues 83, tryclues 41, teachsum 67) need 6.9 min against the 4 scripted, and the two 'check together' slides need 2.6 min each against 2.
- Talk time LOOSE: one discussion question (0357) plus the 'how do you know all the numbers' follow-up and puzzle 2 fill about 7 of the 10 minutes.

**Fixes (no change to answers, tiers or the pass option)**

- Slide warm2 (8-10): ask only Q1-Q3 (value of the 7 in 4719; 3000 + 40 + 5; 1 more than 4999). Move Q4 (100 less than 6050) and Q5 (7089 or 7098) to the take-home page. Slide warm1: play two rounds (biggest, then smallest), no third round. Sneak-peek: one 'show me' for both puzzles.
- Delete slides tryclues (56-57) and teachsum (57-58). Q6 is already 'if time', so teachsum only serves the optional item; keep its content in the notes of the Go further slides and show it to anyone who chooses Q6. Keep teachrename and teachclues.
- Give page 1 about 13 min on the slide (2-minute start, 1.5 min of rooms, 9 min of Q1-Q3; it is 10 now) and turn both 'check together' slides into 60-second self-checks (children hold up the corrected page; ask 'how do you know' on one question only).
- Use pre-assigned breakout rooms with auto-move and auto-close, so each move is about 45 s, not 90 s.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 1.0 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.8 | 9.2 | **9.5** | 1.5-11 |
| Explore | 15 | 14.4 | 12.9 | **13** | 11-24 |
| Mini-lesson | 10 | 10.8 | 10.8 | **11** | 24-35 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 35-40 |
| Worksheet | 30 | 37.9 | 30.7 | **31** | 40-71 |
| Talk time | 10 | 6.9 | 6.4 | **8** | 71-79 |
| Exit + look-back + close | 10 | 10.6 | 10.6 | **11** | 79-90 |
| **Total** | 90 | 98.7 | 86.9 | **90** | built-in float 3.1 min (after-fix range 80.0-96.1) |

Worksheet 31 min = teach before p1 2 + start + rooms 3.5 + page 1 pairs 9.5 + check p1 1.5 + teach before p2 3.5 + page 2 alone 6.5 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 8.5 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 2: Cryptarithm Crackers

Estimated 101.8 min against 90 (+11.8; range 93.1 to 113.0). 28 slides, 289 SAY words in the script, about 1190 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.4 | 0.4 | 0.0 | 0.0 | 0.17 | **1.0** | -1.0 | OK | 1.0-1.0 |
| Sneak-peek + game + quick Qs | 8 | 1.2 | 4.1 | 5.0 | 1.2 | 0.17 | **11.7** | +3.7 | OVER | 11.5-12.0 |
| Explore | 15 | 0.8 | 2.5 | 8.0 | 5.1 | 0.17 | **16.6** | +1.6 | TIGHT | 14.0-20.1 |
| Mini-lesson | 10 | 2.5 | 3.8 | 2.0 | 2.5 | 0.17 | **11.0** | +1.0 | TIGHT | 10.5-11.5 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.3-5.5 |
| Worksheet | 30 | 2.7 | 7.8 | 21.0 | 7.2 | 0.17 | **38.9** | +8.9 | OVER | 34.9-43.7 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.8** | -3.2 | LOOSE | 6.4-7.4 |
| Exit + look-back + close | 10 | 0.9 | 2.1 | 5.0 | 2.2 | 0.17 | **10.5** | +0.5 | OK | 9.6-11.9 |
| **Lesson total** | 90 | 9.6 | 23.3 | 47.5 | 20.1 | 1.33 | **101.8** | +11.8 | OVER | 93.1-113.0 |

Worksheet block detail (central, minutes): teaching slides before page 1 0.0; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 10.4; check page 1 2.6; teaching slides before page 2 8.4; page 2 alone 6.4; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 12 min on the slide, of which about 7.0 min is real work after the 2-minute start and two room moves; page 2 = 7 min, about 6.5 min of work. MID child needs 10.0 min for Q1-Q3 and 5.5 min for the compulsory part of Q4-Q6 (10.0 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 1.3 + 1.3; MID 2.0 + 2.2; HIGH 3.0 + 3.0. The core pages hold about 15 answer boxes.

**Where the time goes**

- Warm-up block OVER (+3.7): same structure as every lesson.
- Explore TIGHT: four instructions on the explore slide (cards 1-9, make a 3-digit sum, check by adding, 'find more, what is always true?') need about 8 min of pair work.
- Worksheet OVER (+8.9): Q2 has three tasks including 'make the difference as small as possible, guess, check, improve' (MID 4 min); Q1 + Q2 + Q3 need 10 min but only about 7 are available after the start and room moves. Four teaching slides between the pages need 8.4 min (teachmagic 83 words, teachpyr 67, teach999 63, teachshape 90). Slide teachmagic is labelled 'before page 2 (Q3)' but Q3 (magic square) is page 1 and the pairs have already done it by minute 54.
- Mini-lesson TIGHT (+1.0): six slides including two whiteboard try-its. Talk time LOOSE (-3.2).

**Fixes (no change to answers, tiers or the pass option)**

- Explore: move the 4th instruction ('Find more. What is always true?') to the Go further card; pairs need about 6.5 min. Group question 3 (add the digits of the answer) stays as the debrief.
- Q2(c) (smallest difference with 3-digit numbers, guess-check-improve) moves to take-home or Think harder; it is the hardest Core part and the idea is taught on slide teach3 with 2-digit numbers. Q2(a),(b) stay.
- Show teachmagic at minute 40 as the pre-page-1 slide (Q3 is on page 1), not at 54. Delete teachshape (Q6 letter puzzle is 'if time'). Drop the second try-it slide in the mini-lesson (try2, 33-34); keep try1, which practises Q1.
- Warm-up and checks as in the level-wide pack: three quick questions (3456 + 1000; 5000 - 1; 2700 + 300), 60-second self-checks, pre-assigned rooms.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 1.0 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.7 | 9.2 | **9.5** | 1.5-11 |
| Explore | 15 | 16.6 | 13.6 | **14** | 11-25 |
| Mini-lesson | 10 | 11.0 | 8.5 | **9** | 25-34 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 34-39 |
| Worksheet | 30 | 38.9 | 31.9 | **32** | 39-71 |
| Talk time | 10 | 6.8 | 6.3 | **8** | 71-79 |
| Exit + look-back + close | 10 | 10.5 | 10.5 | **11** | 79-90 |
| **Total** | 90 | 101.8 | 86.3 | **90** | built-in float 3.7 min (after-fix range 79.3-95.4) |

Worksheet 32 min = start + rooms 3.5 + page 1 pairs 9.5 + check p1 1.5 + teach before p2 6.5 + page 2 alone 6.5 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 8.5 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 3: Times Table Treasure

Estimated 98.7 min against 90 (+8.7; range 90.4 to 109.3). 28 slides, 371 SAY words in the script, about 1367 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.5 | 0.4 | 0.0 | 0.0 | 0.17 | **1.1** | -0.9 | OK | 1.1-1.1 |
| Sneak-peek + game + quick Qs | 8 | 1.5 | 3.6 | 5.0 | 1.2 | 0.17 | **11.5** | +3.5 | OVER | 11.3-11.8 |
| Explore | 15 | 1.3 | 2.5 | 9.0 | 5.1 | 0.17 | **18.0** | +3.0 | OVER | 15.3-21.8 |
| Mini-lesson | 10 | 3.0 | 5.0 | 2.0 | 2.9 | 0.17 | **13.1** | +3.1 | OVER | 12.5-13.6 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.3-5.5 |
| Worksheet | 30 | 2.6 | 6.7 | 16.0 | 6.8 | 0.17 | **32.2** | +2.2 | OVER | 28.9-36.1 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.9** | -3.1 | LOOSE | 6.5-7.5 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.0 | 2.2 | 0.17 | **10.5** | +0.5 | OK | 9.6-12.0 |
| **Lesson total** | 90 | 11.0 | 22.8 | 43.5 | 20.1 | 1.33 | **98.7** | +8.7 | OVER | 90.4-109.3 |

Worksheet block detail (central, minutes): teaching slides before page 1 0.0; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 7.9; check page 1 2.7; teaching slides before page 2 5.6; page 2 alone 4.9; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 12 min on the slide, of which about 7.0 min is real work after the 2-minute start and two room moves; page 2 = 7 min, about 6.5 min of work. MID child needs 7.5 min for Q1-Q3 and 4.0 min for the compulsory part of Q4-Q6 (13.0 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 1.5 + 0.8; MID 2.8 + 1.5; HIGH 3.0 + 2.5. The core pages hold about 17 answer boxes.

**Where the time goes**

- Warm-up block OVER (+3.5). The script is the wordiest in the level: predict is 59 words and warmIntro 70 words (about 25 s each to say), and the slide text is the largest (1 899 words on slides against a level mean of 1 720).
- Explore OVER (+3.0): the circle-clock task has four steps (10 dots, the 6 times table, join the last digits, then the 4s and 8s and compare); MID pair needs about 9 min of drawing and joining.
- Mini-lesson OVER (+3.1): 7 slides in 10 min (teach1, we1, try1, teach2, we2, try2, key; 103, 86, 41, 80, 86, 42 words) with two whiteboard try-its.
- Worksheet OVER (+2.2) although page 2 is the lightest in the level: Q4 and Q6 are 'if time' and only Q5 is compulsory, yet three teaching slides (teachlist 79, teachgrid 106 words, the second-longest teaching slide in the level, and teachboth 92) take 5.6 min. Q4 (4.5 min, 'if time') comes first on the page and Q5 (4 min, compulsory) second, so a MID child cannot do both in the 6.5-min window: the order of the optional and compulsory items fights the clock.
- Talk time LOOSE (-3.1).

**Fixes (no change to answers, tiers or the pass option)**

- Predict SAY: cut to about 35 words ('I write the 6 times table and look only at the last digit: 6, 2, 8. If I join the dots in order, what shape? Will it ever touch an odd digit?'). warmIntro: drop the 'if anyone misses one, that is fine' sentence.
- Explore: tutor does the 6 times table with the class on the shared screen; pairs make ONE more circle (the 4s); the 8s and the comparison go to Go further / take-home. Pair work about 6.5 min.
- Mini-lesson: merge we1 (last digit of 8 x 23) into try1, or equivalently we2 into try2, so there are 6 slides, not 7.
- Worksheet: keep all three teaching slides (there is spare time), show teachgrid (Q4) only to children who start Q4, and use the spare 1.5 min for a longer page 2 so that LOW and MID children can reach Q5 without hurry.
- Quick questions: first three (6 x 7, 9 x 9, 8 x ? = 64); move 'Which is bigger, 6 x 8 or 7 x 7?' to talk time.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.1 | 1.1 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.5 | 9.4 | **9.5** | 1.5-11 |
| Explore | 15 | 18.0 | 14.0 | **14.5** | 11-25.5 |
| Mini-lesson | 10 | 13.1 | 10.9 | **11** | 25.5-36.5 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 36.5-41.5 |
| Worksheet | 30 | 32.2 | 28.7 | **29** | 41.5-70.5 |
| Talk time | 10 | 6.9 | 6.4 | **8** | 70.5-78.5 |
| Exit + look-back + close | 10 | 10.5 | 10.5 | **11.5** | 78.5-90 |
| **Total** | 90 | 98.7 | 86.5 | **90** | built-in float 3.5 min (after-fix range 79.8-95.2) |

Worksheet 29 min = start + rooms 3.5 + page 1 pairs 9 + check p1 1.5 + teach before p2 5.5 + page 2 alone 5 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 7.5 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 4: Model Makers

Estimated 104.2 min against 90 (+14.2; range 95.1 to 115.9). 28 slides, 304 SAY words in the script, about 1168 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.4 | 0.4 | 0.0 | 0.0 | 0.17 | **1.0** | -1.0 | OK | 1.0-1.0 |
| Sneak-peek + game + quick Qs | 8 | 1.4 | 4.1 | 5.0 | 1.2 | 0.17 | **11.9** | +3.9 | OVER | 11.6-12.1 |
| Explore | 15 | 1.1 | 2.5 | 7.0 | 5.1 | 0.17 | **15.8** | +0.8 | TIGHT | 13.4-19.1 |
| Mini-lesson | 10 | 1.7 | 3.0 | 2.2 | 2.1 | 0.17 | **9.2** | -0.8 | OK | 8.8-9.6 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.3-5.5 |
| Worksheet | 30 | 2.8 | 8.4 | 24.0 | 7.6 | 0.17 | **43.0** | +13.0 | OVER | 38.4-48.4 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.9** | -3.1 | LOOSE | 6.5-7.5 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.5 | 2.2 | 0.17 | **11.1** | +1.1 | TIGHT | 10.1-12.6 |
| **Lesson total** | 90 | 9.5 | 23.0 | 50.2 | 20.1 | 1.33 | **104.2** | +14.2 | OVER | 95.1-115.9 |

Worksheet block detail (central, minutes): teaching slides before page 1 4.4; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 8.9; check page 1 2.6; teaching slides before page 2 5.2; page 2 alone 10.9; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 10 min on the slide, of which about 5.0 min is real work after the 2-minute start and two room moves; page 2 = 7 min, about 6.5 min of work. MID child needs 8.5 min for Q1-Q3 and 10.0 min for the compulsory part of Q4-Q6 (10.0 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 1.1 + 1.1; MID 1.8 + 1.9; HIGH 2.9 + 3.0. The core pages hold about 16 answer boxes.

**Where the time goes**

- Warm-up block OVER (+3.9).
- Explore TIGHT (+0.8): two tower tasks (4 more, then 3 times as tall) plus drawing the bars; 22-cubes question can wait.
- Worksheet OVER (+13.0) - the largest worksheet overrun in the level. Page 2 is three full modelling problems (Q4 total and difference, Q5 give to make equal, Q6 same difference) that need 10 min against a 6.5-min working window; before page 1 two slides (teachunits 72 words, tryunits 75 words) need 4.4 min against the 2 scripted (40-42).
- Exit ticket + look-back TIGHT (+1.1): the exit item needs a drawn model (3.5 min).
- Talk time LOOSE (-3.1).

**Fixes (no change to answers, tiers or the pass option)**

- Delete tryunits (41-42): Q3 is the try-it. Keep teachunits.
- Move Q6 (Grandma gives each $10) and the slide teachsame (57-58) to talk time: it becomes the whole-class discussion 'what stays the same?' (+1.5 min), and the Investigation 'What stays the same?' then builds on it. Q6 leaves the compulsory list but stays in the workbook (answers unchanged). Move Q5(b) (Ravi's mistake) to talk time as well.
- Page 2 working window becomes about 7.5 min for Q4 and Q5(a). Self-check slides at 60 s each.
- Explore: do the 'is 4 more' towers with the pairs; the 3-times towers become the first debrief question (class does it on the shared screen); '22 cubes?' moves to talk time. Pair work 6.5 min.
- Quick questions: first three (348 + 52; 1000 - 365; 3 units = 27).

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 1.0 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.9 | 9.2 | **9.5** | 1.5-11 |
| Explore | 15 | 15.8 | 13.8 | **14** | 11-25 |
| Mini-lesson | 10 | 9.2 | 9.2 | **9.5** | 25-34.5 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 34.5-39.5 |
| Worksheet | 30 | 43.0 | 31.8 | **32** | 39.5-71.5 |
| Talk time | 10 | 6.9 | 7.9 | **7.5** | 71.5-79 |
| Exit + look-back + close | 10 | 11.1 | 11.1 | **11** | 79-90 |
| **Total** | 90 | 104.2 | 89.3 | **90** | built-in float 0.7 min (after-fix range 82.1-98.7) |

Worksheet 32 min = teach before p1 2 + start + rooms 3.5 + page 1 pairs 9.5 + check p1 1.5 + teach before p2 3.5 + page 2 alone 7.5 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 8.5 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 5: Remainder Riddles

Estimated 97.3 min against 90 (+7.3; range 88.9 to 107.9). 28 slides, 296 SAY words in the script, about 1245 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.5 | 0.4 | 0.0 | 0.0 | 0.17 | **1.1** | -0.9 | OK | 1.1-1.1 |
| Sneak-peek + game + quick Qs | 8 | 1.3 | 4.1 | 5.0 | 1.2 | 0.17 | **11.8** | +3.8 | OVER | 11.5-12.0 |
| Explore | 15 | 0.8 | 2.5 | 7.0 | 5.1 | 0.17 | **15.6** | +0.6 | OK | 13.1-18.9 |
| Mini-lesson | 10 | 2.4 | 3.7 | 2.0 | 2.5 | 0.17 | **10.8** | +0.8 | TIGHT | 10.3-11.3 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.3-5.5 |
| Worksheet | 30 | 2.8 | 6.5 | 18.5 | 7.2 | 0.17 | **35.2** | +5.2 | OVER | 31.4-39.6 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.9** | -3.1 | LOOSE | 6.5-7.5 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.0 | 2.2 | 0.17 | **10.6** | +0.6 | OK | 9.7-12.0 |
| **Lesson total** | 90 | 10.0 | 21.8 | 44.0 | 20.1 | 1.33 | **97.3** | +7.3 | OVER | 88.9-107.9 |

Worksheet block detail (central, minutes): teaching slides before page 1 1.8; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 7.9; check page 1 2.6; teaching slides before page 2 4.4; page 2 alone 7.4; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 10 min on the slide, of which about 5.0 min is real work after the 2-minute start and two room moves; page 2 = 7 min, about 6.5 min of work. MID child needs 7.5 min for Q1-Q3 and 6.5 min for the compulsory part of Q4-Q6 (11.5 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 1.1 + 1.1; MID 1.8 + 2.0; HIGH 3.0 + 2.9. The core pages hold about 15 answer boxes.

**Where the time goes**

- Warm-up block OVER (+3.8).
- Worksheet OVER (+5.2): Q2 (four remainder stories, MID 3 min) and Q3, Q4 each add parts; three teaching slides before page 2 (teachlist 94 words, teachbig 95, teachtable 79) take 4.4 min against the 4 scripted, and the page-1 pair items need 7.9 min against about 5 available.
- Mini-lesson TIGHT (+0.8).
- Talk time LOOSE (-3.1).

**Fixes (no change to answers, tiers or the pass option)**

- Delete teachtable (57-58): it prepares Q6, the party tables, which is 'if time'.
- Quick questions: 17 / 5, 30 / 7, 45 / 6 only; 50 / 8 and 63 / 9 go to the take-home page.
- Self-check slides at 60 s; rooms pre-assigned. Keep Q3(b) and Q4(b) as 'if time' exactly as printed.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.1 | 1.1 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.8 | 9.2 | **9.5** | 1.5-11 |
| Explore | 15 | 15.6 | 14.1 | **14.5** | 11-25.5 |
| Mini-lesson | 10 | 10.8 | 10.8 | **11** | 25.5-36.5 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 36.5-41.5 |
| Worksheet | 30 | 35.2 | 30.8 | **31** | 41.5-72.5 |
| Talk time | 10 | 6.9 | 6.4 | **7** | 72.5-79.5 |
| Exit + look-back + close | 10 | 10.6 | 10.6 | **10.5** | 79.5-90 |
| **Total** | 90 | 97.3 | 88.3 | **90** | built-in float 1.7 min (after-fix range 81.2-97.6) |

Worksheet 31 min = teach before p1 2 + start + rooms 3.5 + page 1 pairs 8.5 + check p1 1.5 + teach before p2 3.5 + page 2 alone 7.5 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 7.5 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 6: Fraction Walls

Estimated 105.9 min against 90 (+15.9; range 96.5 to 117.8). 28 slides, 244 SAY words in the script, about 1101 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.5 | 0.4 | 0.0 | 0.0 | 0.17 | **1.0** | -1.0 | OK | 1.0-1.0 |
| Sneak-peek + game + quick Qs | 8 | 1.2 | 4.1 | 5.0 | 1.2 | 0.17 | **11.7** | +3.7 | OVER | 11.4-11.9 |
| Explore | 15 | 0.8 | 2.5 | 10.0 | 5.8 | 0.17 | **19.3** | +4.3 | OVER | 16.4-23.3 |
| Mini-lesson | 10 | 1.8 | 4.0 | 2.2 | 2.5 | 0.17 | **10.7** | +0.7 | OK | 10.2-11.2 |
| Brain break | 5 | 0.4 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.4-5.5 |
| Worksheet | 30 | 2.5 | 7.4 | 23.0 | 7.2 | 0.17 | **40.3** | +10.3 | OVER | 36.0-45.5 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.8** | -3.2 | LOOSE | 6.4-7.4 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.0 | 2.2 | 0.17 | **10.6** | +0.6 | OK | 9.7-12.0 |
| **Lesson total** | 90 | 8.9 | 23.0 | 51.7 | 20.8 | 1.33 | **105.9** | +15.9 | OVER | 96.5-117.8 |

Worksheet block detail (central, minutes): teaching slides before page 1 0.0; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 9.9; check page 1 2.6; teaching slides before page 2 7.6; page 2 alone 8.9; check page 2 2.8; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 12 min on the slide, of which about 7.0 min is real work after the 2-minute start and two room moves; page 2 = 7 min, about 6.5 min of work. MID child needs 9.5 min for Q1-Q3 and 8.0 min for the compulsory part of Q4-Q6 (8.0 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 1.2 + 1.1; MID 1.9 + 2.2; HIGH 3.0 + 3.0. The core pages hold about 35 answer boxes.

**Where the time goes**

- Warm-up block OVER (+3.7).
- Explore OVER (+4.3): the task is to make a fraction wall from 7 strips (fold or mark 2, 4, 8, 3, 6 and 12 equal parts, label, stack): about 10 min of cutting and folding plus about 2 min to find the strips.
- Worksheet OVER (+10.3): page 1 is the heaviest in the level, Q1 (12 blanks), Q2 (six comparisons plus an ordering of four fractions) and Q3 (five shapes) need 9.5 min but have about 7; page 2 (Q4 six sums, Q5, Q6 five pairs) is all compulsory, 8 min against a 6.5-min window. Teaching slides before page 2 (teachadd 82 words, tryadd 46, teachpairs 74, teachbetween 64) need 7.6 min against the 4 scripted.
- Talk time LOOSE (-3.2).

**Fixes (no change to answers, tiers or the pass option)**

- Explore: parents pre-cut the printed fraction-wall strips before the lesson (they are on the cut-out pages; add 'cut the strips out before class' to the one-week-before message). In class pairs only mark halves, quarters and eighths and then compare with the printed thirds, sixths and twelfths. Pair work about 6.5 min, no extra 45 s to find strips.
- Q1: do (a), (b) and (d) in class; (c) goes to take-home. Q6 (five partner cards) moves to take-home, so delete teachpairs (56-57), tryadd (55-56) and teachbetween (57-58, it only prepares Think harder 1; show it when a pair chooses Think harder).
- Page 2 working window is then Q4 + Q5 (6 min). Self-check slides at 60 s.
- Quick questions: first three (quarters in a whole; 1/3 or 1/5; 1/2 = ?/10); 2/9 + 4/9 and 1 - 2/5 go to take-home.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 1.0 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.7 | 9.1 | **9.5** | 1.5-11 |
| Explore | 15 | 19.3 | 13.6 | **14** | 11-25 |
| Mini-lesson | 10 | 10.7 | 10.7 | **11** | 25-36 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 36-41 |
| Worksheet | 30 | 40.3 | 28.1 | **30** | 41-71 |
| Talk time | 10 | 6.8 | 6.3 | **8** | 71-79 |
| Exit + look-back + close | 10 | 10.6 | 10.6 | **11** | 79-90 |
| **Total** | 90 | 105.9 | 84.8 | **90** | built-in float 5.2 min (after-fix range 77.9-94.0) |

Worksheet 30 min = start + rooms 3.5 + page 1 pairs 11 + check p1 1.5 + teach before p2 2 + page 2 alone 7 + check p2 2 + choose 3. (Page 1 work needed by a MID child: 8.5 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 7: Area Architects

Estimated 100.4 min against 90 (+10.4; range 91.6 to 111.7). 27 slides, 367 SAY words in the script, about 1278 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.6 | 0.4 | 0.0 | 0.0 | 0.17 | **1.2** | -0.8 | OK | 1.2-1.2 |
| Sneak-peek + game + quick Qs | 8 | 1.4 | 3.6 | 5.0 | 1.2 | 0.17 | **11.4** | +3.4 | OVER | 11.2-11.7 |
| Explore | 15 | 0.8 | 2.5 | 7.0 | 5.1 | 0.17 | **15.5** | +0.5 | OK | 13.1-18.9 |
| Mini-lesson | 10 | 3.3 | 5.0 | 2.0 | 2.9 | 0.17 | **13.4** | +3.4 | OVER | 12.8-14.0 |
| Brain break | 5 | 0.4 | 0.0 | 4.5 | 0.4 | 0.17 | **5.5** | +0.5 | OK | 5.4-5.6 |
| Worksheet | 30 | 1.9 | 5.5 | 22.0 | 6.3 | 0.17 | **35.9** | +5.9 | OVER | 31.8-40.9 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.9** | -3.1 | LOOSE | 6.5-7.5 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.0 | 2.2 | 0.17 | **10.6** | +0.6 | OK | 9.7-12.0 |
| **Lesson total** | 90 | 10.3 | 21.6 | 47.5 | 19.7 | 1.33 | **100.4** | +10.4 | OVER | 91.6-111.7 |

Worksheet block detail (central, minutes): teaching slides before page 1 2.0; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 10.4; check page 1 2.8; teaching slides before page 2 1.3; page 2 alone 8.4; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 11 min on the slide, of which about 6.0 min is real work after the 2-minute start and two room moves; page 2 = 9 min, about 8.5 min of work. MID child needs 10.0 min for Q1-Q3 and 7.5 min for the compulsory part of Q4-Q6 (11.0 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 0.9 + 1.3; MID 1.5 + 2.3; HIGH 3.0 + 3.0. The core pages hold about 31 answer boxes.

**Where the time goes**

- Warm-up block OVER (+3.4).
- Mini-lesson OVER (+3.4): 7 slides in 10 min and teach1 has 126 words, the longest slide in the level (same fence, different gardens), plus two whiteboard try-its (try1, try2).
- Worksheet OVER (+5.9): Q1 (area and perimeter of four figures, 10 boxes, MID 4 min) and Q2 (list every garden with 18 m of fence, MID 4 min) are the long pair items; page 2 fits (Q4 + Q5 need 7.5 min in an 8.5-min window) but page 1 does not (10 min of items against about 6 available) and the 2.8-min check of the 92-word answer slide is longer than the 2 scripted.
- Talk time LOOSE (-3.1).

**Fixes (no change to answers, tiers or the pass option)**

- Mini-lesson: merge we2 (staircase with no numbers) into try2 and trim teach1 to about 80 words (cut the restated steps; Q2 repeats them). Keep teach3 (area of an L-shape).
- Delete teachadd (54-56): it prepares Q6, which is 'if time'. Give page 1 about 14 min on the slide (it is 11 now): 2-minute start, 1.5 min of rooms, 10.4 min of Q1-Q3.
- Explore: 12 squares gives three rectangles (1 x 12, 2 x 6, 3 x 4); record in a 3-row table; pair work about 6 min.
- Quick questions: first three (8 x 7; perimeter of a 6 cm square; area of 8 cm by 3 cm); the square-root question (area 49) goes to take-home.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.2 | 1.2 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.4 | 9.3 | **9.5** | 1.5-11 |
| Explore | 15 | 15.5 | 13.0 | **13.5** | 11-24.5 |
| Mini-lesson | 10 | 13.4 | 11.7 | **11.5** | 24.5-36 |
| Brain break | 5 | 5.5 | 5.5 | **5** | 36-41 |
| Worksheet | 30 | 35.9 | 31.1 | **31** | 41-72 |
| Talk time | 10 | 6.9 | 6.4 | **7** | 72-79 |
| Exit + look-back + close | 10 | 10.6 | 10.6 | **11** | 79-90 |
| **Total** | 90 | 100.4 | 88.9 | **90** | built-in float 1.1 min (after-fix range 81.5-98.5) |

Worksheet 31 min = teach before p1 2 + start + rooms 3.5 + page 1 pairs 10.5 + check p1 2 + page 2 alone 8.5 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 10.0 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 8: Angle and Line Detectives

Estimated 102.9 min against 90 (+12.9; range 93.5 to 114.8). 27 slides, 333 SAY words in the script, about 1178 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.6 | 0.4 | 0.0 | 0.0 | 0.17 | **1.2** | -0.8 | OK | 1.2-1.2 |
| Sneak-peek + game + quick Qs | 8 | 1.4 | 3.1 | 5.0 | 1.2 | 0.17 | **10.9** | +2.9 | OVER | 10.6-11.1 |
| Explore | 15 | 0.9 | 2.5 | 7.0 | 5.1 | 0.17 | **15.7** | +0.7 | OK | 13.2-19.0 |
| Mini-lesson | 10 | 2.4 | 4.4 | 1.0 | 2.5 | 0.17 | **10.5** | +0.5 | OK | 10.0-11.0 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.3-5.5 |
| Worksheet | 30 | 1.8 | 6.2 | 26.5 | 6.8 | 0.17 | **41.6** | +11.6 | OVER | 36.8-47.3 |
| Talk time | 10 | 1.1 | 2.5 | 2.0 | 1.4 | 0.17 | **7.2** | -2.8 | OK | 6.7-7.7 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.0 | 2.2 | 0.17 | **10.6** | +0.6 | OK | 9.7-12.0 |
| **Lesson total** | 90 | 9.5 | 21.3 | 51.0 | 19.7 | 1.33 | **102.9** | +12.9 | OVER | 93.5-114.8 |

Worksheet block detail (central, minutes): teaching slides before page 1 4.2; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 11.4; check page 1 2.6; teaching slides before page 2 1.4; page 2 alone 10.9; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 9 min on the slide, of which about 4.0 min is real work after the 2-minute start and two room moves; page 2 = 8 min, about 7.5 min of work. MID child needs 11.0 min for Q1-Q3 and 10.0 min for the compulsory part of Q4-Q6 (10.0 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 0.7 + 1.3; MID 1.2 + 2.2; HIGH 2.0 + 3.0. The core pages hold about 30 answer boxes.

**Where the time goes**

- Warm-up block OVER (+2.9).
- Worksheet OVER (+11.6) - the worst page-1 squeeze: ws1 is only 43-52 (9 min), the two teaching slides before it (we1, try1) use 40-43, and the work window after the 2-minute start and room moves is about 4 min for Q1 (fold a right-angle checker and sort six angles, MID 3.5 min), Q2 and Q3 (count the angles made by six lines, MID 4.5 min), which need 11 min. A MID child finishes about 1 of 3. Page 2 (Q4 twelve yes/no answers, Q5 ruler drawing, Q6 window) needs 10 min against 7.5.
- Talk time OK (-2.8).

**Fixes (no change to answers, tiers or the pass option)**

- Q3(b) (8 lines, look for a pattern) and its try-it slide try1 (42-43) go to take-home / Think harder together; the pattern is also in the Investigation.
- Q4: four letters (E, H, T, L), not six (drop Z and N); the (b) part about E stays. Q6 (window) becomes 'if time'.
- Fold the right-angle checker during Explore (it is the Explore task) so that Q1 only has to sort; say so on slide ws1.
- Explore: fold twice and hunt for angles, 6 min of pair work. Quick questions: first three (right angles in a rectangle; sides of a hexagon; a capital letter with a right angle).

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.2 | 1.2 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 10.9 | 8.8 | **9** | 1.5-10.5 |
| Explore | 15 | 15.7 | 13.2 | **13.5** | 10.5-24 |
| Mini-lesson | 10 | 10.5 | 10.5 | **10.5** | 24-34.5 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 34.5-39.5 |
| Worksheet | 30 | 41.6 | 30.6 | **31** | 39.5-70.5 |
| Talk time | 10 | 7.2 | 6.7 | **8** | 70.5-78.5 |
| Exit + look-back + close | 10 | 10.6 | 10.6 | **11.5** | 78.5-90 |
| **Total** | 90 | 102.9 | 86.9 | **90** | built-in float 3.1 min (after-fix range 79.7-96.3) |

Worksheet 31 min = teach before p1 1.5 + start + rooms 3.5 + page 1 pairs 11.5 + check p1 1.5 + teach before p2 1.5 + page 2 alone 7 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 10.0 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 9: Measure and Money Masters

Estimated 94.8 min against 90 (+4.8; range 86.4 to 105.6). 26 slides, 363 SAY words in the script, about 1159 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.6 | 0.4 | 0.0 | 0.0 | 0.17 | **1.1** | -0.9 | OK | 1.1-1.1 |
| Sneak-peek + game + quick Qs | 8 | 1.3 | 3.6 | 5.0 | 1.2 | 0.17 | **11.3** | +3.3 | OVER | 11.0-11.5 |
| Explore | 15 | 1.0 | 2.5 | 9.0 | 5.1 | 0.17 | **17.8** | +2.8 | OVER | 15.0-21.5 |
| Mini-lesson | 10 | 1.8 | 2.2 | 1.8 | 1.7 | 0.17 | **7.6** | -2.4 | OK | 7.3-8.0 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.4** | +0.4 | OK | 5.3-5.5 |
| Worksheet | 30 | 2.5 | 6.2 | 17.5 | 7.2 | 0.17 | **33.5** | +3.5 | OVER | 29.9-37.8 |
| Talk time | 10 | 1.0 | 2.5 | 2.0 | 1.4 | 0.17 | **7.0** | -3.0 | OK | 6.6-7.6 |
| Exit + look-back + close | 10 | 1.0 | 2.1 | 5.5 | 2.2 | 0.17 | **11.1** | +1.1 | TIGHT | 10.1-12.6 |
| **Lesson total** | 90 | 9.4 | 19.5 | 45.3 | 19.2 | 1.33 | **94.8** | +4.8 | OVER | 86.4-105.6 |

Worksheet block detail (central, minutes): teaching slides before page 1 1.5; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 8.9; check page 1 2.7; teaching slides before page 2 4.0; page 2 alone 5.4; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 10 min on the slide, of which about 5.0 min is real work after the 2-minute start and two room moves; page 2 = 8 min, about 7.5 min of work. MID child needs 8.5 min for Q1-Q3 and 4.5 min for the compulsory part of Q4-Q6 (12.5 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 0.7 + 1.2; MID 1.4 + 1.9; HIGH 2.9 + 3.0. The core pages hold about 22 answer boxes.

**Where the time goes**

- Warm-up block OVER (+3.3).
- Explore OVER (+2.8): party planning with $20, a menu priced to the cent, a 2-litre punch constraint and 'spend as close as you can' is a long add-up (MID pair 9 min).
- Worksheet OVER (+3.5), the lightest overrun in the level: Q1 (six conversions) and Q5 (three time-line parts) are the long items; Q4 and Q6 are 'if time'.
- Mini-lesson is nearly LOOSE (-2.4): only 4 slides, three of them labelled 3 minutes (teach1 25-28, we1 28-31, try1 31-34) but needing about 2 each. This is the one lesson with spare time to give back.
- Exit ticket + look-back TIGHT (+1.1; the exit item has a money/time calculation). Talk time OK (-3.0 by a hair).

**Fixes (no change to answers, tiers or the pass option)**

- Explore: keep two constraints (at least 2 l of punch, at least one food) and 'spend as close to $20 as you can'; remove 'Go further: spend exactly $20' from the pair task (it stays on the slide as the extension) so the pair work is about 7 min.
- Delete teach24 (56-57): the 24-hour clock is Q4, which is 'if time'. Shorten the three mini-lesson slides to 2-3-3 min and give 1.5 min back to Explore.
- Use the spare budget (about 7 min of float) for a fuller page 1 and a real talk time; this is the only lesson that can keep five quick questions.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.1 | 1.1 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.3 | 8.6 | **9** | 1.5-10.5 |
| Explore | 15 | 17.8 | 14.3 | **15** | 10.5-25.5 |
| Mini-lesson | 10 | 7.6 | 7.6 | **8.5** | 25.5-34 |
| Brain break | 5 | 5.4 | 5.4 | **5** | 34-39 |
| Worksheet | 30 | 33.5 | 28.2 | **31** | 39-70 |
| Talk time | 10 | 7.0 | 6.5 | **8.5** | 70-78.5 |
| Exit + look-back + close | 10 | 11.1 | 11.1 | **11.5** | 78.5-90 |
| **Total** | 90 | 94.8 | 82.9 | **90** | built-in float 7.1 min (after-fix range 76.0-92.0) |

Worksheet 31 min = teach before p1 1.5 + start + rooms 3.5 + page 1 pairs 12 + check p1 1.5 + teach before p2 2.5 + page 2 alone 5.5 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 8.5 min, plus 2 min start and 1.5 min of rooms.)

### Lesson 10: Challenge Day

Estimated 111.6 min against 90 (+21.6; range 101.5 to 124.5). 29 slides, 307 SAY words in the script, about 1191 spoken and read-aloud words in the model. Speak / Wait / Activity / Transit / REC are minutes.

| Part | Scripted | Speak | Wait | Activity | Transit | REC | **Need** | Diff | Flag | Range (low-high) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 0.5 | 0.4 | 0.0 | 0.0 | 0.17 | **1.1** | -0.9 | OK | 1.1-1.1 |
| Sneak-peek + game + quick Qs | 8 | 1.3 | 3.6 | 5.0 | 1.2 | 0.17 | **11.3** | +3.3 | OVER | 11.1-11.6 |
| Explore | 15 | 1.0 | 2.5 | 15.0 | 5.1 | 0.17 | **23.8** | +8.8 | OVER | 20.1-28.7 |
| Mini-lesson | 10 | 2.6 | 3.3 | 2.0 | 2.9 | 0.17 | **11.0** | +1.0 | TIGHT | 10.5-11.6 |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 0.17 | **5.3** | +0.3 | OK | 5.3-5.4 |
| Worksheet | 30 | 2.0 | 5.5 | 21.5 | 6.8 | 0.17 | **35.9** | +5.9 | OVER | 31.8-40.9 |
| Talk time | 10 | 0.8 | 2.5 | 2.0 | 1.4 | 0.17 | **6.8** | -3.2 | LOOSE | 6.4-7.4 |
| Exit + look-back + close | 10 | 1.2 | 2.1 | 10.5 | 2.2 | 0.17 | **16.2** | +6.2 | OVER | 15.2-17.8 |
| **Lesson total** | 90 | 9.7 | 19.9 | 60.5 | 20.1 | 1.33 | **111.6** | +21.6 | OVER | 101.5-124.5 |

Worksheet block detail (central, minutes): teaching slides before page 1 0.0; hand out + get started (2 min) 2.2; breakout in + out 3.0; page 1 pairs work (Q1-Q3) 11.4; check page 1 2.5; teaching slides before page 2 4.1; page 2 alone 6.9; check page 2 2.6; choose Think harder / Go further (3 min) 3.0.

Worksheet window as scripted: page 1 = 12 min on the slide, of which about 7.0 min is real work after the 2-minute start and two room moves; page 2 = 7 min, about 6.5 min of work. MID child needs 11.0 min for Q1-Q3 and 6.0 min for the compulsory part of Q4-Q6 (10.5 with the 'if time' items). Items finished inside the scripted windows (page 1 of 3 + page 2 of 3, 'if time' items counted): LOW 1.0 + 1.3; MID 1.7 + 2.1; HIGH 3.0 + 3.0. The core pages hold about 16 answer boxes.

**Where the time goes**

- Explore OVER (+8.8) - the largest overrun of any part outside the worksheet. The slide and the guide say 'two stations, 7 minutes each' (14 min) inside a block that also needs a 2-min prediction, rooms in and out, a station switch and a 3-question debrief. The guide also says 'at about minute 15 bring the group back', which contradicts the second station.
- Exit ticket + look-back + close OVER (+6.2): the guide gives the close 2 minutes (88-90) but it has to cover 8 certificates with one specific thing said to each child (8 x 30 s = 4 min), volunteers naming a puzzle they enjoyed (end-slide notes) and the parent summary.
- Worksheet OVER (+5.9): Q2 (logic grid, 4 children x 4 CCAs, MID 4.5 min) and Q1 (bar graph, draw a bar) are long, and the three teaching slides between the pages (teachlist 96 words, teachtable 60, teachbetween 57) repeat what the mini-lesson already teaches (queues, logic grid, bar graph); slide teachbetween is labelled 'before page 2 (Q3)' but Q3 is on page 1.
- Mini-lesson TIGHT (+1.0): 7 slides including three worked examples. Talk time LOOSE (-3.2).
- Total +21.6 central; even the low set gives 101.5 min. This lesson needs a rewrite of its shape, not trimming.

**Fixes (no change to answers, tiers or the pass option)**

- Explore: each station 4 min, not 7 (the List station has 6 numbers and the ribbon answers are 30, 40 and 50 cm), switch with a timer on the slide, debrief question 1 only plus the two answers. Pair work 9 min including the switch.
- Replace the three page-2 teaching slides with ONE 'recap: draw it, list it, make a table' slide (reuse teachlist); delete teachtable and teachbetween.
- Certificates: say them in one 20-second sentence each (8 x 20 s = 2.7 min); ask for volunteers on 'a puzzle I enjoyed' once; post the parent summary after the lesson.
- Exit ticket: the queue question (4th from front, 4th from back) is the easiest item of the lesson; allow 2 min, not 3.5.
- Warm-up and checks as in the level-wide pack: first three quick questions (value of the 7 in 4732; 3/8 + 2/8; 47 / 5), 60-second self-checks, pre-assigned rooms.

**New budget (sums to 90)**

| Part | Now (scripted) | Need before fix | Need after fix | **New budget** | New clock |
|---|---:|---:|---:|---:|---|
| Opening | 2 | 1.1 | 1.1 | **1.5** | 0-1.5 |
| Sneak-peek + game + quick Qs | 8 | 11.3 | 8.7 | **9** | 1.5-10.5 |
| Explore | 15 | 23.8 | 16.3 | **16.5** | 10.5-27 |
| Mini-lesson | 10 | 11.0 | 9.2 | **9.5** | 27-36.5 |
| Brain break | 5 | 5.3 | 5.3 | **5** | 36.5-41.5 |
| Worksheet | 30 | 35.9 | 29.4 | **29.5** | 41.5-71 |
| Talk time | 10 | 6.8 | 6.3 | **6** | 71-77 |
| Exit + look-back + close | 10 | 16.2 | 12.9 | **13** | 77-90 |
| **Total** | 90 | 111.6 | 89.2 | **90** | built-in float 0.8 min (after-fix range 81.6-99.2) |

Worksheet 29.5 min = start + rooms 3.5 + page 1 pairs 12 + check p1 1.5 + teach before p2 1 + page 2 alone 7 + check p2 1.5 + choose 3. (Page 1 work needed by a MID child: 11.0 min, plus 2 min start and 1.5 min of rooms.)

## 6. Level-wide fix pack and standing buffer

Changes that apply to every lesson (each keeps all answers, the Core / Think harder / Challenge tiers and the pass and no-pressure rules; the sneak-peek puzzles, look-back, certificates and REC cues all stay):

1. **Warm-up (2-10) budget 8 to 9-9.5.** Keep both sneak-peek puzzles but use one camera hold-up for both; play the game as two rounds (2 min); ask the first three quick questions and put the rest on the take-home page. Need falls from 11-12 to 8.6-9.4.
2. **Pre-assign breakout rooms and use auto-move and auto-close with a timer** so each room move takes about 45 s, not 90 s. Four moves a lesson: saves about 3 min and costs no content. Send a 'what is on your desk' checklist with the one-week-before message so materials are found in the 75 s allowed.
3. **Worksheet: give the slide the minutes it really uses and stop teaching for optional items.** Page 1 slide time = 2-minute start + room moves + items. Delete teaching slides that only serve an 'if time' item (L1 teachsum, L2 teachshape, L5 teachtable, L7 teachadd, L9 teach24) and second try-it slides (L1 tryclues, L4 tryunits, L6 tryadd, L8 try1); show them only to children who choose that item. Make both 'check together' slides 60-second self-checks (children hold up the corrected page; the tutor asks 'how do you know' on one answer).
4. **Talk time 10 to 6.5-8.5.** It is LOOSE by about 3 min in 8 of 10 lessons; the 2 minutes of partner talk, one volunteer round, the return to sneak-peek puzzle 2 and the closing explanation fill 6.3 to 7.9 min. The freed minutes go to the warm-up and the worksheet.
5. **Explore: fix the four materials-heavy tasks** (L3 circle clocks, L6 fraction strips, L9 party menu, L10 stations) as listed in their sections; elsewhere keep 13-14.5 min.
6. **Brain break stays 5 min** but plan it as 2 min of movement, 2 of water and 1 of settling; tell families the toilet break is before the break starts, not in it.
7. **REC cue**: say it as the part's first slide appears, not as a separate action; it costs 10 s a part (1.3 min a lesson) and is already in every budget above.

### New budgets (minutes; each row sums to 90)

| Lesson | Opening | Sneak-peek + game + quick Qs | Explore | Mini-lesson | Brain break | Worksheet | Talk time | Exit + look-back + close | After-fix need (central) | Float |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1. Number Sleuths | 1.5 | 9.5 | 13 | 11 | 5 | 31 | 8 | 11 | 86.9 | 3.1 |
| 2. Cryptarithm Crackers | 1.5 | 9.5 | 14 | 9 | 5 | 32 | 8 | 11 | 86.3 | 3.7 |
| 3. Times Table Treasure | 1.5 | 9.5 | 14.5 | 11 | 5 | 29 | 8 | 11.5 | 86.5 | 3.5 |
| 4. Model Makers | 1.5 | 9.5 | 14 | 9.5 | 5 | 32 | 7.5 | 11 | 89.3 | 0.7 |
| 5. Remainder Riddles | 1.5 | 9.5 | 14.5 | 11 | 5 | 31 | 7 | 10.5 | 88.3 | 1.7 |
| 6. Fraction Walls | 1.5 | 9.5 | 14 | 11 | 5 | 30 | 8 | 11 | 84.8 | 5.2 |
| 7. Area Architects | 1.5 | 9.5 | 13.5 | 11.5 | 5 | 31 | 7 | 11 | 88.9 | 1.1 |
| 8. Angle and Line Detectives | 1.5 | 9 | 13.5 | 10.5 | 5 | 31 | 8 | 11.5 | 86.9 | 3.1 |
| 9. Measure and Money Masters | 1.5 | 9 | 15 | 8.5 | 5 | 31 | 8.5 | 11.5 | 82.9 | 7.1 |
| 10. Challenge Day | 1.5 | 9 | 16.5 | 9.5 | 5 | 29.5 | 6 | 13 | 89.2 | 0.8 |
| Current guide | 2 | 8 | 15 | 10 | 5 | 30 | 10 | 10 | | |

After the fixes the central need is 82.9 to 89.3 min (range 76.0 to 99.2 across the optimistic and pessimistic sets). Lessons 4, 7 and 10 (and 5) keep less than 2 min of float and need the cut ladder below; L9 has about 7 min of float, which is room to put the five quick questions or a longer page 1 back.
Budgets that sit more than 0.25 min under the after-fix need (they borrow from the float): L1 Brain break (budget 5, need 5.4); L2 Brain break (budget 5, need 5.4); L3 Brain break (budget 5, need 5.4); L4 Brain break (budget 5, need 5.4); L4 Talk time (budget 7.5, need 7.9); L5 Brain break (budget 5, need 5.4); L6 Brain break (budget 5, need 5.4); L7 Brain break (budget 5, need 5.5); L8 Brain break (budget 5, need 5.4); L9 Brain break (budget 5, need 5.4); L10 Brain break (budget 5, need 5.3); L10 Talk time (budget 6, need 6.3).

### Standing buffer

Yes. Plan the content so the central need is no more than about 87 min and name a 3-minute float, because the pessimistic set adds about 9 min to any lesson and the model ignores glitches. Put the float in Talk time (it is elastic: the last minutes are the second discussion question and the partner share, never the look-back, exit ticket or certificates). Cut ladder if the tutor is 3 or more minutes behind at minute 40 or minute 70, in this order: (1) quick questions 3 to 2; (2) second game round; (3) 'check page 2' to a one-question self-check; (4) page-2 'if time' items and teaching slides for them; (5) talk time to one question. Never cut the sneak-peek puzzles, look-back, exit ticket, certificates or REC cues, which are fixed.

### If these budgets are adopted (not done here)

The part times live in several places that would all need regenerating together: the `seg('a-b min', ...)` headings and the routine table in `p3/guide.js`, the per-lesson `plan` minutes in `p3/gifted.json`, the minute pill on every slide in `split/p3l*/project/slides/*.html` (and the section list in each `deck.json`), the 'minute 40 / 52 / 67' sentences in the Choice paragraphs of the guide, and the workbook 'if time' marks (L4 Q6 and L8 Q6 are demoted in this proposal, L2 Q2(c), L6 Q1(c)/Q6, L8 Q3(b)/Q4 are moved to take-home). Per-lesson budgets differ (Explore 13 to 16.5, Worksheet 29 to 32), so the guide generator would need per-lesson times.

## 7. Limits of this audit

- Estimates from the text, not stopwatch timings. Children's real answers, repeated questions, tutor ad-libs, camera and audio problems, late arrivals and parents are ignored; real lessons are likelier to run long than short.
- The hand-judged inputs are the minutes per workbook item, the pair-task minutes in Explore and the exit-ticket minutes (tables in `docs/audit/timing_p3.py`); changing them by 20% moves a lesson total by 2 to 4 min but does not change the ranking or the conclusion that the worksheet, the warm-up and the transitions are over budget.
- Sources read: `p3/guide.js`, `p3/data.js`, `p3/content/l1.js`-`l10.js`, `p3/gifted.json`, `p3/workbook_html.js`, the rebuilt `p3/Math_Inquirers_P3_Tutor_Guide.pdf` (81 pages) and `p3/Math_Inquirers_P3_Student_Workbook_Designed.pdf` (58 pages), and all 278 slides with their notes in `split/p3l1`-`split/p3l10`.

