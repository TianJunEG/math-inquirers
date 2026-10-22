# Lesson timing audit: Math Inquirers P5 (Level N=5, ages 10-12)

Analysis only. Nothing in content, guides, decks, builds or outputs was edited and nothing was committed. Everything below is an estimate built from the real text (not stopwatch timings). The helper `docs/audit/timing_p5.py` reproduces every number (`python3 docs/audit/timing_p5.py`, add `--plan-md` for the recommended budgets).

## 1. Answer in brief

**No lesson fits 90 minutes as scripted.** Estimated clock time when each worksheet block is held to its scripted length (the lesson cannot be shorter than this unless something is skipped):

| L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|
| 111 | 107 | 109 | 101 | 111 | 107 | 99 | 102 | 112 | 114 |

Ranges (optimistic to pessimistic, waits/activity/transitions plus or minus 15 percent, speech plus or minus 10 percent): L1 99-123; L2 95-118; L3 97-121; L4 90-112; L5 99-123; L6 95-118; L7 89-109; L8 91-112; L9 100-124; L10 101-126. Only the optimistic ends of L4 and L7 touch 90.

- The over-run is spread over the small whole-group parts, not over tutor talk. Averaged over the level, the whole-group parts run about 15 minutes over their budget (explore +4.0, sneak-peek +2.7, talk time +2.5, the two check slides +1.9, exit/close +1.6, mini-lesson +1.5, warm-up +0.8, break +0.6, teaching -0.4) and the opening, which the guide puts "before the clock starts", costs another 1.8-3.6 minutes of the booked session.
- Tutor speech (SAY lines, questions read aloud, REC cues) is only 12.5-15.5 minutes of a lesson (about 15 percent). The big costs are waiting for children (about 23 minutes), activity (about 55 minutes) and transitions (about 19 minutes: roughly 25 slide changes, two moves to and from breakout rooms, finding materials).
- **The worksheet is the one real content problem.** "Start here" (page 1) holds 9 to 21 minutes of work for a middle child, but the block gives about 7-8 working minutes once the 2-minute start-up and the breakout move are paid. A middle pair finishes only 25-71 percent of the parts on page 1 in nine lessons (L4, at 86 percent, is the exception). Page 2 is a menu and is fine, but its plan set is sometimes bigger than its block (L10) and in four lessons it is loose (L1, L3, L4, L8), so the spare minutes sit on the wrong page.
- If the fixed parts take what they need, the worksheet (page 1 plus page 2, scheduled 26 minutes) is left with only 2-17 minutes (L10 2.4, L9 3.9, L1 5.2, L5 5.4, L3 6.8, L6 9.1, L2 9.3, L8 14.4, L4 14.9, L7 16.9).
- Fixes in section 7 bring all ten lessons to exactly 90 with a 1.5-5 minute standing buffer by (a) giving the sneak-peek 4.5, the explore 12-14 and the talk time 5.5 the minutes they really use, (b) trimming page 1 to about 10 minutes of middle-child work and moving the rest to take-home, (c) shrinking page 2 and its teaching slides to what the plan set needs.

## 2. Model and assumptions (identical for every lesson)

Source of the budgets: `p5/guide.js` (the `seg()` calls) and the one timeline in `p5/data.js` (`TIMELINE`). The seg calls are the same for all ten lessons, lesson 10 included: 0-3 sneak-peek, 3-9 warm-up, 9-21 explore, 21-33 mini-lesson, 33-37 brain break, then the workbook block (page 1 in pairs 37-49, check 49-53, short teaching 53-58, page 2 alone 58-72, check 72-76), 76-82 talk time, 82-90 exit ticket (4), reflection (2), stamp and goodbye (2; lesson 10: certificates). The rebuilt PDF `p5/Math_Inquirers_P5_Tutor_Guide.pdf` carries the same seg headings and text for all ten lessons. The REC cue lines are not in the P5 guide yet (`levels/reccues.js` is new and unused by `p5/guide.js`), so they are added in the model.

| Item | Value used |
|---|---|
| Tutor speech (SAY lines, think-aloud, answers given) | 140 words per minute including pauses |
| Questions and tasks read aloud | 130 words per minute |
| Wait after a question to the group | 10 s, plus 20 s to take one or two answers (30 s per group question) |
| Hold up boards / paper to the camera | 30 s |
| Slide change online | 25 s each (every slide shown in the whole-group flow) |
| Move to or from breakout rooms | 90 s out, 60 s back (only where pairs work in breakouts; otherwise 30 s each way in the main room) |
| Handing out / finding materials | 30-120 s by lesson (L4 grid paper and scissors 120, L5 cubes and L8 paper tearing 90, L1 calculators 60 ...) |
| Starting a worksheet | 2 minutes, plus the breakout move and the SAY lines |
| REC cue | 10 s at the start of each of the 9 guide parts (about 1.5 min), plus 15 s once to tell the group the lesson is recorded |
| Greeting | 30 s (naming each child), pre-clock |
| Sneak-peek | 21-word intro, both puzzles read aloud, answers said with one reason, two hold-ups, one volunteer round; children need about 60-90 s per puzzle (judged puzzle by puzzle) |
| Quick questions | 5 per lesson, 30 s each plus reading |
| Warm-up game | judged per game (80-200 s) |
| Explore | pair work judged per task (6-9 min), three regroup questions of 30 s each plus the guesses, 20 s regroup |
| Mini-lesson | 80 percent of the printed words on each worked-example slide spoken, one group question per worked slide, each "Your turn" slide = read aloud + children solve (judged per item, 15-60 s) + hold-up + feedback |
| Worksheet item (middle child) | Core part 1-3 min, longer multi-step or explain parts 3-5 min; a LOW child takes 1.6 times as long, a HIGH child 0.65 times |
| Check slides | 60 s per question (10 s wait + volunteer explains + tutor confirms), +30 s for a heavy question |
| Talk time | pairs talk 2 min, volunteers share 2 min, Investigation first step 2 min, plus regroup and finding the page |
| Exit ticket | question read aloud, children need 1.5-4 min by task, 40 s to show slips, reflection 90 s + reading, stamp and goodbye 64 s (8 children), certificates 160 s |
| Camera / tech glitches | ignored. Every lesson already has no slack, so any glitch lands on the worksheet |

How the tables are read. "Scripted" is the guide minutes. "Need" = speak + wait + activity + transition. Flags: OVER = need exceeds script by 2.0 min or more; TIGHT = 0.75 to 2.0 over; OK = within -3 to +0.75 (any part with less than 0.5 min of slack is effectively zero-slack); LOOSE = script exceeds need by 3 min or more. The two worksheet work blocks (page 1 in pairs, page 2 alone) are time-boxes: children will fill whatever time they get. Their "Need" is the middle-child content need (page 1: all of Start here; page 2: the questions named on the "Page 2 plan" line), and their flag compares that need with the box. Totals are given twice: with both boxes held to their scripted minutes (what the clock does) and with page 1 allowed to run until a middle pair finishes it.

## 3. Results at a glance

| Lesson | Clock total, worksheet blocks held to script | Range | If middle pairs finish page 1 | Worksheet time left (of 26 scripted) | OVER parts | LOOSE parts |
|---|---|---|---|---|---|---|
| 1 Million Puzzles | **111** (+21) | 99-123 | 121 | 5 | Sneak-peek, Explore, WB p1, Check p1, Teaching, Talk | WB p2 |
| 2 Fraction Feats | **107** (+17) | 95-118 | 120 | 9 | Sneak-peek, Explore, WB p1, Talk | - |
| 3 Before and After | **109** (+19) | 97-121 | 113 | 7 | Sneak-peek, Explore, WB p1, Teaching, Talk, Exit/close | WB p2 |
| 4 Triangle Areas | **101** (+11) | 90-112 | 102 | 15 | Sneak-peek, Explore, Talk | WB p2 |
| 5 Volume Vault | **111** (+21) | 99-123 | 120 | 5 | Sneak-peek, Explore, Mini-lesson, WB p1, Talk | - |
| 6 Rate Racers | **107** (+17) | 95-118 | 120 | 9 | Sneak-peek, Explore, WB p1, Talk | - |
| 7 Percentage Puzzles | **99** (+9) | 89-109 | 110 | 17 | Sneak-peek, WB p1, Talk | - |
| 8 Angle Chasers | **102** (+12) | 91-112 | 105 | 14 | WB p1, Talk | WB p2 |
| 9 Pattern Generalisers | **112** (+22) | 100-124 | 121 | 4 | Sneak-peek, Explore, Mini-lesson, WB p1, Talk | - |
| 10 Challenge Day | **114** (+24) | 101-126 | 121 | 2 | Sneak-peek, Explore, Mini-lesson, WB p1, WB p2, Talk, Exit/close | - |

Time sinks across the level, in minutes over budget per lesson (average of the ten): explore +4.0, sneak-peek +2.7, talk time +2.5, check slides +2.0, opening (pre-clock) +2.0, exit/close +1.6, mini-lesson +1.5, break +0.6, and in the worksheet the page-1 content need is on average 7.9 minutes bigger than its block while page 2 is on average 2.9 minutes looser than its block. Warm-up (+0.8) and teaching (-0.4) are the only parts that roughly hold.

Lessons that run long or short: all ten run long. L7 (+9) and L4 (+11) are closest, L8 (+12); L2 and L6 (+17); L3 (+19); L5 and L1 (+21); L9 (+22) and L10 (+24) are the worst because L9/L10 add a very long explore (18 min) and a 14-15 minute mini-lesson on top of the common over-runs. No lesson runs short in total. Parts that are loose: page 2 in L1, L3, L4 and L8 (the "menu" absorbs the spare minutes, so it is not dead time, but it is time the over-full page 1 and the over-full explore could use).

## 4. Cross-level findings

1. **Sneak-peek (3 min) is a 5-6 minute part in every lesson.** Two puzzles at about a minute each is already 2.5 minutes before the two hold-ups, the volunteer round, the intro line and reading the puzzles aloud. L1, L4, L10 are the heaviest (6.0-6.3: card-testing, draw-and-cut, logic with a table).
2. **Explore (12 min) needs 13-18.** Pair work is 6-9 minutes, then 3 regroup questions (2.3 min), 2 slide changes, materials and (L1, L2, L6, L9, L10) a breakout round trip of 2.5 minutes. The scripts say "at about minute 19 pencils down" leaving two minutes for three questions plus collecting guesses; that is about 1.5 minutes short.
3. **Page 1 of the worksheet is double-booked.** The block (37-49) is paid 12 minutes but 2 minutes go to starting, 1.5 to the breakout move, 25 s to the slide and the SAY lines; 7-8 minutes are left for work that a middle child needs 9-21 minutes for. The page-1 "Start here" is meant to be done by everyone ("check page 1 together" explains every part) so the check slide is walked over answers that many pairs never reached.
4. **Talk time (6 min) is exactly 2+2+2 in the notes and has no slack** for the REC cue, the SAY line, reading the question, regrouping, and finding the Investigation page (about 2.5 minutes). It always runs 8.3-8.5.
5. **The opening is unbudgeted.** "0 min Opening (before the clock starts)" is a hook of 70-90 words, a greeting by name, "Today we will..." and (with REC) the recording notice. It takes 1.8-2.0 minutes (L5 3.6 with the stone demonstration). If the session is booked as 90 minutes the clock has started.
6. **Check slides are one minute per question.** Page 1 checks need 3.6-6.1 minutes against 4, page 2 checks 4.0-5.6 against 4.
7. **Page-2 teaching (53-58) is a second mini-lesson.** It holds 2-4 slides in 5 minutes; it is within budget in 8 lessons only because many lessons have no "Your turn" slide there. L1 (four slides, `trybrackets` has three items) needs 8.3 and L3 (three slides) 7.0.
8. **Brain break** is fine (4.4-5.0), L6 and L10 are tight because they ask children to do and count something.
9. **Exit ticket / reflection / stamp (8 min)** splits as 4+2+2 in the guide; the estimate is exit ticket 5.0-6.4, reflection 2.6, stamp and goodbye 1.3 (typed or shown to camera for eight children). Totals are 7.8-9.9 for eight lessons, L3 10.3 (the exit ticket asks for a drawn model on a slip, about 4 minutes of writing) and L10 12.5 (exit 5.5 + reflection 2.6 + eight certificates and the last stamp 4.5).
10. **Size.** Script (hook, warm-up intro, predict, think-alouds, talk, close) has 317-414 SAY words per lesson (mean 361). L10 is 414 (+15 percent) and has the most slides (29, including `end`). L8 has the longest content file (30.5 KB; the angle-chase reasons). Slide counts are 26-29 per lesson (22-25 shown to the whole group; four are Think harder / Go further slides for a few children; L7 has two more optional teaching slides). The tutor guide runs 7-8 pages per lesson (about 3,500-3,800 words; L10 about 4,000). None of these sizes is out of line except L10; the time problem is the number of group interactions, not the volume of text.

## 5. Worksheet load: what children can do in the block

Parts counted are answer parts (a, b, c ...). "Available" is the block minus start-up, breakout move, SAY lines and slide change. Middle-child minutes per part are judged item by item from the real questions (see `LES` in the helper). Think harder items are 4-6 minutes each and sit on separate pages, so a HIGH child who finishes the plan set is the only one who reaches them.

| Lesson | Page 1 parts (all) | Page 1 MID work needed vs available (min) | LOW / MID / HIGH parts done on page 1 | Page 2 parts (all) | Page-2 plan set needs vs available (min) | LOW / MID / HIGH parts done on page 2 (plan set first) |
|---|---|---|---|---|---|---|
| 1 | 7 | 17.5 vs 7.3 | 4 / 5 / 6 | 10 | 8.0 vs 12.9 | 6 / 7 / 9 |
| 2 | 10 | 20.5 vs 7.3 | 3 / 4 / 6 | 8 | 10.5 vs 12.9 | 3 / 4 / 6 |
| 3 | 6 | 12.5 vs 8.3 | 2 / 4 / 6 | 9 | 9.5 vs 12.9 | 4 / 5 / 8 |
| 4 | 7 | 9.0 vs 8.3 | 4 / 6 / 7 | 12 | 7.5 vs 12.9 | 8 / 11 / 12 |
| 5 | 8 | 18.0 vs 8.3 | 2 / 2 / 5 | 8 | 10.5 vs 12.9 | 3 / 5 / 7 |
| 6 | 10 | 21.0 vs 8.3 | 2 / 3 / 5 | 9 | 11.0 vs 12.9 | 3 / 5 / 7 |
| 7 | 11 | 19.0 vs 8.3 | 2 / 5 / 7 | 6 | 10.5 vs 12.9 | 4 / 5 / 6 |
| 8 | 7 | 11.8 vs 8.3 | 4 / 5 / 7 | 10 | 6.5 vs 12.9 | 5 / 7 / 9 |
| 9 | 7 | 16.0 vs 7.3 | 2 / 3 / 5 | 5 | 11.5 vs 12.9 | 2 / 3 / 5 |
| 10 | 3 | 14.0 vs 8.3 | 1 / 1 / 2 | 6 | 15.0 vs 12.9 | 3 / 4 / 6 |

Reading the table. On page 1 a middle pair completes between a quarter and 70 percent of the parts in nine lessons (L5 and L6 under a third, L2, L7 and L9 about 40-45 percent, L1, L3 and L8 about 70 percent); only L4 is close to complete (6 of 7 parts). A LOW pair completes 2-4 parts, so it never reaches the harder Start-here question (the riddle, the unit-fraction puzzle, the water-tank question) and arrives at the check slide with nothing to check. On page 2 everyone has more time than the plan set needs except in L10 (plan set 15.0 min against 12.9 available), but a LOW child only completes the first third of the plan.

The "tier principle" is respected by the content: page 1 items are Core and scaffolded ("Start here" hints), Think harder needs the taught idea and sits on its own page, Challenge/Go further needs the whole topic. The problem is volume, not difficulty.

## 6. Lesson by lesson

Each table: scripted minutes, then the four components of the estimated need, then the difference and flag. The two worksheet work rows show content need (see section 2). The last two lines are the totals.

### Lesson 1: Million Puzzles

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.0 | 0.5 | 0.0 | 0.4 | 1.9 | +1.9 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.5 | 1.5 | 2.8 | 0.4 | 6.1 | +3.1 | OVER |
| Warm-up 3-9 | 6 | 0.8 | 2.5 | 3.2 | 0.8 | 7.3 | +1.3 | TIGHT |
| Explore 9-21 | 12 | 1.6 | 2.3 | 7.0 | 4.7 | 15.6 | +3.6 | OVER |
| Mini-lesson 21-33 | 12 | 2.6 | 3.2 | 3.8 | 2.5 | 12.1 | +0.1 | OK |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 17.5 | 3.9 | 22.2 | +10.2 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 4.0 | 0.0 | 1.8 | 6.1 | +2.1 | OVER |
| WB teaching 53-58 | 5 | 1.6 | 2.3 | 2.7 | 1.7 | 8.3 | +3.3 | OVER |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 8.0 | 0.9 | 9.1 | -4.9 | LOOSE |
| WB check p2 72-76 | 4 | 0.8 | 4.0 | 0.0 | 0.8 | 5.5 | +1.5 | TIGHT |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.0 | 1.4 | 8.5 | +2.5 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.1 | 1.2 | 8.9 | +0.9 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **110.8** (range 99-123) | **+20.8** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **121.0** | +31.0 | |

Where the time goes:

- Sneak-peek 6.1 (+3.1): P1 (cards 3, 6, 7, 9 closest to 7000, test both sides) about 75 s and P2 (one pair of brackets to make 47) about 90 s; two hold-ups and the volunteer round add 1.5 min.
- Warm-up 7.3 (+1.3): the deck says "Play 3 rounds" of Million Maker, the notes say 1 or 2; two rounds with seven cards are about 3.2 min, then five quick questions (2.5 min of waiting; question 5 is a three-step order-of-operations item).
- Explore 15.6 (+3.6): pair work 7 min (3600, 86 400, then 11-12 days with a calculator), breakout round trip 2.5, calculators and digit cards 1, three regroup questions 2.3.
- Mini-lesson 12.1: six slides, three group questions and two "Your turn" slides; `try2` is three seven-digit constructions (about 2.5 min). No slack at all.
- Page 1 needs 17.5 min (Q1 3.0, Q2 7.5 with 2c "best just below / just above, find each gap" 4.5, Q3 digit riddle 7.0) against 7.3 available. Check p1 needs 6.1 (+2.1).
- Teaching 8.3 (+3.3): four slides in 5 min; `trybrackets` has three items including "make 24 with 3, 4, 6, 8" (about 2.7 min of solving).
- Page 2: the plan set (Q4 and Q5 a, b) needs 8.0 of 12.9 available: LOOSE, but Q5d (target 100 from 3, 5, 7, 9) alone is 5 min.

Fix for this lesson:
Remove or move: Q1 (all three parts duplicate quick questions 1-3 of the warm-up) and Q2c (repeats `try2` c and the `we1` worked example) from page 1 to take-home; page 1 in class = Q2 a, b and Q3 (10.0 min of middle-child work). Keep the neutral line "After question 3 you may choose..." (Q3 is still the last page-1 item). Page 2 in class = Q4 a-d and Q5 a; Q5 b-d and Q6 to take-home. Teaching: keep `teachest` and `teachbrackets`; delete `trybrackets` (children do exactly this on Q5 a) and move `teachfind` with Q6 to the take-home pack. Warm-up: one round of Million Maker (change the deck text from "Play 3 rounds"). Explore: question 3 on `explore2` ("about how long is 10 million seconds") and the step-4 comparison move to the Go further what-if, so pairs stop at minute 15 and the regroup is two questions. SAY lines: shorten the second hook paragraph ("Today our numbers grow up to 10 million ...") to one sentence.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6, Explore 13.5, Mini-lesson 11, Brain break 4.5, WB page 1 pairs 15, WB check p1 4, WB teaching 3, WB page 2 alone 8, WB check p2 3.5, Talk time 5.5, Exit/reflect/close 8, Buffer 1.5 (total 90).

### Lesson 2: Fraction Feats

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.4 | 1.5 | 2.5 | 0.4 | 5.9 | +2.9 | OVER |
| Warm-up 3-9 | 6 | 0.7 | 2.5 | 2.5 | 0.8 | 6.6 | +0.6 | OK |
| Explore 9-21 | 12 | 1.4 | 2.3 | 8.0 | 5.2 | 16.9 | +4.9 | OVER |
| Mini-lesson 21-33 | 12 | 2.7 | 3.2 | 3.9 | 2.5 | 12.3 | +0.3 | OK |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 20.5 | 3.9 | 25.2 | +13.2 | OVER |
| WB check p1 49-53 | 4 | 0.4 | 3.5 | 0.0 | 1.8 | 5.6 | +1.6 | TIGHT |
| WB teaching 53-58 | 5 | 1.8 | 1.5 | 0.0 | 1.2 | 4.5 | -0.5 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 10.5 | 0.9 | 11.6 | -2.4 | OK |
| WB check p2 72-76 | 4 | 0.4 | 4.0 | 0.0 | 0.8 | 5.1 | +1.1 | TIGHT |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.0 | 1.4 | 8.5 | +2.5 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.1 | 1.2 | 8.9 | +0.9 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **106.7** (range 95-118) | **+16.7** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **119.8** | +29.8 | |

Where the time goes:

- Sneak-peek 5.9 (+2.9): pizzas drawn and cut (about 60 s) and the "1/3 then 1/2 of what is left" bar (about 90 s).
- Explore 16.9 (+4.9): the biggest explore after L6/L9/L10: paper pizzas folded or cut on camera (material time 90 s), "2 pieces each" for 3 pizzas among 4 and 5 among 6 needs 8 min of pair work, plus the breakout round trip 2.5.
- Page 1 needs 20.5 min (Q1 4.5, Q2 unit fractions 10.5 with c "two ways for 3/8, test in order, how do you know to stop" 4.5, Q3 5.5); 7.3 available. A LOW pair completes 3 of 10 parts.
- Page 2 plan set (Q5 and Q4 a, b) needs 10.5 of 12.9; fine. Teaching has three slides in 5 min and none has a "Your turn" slide: 4.5 min, OK.
- Mini-lesson 12.3 (+0.3) and break are fine.

Fix for this lesson:
Page 1 in class = Q1 (a-c), Q2 Start-here line and (a), Q3 (a) (10.5 min). To take-home: Q2 b, c (the unit-fraction search, 7.5 min; `we1` and `try2` just practised exactly this) and Q3 b, c. Page 2 in class = Q5 a, b (with `teachback`, which is the model for it) and Q4 a (next two fractions); Q4 b, c and Q6 and slides `teachpattern`, `teachboth` to take-home. Explore: cut the "5 pizzas among 6 with only 2 pieces each" step to the Go further what-if (a pair that finishes the first step may go on), which brings pair work to 6 min.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6.5, Explore 13.5, Mini-lesson 11, Brain break 4, WB page 1 pairs 15.5, WB check p1 4.5, WB teaching 1.5, WB page 2 alone 8, WB check p2 3, Talk time 5.5, Exit/reflect/close 8, Buffer 2.5 (total 90).

### Lesson 3: Before and After

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.8 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.5 | 1.5 | 2.0 | 0.4 | 5.4 | +2.4 | OVER |
| Warm-up 3-9 | 6 | 1.1 | 2.5 | 3.0 | 0.8 | 7.4 | +1.4 | TIGHT |
| Explore 9-21 | 12 | 1.7 | 2.3 | 8.0 | 3.2 | 15.2 | +3.2 | OVER |
| Mini-lesson 21-33 | 12 | 2.7 | 2.7 | 6.2 | 2.1 | 13.7 | +1.7 | TIGHT |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.0 | 0.4 | 4.4 | +0.4 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 12.5 | 2.9 | 16.2 | +4.2 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 2.5 | 0.0 | 1.2 | 4.1 | +0.1 | OK |
| WB teaching 53-58 | 5 | 1.5 | 1.8 | 2.5 | 1.2 | 7.0 | +2.0 | OVER |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 9.5 | 0.9 | 10.6 | -3.4 | LOOSE |
| WB check p2 72-76 | 4 | 0.2 | 4.5 | 0.0 | 0.8 | 5.5 | +1.5 | TIGHT |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.0 | 1.4 | 8.4 | +2.4 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.4 | 1.2 | 6.6 | 1.2 | 10.3 | +2.3 | OVER |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **109.2** (range 97-121) | **+19.2** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **113.4** | +23.4 | |

Where the time goes:

- Sneak-peek 5.4 (+2.4) and warm-up 7.4 (+1.4): "What's left?" has two cards, each asking children to draw a bar, hold up boards and see why "of what is left" changes the whole.
- Explore 15.2 (+3.2): two tables of counters (18 and 6, give one at a time; both +2) and the half question: 8 min of pair work, no breakouts.
- Mini-lesson 13.7 (+1.7): `try1` is two fraction-of-a-remainder stories with a bar drawn each time (about 3.3 min), `try2` is three more (about 2.9 min); five slides.
- Page 1 content 12.5 against 8.3: Q1 (four parts, 8.0 min including "Try $60 first" and the interpretation of "too little") and Q2 (4.5).
- **Slides and workbook disagree:** `ws1` and `ws1ans` show Q3 (marbles) as a page-1 question and the check slide gives its answers in the page-1 check, but in the workbook page 2 starts at Q3 ("Start here: page 2" banner). So page 1 is really Q1-Q2 and the check slide spoils Q3 for the alone block.
- Teaching 7.0 (+2.0): three slides, `trydiff` has two items of about 70-80 s each.
- Exit 10.3 (+2.3): "draw a model on a slip" for 35 and 25 stickers needs about 4 min.

Fix for this lesson:
Page 1 in class = Q1 a-c (drop the optional (d) "try this one if you like") and Q2 a, b: 11.0 min. Move Q3 off the page-1 slides (`ws1`, `ws1ans`) and put it on the page-2 list; Q3, Q5 to take-home. Page 2 in class = Q4 only (6.5 min), with `teachdiff` (keep) ; delete `trydiff` and `teachone`. Mini-lesson: keep both worked examples, one item fewer per `try` slide (mini 12.0). Exit ticket: allow 4 min of writing (it asks for a model), so exit gets 9.5 and the minutes come from page 2.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6.5, Explore 13, Mini-lesson 12, Brain break 4, WB page 1 pairs 15, WB check p1 3.5, WB teaching 1.5, WB page 2 alone 8, WB check p2 2, Talk time 5.5, Exit/reflect/close 9.5, Buffer 3 (total 90).

### Lesson 4: Triangle Areas

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.7 | 1.5 | 2.8 | 0.4 | 6.3 | +3.3 | OVER |
| Warm-up 3-9 | 6 | 0.8 | 2.5 | 2.0 | 0.8 | 6.2 | +0.2 | OK |
| Explore 9-21 | 12 | 1.5 | 2.3 | 8.0 | 4.2 | 16.0 | +4.0 | OVER |
| Mini-lesson 21-33 | 12 | 2.9 | 3.2 | 3.3 | 2.5 | 11.9 | -0.1 | OK |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 9.0 | 2.9 | 12.7 | +0.7 | OK |
| WB check p1 49-53 | 4 | 0.3 | 2.0 | 0.0 | 1.2 | 3.6 | -0.4 | OK |
| WB teaching 53-58 | 5 | 1.5 | 1.5 | 0.0 | 1.2 | 4.2 | -0.8 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 7.5 | 0.9 | 8.6 | -5.4 | LOOSE |
| WB check p2 72-76 | 4 | 0.3 | 3.5 | 0.0 | 0.8 | 4.5 | +0.5 | OK |
| Talk time 76-82 | 6 | 0.9 | 2.0 | 4.0 | 1.4 | 8.3 | +2.3 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.4 | 1.2 | 4.1 | 1.2 | 7.8 | -0.2 | OK |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **101.1** (range 90-112) | **+11.1** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **101.8** | +11.8 | |

Where the time goes:

- The best-balanced lesson. Page 1 content (Q1 5.0, Q2 4.0 = 9.0) fits the 8.3 minutes available within 0.7 min; teaching, check slides and mini-lesson are within +/-0.8.
- Sneak-peek 6.3 (+3.3): P1 asks children to draw a 6 by 4 rectangle, count 24 squares, cut along the diagonal and compare (about 90 s); P2 is a conceptual question (area of PCD as P slides).
- Explore 16.0 (+4.0): draw 8 by 6 on grid paper, mark a point, cut three pieces, compare, repeat; 8 min of pair work, 120 s of materials (scissors, ruler, grid paper), no breakouts.
- Page 2: plan set Q5 + Q3 needs 7.5 of 12.9: LOOSE (-5.4). All of page 2 is 13.5 min for a middle child, so the whole page is realistic.

Fix for this lesson:
Explore: print the 8 by 6 rectangle on the grid cut-out page the night before (pairs only mark the point and cut), pair work capped at 6.5 min: explore 12.5. Sneak-peek: let P1 be answered by drawing only (count squares, no cutting). Because this lesson has the spare time, **add** to page 2: Q5 plus Q4 (taught by `teachtake`) instead of Q3, keeping teaching at 3 min (`teachtake`, `teachsame`); Q3 and `teachsplit` go to take-home. Page 2 = 12 min in the new plan.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6, Explore 12.5, Mini-lesson 11, Brain break 4.5, WB page 1 pairs 13, WB check p1 3.5, WB teaching 3, WB page 2 alone 12, WB check p2 3, Talk time 5.5, Exit/reflect/close 7, Buffer 2.5 (total 90).

### Lesson 5: Volume Vault

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.2 | 2.0 | 0.0 | 0.4 | 3.6 | +3.6 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.5 | 1.5 | 2.2 | 0.4 | 5.7 | +2.7 | OVER |
| Warm-up 3-9 | 6 | 0.9 | 2.5 | 3.0 | 0.8 | 7.3 | +1.3 | TIGHT |
| Explore 9-21 | 12 | 1.7 | 2.3 | 8.0 | 3.7 | 15.7 | +3.7 | OVER |
| Mini-lesson 21-33 | 12 | 3.3 | 3.7 | 6.0 | 2.9 | 15.9 | +3.9 | OVER |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 18.0 | 2.9 | 21.7 | +9.7 | OVER |
| WB check p1 49-53 | 4 | 0.4 | 4.0 | 0.0 | 1.2 | 5.7 | +1.7 | TIGHT |
| WB teaching 53-58 | 5 | 1.1 | 1.0 | 0.0 | 0.8 | 2.9 | -2.1 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 10.5 | 0.9 | 11.6 | -2.4 | OK |
| WB check p2 72-76 | 4 | 0.3 | 4.5 | 0.0 | 0.8 | 5.6 | +1.6 | TIGHT |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.0 | 1.4 | 8.4 | +2.4 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.6 | 1.2 | 9.4 | +1.4 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **110.6** (range 99-123) | **+20.6** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **120.3** | +30.3 | |

Where the time goes:

- Opening 3.6: the hook is two paragraphs (78 words) plus a live demonstration (a stone dropped into a clear box with a ruler) and a prediction question, about 90 s more.
- Mini-lesson 15.9 (+3.9): seven slides (`teach1`, `we1`, `try1`, `we2`, `try2`, `teachlist`, `key`); `try1` is three litres-to-depth conversions (about 2.7 min), `try2` three sinking-object items (1.8), and `teachlist` ends with a "your turn: how many cuboids from 20 cubes" (about 90 s).
- Explore 15.7 (+3.7): 24 cubes (or dice/Lego) or squared paper, find all six cuboids and prove it, 8 min of pair work and 90 s of materials.
- Page 1 content 18.0 against 8.3: Q2 is all the cuboids from 36 cubes (4.5) plus the fit-in-a-box part, Q3 is the 50 by 30 by 40 tank with three parts (8.0 including the Start-here scaffold). A middle pair completes 2 of 8 parts and a LOW pair 2.
- Teaching 2.9 (OK), page 2 plan set (Q4 a-c and Q5 painted cube, 6 min) needs 10.5 of 12.9.

Fix for this lesson:
Mini-lesson: delete `teachlist` (the explore has just done "list in order"; Q2 repeats it with 36 cubes) and cut the third item from `try1`, `try2`: mini 12.0. Page 1 in class = Q2 (a, b) and Q3 (Start-here scaffold, a, b): 11.0 min; Q1 and Q3c to take-home. Page 2 in class = Q4 only (6.5 min); delete `teachpaint`, `teachpour` and send Q5, Q6 to take-home (the painted-cube and pouring questions each need their own worked slide, which is why they cannot go in a short block). Opening: keep the stone demonstration but cut the hook SAY to its second paragraph ("Watch this clear box ..."): opening 3.5.

New budgets (min): Opening (inside the 90) 3.5, Sneak-peek 4.5, Warm-up 6.5, Explore 13, Mini-lesson 12, Brain break 4.5, WB page 1 pairs 15, WB check p1 3.5, WB teaching 0, WB page 2 alone 8, WB check p2 2, Talk time 5.5, Exit/reflect/close 8.5, Buffer 3.5 (total 90).

### Lesson 6: Rate Racers

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.1 | 0.5 | 0.0 | 0.4 | 2.0 | +2.0 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.4 | 1.5 | 2.0 | 0.4 | 5.3 | +2.3 | OVER |
| Warm-up 3-9 | 6 | 1.0 | 2.5 | 2.0 | 0.8 | 6.3 | +0.3 | OK |
| Explore 9-21 | 12 | 1.5 | 2.3 | 9.0 | 4.7 | 17.5 | +5.5 | OVER |
| Mini-lesson 21-33 | 12 | 3.6 | 3.7 | 3.5 | 2.9 | 13.6 | +1.6 | TIGHT |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.5 | 0.4 | 5.0 | +1.0 | TIGHT |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 21.0 | 2.9 | 24.7 | +12.7 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 4.0 | 0.0 | 1.2 | 5.6 | +1.6 | TIGHT |
| WB teaching 53-58 | 5 | 1.0 | 1.0 | 0.0 | 0.8 | 2.9 | -2.1 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 11.0 | 0.9 | 12.1 | -1.9 | OK |
| WB check p2 72-76 | 4 | 0.3 | 4.0 | 0.0 | 0.8 | 5.0 | +1.0 | TIGHT |
| Talk time 76-82 | 6 | 0.9 | 2.0 | 4.0 | 1.4 | 8.3 | +2.3 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.6 | 1.2 | 9.4 | +1.4 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **106.9** (range 95-118) | **+16.9** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **119.6** | +29.6 | |

Where the time goes:

- Explore 17.5 (+5.5): the largest single over-run after L9/L10: two rate tables of four cells each (1, 2, 4, 10 minutes) plus "which is faster", plus "how long do both take for 430 pages" (A 18 + B 25 = 43 a minute, 10 minutes), 9 min of pair work and a breakout round trip.
- Mini-lesson 13.6 (+1.6): seven slides (`teach1`, `we1`, `try1`, `teachfree`, `we2`, `try2`, `key`).
- Page 1 content 21.0 (the largest): Q1 5.0, Q2 9.0 (three prices to the cent, best buy, then 20 cans from whole packs 4.5), Q3 7.0 (four time questions with a leak). A middle pair completes 3 of 10 parts.
- Page 2: plan set Q4 (a), Q6 (a) and Q5 needs 11.0 of 12.9 and the whole page is 22 min; fine as a menu.
- Brain break 5.0 (+1.0): the star-jump predict-then-test uses 150 s of activity.

Fix for this lesson:
Explore: cap at 6 minutes (drop the 430-page together question into the Go further what-if, which already asks the same kind of thing). Page 1 in class = Q1 a, b, Q2 start-here line, a, b, and Q3 a (10.5 min); Q2c (20 cans) and Q3 b-d to take-home. Mini-lesson: keep `teachfree`, give every `try` two items (12.5). Page 2 in class = Q4 a, b and Q6 a with `teachplans`; delete `teachpark`, Q5 car-park to take-home. Brain break: 60 s of star jumps, count once (4.0).

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4, Warm-up 6, Explore 13.5, Mini-lesson 12.5, Brain break 4, WB page 1 pairs 14.5, WB check p1 4, WB teaching 1.5, WB page 2 alone 9, WB check p2 3, Talk time 5.5, Exit/reflect/close 8.5, Buffer 2 (total 90).

### Lesson 7: Percentage Puzzles

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.3 | 1.5 | 2.2 | 0.4 | 5.5 | +2.5 | OVER |
| Warm-up 3-9 | 6 | 0.6 | 2.5 | 2.0 | 0.8 | 5.9 | -0.1 | OK |
| Explore 9-21 | 12 | 1.6 | 2.3 | 6.0 | 3.2 | 13.1 | +1.1 | TIGHT |
| Mini-lesson 21-33 | 12 | 2.3 | 3.2 | 4.0 | 2.5 | 12.0 | -0.0 | OK |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 19.0 | 2.9 | 22.7 | +10.7 | OVER |
| WB check p1 49-53 | 4 | 0.4 | 3.5 | 0.0 | 1.2 | 5.1 | +1.1 | TIGHT |
| WB teaching 53-58 | 5 | 1.0 | 1.0 | 0.0 | 0.8 | 2.8 | -2.2 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 10.5 | 0.9 | 11.6 | -2.4 | OK |
| WB check p2 72-76 | 4 | 0.3 | 3.0 | 0.0 | 0.8 | 4.0 | +0.0 | OK |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.0 | 1.4 | 8.5 | +2.5 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.4 | 1.2 | 6.1 | 1.2 | 9.8 | +1.8 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **99.1** (range 89-109) | **+9.1** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **109.7** | +19.7 | |

Where the time goes:

- The lightest fixed parts of the level: explore 13.1 (+1.1, 6 min of pair work and no breakouts) and mini-lesson 12.0 (no slack) are close to budget.
- Sneak-peek 5.5 (+2.5), talk 8.5 (+2.5), exit 9.8 (+1.8: three-step $26.16 answer on a slip).
- Page 1 content 19.0: Q1 table (10%, 5%, 1%, 15%, 35%, 99%) 5.5, Q2 two shops with discount and GST 9.0 (a step of 1.0, then four parts), Q3 4.5. A middle pair completes 5 of 11 parts.
- Page 2: plan set (Q4 a-c and Q5) 10.5 of 12.9; teaching 2.8.
- `teachchange` and `teachdeal` are labelled 72-76 (the page-2 check minutes) but are "optional, after worksheet page 2, for the Think harder page" - they are not in the whole-group flow and are not counted. They compete with the check if a tutor shows them.

Fix for this lesson:
Page 1 in class = Q1 (a, b) and Q3 (a-c) (10.0 min); move Q2 (rice cooker, 9.0) to page 2 where it is the first item (it is exactly `we2`/`try2` applied). Page 2 in class = Q2 a-c and Q4 a-c, with `teachrem` only; delete `teachtable` and send Q5 to take-home. Relabel `teachchange` / `teachdeal` "after class" (not 72-76). Sneak-peek and talk-time fixes as for all lessons; exit ticket kept (3.5 min).

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 5.5, Explore 12, Mini-lesson 11, Brain break 4.5, WB page 1 pairs 14, WB check p1 3.5, WB teaching 1.5, WB page 2 alone 11.5, WB check p2 3, Talk time 5.5, Exit/reflect/close 9, Buffer 2.5 (total 90).

### Lesson 8: Angle Chasers

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.3 | 1.5 | 1.8 | 0.4 | 5.0 | +2.0 | TIGHT |
| Warm-up 3-9 | 6 | 0.9 | 2.5 | 2.0 | 0.8 | 6.2 | +0.2 | OK |
| Explore 9-21 | 12 | 1.6 | 2.3 | 6.0 | 3.7 | 13.6 | +1.6 | TIGHT |
| Mini-lesson 21-33 | 12 | 3.1 | 3.7 | 3.6 | 2.9 | 13.2 | +1.2 | TIGHT |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 11.8 | 2.9 | 15.4 | +3.4 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 2.5 | 0.0 | 1.2 | 4.1 | +0.1 | OK |
| WB teaching 53-58 | 5 | 1.6 | 1.5 | 0.0 | 1.2 | 4.3 | -0.7 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 6.5 | 0.9 | 7.6 | -6.4 | LOOSE |
| WB check p2 72-76 | 4 | 0.4 | 4.0 | 0.0 | 0.8 | 5.1 | +1.1 | TIGHT |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.0 | 1.4 | 8.5 | +2.5 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.3 | 1.2 | 5.6 | 1.2 | 9.2 | +1.2 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **101.6** (range 91-112) | **+11.6** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **105.1** | +15.1 | |

Where the time goes:

- Page 1 content 11.8 (Q1 4.25, Q2 parallelogram + rhombus + trapezium 8.0, each with a stated angle fact) against 8.3: OVER by 3.4 on content; page 2 plan set (Q3 a, b and Q4 a, b) is only 6.5 of 12.9, so the lesson is the clearest LOOSE page 2 (-6.4).
- Sneak-peek 5.0, explore 13.6 (tearing triangle corners and a quadrilateral on camera, 6 min), mini-lesson 13.2 (+1.2: `teachshapes` plus two worked angle chases), talk 8.5.
- Exit 9.2: the exit ticket demands "write the reason for each step".

Fix for this lesson:
This lesson is the closest to fitting after L4/L7. Page 1 in class = Q1 (a-d) and Q2 a, b (9.2 min; Q2c trapezium to take-home, practised in `try2` b). Page 2 in class = Q3 a, b and Q4 a, b with `teachchain` and `teachcombo`; delete `teachcases` and send Q5 (try every case) to take-home or to the Think-harder menu. That leaves 5 minutes of buffer: if you want them used, restore Q5 a with `teachcases` (about 3.5 min). Mini-lesson: one item fewer per `try` slide.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4, Warm-up 6, Explore 12, Mini-lesson 12, Brain break 4.5, WB page 1 pairs 13, WB check p1 3.5, WB teaching 3, WB page 2 alone 8, WB check p2 3, Talk time 5.5, Exit/reflect/close 8.5, Buffer 5 (total 90).

### Lesson 9: Pattern Generalisers

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.0 | 0.5 | 0.0 | 0.4 | 1.9 | +1.9 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.4 | 1.5 | 2.5 | 0.4 | 5.8 | +2.8 | OVER |
| Warm-up 3-9 | 6 | 0.7 | 2.5 | 3.0 | 0.8 | 7.0 | +1.0 | TIGHT |
| Explore 9-21 | 12 | 1.6 | 2.3 | 9.0 | 5.2 | 18.1 | +6.1 | OVER |
| Mini-lesson 21-33 | 12 | 2.9 | 4.0 | 5.8 | 2.9 | 15.7 | +3.7 | OVER |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.0 | 0.4 | 4.4 | +0.4 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 16.0 | 3.9 | 20.7 | +8.7 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 3.0 | 0.0 | 1.8 | 5.1 | +1.1 | TIGHT |
| WB teaching 53-58 | 5 | 1.8 | 1.5 | 0.0 | 1.2 | 4.5 | -0.5 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 11.5 | 0.9 | 12.6 | -1.4 | OK |
| WB check p2 72-76 | 4 | 0.4 | 4.0 | 0.0 | 0.8 | 5.1 | +1.1 | TIGHT |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.0 | 1.4 | 8.4 | +2.4 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 6.1 | 1.2 | 9.9 | +1.9 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **112.1** (range 100-124) | **+22.1** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **120.8** | +30.8 | |

Where the time goes:

- Explore 18.1 (+6.1): High Fives (guess for 8 children, then build the table 2, 3, 4, 5 ... children, then find the pattern for 8 and for 30) needs 9 min of pair work with a breakout round trip and toothpicks; the largest explore of the level.
- Mini-lesson 15.7 (+3.7): seven slides including three "Your turn" slides (`try1`, `try2`, `try3`) and a two-way border-tile example (`we2`).
- Warm-up 7.0: deck text says "3 rounds" of Guess My Rule.
- Page 1 content 16.0 against 7.3 (the lowest availability because of the breakout): Q1 9.0 (tables and chairs, four parts, one explanation), Q2 7.0 (matchstick houses). A middle pair completes 3 of 7 parts.
- Page 2: plan set Q3 + Q4 (a, b) 11.5 of 12.9, near the limit.
- Totals: 112 min; worksheet left with only 3.9 of 26 minutes if the other parts take what they need.

Fix for this lesson:
Mini-lesson: delete `try3` (border-tile items; `we2` already shows both ways) and keep two items on `try1`, `try2` (11.5). Warm-up: one round of Guess My Rule. Explore: pairs get 5.5 min (stop at the table up to 6 children; the quick rule for 8 and 30 goes to the Go further what-if). Page 1 in class = Q1 a, b (tables and chairs and the rule) and Q2 a, b (9.0 min); Q1 c, d and Q2 c to take-home (they repeat the working-backwards practice of `we1`/`try2`). Page 2 in class = Q3 and Q4 a with `teachgs`, `teachsup`; delete `teachmarks` and send Q5 (marks) to take-home. Buffer 1.5 only: this lesson should have its stamp and goodbye cut to the typed stamp.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 5.5, Explore 13, Mini-lesson 11.5, Brain break 4, WB page 1 pairs 14, WB check p1 4, WB teaching 3.5, WB page 2 alone 9, WB check p2 3, Talk time 5.5, Exit/reflect/close 9, Buffer 1.5 (total 90).

### Lesson 10: Challenge Day

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.9 | +1.9 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.6 | 1.5 | 2.5 | 0.4 | 6.0 | +3.0 | OVER |
| Warm-up 3-9 | 6 | 1.2 | 2.5 | 3.3 | 0.8 | 7.9 | +1.9 | TIGHT |
| Explore 9-21 | 12 | 1.8 | 2.3 | 9.0 | 4.7 | 17.8 | +5.8 | OVER |
| Mini-lesson 21-33 | 12 | 3.7 | 3.7 | 4.5 | 2.9 | 14.7 | +2.7 | OVER |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.5 | 0.4 | 5.0 | +1.0 | TIGHT |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 14.0 | 2.9 | 17.7 | +5.7 | OVER |
| WB check p1 49-53 | 4 | 0.2 | 3.0 | 0.0 | 1.2 | 4.4 | +0.4 | OK |
| WB teaching 53-58 | 5 | 1.5 | 1.5 | 0.0 | 1.2 | 4.3 | -0.7 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 15.0 | 0.9 | 16.1 | +2.1 | OVER |
| WB check p2 72-76 | 4 | 0.3 | 3.5 | 0.0 | 0.8 | 4.6 | +0.6 | OK |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.0 | 1.4 | 8.5 | +2.5 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 8.2 | 1.6 | 12.5 | +4.5 | OVER |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **113.6** (range 101-126) | **+23.6** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **121.3** | +31.3 | |

Where the time goes:

- Exit 12.5 (+4.5): the exit ticket is a three-step backwards problem plus "say which start you used" (5.5 including reading and showing slips), the reflection 2.6, eight certificates and the last stamp 4.5 min (the `end` slide is also a slide change).
- Explore 17.8 (+5.8): "pick 2 of the 4 puzzle cards", each worth about 4.5 min, plus write how you started, plus be ready to teach one card; 9 min of pair work, a breakout round trip, cards sent to the rooms.
- Mini-lesson 14.7 (+2.7): seven slides (toolbox, three worked examples, two "Your turn" slides, key). Warm-up 7.9 (+1.9): the relay has eight cards, each answered by a volunteer who then invites the next (the `warmIntro` SAY is 90 words, the longest in the level).
- Page 1 content 14.0 (three medium-long questions: logic grid 5.0, working backwards 4.5, units and an extra 4.5) against 8.3: a middle pair completes 1 of 3 questions. Page 2 plan set (Q4, Q5 and Q6 a) needs 15.0 against 12.9: OVER (+2.1), the only OVER page 2 in the level.
- Script is the longest (414 SAY words, 29 slides). Total 113.6; the worksheet is left with only 2.4 of 26 scheduled minutes if the other parts take what they need.

Fix for this lesson:
Explore: send one card per room as images and ask each pair to solve ONE card and teach it (the second card becomes the Go further what-if): pair work 6 min, explore 14.0. Mini-lesson: delete `try2` (squares in a 2 by 2 grid is `teachsq` material anyway): 10.5. Warm-up: shorten `warmIntro` to "Mix-up relay: I read a card, a volunteer answers and invites the next volunteer. You may pass once." and read 6 of the 8 cards (volunteers who have not yet answered first). Page 1 in class = Q1 and Q2 (9.5 min); Q3 (draw a model) is the first item of page 2 with Q4 a (6.0). Page 2 teaching = `teachsq` only; `teachliar`, `teachage`, Q5, Q6 and Q4 b, c to take-home. Certificates: show each certificate for 12 s and send the PDF in the approved channel; last stamp typed in the chat. Exit ticket: keep, 3 min of writing.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6.5, Explore 14, Mini-lesson 10.5, Brain break 4, WB page 1 pairs 13.5, WB check p1 3, WB teaching 2, WB page 2 alone 7.5, WB check p2 3, Talk time 5.5, Exit/reflect/close 10.5, Buffer 3.5 (total 90).

Fixes applied to every lesson (see section 7 for the budgets): (1) sneak-peek: one hold-up for both puzzles, drop the volunteer round, intro line shortened to "Guessing is welcome. Nobody is marked.", answer said with one short reason; (2) warm-up: four quick questions and one game round (the guide already allows "only the first three"); (3) explore: pair work capped at 6 minutes (6.5 where pairs stay in the main room, 5.5 in L9), the regroup is two questions not three, materials listed in the pre-lesson message; (4) mini-lesson: every "Your turn" slide keeps items a and b only; (5) talk time: pairs 2 min, volunteers 1.5 min, the Investigation first step moves to take-home or the start of the next lesson (the reflection box stays); (6) check slides: one pair explains the heavy question, the tutor clicks through the rest; (7) stamp: type or send the stamp in the chat (15 s), reflection 75 s.

## 7. Recommended budgets and where the minutes go

Method: each fix is applied in the helper's fix scenario (`plan()` in `docs/audit/timing_p5.py`), the part needs are recomputed, rounded up to half a minute and set as the new budgets; page 2 and the standing buffer take what is left. Same assumptions as in section 2. The new totals are exactly 90.

| Part | Old | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Opening (inside the 90) | 0 | 2 | 2 | 2 | 2 | 3.5 | 2 | 2 | 2 | 2 | 2 |
| Sneak-peek | 3 | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 | 4 | 4.5 | 4 | 4.5 | 4.5 |
| Warm-up | 6 | 6 | 6.5 | 6.5 | 6 | 6.5 | 6 | 5.5 | 6 | 5.5 | 6.5 |
| Explore | 12 | 13.5 | 13.5 | 13 | 12.5 | 13 | 13.5 | 12 | 12 | 13 | 14 |
| Mini-lesson | 12 | 11 | 11 | 12 | 11 | 12 | 12.5 | 11 | 12 | 11.5 | 10.5 |
| Brain break | 4 | 4.5 | 4 | 4 | 4.5 | 4.5 | 4 | 4.5 | 4.5 | 4 | 4 |
| WB page 1 pairs | 12 | 15 | 15.5 | 15 | 13 | 15 | 14.5 | 14 | 13 | 14 | 13.5 |
| WB check p1 | 4 | 4 | 4.5 | 3.5 | 3.5 | 3.5 | 4 | 3.5 | 3.5 | 4 | 3 |
| WB teaching | 5 | 3 | 1.5 | 1.5 | 3 | 0 | 1.5 | 1.5 | 3 | 3.5 | 2 |
| WB page 2 alone | 14 | 8 | 8 | 8 | 12 | 8 | 9 | 11.5 | 8 | 9 | 7.5 |
| WB check p2 | 4 | 3.5 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| Talk time | 6 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 |
| Exit/reflect/close | 8 | 8 | 8 | 9.5 | 7 | 8.5 | 8.5 | 9 | 8.5 | 9 | 10.5 |
| Buffer | 0 | 1.5 | 2.5 | 3 | 2.5 | 3.5 | 2 | 2.5 | 5 | 1.5 | 3.5 |
| **Total** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** |

What changes, in one place:

| Where | Old | New | How the budget is met |
|---|---|---|---|
| Opening | 0 (pre-clock) | 2.0 (L5 3.5) | One-paragraph hook, greeting by wave and chat, one-sentence recording notice, "Today we will..." |
| Sneak-peek | 3 | 4-4.5 | One hold-up for both puzzles, no volunteer round, 12-word intro, answer plus one reason; think time stays about a minute each |
| Warm-up | 6 | 5.5-6.5 | 4 quick questions, one game round (L1, L9: the decks must stop saying "3 rounds") |
| Explore | 12 | 12-14 | Pair work 5.5-6.5 min, regroup two questions not three, materials sent the day before, pairs preassigned to breakout rooms |
| Mini-lesson | 12 | 10.5-12.5 | Two items per "Your turn" slide; L5 `teachlist`, L9 `try3`, L10 `try2` removed |
| Page 1 pairs | 12 | 13-15.5 | Longer block, but about 10 minutes of middle-child content (9.0-11.0 min) instead of 9-21 |
| Check p1 | 4 | 3-4.5 | One pair explains the heaviest question; others clicked through |
| Teaching | 5 | 0-3.5 | Only the teaching slides for questions that stay in class |
| Page 2 | 14 | 7.5-12 | Plan line names the in-class items only; everything else is "take-home / Think harder" |
| Check p2 | 4 | 2-3.5 | Only the questions that were set |
| Talk time | 6 | 5.5 | Pairs 2 min, volunteers 1.5, Investigation first step to take-home or the next lesson's opener |
| Exit/reflect/close | 8 | 7-10.5 | Typed stamp; reflection 75 s; L10 certificates 12 s each; L3 and L7 exit tickets keep their 3.5 min |
| Buffer | 0 | 1.5-5 | see section 8 |

What is moved to take-home (per lesson) is in each lesson's fix note above. It is moved, not cut: the answers, the tier labels and the pass option are untouched. The first-step Investigation prompt stays on its page; only the in-class minutes go.

Honest caveat on the fix: a lesson that fits 90 minutes by this arithmetic keeps roughly two thirds of its in-class worksheet (page 1 about 10 minutes of middle-child work, page 2 about 6-10 minutes). If that is too much content to lose, the alternative is to lengthen the session to about 105 minutes (the estimates in section 3 are 99-114 clock minutes).

## 8. Standing buffer

Yes. Recommended: **3 minutes held back, not scheduled**, placed at the end (88-90 becomes "stamp and goodbye, typed, plus 2-3 minutes of floating time"). With every fixed part already running at or above its budget, no lesson has any slack today, so every glitch lands on the worksheet, which is the least elastic content. A 3-minute buffer covers normal slippage (late arrivals, a mute, a slow breakout) but not the full estimate range of plus or minus 10 minutes, so also add:

1. A printed cut-first list in each tutor script, in this order: the Investigation first step, quick question 4, the Go further what-if, the last in-class item of page 2, the reflection to a one-tick version. These are all "pass is allowed" or optional items, so no rule is broken.
2. Clock checkpoints in the guide: 21 (explore done), 33 (mini done), 37 (break done), 49 (page 1 done), 58 (teaching done), 76 (page 2 check done). If the tutor is more than 2 minutes behind at 37, cut the first item on the list.
3. Fix the heading in `p5/guide.js`: the workbook segment is labelled `37-72 min` but its text runs to minute 76 and the next segment is `76-82`, so a tutor reading the headings sees a 4-minute gap.

## 9. Inconsistencies found in the sources (timing relevant)

- `p5/guide.js`: `seg('37-72 min', 'Workbook ...')` while the DO text and `p5/data.js` TIMELINE run to 76 (page-2 check 72-76); the same label is repeated in the rebuilt PDF for all ten lessons.
- `p5/data.js` / decks: L1 and L9 warm-up game text says "Play 3 rounds" while the slide note says "play only 1 or 2 rounds"; three rounds cannot fit in 3 minutes.
- L3: `ws1` and `ws1ans` slides put Q3 on page 1; the workbook page 2 begins at Q3. For L3, L4, L8, L9 page 1 has only two questions, so the printed line "After question 3 you may choose" (on every page 1) points at a question that is on page 2.
- L7: `teachchange` and `teachdeal` are labelled 72-76 min (the page-2 check) although they are optional after-page-2 slides.
- The P5 guide's REC cue lines do not exist yet (`levels/reccues.js` is new, untracked and not required by `p5/guide.js`); `levels/reccues.js` privacy text says to record, while `p5/guide.js` still says "Do not record lessons (this is in the tutor agreement)". The 1.5-minute REC cost is included here.
- Online set-up text mentions breakout rooms for explore (and page 1) in L1, L2, L6, L9, L10 only; for L3, L4, L5, L7, L8 children work on camera in the main room. The model charges 2.5 min for a breakout round trip in the first group and 1 min for the second group; if all lessons use breakouts for explore and page 1 (as the generic "pairs first" instructions imply), add about 2 minutes to each of L3, L4, L5, L7, L8.

## 10. Caveats

Estimates, not stopwatch timings. Biggest uncertainties: how long a mixed group of 10-12 year olds really takes on the puzzles and Your-turn items (plus or minus 15 percent applied in the ranges), how quickly a tutor switches slides, and whether the group is 6 or 8 children (the model uses 8 for greetings, hand-ins and stamps). The judgement inputs (seconds per puzzle, per Your-turn slide, minutes per worksheet part) are listed in `LES` and `FIX` in the helper so any of them can be changed and rerun. Think harder / Go further / Investigation pages are not in the whole-group flow and are not timed. Camera and tech glitches are ignored.
