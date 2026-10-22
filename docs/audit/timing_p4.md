# Lesson timing audit, Math Inquirers Level N=4 (P4, ages 9-11)

Question: when a tutor runs each of the 10 lessons live online from the slides and script, does the lesson fit its 90 minutes?

Status: analysis only. Estimates from a stated model, not stopwatch timings. Nothing in content, guides, decks, builds or outputs was edited. Helper: `docs/audit/timing_p4.py` (prints every table in this file). Snapshot: the files in /home/user/math-inquirers on 22 Oct 2026, around 02:05 UTC. `p4/content/l1..l9.js` were being edited by someone else while this audit ran (word counts shifted by a few words between runs); re-run the helper if they change again.

## 1. Answer in brief


| L | Title | Slides | Best A | Typ A | Slow A | Typ B (ws held) | Slow B | ws left (typ) | Typical verdict |
|--:|---|--:|--:|--:|--:|--:|--:|--:|---|
| 1 | Factor Hunters | 28 | 79.8 | 99.6 | 104.7 | 103.9 | 107.4 | 32.1 | does not fit |
| 2 | Big Number Puzzles | 28 | 81.4 | 98.8 | 103.9 | 102.1 | 105.6 | 33.9 | does not fit |
| 3 | Operation Detectives | 29 | 82.8 | 104.9 | 110.1 | 102.3 | 105.8 | 33.7 | does not fit |
| 4 | Fraction Frontier | 30 | 77.3 | 96.0 | 101.3 | 102.5 | 106.1 | 33.5 | does not fit |
| 5 | Decimal Detectives | 29 | 78.5 | 95.4 | 100.6 | 102.7 | 106.2 | 33.3 | does not fit |
| 6 | Angle Turns | 28 | 77.4 | 93.9 | 99.0 | 100.1 | 103.5 | 35.9 | does not fit |
| 7 | Area Architects II | 29 | 83.8 | 104.5 | 109.7 | 104.0 | 107.6 | 32.0 | does not fit |
| 8 | Symmetry and Nets | 28 | 78.3 | 96.1 | 101.2 | 102.3 | 105.7 | 33.7 | does not fit |
| 9 | Data Detectives | 27 | 78.3 | 93.4 | 98.5 | 101.3 | 104.8 | 34.7 | does not fit |
| 10 | Challenge Day | 29 | 90.9 | 105.3 | 110.5 | 108.9 | 112.5 | 27.1 | does not fit |

How to read it. **A** = minutes the content needs if the worksheet is held to the items the printed "Aim for" note names (Start here page plus the priority items on page 2). **B** = clock reading if the tutor lets the worksheet run its full 46 scripted minutes (the other parts take what they need). Best / Typ / Slow are three tutor styles (section 2). "ws left" = minutes of the 46-minute worksheet window still available after every other part has taken what it needs (typical tutor).


* No lesson fits at the typical setting. Typical totals are 93.4 to 105.3 minutes (best case 77.3 to 90.9; slow 98.5 to 110.5). In the best case (optional slides and speaker-note ASKs skipped, 20 s slide changes, 60 s breakout moves) 9 of 10 lessons fit; Lesson 10 does not.
* Every lesson has the same shape: the lead-in parts overrun (sneak-peek +3.5, warm-up +3.1, explore +3.6 on average, all ten lessons OVER on each), page 1 of the worksheet is OVER in 9 lessons and TIGHT in the other (range +1.5 to +8.9), and the worksheet's page-2 solo block has 3.4 to 9.4 minutes of unused time (the cushion that the printed choice questions use).
* If a tutor skips the optional "your turn" slides and the speaker-note ASKs (as the guide allows) the typical total falls by 7.0 to 15.0 minutes (mean 10.8) to 84.0-91.5 minutes (Lesson 10: 98.3).
* Lessons running long (typical total over 90): L10 (+15.3), L3 (+14.9), L7 (+14.5), L1 (+9.6), L2 (+8.8), L8 (+6.1), L4 (+6.0), L5 (+5.4), L6 (+3.9), L9 (+3.4). Lessons running short: none. Loose parts (3+ min spare): worksheet page 2 in all ten lessons, the mini-lesson in L9 and L10.
* With the fixes in section 6 the typical need is 76.2 to 86.6 minutes (best 67.7-77.5, slow 80.2-90.8) and every lesson keeps at least 3 minutes of cushion.

## 2. Model and assumptions (same for every level)

| Item | Value used |
|---|---|
| Tutor speech to children | 135 words per minute including natural pauses (SAY lines, think-alouds, answer reveals, narration of teaching slides at 60% of the words on the slide) |
| Questions read aloud | 125 wpm (sneak-peek puzzles, warm-up quick questions, explore set-up and debrief, workbook questions on the worksheet, exit ticket) |
| Waiting | 10 s think + 20 s to take one or two answers = 30 s for every question put to the group (warm-up quick questions, explore debrief, each answer check, talk time); "hold up" moments 30 s |
| Slide change | 20 / 25 / 30 s (best / typical / slow) for every slide shown |
| Breakout rooms | 60 / 90 / 120 s each way; used for explore (in and out) and page 1 of the worksheet (in and out); pair talk in Talk time adds 0 / 60 / 120 s |
| Worksheet start | 2 min (finding the page, reading the title and the "Pairs first" line) |
| Greeting | 1.5 / 2.5 / 4 s per child, 8 children |
| Fixed items | Sneak-peek (2 x 90 s scripted, 2 hold-ups, walkthrough of both answers and the "good reason" sentence); Looking back (2 min of child time); recording notice (10 s); REC cue lines at the start of every part (real text from `levels/reccues.js`, 10 per lesson); L10 final minute |
| REC cues | The real lines are 15 to 39 words, 7 to 17 s each, 119 s (2.0 min) per lesson, not "about 10 seconds"; the opening, sneak-peek, explore and worksheet cues are over 13 s |
| Optional items | BEST skips the optional "your turn" slides and the speaker-note ASKs, TYPICAL and SLOW include them. LEAN = TYPICAL minus those |
| Child pace | MIDDLE child sets the activity time; LOW takes 1.7 x, HIGH 0.65 x |
| Flags | OVER = needed exceeds scripted by 2+ min; TIGHT = from 1 min under to under 2 min over; OK = 1 to 3 min spare; LOOSE = 3+ min spare |
| Not modelled | camera and tech glitches; repeating a child's answer in the tutor's own words (REC rule, about 3 s per answer, roughly 1 min per lesson); the REC rule to read every workbook question aloud is modelled (page 1 in full, page 2 priority items only); dead time between children's answers beyond 30 s; a tutor helping individual children during solo work (assumed to happen during the activity minutes) |

Judged inputs (MIDDLE child, minutes). Workbook items are the 5 to 7 core questions on pages 1 and 2 of the printed workbook; page 2 is divided into priority items (named by the printed "Aim for" note) and choice items.

| L | Workbook items (minutes for a middle child) | Explore hands-on | Exit ticket writing |
|--:|---|--:|--:|
| 1 | Q1 3.5; Q2 3.0; Q3 3.5; Q4 4.5; Q5 7.0; Q6 6.0 (choice) | 5.0 | 2.0 |
| 2 | Q1 4.0; Q2 6.0; Q3 4.5; Q4a 4.0; Q5 4.5; Q6a 1.5; Q4b 3.0 (choice); Q6bc 4.0 (choice) | 6.0 | 1.5 |
| 3 | Q1 4.0; Q2 5.0; Q3 4.8; Q4 2.5; Q5 5.0; Q6 5.0; Q7 4.0 (choice) | 5.0 | 1.0 |
| 4 | Q1 5.0; Q2 2.5; Q3 2.5; Q4 6.5; Q5 3.2; Q6 4.0 (choice) | 6.0 | 1.7 |
| 5 | Q1 4.7; Q2 3.5; Q3 2.5; Q4 5.5; Q5 4.0; Q6 4.5 (choice) | 6.5 | 2.0 |
| 6 | Q1 8.0; Q2 5.0; Q3 2.9; Q4 4.0; Q5 3.0 (choice); Q6 1.5 (choice) | 5.0 | 1.7 |
| 7 | Q1 6.0; Q2 4.0; Q3 3.5; Q4 5.0; Q5 6.5; Q6 5.5 (choice) | 5.0 | 2.5 |
| 8 | Q1 5.0; Q2 3.0; Q3 3.5; Q4 4.0; Q5 5.0; Q6 5.0 (choice) | 7.0 | 1.0 |
| 9 | Q1 5.5; Q2 5.0; Q3 5.5; Q4 4.5; Q5 4.0 (choice) | 7.5 | 1.5 |
| 10 | Q1 6.5; Q2 6.0; Q3 4.5; Q4 4.5; Q5 3.5; Q6 5.0 (choice) | 9.0 | 3.0 |

Reasoning, briefly: Core items 2 to 3 min per item for ages 9-11 (a question with three parts 4 to 5 min), Think Harder style items 3 to 4 min per sub-part. Examples: L1 Q5 7 min = seven factor counts at 40 s plus a pattern and a check; L6 Q1 8 min = four angles at 2 min each with a first-time protractor; L10 page 1 17 min = guess-and-check 6.5, chickens and goats 6, working backwards 4.5.

Brain break: 3 of the 4 scripted minutes are activity (about 1.75 min play, 1.25 min water, toilet and return); warm-up game 2 min as scripted.

## 3. Lesson-by-lesson tables

Columns: scripted minutes, then the typical tutor's speaking, waiting (questions, hold-ups, "your turn" slides), activity (children working, game, break), transition (slide changes, breakouts, worksheet start, greeting) and REC cue minutes, then total needed, difference and flag, then the range best-slow. The worksheet is split into five blocks (WS-a to WS-e) with their scripted windows 34-50, 50-53, 53-58, 58-76, 76-80; its page-2 row (WS-d) counts only the priority items. Flags apply per row.


#### Lesson 1: Factor Hunters  (28 slides, 345 SAY words, 6 core workbook questions / 16 sub-parts, 404 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.7 | 0.0 | 0.0 | 0.3 | 0.3 | **1.2** | +0.2 | TIGHT | 1.1-1.4 |
| Sneak-peek puzzles | 3.0 | 1.8 | 1.5 | 3.0 | 0.4 | 0.2 | **6.9** | +3.9 | OVER | 6.3-7.0 |
| Warm-up game + quick questions | 4.0 | 0.9 | 4.1 | 2.0 | 0.8 | 0.1 | **8.1** | +4.1 | OVER | 6.8-8.2 |
| Explore (pairs, objects) | 10.0 | 1.5 | 2.0 | 5.0 | 3.8 | 0.3 | **12.5** | +2.5 | OVER | 11.4-13.7 |
| Mini-lesson (7 slides) | 12.0 | 1.6 | 6.6 | 0.0 | 2.9 | 0.2 | **11.3** | -0.7 | TIGHT | 3.7-11.9 |
| Brain break | 4.0 | 0.2 | 0.6 | 3.0 | 0.8 | 0.1 | **4.7** | +0.7 | TIGHT | 4.0-4.7 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.7 | 0.6 | 10.0 | 5.4 | 0.3 | **18.0** | +2.0 | OVER | 15.7-19.1 |
| WS-b  Check page 1 | 3.0 | 0.6 | 1.5 | 0.0 | 0.4 | 0.0 | **2.5** | -0.5 | TIGHT | 2.4-2.6 |
| WS-c  Teaching before page 2 | 5.0 | 1.2 | 2.6 | 0.0 | 1.2 | 0.0 | **5.0** | -0.0 | TIGHT | 2.2-5.2 |
| WS-d  Page 2 solo (priority items) | 18.0 | 1.4 | 0.0 | 11.5 | 0.9 | 0.0 | **13.8** | -4.2 | LOOSE | 12.6-13.9 |
| WS-e  Check page 2 | 4.0 | 0.5 | 1.5 | 0.0 | 0.4 | 0.0 | **2.4** | -1.6 | OK | 2.3-2.5 |
| Talk time | 5.0 | 0.5 | 2.0 | 2.0 | 1.4 | 0.2 | **6.1** | +1.1 | TIGHT | 4.5-7.2 |
| Exit ticket + closing | 3.0 | 0.4 | 0.5 | 2.0 | 0.4 | 0.1 | **3.5** | +0.5 | TIGHT | 3.4-3.5 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.5-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **41.7** | -4.3 | LOOSE | |

Total needed (worksheet at priority items only): best 79.8 / typical 99.6 / slow 104.7 min. As scripted (worksheet runs its full 46): best 90.6 / typical 103.9 / slow 107.4. Worksheet time left after the other parts take what they need (typical): 32.1 of 46 scripted; spare after priority items: -9.6.


**Reading it.** Page 1 (Q1 factor pairs of 48, Q2 40 trees, Q3 18 red and 24 blue beads) is the one page that fits: a MIDDLE child needs about 10 min of the 11 available. Q5 on page 2 (a 7-number factor-count table, the "exactly 3 factors" pattern and 49) is the longest single item of the level at about 7 min, so a LOW child reaches Q4 only. Sneak-peek puzzle 2 (two lifts, floors to 40) needs two lists; 90 s is tight for a LOW child. Fizz-Buzz is scripted at 2 min and fits, but the five quick questions after it do not (4.1 min of waiting alone).


#### Lesson 2: Big Number Puzzles  (28 slides, 306 SAY words, 6 core workbook questions / 17 sub-parts, 309 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.7 | 0.0 | 0.0 | 0.3 | 0.3 | **1.3** | +0.3 | TIGHT | 1.2-1.5 |
| Sneak-peek puzzles | 3.0 | 1.4 | 1.5 | 3.0 | 0.4 | 0.2 | **6.6** | +3.6 | OVER | 6.0-6.7 |
| Warm-up game + quick questions | 4.0 | 0.8 | 3.0 | 2.0 | 0.8 | 0.1 | **6.7** | +2.7 | OVER | 6.6-6.9 |
| Explore (pairs, objects) | 10.0 | 1.3 | 2.0 | 6.0 | 3.8 | 0.3 | **13.4** | +3.4 | OVER | 12.2-14.6 |
| Mini-lesson (7 slides) | 12.0 | 1.2 | 6.5 | 0.0 | 2.9 | 0.2 | **10.8** | -1.2 | OK | 3.3-11.3 |
| Brain break | 4.0 | 0.2 | 0.5 | 3.0 | 0.8 | 0.1 | **4.6** | +0.6 | TIGHT | 4.0-4.7 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.4 | 0.6 | 14.5 | 5.4 | 0.3 | **22.2** | +6.2 | OVER | 19.7-23.3 |
| WS-b  Check page 1 | 3.0 | 0.4 | 1.5 | 0.0 | 0.4 | 0.0 | **2.4** | -0.6 | TIGHT | 2.3-2.4 |
| WS-c  Teaching before page 2 | 5.0 | 1.0 | 1.7 | 0.0 | 1.2 | 0.0 | **4.0** | -1.0 | TIGHT | 2.0-4.3 |
| WS-d  Page 2 solo (priority items) | 18.0 | 1.0 | 0.0 | 10.0 | 0.9 | 0.0 | **11.9** | -6.1 | LOOSE | 11.1-12.0 |
| WS-e  Check page 2 | 4.0 | 0.3 | 1.5 | 0.0 | 0.4 | 0.0 | **2.2** | -1.8 | OK | 2.2-2.3 |
| Talk time | 5.0 | 0.6 | 2.0 | 2.0 | 1.4 | 0.2 | **6.2** | +1.2 | TIGHT | 4.5-7.3 |
| Exit ticket + closing | 3.0 | 0.4 | 0.5 | 1.5 | 0.4 | 0.1 | **3.0** | -0.0 | TIGHT | 2.9-3.1 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.5-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **42.7** | -3.3 | LOOSE | |

Total needed (worksheet at priority items only): best 81.4 / typical 98.8 / slow 103.9 min. As scripted (worksheet runs its full 46): best 90.1 / typical 102.1 / slow 105.6. Worksheet time left after the other parts take what they need (typical): 33.9 of 46 scripted; spare after priority items: -8.8.


**Reading it.** Page 1 is the heaviest "Start here" page after Lesson 10: 14.5 min against 11. Q2a/Q2b (smallest and largest number that rounds to 63 000; all numbers that round to 5350) are boundary-case reasoning that sits closer to Think Harder than Core, and Q3c is a 4-digit by 1-digit multiplication on top of an estimate. Explore (find every 5-digit number from the cards 2, 4, 5, 7, 9 that rounds to 50 000: there are only four) is 6 min of enumeration. The mini-lesson has 4 worked examples (we1 to we4) plus 2 optional "your turn" slides.


#### Lesson 3: Operation Detectives  (29 slides, 330 SAY words, 7 core workbook questions / 15 sub-parts, 324 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.7 | 0.0 | 0.0 | 0.3 | 0.3 | **1.3** | +0.3 | TIGHT | 1.1-1.5 |
| Sneak-peek puzzles | 3.0 | 1.2 | 1.5 | 3.0 | 0.4 | 0.2 | **6.4** | +3.4 | OVER | 5.8-6.5 |
| Warm-up game + quick questions | 4.0 | 0.5 | 3.0 | 2.0 | 0.8 | 0.1 | **6.5** | +2.5 | OVER | 6.3-6.7 |
| Explore (pairs, objects) | 10.0 | 1.3 | 2.0 | 5.0 | 3.8 | 0.3 | **12.4** | +2.4 | OVER | 11.2-13.5 |
| Mini-lesson (7 slides) | 12.0 | 1.7 | 8.6 | 0.0 | 2.9 | 0.2 | **13.4** | +1.4 | TIGHT | 3.5-14.0 |
| Brain break | 4.0 | 0.3 | 0.0 | 3.0 | 0.8 | 0.1 | **4.2** | +0.2 | TIGHT | 4.1-4.3 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.6 | 0.6 | 13.8 | 5.4 | 0.3 | **21.6** | +5.6 | OVER | 19.3-22.7 |
| WS-b  Check page 1 | 3.0 | 0.4 | 1.5 | 0.0 | 0.4 | 0.0 | **2.3** | -0.7 | TIGHT | 2.2-2.4 |
| WS-c  Teaching before page 2 | 5.0 | 1.5 | 4.1 | 0.0 | 1.7 | 0.0 | **7.2** | +2.2 | OVER | 2.1-7.5 |
| WS-d  Page 2 solo (priority items) | 18.0 | 1.2 | 0.0 | 12.5 | 0.9 | 0.0 | **14.6** | -3.4 | LOOSE | 14.0-14.7 |
| WS-e  Check page 2 | 4.0 | 0.5 | 2.0 | 0.0 | 0.4 | 0.0 | **2.9** | -1.1 | OK | 2.8-3.0 |
| Talk time | 5.0 | 0.6 | 2.0 | 2.0 | 1.4 | 0.2 | **6.2** | +1.2 | TIGHT | 4.6-7.3 |
| Exit ticket + closing | 3.0 | 0.3 | 0.5 | 1.0 | 0.4 | 0.1 | **2.3** | -0.7 | TIGHT | 2.3-2.4 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.4-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **48.7** | +2.7 | OVER | |

Total needed (worksheet at priority items only): best 82.8 / typical 104.9 / slow 110.1 min. As scripted (worksheet runs its full 46): best 88.3 / typical 102.3 / slow 105.8. Worksheet time left after the other parts take what they need (typical): 33.7 of 46 scripted; spare after priority items: -14.9.


**Reading it.** Second-highest typical total (L10 is first, L7 close behind). The mini-lesson has three optional "your turn" slides (try1, try2, try3) and 7 slides in 12 minutes; the worksheet teaching block has four slides (teachback, trytrick, teachbar, teachchain) for 5 minutes, and trytrick and teachchain carry no minute badge on the deck, so they are unscheduled. Page 1 is 13.8 min of work: Q2 (four missing-sign sentences, the last with three blanks) is trial and error at about 1.2 min each.


#### Lesson 4: Fraction Frontier  (30 slides, 287 SAY words, 6 core workbook questions / 13 sub-parts, 246 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.7 | 0.0 | 0.0 | 0.3 | 0.3 | **1.3** | +0.3 | TIGHT | 1.1-1.5 |
| Sneak-peek puzzles | 3.0 | 1.3 | 1.5 | 3.0 | 0.4 | 0.2 | **6.4** | +3.4 | OVER | 5.8-6.5 |
| Warm-up game + quick questions | 4.0 | 0.6 | 3.5 | 2.0 | 0.8 | 0.1 | **7.1** | +3.1 | OVER | 6.4-7.2 |
| Explore (pairs, objects) | 10.0 | 1.1 | 2.0 | 6.0 | 3.8 | 0.3 | **13.2** | +3.2 | OVER | 12.1-14.4 |
| Mini-lesson (7 slides) | 12.0 | 1.5 | 7.0 | 0.0 | 2.9 | 0.2 | **11.6** | -0.4 | TIGHT | 3.6-12.1 |
| Brain break | 4.0 | 0.3 | 0.0 | 3.0 | 0.8 | 0.1 | **4.1** | +0.1 | TIGHT | 4.1-4.2 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.3 | 0.5 | 10.0 | 5.4 | 0.3 | **17.5** | +1.5 | TIGHT | 15.3-18.6 |
| WS-b  Check page 1 | 3.0 | 0.4 | 1.5 | 0.0 | 0.4 | 0.0 | **2.3** | -0.7 | TIGHT | 2.2-2.4 |
| WS-c  Teaching before page 2 | 5.0 | 1.5 | 2.3 | 0.0 | 2.1 | 0.0 | **5.9** | +0.9 | TIGHT | 2.6-6.3 |
| WS-d  Page 2 solo (priority items) | 18.0 | 0.9 | 0.0 | 9.7 | 0.9 | 0.0 | **11.5** | -6.5 | LOOSE | 11.1-11.6 |
| WS-e  Check page 2 | 4.0 | 0.3 | 1.5 | 0.0 | 0.4 | 0.0 | **2.2** | -1.8 | OK | 2.2-2.3 |
| Talk time | 5.0 | 0.7 | 2.0 | 2.0 | 1.4 | 0.2 | **6.3** | +1.3 | TIGHT | 4.6-7.4 |
| Exit ticket + closing | 3.0 | 0.3 | 0.5 | 1.7 | 0.4 | 0.1 | **3.1** | +0.1 | TIGHT | 3.0-3.2 |
| Looking back | 2.0 | 0.6 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.4-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **39.4** | -6.6 | LOOSE | |

Total needed (worksheet at priority items only): best 77.3 / typical 96.0 / slow 101.3 min. As scripted (worksheet runs its full 46): best 90.0 / typical 102.5 / slow 106.1. Worksheet time left after the other parts take what they need (typical): 33.5 of 46 scripted; spare after priority items: -6.0.


**Reading it.** No single part is badly over except the lead-in (sneak, warm-up, explore). Page 1 is 10 min of work and fits. The warm-up quick questions Q4 (3/4 + 1/8) and Q5 (1 - 3/10) need unlike denominators and are not 30-second questions for a LOW child. Explore (cut paper circles into quarters, build 11 slices into pizzas, write it two ways, then "what if 6 slices") is about 6 min of hands-on plus cutting. Largest slide count of the level (30).


#### Lesson 5: Decimal Detectives  (29 slides, 305 SAY words, 6 core workbook questions / 14 sub-parts, 271 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.6 | 0.0 | 0.0 | 0.3 | 0.3 | **1.2** | +0.2 | TIGHT | 1.1-1.4 |
| Sneak-peek puzzles | 3.0 | 1.2 | 1.5 | 3.0 | 0.4 | 0.2 | **6.4** | +3.4 | OVER | 5.8-6.5 |
| Warm-up game + quick questions | 4.0 | 0.8 | 3.0 | 2.0 | 0.8 | 0.1 | **6.8** | +2.8 | OVER | 6.6-6.9 |
| Explore (pairs, objects) | 10.0 | 1.3 | 2.0 | 6.5 | 3.8 | 0.3 | **13.9** | +3.9 | OVER | 12.7-15.0 |
| Mini-lesson (7 slides) | 12.0 | 1.3 | 6.9 | 0.0 | 2.9 | 0.2 | **11.3** | -0.7 | TIGHT | 3.4-11.9 |
| Brain break | 4.0 | 0.2 | 0.0 | 3.0 | 0.8 | 0.1 | **4.0** | +0.0 | TIGHT | 3.9-4.1 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.3 | 0.5 | 10.7 | 5.4 | 0.3 | **18.3** | +2.3 | OVER | 16.1-19.3 |
| WS-b  Check page 1 | 3.0 | 0.2 | 1.5 | 0.0 | 0.4 | 0.0 | **2.1** | -0.9 | TIGHT | 2.1-2.2 |
| WS-c  Teaching before page 2 | 5.0 | 1.4 | 1.7 | 0.0 | 1.7 | 0.0 | **4.8** | -0.2 | TIGHT | 2.7-5.1 |
| WS-d  Page 2 solo (priority items) | 18.0 | 1.0 | 0.0 | 9.5 | 0.9 | 0.0 | **11.4** | -6.6 | LOOSE | 10.8-11.5 |
| WS-e  Check page 2 | 4.0 | 0.2 | 1.5 | 0.0 | 0.4 | 0.0 | **2.1** | -1.9 | OK | 2.0-2.2 |
| Talk time | 5.0 | 0.7 | 2.0 | 2.0 | 1.4 | 0.2 | **6.3** | +1.3 | TIGHT | 4.6-7.4 |
| Exit ticket + closing | 3.0 | 0.3 | 0.5 | 2.0 | 0.4 | 0.1 | **3.4** | +0.4 | TIGHT | 3.3-3.5 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.4-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **38.7** | -7.3 | LOOSE | |

Total needed (worksheet at priority items only): best 78.5 / typical 95.4 / slow 100.6 min. As scripted (worksheet runs its full 46): best 90.7 / typical 102.7 / slow 106.2. Worksheet time left after the other parts take what they need (typical): 33.3 of 46 scripted; spare after priority items: -5.4.


**Reading it.** Same pattern as Lesson 4. Explore (digit cards 2, 5, 8 and a point: make every number, order them, find the one closest to 5) is 6.5 min and the highest hands-on figure before Lesson 8. Page 1 Q1 (five arrows on a zoomed number line, decide what one step is worth first) is about 4.7 min; LOW finishes one of three page-1 questions.


#### Lesson 6: Angle Turns  (28 slides, 305 SAY words, 6 core workbook questions / 11 sub-parts, 231 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.6 | 0.0 | 0.0 | 0.3 | 0.3 | **1.2** | +0.2 | TIGHT | 1.1-1.4 |
| Sneak-peek puzzles | 3.0 | 1.2 | 1.5 | 3.0 | 0.4 | 0.2 | **6.3** | +3.3 | OVER | 5.7-6.4 |
| Warm-up game + quick questions | 4.0 | 0.7 | 4.1 | 2.0 | 0.8 | 0.1 | **7.8** | +3.8 | OVER | 6.5-7.9 |
| Explore (pairs, objects) | 10.0 | 1.2 | 2.0 | 5.0 | 3.8 | 0.3 | **12.3** | +2.3 | OVER | 11.1-13.5 |
| Mini-lesson (5 slides) | 12.0 | 2.0 | 5.2 | 0.0 | 2.1 | 0.2 | **9.5** | -2.5 | OK | 3.4-9.9 |
| Brain break | 4.0 | 0.2 | 0.0 | 3.0 | 0.8 | 0.1 | **4.1** | +0.1 | TIGHT | 4.0-4.1 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.5 | 0.5 | 13.0 | 5.8 | 0.3 | **21.1** | +5.1 | OVER | 19.2-22.3 |
| WS-b  Check page 1 | 3.0 | 0.3 | 2.0 | 0.0 | 0.4 | 0.0 | **2.7** | -0.3 | TIGHT | 2.6-2.8 |
| WS-c  Teaching before page 2 | 5.0 | 1.3 | 1.8 | 0.0 | 1.7 | 0.0 | **4.7** | -0.3 | TIGHT | 2.0-5.0 |
| WS-d  Page 2 solo (priority items) | 18.0 | 0.8 | 0.0 | 6.9 | 0.9 | 0.0 | **8.6** | -9.4 | LOOSE | 8.1-8.7 |
| WS-e  Check page 2 | 4.0 | 0.2 | 2.0 | 0.0 | 0.4 | 0.0 | **2.6** | -1.4 | OK | 2.6-2.7 |
| Talk time | 5.0 | 0.6 | 2.0 | 2.0 | 1.4 | 0.2 | **6.2** | +1.2 | TIGHT | 4.5-7.3 |
| Exit ticket + closing | 3.0 | 0.4 | 0.5 | 1.7 | 0.4 | 0.1 | **3.1** | +0.1 | TIGHT | 3.1-3.2 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.5-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **39.8** | -6.2 | LOOSE | |

Total needed (worksheet at priority items only): best 77.4 / typical 93.9 / slow 99.0 min. As scripted (worksheet runs its full 46): best 88.9 / typical 100.1 / slow 103.5. Worksheet time left after the other parts take what they need (typical): 35.9 of 46 scripted; spare after priority items: -3.9.


**Reading it.** The only lesson whose worksheet is too light on page 2 and too heavy on page 1. Page 1 holds only Q1 and Q2, although the printed line and the guide say "after question 3 you may choose" (Q3 is on page 2). Q1 asks a child who is probably new to the protractor to estimate, extend the arms with a ruler and measure four angles: about 2 min each, 8 min, plus Q2 (name every angle, size each) 5 min, against a 9 min working window (the teachfan slide takes 34-36). Page 2 priority items (Q3, Q4) are only 6.9 min, so there is 9 min of loose time there.


#### Lesson 7: Area Architects II  (29 slides, 418 SAY words, 6 core workbook questions / 9 sub-parts, 375 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.7 | 0.0 | 0.0 | 0.3 | 0.3 | **1.3** | +0.3 | TIGHT | 1.2-1.5 |
| Sneak-peek puzzles | 3.0 | 1.4 | 1.5 | 3.0 | 0.4 | 0.2 | **6.5** | +3.5 | OVER | 5.9-6.6 |
| Warm-up game + quick questions | 4.0 | 0.8 | 3.5 | 2.0 | 0.8 | 0.1 | **7.3** | +3.3 | OVER | 6.6-7.5 |
| Explore (pairs, objects) | 10.0 | 1.4 | 2.0 | 5.0 | 3.8 | 0.3 | **12.5** | +2.5 | OVER | 11.3-13.6 |
| Mini-lesson (7 slides) | 12.0 | 2.2 | 7.2 | 0.0 | 2.9 | 0.2 | **12.5** | +0.5 | TIGHT | 4.3-13.0 |
| Brain break | 4.0 | 0.2 | 0.0 | 3.0 | 0.8 | 0.1 | **4.0** | +0.0 | TIGHT | 3.9-4.1 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.5 | 1.1 | 13.5 | 5.4 | 0.3 | **21.8** | +5.8 | OVER | 18.9-22.9 |
| WS-b  Check page 1 | 3.0 | 0.5 | 1.5 | 0.0 | 0.4 | 0.0 | **2.4** | -0.6 | TIGHT | 2.4-2.5 |
| WS-c  Teaching before page 2 | 5.0 | 1.4 | 2.9 | 0.0 | 1.7 | 0.0 | **6.0** | +1.0 | TIGHT | 2.1-6.3 |
| WS-d  Page 2 solo (priority items) | 18.0 | 1.4 | 0.0 | 11.5 | 0.9 | 0.0 | **13.8** | -4.2 | LOOSE | 12.8-13.9 |
| WS-e  Check page 2 | 4.0 | 0.5 | 1.5 | 0.0 | 0.4 | 0.0 | **2.4** | -1.6 | OK | 2.3-2.5 |
| Talk time | 5.0 | 0.7 | 2.0 | 2.0 | 1.4 | 0.2 | **6.4** | +1.4 | TIGHT | 4.6-7.4 |
| Exit ticket + closing | 3.0 | 0.5 | 0.5 | 2.5 | 0.4 | 0.1 | **4.0** | +1.0 | TIGHT | 4.0-4.1 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.6** | +1.6 | TIGHT | 3.5-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **46.4** | +0.4 | TIGHT | |

Total needed (worksheet at priority items only): best 83.8 / typical 104.5 / slow 109.7 min. As scripted (worksheet runs its full 46): best 91.3 / typical 104.0 / slow 107.6. Worksheet time left after the other parts take what they need (typical): 32.0 of 46 scripted; spare after priority items: -14.5.


**Reading it.** Largest script of the level: 418 SAY words (median 322), of which the mini-lesson think-aloud is 4 paragraphs and 207 words; also the most text on slides (2 179 visible words). Page 1 is 13.5 min (Q1 is a three-part L-shaped figure: missing sides, area two ways, perimeter). The exit ticket (area and perimeter of a 7 by 5 rectangle with a 2 by 2 corner cut out) needs about 2.5 min of child time, so the 3 min slot is exceeded.


#### Lesson 8: Symmetry and Nets  (28 slides, 344 SAY words, 6 core workbook questions / 7 sub-parts, 197 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.7 | 0.0 | 0.0 | 0.3 | 0.3 | **1.3** | +0.3 | TIGHT | 1.1-1.5 |
| Sneak-peek puzzles | 3.0 | 1.2 | 1.5 | 3.0 | 0.4 | 0.2 | **6.4** | +3.4 | OVER | 5.8-6.5 |
| Warm-up game + quick questions | 4.0 | 0.7 | 3.0 | 2.0 | 0.8 | 0.1 | **6.7** | +2.7 | OVER | 6.5-6.8 |
| Explore (pairs, objects) | 10.0 | 1.4 | 2.0 | 7.0 | 3.8 | 0.3 | **14.5** | +4.5 | OVER | 13.3-15.6 |
| Mini-lesson (6 slides) | 12.0 | 1.9 | 6.1 | 0.0 | 2.5 | 0.2 | **10.7** | -1.3 | OK | 3.7-11.2 |
| Brain break | 4.0 | 0.1 | 0.6 | 3.0 | 0.8 | 0.1 | **4.6** | +0.6 | TIGHT | 3.9-4.7 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.0 | 0.5 | 11.5 | 5.4 | 0.3 | **18.8** | +2.8 | OVER | 16.9-19.9 |
| WS-b  Check page 1 | 3.0 | 0.4 | 1.5 | 0.0 | 0.4 | 0.0 | **2.4** | -0.6 | TIGHT | 2.3-2.4 |
| WS-c  Teaching before page 2 | 5.0 | 1.2 | 2.9 | 0.0 | 1.7 | 0.0 | **5.8** | +0.8 | TIGHT | 2.0-6.1 |
| WS-d  Page 2 solo (priority items) | 18.0 | 0.7 | 0.0 | 9.0 | 0.9 | 0.0 | **10.7** | -7.3 | LOOSE | 10.3-10.7 |
| WS-e  Check page 2 | 4.0 | 0.3 | 1.5 | 0.0 | 0.4 | 0.0 | **2.2** | -1.8 | OK | 2.2-2.3 |
| Talk time | 5.0 | 0.7 | 2.0 | 2.0 | 1.4 | 0.2 | **6.3** | +1.3 | TIGHT | 4.7-7.4 |
| Exit ticket + closing | 3.0 | 0.3 | 0.5 | 1.0 | 0.4 | 0.1 | **2.4** | -0.6 | TIGHT | 2.3-2.5 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.4-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **39.8** | -6.2 | LOOSE | |

Total needed (worksheet at priority items only): best 78.3 / typical 96.1 / slow 101.2 min. As scripted (worksheet runs its full 46): best 90.7 / typical 102.3 / slow 105.7. Worksheet time left after the other parts take what they need (typical): 33.7 of 46 scripted; spare after priority items: -6.1.


**Reading it.** Explore is the problem: join six paper squares edge to edge, tape, try to fold into a cube, then draw every shape that works: about 7 min of hands-on, so the part needs 14.5 against 10. Q1 (six nets, which fold into a cube, tick and explain) is mental folding at about 5 min and the hardest page-1 item for LOW children. The exit ticket (dice net) is only 1 min of child time, so the closing part needs only about 2.4 min.


#### Lesson 9: Data Detectives  (27 slides, 330 SAY words, 5 core workbook questions / 12 sub-parts, 264 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.7 | 0.0 | 0.0 | 0.3 | 0.3 | **1.3** | +0.3 | TIGHT | 1.1-1.5 |
| Sneak-peek puzzles | 3.0 | 1.1 | 1.5 | 3.0 | 0.4 | 0.2 | **6.2** | +3.2 | OVER | 5.7-6.3 |
| Warm-up game + quick questions | 4.0 | 0.8 | 3.6 | 2.0 | 0.8 | 0.1 | **7.3** | +3.3 | OVER | 6.6-7.5 |
| Explore (pairs, objects) | 10.0 | 1.3 | 2.0 | 7.5 | 3.8 | 0.3 | **14.9** | +4.9 | OVER | 13.7-16.1 |
| Mini-lesson (6 slides) | 12.0 | 1.5 | 4.7 | 0.0 | 2.5 | 0.2 | **8.9** | -3.1 | LOOSE | 3.3-9.4 |
| Brain break | 4.0 | 0.2 | 0.0 | 3.0 | 0.8 | 0.1 | **4.1** | +0.1 | TIGHT | 4.0-4.1 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.4 | 0.5 | 10.5 | 5.4 | 0.3 | **18.1** | +2.1 | OVER | 15.8-19.2 |
| WS-b  Check page 1 | 3.0 | 0.3 | 1.0 | 0.0 | 0.4 | 0.0 | **1.8** | -1.2 | OK | 1.7-1.8 |
| WS-c  Teaching before page 2 | 5.0 | 1.1 | 1.7 | 0.0 | 1.2 | 0.0 | **4.1** | -0.9 | TIGHT | 2.1-4.3 |
| WS-d  Page 2 solo (priority items) | 18.0 | 0.9 | 0.0 | 10.0 | 0.9 | 0.0 | **11.9** | -6.1 | LOOSE | 11.3-11.9 |
| WS-e  Check page 2 | 4.0 | 0.4 | 1.5 | 0.0 | 0.4 | 0.0 | **2.3** | -1.7 | OK | 2.2-2.4 |
| Talk time | 5.0 | 0.5 | 2.0 | 2.0 | 1.4 | 0.2 | **6.1** | +1.1 | TIGHT | 4.4-7.2 |
| Exit ticket + closing | 3.0 | 0.4 | 0.5 | 1.5 | 0.4 | 0.1 | **3.0** | +0.0 | TIGHT | 2.9-3.1 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.4-3.6 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **38.1** | -7.9 | LOOSE | |

Total needed (worksheet at priority items only): best 78.3 / typical 93.4 / slow 98.5 min. As scripted (worksheet runs its full 46): best 91.1 / typical 101.3 / slow 104.8. Worksheet time left after the other parts take what they need (typical): 34.7 of 46 scripted; spare after priority items: -3.4.


**Reading it.** Explore asks children to choose a scale, plot about seven points and join them, then write three findings: 7.5 min hands-on, 14.9 min needed against 10. The mini-lesson has only 6 slides with little new vocabulary and is the one regular part that is LOOSE (about 9 against 12). Page 1 has only two questions (Q1 reading a line graph, Q2 filling a table) so 'after question 3' in the printed line is not reached on this lesson either.


#### Lesson 10: Challenge Day  (29 slides, 314 SAY words, 6 core workbook questions / 13 sub-parts, 294 words)

| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|
| Opening | 1.0 | 0.6 | 0.0 | 0.0 | 0.3 | 0.3 | **1.2** | +0.2 | TIGHT | 1.1-1.4 |
| Sneak-peek puzzles | 3.0 | 1.3 | 1.5 | 3.0 | 0.4 | 0.2 | **6.5** | +3.5 | OVER | 5.9-6.5 |
| Warm-up game + quick questions | 4.0 | 0.7 | 3.5 | 2.0 | 0.8 | 0.1 | **7.2** | +3.2 | OVER | 6.5-7.4 |
| Explore (pairs, objects) | 10.0 | 1.3 | 2.0 | 9.0 | 3.8 | 0.3 | **16.4** | +6.4 | OVER | 15.2-17.6 |
| Mini-lesson (7 slides) | 12.0 | 1.4 | 4.2 | 0.0 | 2.9 | 0.2 | **8.7** | -3.3 | LOOSE | 3.5-9.3 |
| Brain break | 4.0 | 0.2 | 0.0 | 3.0 | 0.8 | 0.1 | **4.1** | +0.1 | TIGHT | 4.0-4.1 |
| WS-a  Start + page 1 (pairs) | 16.0 | 1.6 | 0.5 | 17.0 | 5.4 | 0.3 | **24.9** | +8.9 | OVER | 22.3-25.9 |
| WS-b  Check page 1 | 3.0 | 0.3 | 1.5 | 0.0 | 0.4 | 0.0 | **2.2** | -0.8 | TIGHT | 2.1-2.3 |
| WS-c  Teaching before page 2 | 5.0 | 1.1 | 1.1 | 0.0 | 1.2 | 0.0 | **3.5** | -1.5 | OK | 2.1-3.7 |
| WS-d  Page 2 solo (priority items) | 18.0 | 0.8 | 0.0 | 8.0 | 0.9 | 0.0 | **9.8** | -8.2 | LOOSE | 9.3-9.8 |
| WS-e  Check page 2 | 4.0 | 0.2 | 1.5 | 0.0 | 0.4 | 0.0 | **2.1** | -1.9 | OK | 2.0-2.2 |
| Talk time | 5.0 | 0.4 | 2.0 | 2.0 | 1.4 | 0.2 | **6.0** | +1.0 | TIGHT | 4.3-7.1 |
| Exit ticket + closing | 2.0 | 0.4 | 0.5 | 3.0 | 0.4 | 0.1 | **4.5** | +2.5 | OVER | 4.4-4.6 |
| Looking back | 2.0 | 0.7 | 0.0 | 2.0 | 0.7 | 0.2 | **3.5** | +1.5 | TIGHT | 3.5-3.6 |
| Certificates + last stamp (slide "end") | 1.0 | 1.5 | 2.0 | 0.0 | 1.1 | 0.2 | **4.7** | +3.7 | OVER | 4.7-4.8 |
| **Worksheet total (a-e)** | 46.0 | | | | | | **42.4** | -3.6 | LOOSE | |

Total needed (worksheet at priority items only): best 90.9 / typical 105.3 / slow 110.5 min. As scripted (worksheet runs its full 46): best 99.0 / typical 108.9 / slow 112.5. Worksheet time left after the other parts take what they need (typical): 27.1 of 46 scripted; spare after priority items: -15.3.


**Reading it.** The only lesson that fails even for a lean tutor (best case 90.9). Page 1 is 17 min of guess-and-check, chickens and goats, and working backwards for an 11 min window (a Core page that reads like Think Harder). Explore has four puzzle cards for 10 min, and four cards take 12+ min even without setting up. The exit ticket (12 heads, 34 legs, "show your way in") is scheduled at 2 min (85-87), the shortest slot of the level, for the hardest exit task. The final minute (89-90, slide "end") asks the tutor to hand out certificates and stamped journals, ask each child for a favourite puzzle and a way in, and tell each child something specific: about 4.7 min for 8 children, not 1. The guide has no segment, no REC cue and no budget for this final minute.


## 4. Workbook block: how many questions do children finish?


| L | Page-1 items | Page-1 window | LOW p1 | MID p1 | HIGH p1 | Page-2 window (scripted / squeezed) | LOW p2 prio+choice | MID | HIGH |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | 3 (10.0 min) | 11.0 | 1/3 | 3/3 | 3/3 | 16.5 / 11.5 | 1/2+0/1 -> 1/2+0/1 | 2/2+0/1 -> 2/2+0/1 | 2/2+1/1 -> 2/2+1/1 |
| 2 | 3 (14.5 min) | 11.0 | 1/3 | 2/3 | 3/3 | 16.5 / 12.0 | 2/3+0/2 -> 1/3+0/2 | 3/3+1/2 -> 3/3+0/2 | 3/3+2/2 -> 3/3+2/2 |
| 3 | 3 (13.8 min) | 11.0 | 1/3 | 2/3 | 3/3 | 16.5 / 13.9 | 2/3+0/1 -> 2/3+0/1 | 3/3+1/1 -> 3/3+0/1 | 3/3+1/1 -> 3/3+1/1 |
| 4 | 3 (10.0 min) | 11.0 | 1/3 | 3/3 | 3/3 | 16.5 / 12.1 | 2/2+0/1 -> 1/2+0/1 | 2/2+1/1 -> 2/2+0/1 | 2/2+1/1 -> 2/2+1/1 |
| 5 | 3 (10.7 min) | 11.0 | 1/3 | 3/3 | 3/3 | 16.5 / 11.3 | 2/2+0/1 -> 1/2+0/1 | 2/2+1/1 -> 2/2+0/1 | 2/2+1/1 -> 2/2+1/1 |
| 6 | 2 (13.0 min) | 9.0 | 0/2 | 1/2 | 2/2 | 16.5 / 13.4 | 2/2+0/2 -> 2/2+0/2 | 2/2+2/2 -> 2/2+2/2 | 2/2+2/2 -> 2/2+2/2 |
| 7 | 3 (13.5 min) | 11.0 | 1/3 | 2/3 | 3/3 | 16.5 / 10.8 | 1/2+0/1 -> 1/2+0/1 | 2/2+0/1 -> 1/2+0/1 | 2/2+1/1 -> 2/2+0/1 |
| 8 | 3 (11.5 min) | 11.0 | 1/3 | 2/3 | 3/3 | 16.5 / 11.5 | 2/2+0/1 -> 1/2+0/1 | 2/2+1/1 -> 2/2+0/1 | 2/2+1/1 -> 2/2+1/1 |
| 9 | 2 (10.5 min) | 11.0 | 1/2 | 2/2 | 2/2 | 16.5 / 11.1 | 1/2+0/1 -> 1/2+0/1 | 2/2+1/1 -> 2/2+0/1 | 2/2+1/1 -> 2/2+1/1 |
| 10 | 3 (17.0 min) | 11.0 | 0/3 | 1/3 | 2/3 | 16.5 / 3.0 | 2/2+0/1 -> 0/2+0/1 | 2/2+1/1 -> 0/2+0/1 | 2/2+1/1 -> 1/2+0/1 |

Reading: the first "p1" columns count page-1 questions finished in the pairs window (16 minutes minus the 2 min start and the 3 min of breakout moves = 11 minutes; Lesson 6 has the 2-minute teachfan slide first = 9 minutes). The "p2" columns show priority questions finished + choice questions finished in the 16.5 min of the solo window, before and after (arrow) the window is squeezed by what the other parts really need (tutor skipping optional slides).

* **Page 1 is sized for a HIGH child.** A MIDDLE child finishes all of page 1 in lessons 1, 4, 5, 9 and not in the other 6 (L2, L3, L7, L8 finish 2 of 3, L6 1 of 2, L10 1 of 3). A LOW child finishes one page-1 question in every lesson except L6 and L10 (none).
* **Page 2 (solo).** With the windows as scripted a MIDDLE child finishes the priority questions in 10 of 10 lessons and a LOW child 1 or 2 of them. Once the earlier parts take their natural length (the lean tutor), a MIDDLE child loses a priority question in L7 (1 of 2 left), L10 (0 of 2 left); a LOW child loses one in L2 (2 to 1 of 3), L4 (2 to 1 of 2), L5 (2 to 1 of 2), L8 (2 to 1 of 2), L10 (2 to 0 of 2).
* **Think Harder, Go further and the Investigation have no slot.** Only HIGH children get to them: with the scripted windows a HIGH child has 10 to 15 minutes spare across the two worksheet pages (13 on average), which is one or two Think Harder items; MIDDLE and LOW children have none and the printed text sends them to take-home.

## 5. Where the time goes


| L | Speak | Wait | Activity | Transition | REC | Total (worksheet at priority) | Lean script (skip optional + note ASKs) | Slide changes (n x 25 s) | Breakout moves (4 x 90 s + 60 s pair talk) |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | 13.6 | 23.5 | 40.5 | 20.0 | 2.0 | 99.6 | 87.5 | 24 (10.0 min) | 7.0 |
| 2 | 11.5 | 21.3 | 44.0 | 20.0 | 2.0 | 98.8 | 88.9 | 24 (10.0 min) | 7.0 |
| 3 | 12.5 | 25.8 | 44.3 | 20.4 | 2.0 | 104.9 | 89.9 | 25 (10.4 min) | 7.0 |
| 4 | 11.4 | 22.4 | 39.4 | 20.8 | 2.0 | 96.0 | 84.4 | 26 (10.8 min) | 7.0 |
| 5 | 11.2 | 21.1 | 40.7 | 20.4 | 2.0 | 95.4 | 85.7 | 25 (10.4 min) | 7.0 |
| 6 | 11.6 | 21.7 | 38.6 | 20.0 | 2.0 | 93.9 | 84.0 | 24 (10.0 min) | 7.0 |
| 7 | 13.9 | 23.7 | 44.5 | 20.4 | 2.0 | 104.5 | 91.5 | 25 (10.4 min) | 7.0 |
| 8 | 11.5 | 22.1 | 40.5 | 20.0 | 2.0 | 96.1 | 84.8 | 24 (10.0 min) | 7.0 |
| 9 | 11.3 | 19.1 | 41.5 | 19.6 | 2.0 | 93.4 | 85.3 | 23 (9.6 min) | 7.0 |
| 10 | 12.7 | 20.4 | 49.0 | 21.1 | 2.1 | 105.3 | 98.3 | 25 (10.4 min) | 7.0 |
| mean | 12.1 | 22.1 | 42.3 | 20.3 | 2.0 | | | | |

Three biggest time sinks across the level (typical tutor):

1. **Waiting and hold-ups, 22 min per lesson.** Thirty seconds for each of the 5 warm-up questions, 3 explore questions, the six answer-check questions, 2 sneak-peek hold-ups, the prediction and the talk time; plus 2 to 5 "your turn" and ASK interruptions in the mini-lesson. The script budgets these at a few seconds each.
2. **Transitions, 20 min per lesson.** 23 to 26 slide changes (about 10 min), four breakout moves and the worksheet start (about 8 min), greetings and the 15 s goodbye. The pill timetable on the slides (one badge per slide, as short as one minute) has no time for changing slides.
3. **Task size in the explore and on worksheet page 1.** Explore needs 12.3 to 16.4 min (scripted 10); page 1 needs 17.5 to 24.9 min including the start (scripted 16). Hands-on tasks in L8, L9, L10 and the 17-min page 1 of L10 are the extreme cases. Smaller items: the sneak-peek puzzles (6.5 against 3) and the Looking back routine (3.5 against 2).

Other findings about the plan:

* **Slide counts are similar, not unusual:** 27 (L9) to 30 (L4), 28.5 on average, 24 live slides after the four take-home slides. L4 has the most (30), L9 the fewest.
* **Script word counts:** SAY lines 287 (L4) to 418 (L7), median 322. L7 is unusually large (+30%), driven by a 4-paragraph, 207-word think-aloud; L1 (345) and L8 (344) are next. Slide text is heaviest on L7 (2 180 visible words in the deck, 1 825 on the live slides; median about 1 960 and 1 600) and on single slides: the sneak-peek slide carries up to 144 words and L10's warm-up slide 163 words.
* **Unscheduled or inconsistent items found while walking through:** L3 trytrick and teachchain have no minute badge; the explore slides are badged 8-13 and 13-18 while the guide says pencils down at 16; L6 page 1 has two questions yet the printed line says "after question 3" (also true of L9); the L10 final minute has no guide segment, no REC cue and no budget; L10 slide `end` notes say "Minutes 88 to 90" and the badge says 89-90.
* **REC cue lines** are not "under ten seconds": at 135 wpm the average is 11.9 s and the worksheet cue is 17 s. Over a lesson that is 2.0 min of speech, and it also adds ten "Recording: pause now..." sentences that a live class hears.

## 6. Fixes, with exact new budgets (total 90 in every lesson)

All numbers in this section come from the same model re-run with the fixes switched on (`--fix` tables in the helper; typical tutor). "Need after fixes" shows the best / typical / slow figure for each part so a reader can see the margin.

**F1 Re-budget the clock.** The scripted splits (1 / 3 / 4 / 10 / 12 / 4 / 46 / 5 / 3 / 2) assume zero overhead. With the model's constants the lead-in parts need roughly 1.5 / 5-5.5 / 5 / 11.5-14.5, the closing parts 3.5 / 2.5-4.5 / 3.5. The worksheet gives back 3-5 minutes and takes whatever is left, with a cushion inside page 2 (F11).
**F2 Sneak-peek puzzles.** Budget 5-5.5 min (minutes 1.5-7). Give 60 s for puzzle 1 (the objects/drawing one) and 90 s for puzzle 2, then ONE hold-up moment for both papers, not one per puzzle; delete the optional "can anyone find another way?" question. All privacy rules stay (own paper, camera to the tutor only, no names).
**F3 Warm-up.** Keep the game at 90 s and the quick questions at three (Q1 to Q3, the ones that revisit last lesson's idea); move Q4 and Q5 to the Weekly Dose of Thinking Math. Delete the ASK follow-ups in the warm-up speaker notes. Budget 5 min.
**F4 Explore.** Ask two debrief questions, not three: the third ("What do the side lengths tell us about 24?" and its equivalents) is the first slide of the mini-lesson. Online, name the explore as the only breakout of the first half, with a 60 s auto-close timer; budget 11.5-14.5 min (see table).
**F5 Mini-lesson.** Keep the worked examples and the key-idea slide; keep one "your turn" slide (the last one) or none (L2, L3, L7); keep at most three of the speaker-note ASKs. Budget 5-8.5 min. In the typical model the 12 scripted minutes are about 1.5 min of speech, 2.9 min of slide changes and 6-7 min of "your turn" slides (2.4 min each: change, read, 60 s write, 30 s hold-up, reveal) and speaker-note ASKs (30 s each); the typical need is 8.7 to 13.4 min.
**F6 Brain break.** 3.5 min (water and toilet before the game, not after).
**F7 Worksheet.** Keep Start here / check / short teaching / solo page, but re-set the windows to the tables below (page 1 and the opening need 16.5-19 min once the 2 min start and 2 breakout moves are counted). Skip every "your turn"/"Optional" slide in the teaching block and limit speaker-note ASKs to three.
**F8 Talk time.** Pair talk 60 s (no breakout: online, "tell the grown-up beside you, or write one sentence"); volunteers first; the second discussion question moves to the Weekly Dose. Budget 3.5-4 min.
**F9 Looking back.** Keep the child's 2 minutes untouched. Shorten the first SAY paragraph to one sentence ("Turn to page 3, the Looking back box. Write, tick or pass. Two minutes, no talking.") because the printed box already says the rest; keep the model line and the "still stuck" line. Budget 3.5 min (2 child + 1.5 routine).
**F10 Do not change** the answers, the tier split (Core approachable / Think Harder / Challenge), the pass option or the "no marking, no names" rules: every fix above removes optional material, repeats or waiting, or moves minutes between parts.
**F11 Standing cushion.** Hold 2-3 minutes inside the page-2 solo block (WS-d) as an unallocated buffer. If earlier parts overrun, the tutor spends the buffer first, then the choice questions at the end of page 2, and never the checks, exit ticket or Looking back. In lessons where the cushion is above 4 minutes the extra is the printed choice question (L4 Q6, L5 Q6, L8 Q6, L9 Q5) or, in L6, the first Think Harder item.

### Per-lesson fixes and budgets


### After-fix summary

| L | Opening | Sneak | Warm-up | Explore | Mini | Break | Worksheet (a+b+c+d+e) | Talk | Exit | Looking back | Final minute | Need after fixes best / typical / slow | Cushion (typical) |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | 1.5 | 5.5 | 5.5 | 12.0 | 8.0 | 3.5 | 43.5 (18.0 + 2.5 + 3.5 + 17.0 + 2.5) | 3.5 | 3.5 | 3.5 | - | 74.7 / 85.8 / 89.8 | 4.2 |
| 2 | 1.5 | 5.0 | 5.0 | 13.0 | 5.0 | 3.5 | 47.0 (17.5 + 2.0 + 4.0 + 20.0 + 3.5) | 3.5 | 3.0 | 3.5 | - | 76.8 / 85.8 / 89.8 | 4.2 |
| 3 | 1.5 | 5.0 | 5.0 | 12.0 | 5.0 | 4.0 | 48.0 (16.5 + 2.0 + 2.5 + 23.0 + 4.0) | 3.5 | 2.5 | 3.5 | - | 77.5 / 85.4 / 89.2 | 4.6 |
| 4 | 1.5 | 5.0 | 5.0 | 12.5 | 8.0 | 3.5 | 44.0 (17.5 + 2.5 + 3.5 + 18.0 + 2.5) | 4.0 | 3.0 | 3.5 | - | 72.4 / 82.6 / 86.7 | 7.4 |
| 5 | 1.5 | 5.0 | 5.0 | 13.5 | 8.0 | 3.5 | 43.0 (18.5 + 2.0 + 5.0 + 15.5 + 2.0) | 3.5 | 3.5 | 3.5 | - | 73.5 / 84.9 / 89.0 | 5.1 |
| 6 | 1.5 | 5.0 | 5.0 | 11.5 | 7.5 | 3.5 | 46.0 (17.5 + 1.5 + 2.5 + 22.0 + 2.5) | 3.5 | 3.0 | 3.5 | - | 67.7 / 76.2 / 80.2 | 13.8 |
| 7 | 1.5 | 5.0 | 5.0 | 12.0 | 5.5 | 3.5 | 46.0 (16.0 + 2.0 + 3.5 + 21.0 + 3.5) | 4.0 | 4.0 | 3.5 | - | 76.4 / 85.9 / 89.8 | 4.1 |
| 8 | 1.5 | 5.0 | 5.0 | 14.0 | 8.5 | 3.5 | 42.5 (19.0 + 2.5 + 3.5 + 15.0 + 2.5) | 4.0 | 2.5 | 3.5 | - | 73.2 / 83.5 / 87.5 | 6.5 |
| 9 | 1.5 | 5.0 | 5.0 | 14.5 | 6.5 | 3.5 | 44.0 (18.0 + 2.0 + 4.0 + 17.5 + 2.5) | 3.5 | 3.0 | 3.5 | - | 73.3 / 83.3 / 87.3 | 6.7 |
| 10 | 1.5 | 5.0 | 5.0 | 13.0 | 6.5 | 3.5 | 41.5 (16.5 + 1.5 + 3.5 + 17.0 + 3.0) | 3.5 | 4.5 | 3.5 | 2.5 | 77.3 / 86.6 / 90.8 | 3.4 |

Every row adds to 90.0. The five worksheet figures are WS-a + WS-b + WS-c + WS-d + WS-e (page 2 solo includes the standing cushion). A SLOW tutor uses almost all of the cushion in L1, L2, L3, L5, L7 and L9-L10 (L10 ends 0.8 min over); BEST tutors finish 12 to 22 minutes early and have that time for the Think Harder, Go further and Investigation pages.


#### Lesson 1

- Warm-up: keep Q1-Q3 (7 a factor of 56? / first five multiples of 6 / a common multiple of 4 and 6); move Q4 (45 a multiple of 4?) and Q5 (18 as a product, 3 ways) to the Weekly Dose.
- Mini-lesson: cut try1 (22-23, factor pairs on whiteboards); keep try2 (28-29, "when do they meet?"). Keep ASKs on teach1 ("Is 5 a factor of 24?"), we2 ("Could we use 4 bags?") and we3 ("Ravi says 6 x 8 = 48...").
- Worksheet teaching: ASKs only on teachriddle and teachtest.
- Explore: drop debrief question 3.

worksheet window 43.5 min (was 46), page-2 spare after priority items 3.2 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.2 / 1.4 |
| Sneak-peek puzzles | 3.0 | 5.5 | 1.5-7.0 | 5.3 / 5.4 / 5.5 |
| Warm-up game + quick questions | 4.0 | 5.5 | 7.0-12.5 | 5.1 / 5.2 / 5.4 |
| Explore (pairs, objects) | 10.0 | 12.0 | 12.5-24.5 | 10.7 / 11.9 / 13.0 |
| Mini-lesson (6 slides) | 12.0 | 8.0 | 24.5-32.5 | 3.7 / 7.8 / 8.3 |
| Brain break | 4.0 | 3.5 | 32.5-36.0 | 3.5 / 3.6 / 3.7 |
| WS-a  Start + page 1 (pairs) | 16.0 | 18.0 | 36.0-54.0 | 15.7 / 18.0 / 19.1 |
| WS-b  Check page 1 | 3.0 | 2.5 | 54.0-56.5 | 2.4 / 2.5 / 2.6 |
| WS-c  Teaching before page 2 | 5.0 | 3.5 | 56.5-60.0 | 2.2 / 3.6 / 3.8 |
| WS-d  Page 2 solo (priority items) | 18.0 | 17.0 | 60.0-77.0 | 12.6 / 13.8 / 13.9 |
| WS-e  Check page 2 | 4.0 | 2.5 | 77.0-79.5 | 2.3 / 2.4 / 2.5 |
| Talk time | 5.0 | 3.5 | 79.5-83.0 | 3.5 / 3.6 / 3.6 |
| Exit ticket + closing | 3.0 | 3.5 | 83.0-86.5 | 3.4 / 3.5 / 3.5 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.5 |
| Sum | 90.0 | 90.0 | | typical need 85.8; cushion 4.2 |



#### Lesson 2

- Mini-lesson: cut both "your turn" slides (try1 20-21, try2 23-25); keep we1-we4 and key; two ASKs. This is the one lesson where the mini-lesson is shortened to 5 min, and it is the cheapest cut because rounding is practised again in explore and on both worksheet pages.
- Warm-up: keep Q1-Q3 (the 7 in 47 352 / sixty thousand and forty-five / 1 000 more than 59 600); move Q4 and Q5 (40 000 + 3 000 + 50 + 8; 36 815 to the nearest 1 000) to the Weekly Dose.
- Worksheet: pairs do Q1 and Q2 (10 min); Q3 (the bakery) is the first solo question; its answer is checked with page 2 (WS-e takes 30 s longer). Q2a and Q2b stay (no change of answer or tier).

worksheet window 47.0 min (was 46), page-2 spare after priority items 3.2 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.2 / 1.3 / 1.5 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 5.0 / 5.1 / 5.2 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 4.9 / 5.1 / 5.2 |
| Explore (pairs, objects) | 10.0 | 13.0 | 11.5-24.5 | 11.7 / 12.8 / 14.0 |
| Mini-lesson (5 slides) | 12.0 | 5.0 | 24.5-29.5 | 3.3 / 4.8 / 5.3 |
| Brain break | 4.0 | 3.5 | 29.5-33.0 | 3.5 / 3.6 / 3.7 |
| WS-a  Start + page 1 (pairs) | 16.0 | 17.5 | 33.0-50.5 | 15.1 / 17.4 / 18.4 |
| WS-b  Check page 1 | 3.0 | 2.0 | 50.5-52.5 | 1.6 / 1.7 / 1.8 |
| WS-c  Teaching before page 2 | 5.0 | 4.0 | 52.5-56.5 | 2.0 / 4.0 / 4.3 |
| WS-d  Page 2 solo (priority items) | 18.0 | 20.0 | 56.5-76.5 | 15.7 / 16.8 / 16.8 |
| WS-e  Check page 2 | 4.0 | 3.5 | 76.5-80.0 | 3.1 / 3.3 / 3.5 |
| Talk time | 5.0 | 3.5 | 80.0-83.5 | 3.5 / 3.6 / 3.7 |
| Exit ticket + closing | 3.0 | 3.0 | 83.5-86.5 | 2.9 / 3.0 / 3.1 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.5 |
| Sum | 90.0 | 90.0 | | typical need 85.8; cushion 4.2 |



#### Lesson 3

- Mini-lesson: cut try1 (20-22), try2 (24-25) and try3 (28-29); keep teach1, we1, we2 and key (4 slides), two ASKs. The three "your turn" slides alone cost about 7 min.
- Worksheet teaching: drop trytrick and teachchain (Q7, the choice question, is taught only to a child who picks it; put teachchain in the take-home pack); keep teachback and teachbar.
- Worksheet: pairs do Q1 and Q2 (9 min of work); Q3 (brackets in 4 + 8 x 5 - 3) is solo, first. Q2(d), the sentence with three blanks, stays as a pass-allowed item.

worksheet window 48.0 min (was 46), page-2 spare after priority items 3.2 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.3 / 1.5 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.8 / 4.9 / 5.0 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 4.7 / 4.9 / 5.1 |
| Explore (pairs, objects) | 10.0 | 12.0 | 11.5-23.5 | 10.6 / 11.7 / 12.9 |
| Mini-lesson (4 slides) | 12.0 | 5.0 | 23.5-28.5 | 3.5 / 5.0 / 5.4 |
| Brain break | 4.0 | 4.0 | 28.5-32.5 | 3.6 / 3.7 / 3.8 |
| WS-a  Start + page 1 (pairs) | 16.0 | 16.5 | 32.5-49.0 | 14.3 / 16.4 / 17.5 |
| WS-b  Check page 1 | 3.0 | 2.0 | 49.0-51.0 | 1.6 / 1.7 / 1.8 |
| WS-c  Teaching before page 2 | 5.0 | 2.5 | 51.0-53.5 | 1.3 / 2.6 / 2.8 |
| WS-d  Page 2 solo (priority items) | 18.0 | 23.0 | 53.5-76.5 | 19.0 / 19.8 / 19.9 |
| WS-e  Check page 2 | 4.0 | 4.0 | 76.5-80.5 | 3.8 / 3.9 / 4.1 |
| Talk time | 5.0 | 3.5 | 80.5-84.0 | 3.6 / 3.6 / 3.7 |
| Exit ticket + closing | 3.0 | 2.5 | 84.0-86.5 | 2.3 / 2.3 / 2.4 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.5 |
| Sum | 90.0 | 90.0 | | typical need 85.4; cushion 4.6 |



#### Lesson 4

- Warm-up: keep Q1-Q3 (1/2 of 18 / 1/4 of 20 / 2/3 = ?/12); move Q4 (3/4 + 1/8) and Q5 (1 - 3/10) to the Weekly Dose.
- Mini-lesson: cut try1 (22-23); keep try2 (28-29); ASKs on teach1, we1 and teachline.
- Worksheet teaching: skip trycompare; ASK only on teachcompare2.
- The cushion is 6.4 min: 2 min stays as buffer and 4 min is Q6 (fractions with denominator 12 between 1/3 and 3/4), which now fits as a real choice question.

worksheet window 44.0 min (was 46), page-2 spare after priority items 6.5 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.3 / 1.5 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.8 / 4.9 / 5.0 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 4.8 / 4.9 / 5.1 |
| Explore (pairs, objects) | 10.0 | 12.5 | 11.5-24.0 | 11.4 / 12.6 / 13.7 |
| Mini-lesson (6 slides) | 12.0 | 8.0 | 24.0-32.0 | 3.6 / 8.1 / 8.6 |
| Brain break | 4.0 | 3.5 | 32.0-35.5 | 3.6 / 3.6 / 3.7 |
| WS-a  Start + page 1 (pairs) | 16.0 | 17.5 | 35.5-53.0 | 15.3 / 17.5 / 18.6 |
| WS-b  Check page 1 | 3.0 | 2.5 | 53.0-55.5 | 2.2 / 2.3 / 2.4 |
| WS-c  Teaching before page 2 | 5.0 | 3.5 | 55.5-59.0 | 2.6 / 3.5 / 3.8 |
| WS-d  Page 2 solo (priority items) | 18.0 | 18.0 | 59.0-77.0 | 11.1 / 11.5 / 11.6 |
| WS-e  Check page 2 | 4.0 | 2.5 | 77.0-79.5 | 2.2 / 2.2 / 2.3 |
| Talk time | 5.0 | 4.0 | 79.5-83.5 | 3.6 / 3.7 / 3.8 |
| Exit ticket + closing | 3.0 | 3.0 | 83.5-86.5 | 3.0 / 3.1 / 3.2 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.3 / 3.4 |
| Sum | 90.0 | 90.0 | | typical need 82.6; cushion 7.4 |



#### Lesson 5

- Warm-up: keep Q1-Q3 (the 7 in 3.475 / 6 tenths and 4 thousandths / 0.8 or 0.75); move Q4 and Q5 (round 4.68; $5 - $3.05) to the Weekly Dose.
- Mini-lesson: cut try1 (22-23); keep try2 (28-29); ASKs on teach1, we2 and the first ASK on we3.
- Explore: stop the hands-on at 6 min and finish ordering in the debrief (question 1 and 2 only).
- Worksheet teaching: no slide is optional (4 slides, 3.5-5 min); limit the ASKs to three.

worksheet window 43.0 min (was 46), page-2 spare after priority items 4.1 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.2 / 1.4 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.8 / 4.9 / 5.0 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 5.0 / 5.1 / 5.3 |
| Explore (pairs, objects) | 10.0 | 13.5 | 11.5-25.0 | 12.0 / 13.2 / 14.4 |
| Mini-lesson (6 slides) | 12.0 | 8.0 | 25.0-33.0 | 3.4 / 7.8 / 8.3 |
| Brain break | 4.0 | 3.5 | 33.0-36.5 | 3.4 / 3.5 / 3.6 |
| WS-a  Start + page 1 (pairs) | 16.0 | 18.5 | 36.5-55.0 | 16.1 / 18.3 / 19.3 |
| WS-b  Check page 1 | 3.0 | 2.0 | 55.0-57.0 | 2.1 / 2.1 / 2.2 |
| WS-c  Teaching before page 2 | 5.0 | 5.0 | 57.0-62.0 | 2.7 / 4.8 / 5.1 |
| WS-d  Page 2 solo (priority items) | 18.0 | 15.5 | 62.0-77.5 | 10.8 / 11.4 / 11.5 |
| WS-e  Check page 2 | 4.0 | 2.0 | 77.5-79.5 | 2.0 / 2.1 / 2.2 |
| Talk time | 5.0 | 3.5 | 79.5-83.0 | 3.6 / 3.6 / 3.7 |
| Exit ticket + closing | 3.0 | 3.5 | 83.0-86.5 | 3.3 / 3.4 / 3.5 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.5 |
| Sum | 90.0 | 90.0 | | typical need 84.9; cushion 5.1 |



#### Lesson 6

- Page 1 holds Q1 and Q2 only. Change the guide line and the slide ws1 text "after question 3" to "after question 2 (the last on this page)".
- Q1: pair work is a real pair task here: each child estimates and measures two angles, then checks the partner's two (about 4.5 min, not 8).
- Cushion is 13.4 min against a 2-3 min target. Use it as follows: promote Q5 and Q6 from "choices" to "aim for" (3.0 + 1.5 min), schedule a 4-minute Think Harder slot (workbook Think Harder 1 or 2) before the check, and keep a 4-5 min cushion. Alternatively give the Explore 1 extra minute and the Sneak-peek 0.5 min and keep the rest as cushion.
- Mini-lesson: cut try1 (21-23); keep try2 (27-28).

worksheet window 46.0 min (was 46), page-2 spare after priority items 13.4 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.2 / 1.4 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.7 / 4.8 / 4.9 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 4.8 / 5.0 / 5.1 |
| Explore (pairs, objects) | 10.0 | 11.5 | 11.5-23.0 | 10.4 / 11.6 / 12.8 |
| Mini-lesson (4 slides) | 12.0 | 7.5 | 23.0-30.5 | 3.4 / 7.2 / 7.5 |
| Brain break | 4.0 | 3.5 | 30.5-34.0 | 3.5 / 3.6 / 3.6 |
| WS-a  Start + page 1 (pairs) | 16.0 | 17.5 | 34.0-51.5 | 15.7 / 17.6 / 18.8 |
| WS-b  Check page 1 | 3.0 | 1.5 | 51.5-53.0 | 1.5 / 1.6 / 1.6 |
| WS-c  Teaching before page 2 | 5.0 | 2.5 | 53.0-55.5 | 2.0 / 2.3 / 2.5 |
| WS-d  Page 2 solo (priority items) | 18.0 | 22.0 | 55.5-77.5 | 8.1 / 8.6 / 8.7 |
| WS-e  Check page 2 | 4.0 | 2.5 | 77.5-80.0 | 2.6 / 2.6 / 2.7 |
| Talk time | 5.0 | 3.5 | 80.0-83.5 | 3.5 / 3.6 / 3.7 |
| Exit ticket + closing | 3.0 | 3.0 | 83.5-86.5 | 3.1 / 3.1 / 3.2 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.5 |
| Sum | 90.0 | 90.0 | | typical need 76.2; cushion 13.8 |



#### Lesson 7

- SAY: the 4-paragraph, 207-word think-aloud is the longest of the level. Its 4th paragraph and the slide we3 (area 20: list the rectangles, perimeters 42, 24, 18) repeat the 12-tile explore and Q2 (area 24), so drop both (about 50 words and one slide change).
- Mini-lesson: cut try1 (22-23) and try2 (26-27); keep teach1, we1, we2, key; ASKs on teach1, we1, we2.
- Worksheet: pair task for Q1: partner A splits the figure into two rectangles, partner B uses big rectangle minus the missing piece, then they compare (about 4 min instead of 6). Q3 (six tiles, smallest and largest perimeter) is the first solo question.
- Exit ticket: keep the question; budget 4 min (2.5 min of writing) for this lesson only.

worksheet window 46.0 min (was 46), page-2 spare after priority items 3.3 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.2 / 1.3 / 1.5 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.9 / 5.0 / 5.1 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 5.0 / 5.1 / 5.3 |
| Explore (pairs, objects) | 10.0 | 12.0 | 11.5-23.5 | 10.6 / 11.8 / 13.0 |
| Mini-lesson (4 slides) | 12.0 | 5.5 | 23.5-29.0 | 3.6 / 5.6 / 5.9 |
| Brain break | 4.0 | 3.5 | 29.0-32.5 | 3.4 / 3.5 / 3.6 |
| WS-a  Start + page 1 (pairs) | 16.0 | 16.0 | 32.5-48.5 | 13.3 / 15.9 / 17.0 |
| WS-b  Check page 1 | 3.0 | 2.0 | 48.5-50.5 | 1.7 / 1.8 / 1.8 |
| WS-c  Teaching before page 2 | 5.0 | 3.5 | 50.5-54.0 | 2.1 / 3.5 / 3.7 |
| WS-d  Page 2 solo (priority items) | 18.0 | 21.0 | 54.0-75.0 | 16.4 / 17.7 / 17.8 |
| WS-e  Check page 2 | 4.0 | 3.5 | 75.0-78.5 | 3.3 / 3.5 / 3.7 |
| Talk time | 5.0 | 4.0 | 78.5-82.5 | 3.6 / 3.7 / 3.8 |
| Exit ticket + closing | 3.0 | 4.0 | 82.5-86.5 | 4.0 / 4.0 / 4.1 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.5 |
| Sum | 90.0 | 90.0 | | typical need 85.9; cushion 4.1 |



#### Lesson 8

- Explore: ask families to cut the six squares (from the Square grid cut-out page) before the lesson, so minutes 12.5-24.5 are joining, folding and drawing, not cutting. Budget 14 min (hands-on 7 min).
- Mini-lesson: cut try1 (23-25); keep try2 (27-29); ASKs on teach1, we1, we2.
- Worksheet teaching: skip try3.
- Page 1 Q1 (six nets): LOW children finish only Q1 of 3 on page 1 even at the new 18.5-19 min window; Q2 and Q3 are the 'carry on' questions.
- Exit ticket is 1 min of child time: closing can end at 2.5 min.

worksheet window 42.5 min (was 46), page-2 spare after priority items 4.3 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.3 / 1.5 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.8 / 4.9 / 5.0 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 4.8 / 4.9 / 5.1 |
| Explore (pairs, objects) | 10.0 | 14.0 | 11.5-25.5 | 12.6 / 13.7 / 14.9 |
| Mini-lesson (5 slides) | 12.0 | 8.5 | 25.5-34.0 | 3.7 / 8.2 / 8.7 |
| Brain break | 4.0 | 3.5 | 34.0-37.5 | 3.4 / 3.5 / 3.6 |
| WS-a  Start + page 1 (pairs) | 16.0 | 19.0 | 37.5-56.5 | 16.9 / 18.8 / 19.9 |
| WS-b  Check page 1 | 3.0 | 2.5 | 56.5-59.0 | 2.3 / 2.4 / 2.4 |
| WS-c  Teaching before page 2 | 5.0 | 3.5 | 59.0-62.5 | 2.0 / 3.4 / 3.7 |
| WS-d  Page 2 solo (priority items) | 18.0 | 15.0 | 62.5-77.5 | 10.3 / 10.7 / 10.7 |
| WS-e  Check page 2 | 4.0 | 2.5 | 77.5-80.0 | 2.2 / 2.2 / 2.3 |
| Talk time | 5.0 | 4.0 | 80.0-84.0 | 3.7 / 3.8 / 3.8 |
| Exit ticket + closing | 3.0 | 2.5 | 84.0-86.5 | 2.3 / 2.4 / 2.5 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.4 |
| Sum | 90.0 | 90.0 | | typical need 83.5; cushion 6.5 |



#### Lesson 9

- Explore: about 14.5 min (7.5 min hands-on: choose a scale, plot about seven points, join them, write three findings; about 3 min debrief; 3 min set-up and breakout moves). The extra minutes come from the mini-lesson, which is loose in the script (6 slides, 2 'your turn' slides).
- Mini-lesson: cut try1 (23-25); keep try2 (27-29); ASKs on we1 only.
- Worksheet: page 1 has two questions (Q1, Q2): the "after question 3" wording is reached on page 2. Say "after Q2" for this lesson.
- Cushion 5.6 min: 2 min buffer + Q5 (two shops, 4.0 min) becomes a real choice question.

worksheet window 44.0 min (was 46), page-2 spare after priority items 5.6 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.3 / 1.5 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.7 / 4.7 / 4.8 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 4.9 / 5.0 / 5.2 |
| Explore (pairs, objects) | 10.0 | 14.5 | 11.5-26.0 | 13.1 / 14.2 / 15.4 |
| Mini-lesson (5 slides) | 12.0 | 6.5 | 26.0-32.5 | 3.3 / 6.5 / 6.9 |
| Brain break | 4.0 | 3.5 | 32.5-36.0 | 3.5 / 3.6 / 3.6 |
| WS-a  Start + page 1 (pairs) | 16.0 | 18.0 | 36.0-54.0 | 15.8 / 18.1 / 19.2 |
| WS-b  Check page 1 | 3.0 | 2.0 | 54.0-56.0 | 1.7 / 1.8 / 1.8 |
| WS-c  Teaching before page 2 | 5.0 | 4.0 | 56.0-60.0 | 2.1 / 4.1 / 4.3 |
| WS-d  Page 2 solo (priority items) | 18.0 | 17.5 | 60.0-77.5 | 11.3 / 11.9 / 11.9 |
| WS-e  Check page 2 | 4.0 | 2.5 | 77.5-80.0 | 2.2 / 2.3 / 2.4 |
| Talk time | 5.0 | 3.5 | 80.0-83.5 | 3.4 / 3.5 / 3.6 |
| Exit ticket + closing | 3.0 | 3.0 | 83.5-86.5 | 2.9 / 3.0 / 3.1 |
| Looking back | 2.0 | 3.5 | 86.5-90.0 | 3.3 / 3.4 / 3.4 |
| Sum | 90.0 | 90.0 | | typical need 83.3; cushion 6.7 |



#### Lesson 10

- Explore: do two puzzle cards in the live lesson (A and B, 6 min of hands-on); C and D go in the take-home pack as the first Think Harder tasks.
- Page 1: Q1a stays (consecutive numbers with product 552); Q1b ($4 pens, $7 notebooks, find ALL the ways, 24-cell table) is moved to take-home; pairs do Q1a and Q2 (about 9 min); Q3 (working backwards) is the first solo question.
- Mini-lesson: cut try1 (22-23); keep try2 (26-27). 
- Exit ticket: budget 4.5 min (it is the heaviest exit task of the level; about 3 min of child time).
- Final minute: replace the per-child comments (8 x ~35 s) by a 2.5-min whole-group close: certificates and journals are posted/sent with a personal sentence the tutor writes before the lesson; live, three volunteers each name one puzzle and one way in (20 s each), the tutor says one sentence about the group, then goodbye. Add a segment '89-90 Certificates and goodbye' to the guide so it gets a budget and a REC cue (the guide has none).

worksheet window 41.5 min (was 46), page-2 spare after priority items 2.4 min

| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |
|---|--:|--:|--:|--:|
| Opening | 1.0 | 1.5 | 0.0-1.5 | 1.1 / 1.2 / 1.4 |
| Sneak-peek puzzles | 3.0 | 5.0 | 1.5-6.5 | 4.9 / 5.0 / 5.0 |
| Warm-up game + quick questions | 4.0 | 5.0 | 6.5-11.5 | 4.9 / 5.0 / 5.2 |
| Explore (pairs, objects) | 10.0 | 13.0 | 11.5-24.5 | 11.5 / 12.7 / 13.8 |
| Mini-lesson (6 slides) | 12.0 | 6.5 | 24.5-31.0 | 3.5 / 6.3 / 6.8 |
| Brain break | 4.0 | 3.5 | 31.0-34.5 | 3.5 / 3.6 / 3.6 |
| WS-a  Start + page 1 (pairs) | 16.0 | 16.5 | 34.5-51.0 | 14.2 / 16.4 / 17.5 |
| WS-b  Check page 1 | 3.0 | 1.5 | 51.0-52.5 | 1.5 / 1.6 / 1.7 |
| WS-c  Teaching before page 2 | 5.0 | 3.5 | 52.5-56.0 | 2.1 / 3.5 / 3.7 |
| WS-d  Page 2 solo (priority items) | 18.0 | 17.0 | 56.0-73.0 | 14.0 / 14.6 / 14.7 |
| WS-e  Check page 2 | 4.0 | 3.0 | 73.0-76.0 | 3.0 / 3.1 / 3.3 |
| Talk time | 5.0 | 3.5 | 76.0-79.5 | 3.3 / 3.4 / 3.5 |
| Exit ticket + closing | 2.0 | 4.5 | 79.5-84.0 | 4.4 / 4.5 / 4.6 |
| Looking back | 2.0 | 3.5 | 84.0-87.5 | 3.3 / 3.4 / 3.5 |
| Certificates + last stamp (slide "end") | 1.0 | 2.5 | 87.5-90.0 | 2.1 / 2.2 / 2.3 |
| Sum | 90.0 | 90.0 | | typical need 86.6; cushion 3.4 |



Read the cushion line: "page-2 spare after priority items" is the budgeted WS-d window minus the priority-item time for a typical tutor; it is the standing buffer plus the choice question time, and it is positive in every lesson (2.3 to 13.4 min). The "cushion" under each table is 90 minus the typical need of all parts, i.e. how much slack remains if everything else runs to the typical figure (3.3 to 13.8 min); keep 2-3 of it as the buffer.

## 7. Standing buffer: yes

Recommendation: a 2-3 minute standing buffer inside the page-2 solo block, shown on the tutor's timeline as "buffer" and nowhere else. Reasons: the model's range for the same lesson is 20 to 27 minutes (e.g. the unfixed plan: L3 spans 82.8 to 110.1), most of that difference is tutor style rather than content, and the worksheet's printed "choice questions" are already the natural place to take it from. A second guard rail: a clock check at the end of the brain break (minute 36 on the new clock); more than 1.5 min behind means skip the next optional item (second 'your turn' slide, the second ASK in WS-c), not the check or the exit ticket.

## 8. Limits of this audit

* Everything is estimated from words counted in the guide, slides and workbook plus judged child times; a stopwatch run with 6 to 8 real children would move any figure by 10 to 20%. The ranking of the problems (sneak-peek, warm-up, explore, page 1) is more reliable than the exact minutes.
* Judged child times were set from the actual task text, once, for a MIDDLE child; they are the main uncertainty. Change `EXPLORE_HANDS`, `EXIT_WRITE` and `ITEMS` in the helper and re-run.
* Tutor behaviour that adds time and is not modelled: repeating answers, tech glitches, a child who needs extra help, questions from parents, "how do you know?" after every answer (the guide asks for it each time, which would add roughly 20 s per answer taken).
* Tutor behaviour that saves time and is not modelled: asking for answers in chat, a whole-class "thumbs", skipping the greeting by name, running page 1 as a whole-group screen share (saves about 3 min).
* The fix tables assume the tutor guide, slide pills and printed notes are updated together; none were edited here.
