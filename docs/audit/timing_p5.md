# Lesson timing audit: Math Inquirers P5 (Level N=5, ages 10-12)

Analysis only. Nothing in content, guides, decks, builds or outputs was edited and nothing was committed by this audit. Everything below is an estimate built from the real text (not stopwatch timings). The helper `docs/audit/timing_p5.py` reproduces every number (`python3 docs/audit/timing_p5.py`; `--plan-md` prints the recommended budgets).

Snapshot: repo HEAD `ae350d2` plus the working tree at the time of the audit. Other fix passes were editing `p5/` while this was written (workbook items turned optional or scaffolded, a 30-second "protected think time" added to the explore and the Investigation first step, a `pageOne` / `choiceQ` correction in `p5/data.js`). The model reads `p5/data.js` and the slide decks live and includes those changes; the judgement inputs for worksheet items were re-entered from the workbook text of that moment. Rebuilt PDFs and some slides may lag the source.

## 1. Answer in brief

**No lesson fits 90 minutes as scripted.** Estimated clock minutes when each worksheet block is held to its scripted length (a lesson cannot be shorter unless something is skipped):

| L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|
| 110 | 107 | 109 | 102 | 111 | 106 | 100 | 102 | 113 | 115 |

Ranges (optimistic to pessimistic: waits, activity and transitions plus or minus 15 percent, speech plus or minus 10 percent): L1 98-122; L2 96-119; L3 97-121; L4 91-112; L5 99-123; L6 95-117; L7 89-110; L8 91-112; L9 101-126; L10 102-127. Only the optimistic ends of L4 and L7 reach 90. If a middle pair is allowed to finish page 1 the totals rise to 115, 116, 111, 102, 120, 112, 110, 105, 122, 122.

- The over-run is spread over the small whole-group parts, not over tutor talk. Averaged over the ten lessons the whole-group parts run about 15 minutes over their budget (explore +4.5, talk time +3.0, sneak-peek +2.7, the two check slides +1.2, exit/close +1.6, mini-lesson +1.5, warm-up +0.8, break +0.6, page-2 teaching -0.4). The opening, which the guide puts "before the clock starts", costs another 1.8-3.6 minutes of a booked 90.
- Tutor speech (SAY lines, questions read aloud, REC cues) is only 12.5-15.5 minutes of a lesson (about 15 percent). The costs are waiting for children (about 23 minutes), activity, and transitions (about 19 minutes: some 25 slide changes, two moves to and from breakout rooms, finding materials).
- **The worksheet is the one real content problem.** Page 1 ("Start here") holds 9 to 19 minutes of work for a middle child (excluding the "try this one if you like" parts), but the block gives only 7-8 working minutes once the 2-minute start-up and the breakout move are paid. A middle pair completes 25-80 percent of the parts on page 1 in nine lessons (L4, 86 percent, is the exception). Page 2 is a menu and holds, but in several lessons its plan set is much smaller than its block (spare minutes sitting on the wrong page) and in L10 it is bigger.
- If the fixed parts take what they need, the worksheet (page 1 plus page 2, scheduled 26 minutes) is left with only L10 1.4, L9 2.9, L5 5.4, L1 5.7, L3 6.7, L2 8.9, L6 10.0, L8 14.3, L4 14.4, L7 16.4 minutes.
- The fixes in section 7 bring all ten lessons to exactly 90 with 1.0-5.0 minutes of standing buffer by (a) giving the sneak-peek 4-4.5, the explore 12.5-14.5 and the talk time 5.5 the minutes they really use, (b) trimming page 1 to about 9-11 minutes of middle-child work and moving the rest to take-home, (c) shrinking page 2 and its teaching slides to what the plan set needs.

## 2. Model and assumptions (identical for every lesson)

Source of the budgets: `p5/guide.js` (the `seg()` calls) and the one timeline in `p5/data.js` (`TIMELINE`). The seg calls are the same for all ten lessons, lesson 10 included: 0-3 sneak-peek, 3-9 warm-up, 9-21 explore, 21-33 mini-lesson, 33-37 brain break, then the workbook block (page 1 in pairs 37-49, check 49-53, short teaching 53-58, page 2 alone 58-72, check 72-76), 76-82 talk time, 82-90 exit ticket (4), reflection (2), stamp and goodbye (2; lesson 10: certificates). The rebuilt PDF `p5/Math_Inquirers_P5_Tutor_Guide.pdf` carries the same seg headings for all ten lessons. The REC cue lines are not in the P5 guide yet (`levels/reccues.js` is new and not used by `p5/guide.js`), so they are added in the model.

| Item | Value used |
|---|---|
| Tutor speech (SAY lines, think-aloud, answers given) | 140 words per minute including pauses |
| Questions and tasks read aloud | 130 words per minute |
| Wait after a question to the group | 10 s, plus 20 s to take one or two answers (30 s per group question) |
| Hold up boards / paper to the camera | 30 s |
| Slide change online | 25 s each (every slide shown in the whole-group flow) |
| Move to or from breakout rooms | 90 s out, 60 s back where pairs work in breakouts; 30 s each way where pairs stay in the main room |
| Handing out / finding materials | 60-120 s by lesson (L4 grid paper and scissors 120; L2, L5, L8, L9 90; the rest 60) |
| Starting a worksheet | 2 minutes, plus the breakout move and the SAY lines |
| REC cue | 10 s at the start of each of the 9 guide parts (1.5 min), plus 15 s once to tell the group the lesson is recorded |
| Greeting | 30 s (naming each child), pre-clock |
| Sneak-peek | intro line, both puzzles read aloud, answers said with a reason, two hold-ups, one volunteer round; children need 45-90 s per puzzle (judged puzzle by puzzle) |
| Quick questions | 5 per lesson, 30 s each plus reading |
| Warm-up game | judged per game (120-200 s) |
| Explore | pair work judged per task (6-9 min), 30 s of protected silent think time, three regroup questions of 30 s each plus the guesses (20 s) |
| Mini-lesson | 80 percent of the printed words on each worked-example slide spoken, one group question per worked slide; each "Your turn" slide = read aloud + children solve (judged per item, 15-60 s) + hold-up + feedback |
| Worksheet part (middle child) | Core part 1-3 min, multi-step or "explain" parts 3-5 min; a LOW child takes 1.6 times as long, a HIGH child 0.65 times; parts marked "(try this one if you like)" are optional and not counted |
| Check slides | 60 s per question (10 s wait, volunteer explains, tutor confirms), +30 s for a heavy question |
| Talk time | 30 s protected think, pairs talk 2 min, volunteers 2 min, Investigation first step 2 min, plus regroup and finding the page |
| Exit | question read aloud, children write 1.5-4 min by task, slips shown, reflection 90 s plus reading, stamp and goodbye 64 s (8 children), certificates 160 s |
| Camera / tech glitches | ignored. No lesson has slack, so any glitch lands on the worksheet |

How the tables are read. "Scripted" is the guide minutes. "Need" = speak + wait + activity + transition. Flags: OVER = need exceeds script by 2.0 min or more; TIGHT = 0.75 to 2.0 over; OK = within -3 to +0.75 (a part with under 0.5 min of slack is effectively zero-slack); LOOSE = script exceeds need by 3 min or more. The two worksheet work blocks (page 1 in pairs, page 2 alone) are time-boxes: children fill whatever time they get. Their "Need" is the middle-child content need (page 1: all of Start here; page 2: the questions named on the "Page 2 plan" line) and the flag compares that with the box; a LOOSE page 2 is not dead time because the rest of the page is a menu, but the minutes are idle for the plan set. Totals are given twice: with both boxes held to their scripted minutes (what the clock does), and with page 1 allowed to run until a middle pair finishes it.

## 3. Results at a glance

| Lesson | Clock total, worksheet blocks held to script | Range | If middle pairs finish page 1 | Worksheet time left (of 26 scripted) | OVER parts | LOOSE parts |
|---|---|---|---|---|---|---|
| 1 Million Puzzles | **110** (+20) | 98-122 | 115 | 6 | Sneak-peek, Explore, WB p1, Teaching, Talk | WB p2 |
| 2 Fraction Feats | **107** (+17) | 96-119 | 116 | 9 | Sneak-peek, Explore, WB p1, Talk | - |
| 3 Before and After | **109** (+19) | 97-121 | 111 | 7 | Sneak-peek, Explore, Teaching, Talk, Exit/close | WB p2 |
| 4 Triangle Areas | **102** (+12) | 91-112 | 102 | 14 | Sneak-peek, Explore, Talk | WB p2 |
| 5 Volume Vault | **111** (+21) | 99-123 | 120 | 5 | Sneak-peek, Explore, Mini-lesson, WB p1, Talk | - |
| 6 Rate Racers | **106** (+16) | 95-117 | 112 | 10 | Sneak-peek, Explore, WB p1, Talk | WB p2 |
| 7 Percentage Puzzles | **100** (+10) | 89-110 | 110 | 16 | Sneak-peek, WB p1, Talk | - |
| 8 Angle Chasers | **102** (+12) | 91-112 | 105 | 14 | Explore, WB p1, Talk | WB p2 |
| 9 Pattern Generalisers | **113** (+23) | 101-126 | 122 | 3 | Sneak-peek, Explore, Mini-lesson, WB p1, Talk | - |
| 10 Challenge Day | **115** (+25) | 102-127 | 122 | 1 | Sneak-peek, Explore, Mini-lesson, WB p1, WB p2, Talk, Exit/close | - |

Average minutes over budget per lesson: explore +4.5, talk time +3.0, sneak-peek +2.7, opening (pre-clock) +2.0, exit/close +1.6, mini-lesson +1.5, check slides +1.2, warm-up +0.8, break +0.6, teaching -0.4. In the worksheet the page-1 content need is on average 6.0 minutes bigger than its block while the page-2 plan set is on average 3.2 minutes smaller than its block.

Which lessons run long or short: all ten run long and none runs short. Closest to 90: L7 (+10), L4 (+12), L8 (+12); worst: L10 (+25), L9 (+23), L5 (+21). The three worst each pair a 16-19 minute explore with a 15-16 minute mini-lesson (L5, L9) or with a 14.7-minute mini-lesson and a 12.5-minute exit (L10), on top of the common over-runs. Loose parts: page 2 in L1, L3, L4, L6, L8 (the plan set needs 6-9 minutes of a 14-minute block).

## 4. Cross-level findings

1. **Sneak-peek (3 min) is a 5-6 minute part in every lesson.** Two puzzles at about a minute each is already 2-2.5 minutes before the two hold-ups, the volunteer round, the intro line and reading the puzzles aloud. L1, L4, L10 are heaviest (6.1, 6.3, 6.0: card-testing, draw-and-cut, logic with a table).
2. **Explore (12 min) needs 13.6-18.6.** Pair work is 6-9 minutes, plus 30 s of protected think time, three regroup questions (2.3 min), 2 slide changes, materials and (L1, L2, L6, L9, L10) a breakout round trip of 2.5 minutes. The notes say "at about minute 19, pencils down", leaving two minutes for three questions plus collecting guesses: about 2 minutes short.
3. **Page 1 of the worksheet is double-booked.** The block (37-49) pays 12 minutes, but 2 go to starting, 1-1.5 to the breakout move, and the slide and SAY lines take 1: 7-8 minutes are left for work a middle child needs 9-19 minutes for. Page 1 is meant for everyone (the "check page 1 together" slide explains every part), so the check is walked over answers many pairs never reached.
4. **Talk time (6 min) is exactly 2+2+2 in the notes and now also carries 30 s of protected silent thinking**, plus the REC cue, the SAY line, reading the question, regrouping and finding the Investigation page. It runs 8.8-9.0 in every lesson.
5. **The opening is unbudgeted.** "0 min Opening (before the clock starts)" is a hook of 48-78 words, a greeting by name, "Today we will..." and (with REC) the recording notice: 1.8-2.0 minutes, L5 3.6 with the stone demonstration. If the session is booked as 90 minutes the clock has started.
6. **Check slides are one minute per question.** Page-1 checks need 3.6-5.7 minutes against 4, page-2 checks 3.5-5.1 against 4.
7. **Page-2 teaching (53-58) is a second mini-lesson.** It holds 2-4 slides in 5 minutes and is within budget in eight lessons; L1 (four slides, `trybrackets` has three items) needs 8.3 and L3 (three slides) 7.0.
8. **Brain break** is fine (4.4-5.0); L6 and L10 are tight because they ask children to do and count something.
9. **Exit ticket / reflection / stamp (8 min)** is split 4+2+2 in the guide; the estimate is exit ticket 5.0-6.4, reflection 2.6, stamp and goodbye 1.3 (typed or shown to camera for eight children). Totals are 7.8-9.9 for eight lessons, L3 10.3 (the exit ticket asks for a model drawn on a slip, about 4 minutes) and L10 12.5 (exit 5.5 + reflection 2.6 + eight certificates and the last stamp 4.5).
10. **Size.** The script (hook, warm-up intro, predict, think-alouds, talk, close) has 342-439 SAY words per lesson (mean 386). L10 is 439 (+14 percent) and has the most slides (29, including `end`). L8 has the longest content file (30.5 KB; the angle-chase reasons). Slide counts are 26-29 per lesson (22-25 shown to the whole group; four are Think harder / Go further slides for a few children; L7 has two more optional teaching slides). The tutor guide runs 7-8 pages per lesson (about 3,500-3,800 words; L10 about 4,000). Nothing is out of line except L10; the time problem is the number of group interactions, not the volume of text.

## 5. Worksheet load: what children can do in the block

Parts counted are answer parts (a, b, c ...), without the optional "(try this one if you like)" parts. "Available" is the block minus start-up, breakout move, SAY lines and slide change. Middle-child minutes per part are judged item by item from the real questions (see `LES` in the helper). Think harder items are 4-6 minutes each and sit on separate pages, so only a HIGH child who finishes the plan set reaches them.

| Lesson | Page 1 parts (all) | Page 1 MID work needed vs available (min) | LOW / MID / HIGH parts done on page 1 | Page 2 parts (all) | Page-2 plan set needs vs available (min) | LOW / MID / HIGH parts done on page 2 (plan set first) |
|---|---|---|---|---|---|---|
| 1 | 8 | 12.5 vs 7.3 | 4 / 5 / 7 | 9 | 8.0 vs 12.9 | 6 / 8 / 9 |
| 2 | 8 | 16.0 vs 7.3 | 3 / 3 / 5 | 7 | 10.5 vs 12.9 | 3 / 4 / 6 |
| 3 | 5 | 10.0 vs 8.3 | 2 / 4 / 5 | 7 | 8.0 vs 12.9 | 5 / 6 / 7 |
| 4 | 7 | 8.8 vs 8.3 | 4 / 6 / 7 | 10 | 7.5 vs 12.9 | 8 / 10 / 10 |
| 5 | 8 | 18.0 vs 8.3 | 2 / 2 / 5 | 7 | 11.5 vs 12.9 | 4 / 5 / 7 |
| 6 | 8 | 14.0 vs 8.3 | 2 / 3 / 7 | 7 | 8.5 vs 12.9 | 3 / 5 / 7 |
| 7 | 11 | 19.0 vs 8.3 | 2 / 5 / 7 | 6 | 10.0 vs 12.9 | 4 / 5 / 6 |
| 8 | 7 | 11.8 vs 8.3 | 4 / 5 / 7 | 8 | 6.2 vs 12.9 | 5 / 7 / 8 |
| 9 | 7 | 16.0 vs 7.3 | 2 / 3 / 5 | 5 | 11.5 vs 12.9 | 2 / 3 / 5 |
| 10 | 3 | 14.0 vs 8.3 | 1 / 1 / 2 | 6 | 15.0 vs 12.9 | 3 / 4 / 6 |

Reading the table. Share of the page-1 parts a middle pair completes: L1 62%, L2 38%, L3 80%, L4 86%, L5 25%, L6 38%, L7 45%, L8 71%, L9 43%, L10 33% (L10 has only three long questions, so 1 of 3). Only L4 is close to complete (6 of 7 parts). A LOW pair completes 1-4 parts, so it never reaches the harder Start-here question (the riddle, the unit-fraction puzzle, the water-tank question) and arrives at the check slide with nothing to check. On page 2 everyone has more time than the plan set needs except in L10 (plan set 15.0 min against 12.9 available), but a LOW child completes only 2-8 parts of the page.

The tier principle is intact: page 1 items are Core and scaffolded ("Start here" hints and worked examples), Think harder needs the taught idea and sits on its own page, Challenge/Go further needs the whole topic. The problem is volume, not difficulty.

## 6. Lesson by lesson

Each table: scripted minutes, then the four components of the estimated need, then the difference and flag. The two worksheet work rows show content need (see section 2). The last two lines are the totals.

Fixes applied to every lesson (the budgets are in section 7): (1) sneak-peek: one hold-up for both puzzles, drop the volunteer round, intro line shortened to "Guessing is welcome. Nobody is marked.", answer said with one short reason; (2) warm-up: four quick questions and one game round (the guide already allows "only the first three"); (3) explore: pair work capped at 6 minutes (6.5 where pairs stay in the main room, 5.5 in L9), the regroup is two questions not three, the materials list goes out the day before; (4) mini-lesson: every "Your turn" slide keeps items a and b only; (5) talk time: pairs 2 min, volunteers 1.5 min, the Investigation first step moves to take-home or the start of the next lesson (the reflection box stays); (6) check slides: one pair explains the heavy question, the tutor clicks through the rest; (7) stamp: type or send the stamp in the chat (15 s), reflection 75 s.

### Lesson 1: Million Puzzles

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.0 | 0.5 | 0.0 | 0.4 | 1.9 | +1.9 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.5 | 1.5 | 2.8 | 0.4 | 6.1 | +3.1 | OVER |
| Warm-up 3-9 | 6 | 0.8 | 2.5 | 3.2 | 0.8 | 7.3 | +1.3 | TIGHT |
| Explore 9-21 | 12 | 1.6 | 2.3 | 7.5 | 4.7 | 16.1 | +4.1 | OVER |
| Mini-lesson 21-33 | 12 | 2.6 | 3.2 | 3.8 | 2.5 | 12.1 | +0.1 | OK |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 12.5 | 3.9 | 17.2 | +5.2 | OVER |
| WB check p1 49-53 | 4 | 0.4 | 3.5 | 0.0 | 1.8 | 5.6 | +1.6 | TIGHT |
| WB teaching 53-58 | 5 | 1.6 | 2.3 | 2.7 | 1.7 | 8.3 | +3.3 | OVER |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 8.0 | 0.9 | 9.1 | -4.9 | LOOSE |
| WB check p2 72-76 | 4 | 0.7 | 3.0 | 0.0 | 0.8 | 4.5 | +0.5 | OK |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.5 | 1.4 | 9.0 | +3.0 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.1 | 1.2 | 8.9 | +0.9 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **110.3** (range 98-122) | **+20.3** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **115.5** | +25.5 | |

Where the time goes:

- Sneak-peek 6.1 (+3.1): P1 (cards 3, 6, 7, 9 closest to 7000, test both sides) about 75 s and P2 (one pair of brackets to make 47) about 90 s; two hold-ups and the volunteer round add 1.5 min.
- Warm-up 7.3: the deck says "Play 3 rounds" of Million Maker, the notes say 1 or 2; two rounds with seven cards are about 3.2 min, then five quick questions (question 5 is a three-step order-of-operations item).
- Explore 16.1 (+4.1): pair work 7 min (3600, 86 400, then 11-12 days with a calculator), 30 s protected think time, breakout round trip 2.5, calculators and digit cards 1, three regroup questions 2.3.
- Mini-lesson 12.1: six slides, three group questions and two "Your turn" slides; `try2` is three seven-digit constructions (about 2.5 min). No slack.
- Page 1 needs 17.2 min of block time (12.5 min of middle-child work: Q1 3.0, Q2 3.0, Q3 digit riddle now in three steps 6.5) against 7.3 available. Check p1 5.6.
- Teaching 8.3 (+3.3): four slides in 5 min; `trybrackets` has three items including "make 24 with 3, 4, 6, 8" (about 2.7 min of solving).
- Page 2: the plan set (Q4 and Q5 a, b) needs 8.0 of 12.9 available: LOOSE, but the rest of the page (Q5c, Q6) is a menu.

Fix for this lesson: Page 1 in class = Q2 a, b and Q3 (a-c): 9.5 min of middle-child work. Q1 goes to take-home: its three parts repeat quick questions 1-3 of the warm-up. Keep the neutral line "After question 3 you may choose..." (Q3 is still the last page-1 item). Page 2 in class = Q4 a-d and Q5 a, b; Q5c and Q6 to take-home. Teaching: keep `teachest` and `teachbrackets`; delete `trybrackets` (children do exactly this on Q5 a, b) and move `teachfind` with Q6 to the take-home pack. Warm-up: one round of Million Maker (change the deck text from "Play 3 rounds"). Explore: question 3 on `explore2` ("about how long is 10 million seconds") moves to the Go further what-if, so pair work is capped at 6 minutes and the regroup is two questions. SAY lines: shorten the second hook paragraph ("Today our numbers grow up to 10 million ...") to one sentence.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6, Explore 14, Mini-lesson 11, Brain break 4.5, WB page 1 pairs 14.5, WB check p1 4, WB teaching 3, WB page 2 alone 8, WB check p2 3, Talk time 5.5, Exit/reflect/close 8, Buffer 2 (total 90).

### Lesson 2: Fraction Feats

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.4 | 1.5 | 2.5 | 0.4 | 5.9 | +2.9 | OVER |
| Warm-up 3-9 | 6 | 0.7 | 2.5 | 2.5 | 0.8 | 6.6 | +0.6 | OK |
| Explore 9-21 | 12 | 1.4 | 2.3 | 8.5 | 5.2 | 17.4 | +5.4 | OVER |
| Mini-lesson 21-33 | 12 | 2.7 | 3.2 | 3.9 | 2.5 | 12.3 | +0.3 | OK |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 16.0 | 3.9 | 20.7 | +8.7 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 3.5 | 0.0 | 1.8 | 5.5 | +1.5 | TIGHT |
| WB teaching 53-58 | 5 | 1.8 | 1.5 | 0.0 | 1.2 | 4.5 | -0.5 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 10.5 | 0.9 | 11.6 | -2.4 | OK |
| WB check p2 72-76 | 4 | 0.4 | 3.5 | 0.0 | 0.8 | 4.6 | +0.6 | OK |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.5 | 1.4 | 9.0 | +3.0 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.1 | 1.2 | 8.9 | +0.9 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **107.1** (range 96-119) | **+17.1** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **115.7** | +25.7 | |

Where the time goes:

- Sneak-peek 5.9 (+2.9): pizzas drawn and cut (about 60 s) and the "1/3 then 1/2 of what is left" bar (about 90 s).
- Explore 17.4 (+5.4): one of the larger explores: paper pizzas folded or cut on camera (90 s of materials), "2 pieces each" for 3 pizzas among 4 and 5 among 6 needs 8 min of pair work, plus 30 s think time and the breakout round trip 2.5.
- Page 1 needs 16.0 min of middle-child work (Q1 4.5, Q2 now has a worked example and two parts 6.0, Q3 5.5) against 7.3; a LOW pair completes 3 of 8 parts.
- Page 2 plan set (Q5 and Q4 a, b) needs 10.5 of 12.9; fine. Teaching has three slides in 5 min and none has a "Your turn": 4.5, OK.
- Mini-lesson 12.3 and break are fine; talk 9.0.

Fix for this lesson: Page 1 in class = Q1 a-c and Q2 (worked example, a, b): 10.5 min; Q3 to take-home (it is the same model idea as `we2`). Page 2 in class = Q5 a, b (with `teachback`, which is the model for it) and Q4 a (next two fractions); Q4 b, Q6 and slides `teachpattern`, `teachboth` to take-home. Explore: move the "5 pizzas among 6 with only 2 pieces each" step and regroup question 3 into the Go further what-if (it already asks about 5 among 6), so pair work is 6 min and the regroup is two questions.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6.5, Explore 14, Mini-lesson 11, Brain break 4, WB page 1 pairs 15.5, WB check p1 4, WB teaching 1.5, WB page 2 alone 8, WB check p2 3, Talk time 5.5, Exit/reflect/close 8, Buffer 2.5 (total 90).

### Lesson 3: Before and After

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.8 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.5 | 1.5 | 2.0 | 0.4 | 5.4 | +2.4 | OVER |
| Warm-up 3-9 | 6 | 1.1 | 2.5 | 3.0 | 0.8 | 7.4 | +1.4 | TIGHT |
| Explore 9-21 | 12 | 1.7 | 2.3 | 8.5 | 3.2 | 15.7 | +3.7 | OVER |
| Mini-lesson 21-33 | 12 | 2.7 | 2.7 | 6.2 | 2.1 | 13.7 | +1.7 | TIGHT |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.0 | 0.4 | 4.4 | +0.4 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 10.0 | 2.9 | 13.7 | +1.7 | TIGHT |
| WB check p1 49-53 | 4 | 0.3 | 2.5 | 0.0 | 1.2 | 4.1 | +0.1 | OK |
| WB teaching 53-58 | 5 | 1.5 | 1.8 | 2.5 | 1.2 | 7.0 | +2.0 | OVER |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 8.0 | 0.9 | 9.1 | -4.9 | LOOSE |
| WB check p2 72-76 | 4 | 0.3 | 3.5 | 0.0 | 0.8 | 4.6 | +0.6 | OK |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.5 | 1.4 | 8.9 | +2.9 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.4 | 1.2 | 6.6 | 1.2 | 10.3 | +2.3 | OVER |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **109.3** (range 97-121) | **+19.3** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **111.0** | +21.0 | |

Where the time goes:

- Sneak-peek 5.4 (+2.4) and warm-up 7.4 (+1.4): "What's left?" has two cards, each asking children to draw a bar, hold up boards and see why "of what is left" changes the whole.
- Explore 15.7 (+3.7): two tables of counters (18 and 6, one at a time; both +2) and the half question: 8 min of pair work, no breakouts.
- Mini-lesson 13.7 (+1.7): `try1` is two fraction-of-a-remainder stories with a bar drawn each time (about 3.3 min), `try2` three more (about 2.9 min); five slides.
- Page 1 now has 10.0 min of middle-child work (Q1 6.5, Q2 3.5 with the new "3 and 4, 6 and 8, 9 and 12" tip) against 8.3: 13.7 block time, TIGHT.
- **Slides vs workbook:** the `ws1` / `ws1ans` slides still show Q3 (marbles) as a page-1 question; in the workbook page 2 starts at Q3. A correction (`pageOne`, `choiceQ` in `p5/data.js`) is being made in the source; recheck after the rebuild.
- Teaching 7.0 (+2.0): three slides; `trydiff` has two items of about 70-80 s each.
- Exit 10.3 (+2.3): "draw a model on a slip" for 35 and 25 stickers needs about 4 min.

Fix for this lesson: Page 1 in class = Q1 a-c and Q2 a, b: 10.0 min (the optional (d) stays "if you like"). Move Q3 off the page-1 slides (`ws1`, `ws1ans`) and list it on page 2; Q3 and Q5 to take-home. Page 2 in class = Q4 only (6.5 min) with `teachdiff`; delete `trydiff` and `teachone`. Mini-lesson: keep both worked examples, one item fewer per `try` slide (mini 12.0). Exit ticket: allow 4 min of writing (it asks for a model), so exit gets 9.5 and the minutes come from page 2.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6.5, Explore 13.5, Mini-lesson 12, Brain break 4, WB page 1 pairs 14, WB check p1 3.5, WB teaching 1.5, WB page 2 alone 8, WB check p2 2, Talk time 5.5, Exit/reflect/close 9.5, Buffer 3.5 (total 90).

### Lesson 4: Triangle Areas

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.7 | 1.5 | 2.8 | 0.4 | 6.3 | +3.3 | OVER |
| Warm-up 3-9 | 6 | 0.8 | 2.5 | 2.0 | 0.8 | 6.2 | +0.2 | OK |
| Explore 9-21 | 12 | 1.5 | 2.3 | 8.5 | 4.2 | 16.5 | +4.5 | OVER |
| Mini-lesson 21-33 | 12 | 2.9 | 3.2 | 3.3 | 2.5 | 11.9 | -0.1 | OK |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 8.8 | 2.9 | 12.4 | +0.4 | OK |
| WB check p1 49-53 | 4 | 0.3 | 2.0 | 0.0 | 1.2 | 3.6 | -0.4 | OK |
| WB teaching 53-58 | 5 | 1.5 | 1.5 | 0.0 | 1.2 | 4.2 | -0.8 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 7.5 | 0.9 | 8.6 | -5.4 | LOOSE |
| WB check p2 72-76 | 4 | 0.3 | 3.0 | 0.0 | 0.8 | 4.0 | +0.0 | OK |
| Talk time 76-82 | 6 | 0.9 | 2.0 | 4.5 | 1.4 | 8.8 | +2.8 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.4 | 1.2 | 4.1 | 1.2 | 7.8 | -0.2 | OK |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **101.6** (range 91-112) | **+11.6** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **102.0** | +12.0 | |

Where the time goes:

- The best-balanced lesson. Page 1 content (8.8 min of middle-child work: Q1 4.75 with the new half-of-a-rectangle start, Q2 4.0) fits the 8.3 minutes available within 0.4 min; teaching, check slides and mini-lesson are within +/-0.8.
- Sneak-peek 6.3 (+3.3): P1 asks children to draw a 6 by 4 rectangle, count 24 squares, cut along the diagonal and compare (about 90 s); P2 is a conceptual question (area of PCD as P slides).
- Explore 16.5 (+4.5): draw 8 by 6 on grid paper, mark a point, cut three pieces, compare, repeat; 8 min of pair work, 120 s of materials (scissors, ruler, grid paper), no breakouts.
- Page 2: plan set Q5 + Q3 needs 7.5 of 12.9: LOOSE (-5.4). All of page 2 is 11.5 min for a middle child, so the whole page is realistic here.

Fix for this lesson: Explore: print the 8 by 6 rectangle on the grid cut-out page the night before (pairs only mark the point and cut), pair work capped at 6.5 min: explore 13.0. Sneak-peek: let P1 be answered by drawing only (count squares, no cutting). Because this lesson has spare time, add to page 2: Q5 plus Q4 (taught by `teachtake`) instead of Q3, with teaching 3 min (`teachtake`, `teachsame`); Q3 and `teachsplit` go to take-home. Page 2 = 10 min in the new plan.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6, Explore 13, Mini-lesson 11, Brain break 4.5, WB page 1 pairs 12.5, WB check p1 3.5, WB teaching 3, WB page 2 alone 10, WB check p2 3, Talk time 5.5, Exit/reflect/close 7, Buffer 4.5 (total 90).

### Lesson 5: Volume Vault

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.2 | 2.0 | 0.0 | 0.4 | 3.6 | +3.6 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.5 | 1.5 | 2.2 | 0.4 | 5.7 | +2.7 | OVER |
| Warm-up 3-9 | 6 | 0.9 | 2.5 | 3.0 | 0.8 | 7.3 | +1.3 | TIGHT |
| Explore 9-21 | 12 | 1.7 | 2.3 | 8.5 | 3.7 | 16.2 | +4.2 | OVER |
| Mini-lesson 21-33 | 12 | 3.3 | 3.7 | 6.0 | 2.9 | 15.9 | +3.9 | OVER |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 18.0 | 2.9 | 21.7 | +9.7 | OVER |
| WB check p1 49-53 | 4 | 0.4 | 4.0 | 0.0 | 1.2 | 5.7 | +1.7 | TIGHT |
| WB teaching 53-58 | 5 | 1.1 | 1.0 | 0.0 | 0.8 | 2.9 | -2.1 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 11.5 | 0.9 | 12.6 | -1.4 | OK |
| WB check p2 72-76 | 4 | 0.4 | 3.5 | 0.0 | 0.8 | 4.6 | +0.6 | OK |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.5 | 1.4 | 8.9 | +2.9 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.6 | 1.2 | 9.4 | +1.4 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **110.6** (range 99-123) | **+20.6** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **120.3** | +30.3 | |

Where the time goes:

- Opening 3.6: the hook is two paragraphs (78 words) plus a live demonstration (a stone dropped into a clear box with a ruler) and a prediction question, about 90 s more.
- Mini-lesson 15.9 (+3.9): seven slides (`teach1`, `we1`, `try1`, `we2`, `try2`, `teachlist`, `key`); `try1` is three litres-to-depth conversions (about 2.7 min), `try2` three sinking-object items (1.8), and `teachlist` ends with a "your turn: how many cuboids from 20 cubes" (about 90 s).
- Explore 16.2 (+4.2): 24 cubes (or dice/Lego) or squared paper, find all six cuboids and prove it, 8 min of pair work, 90 s of materials.
- Page 1 content 18.0 against 8.3: Q1 4.0, Q2 all the cuboids from 36 cubes plus the fit-in-a-box part 6.0, Q3 the 50 by 30 by 40 tank with its scaffold 8.0. A middle pair completes 2 of 8 parts, a LOW pair 2.
- Teaching 2.9 (OK); the page 2 plan set (Q4 with the new Start-here line, and Q5 painted cube) needs 11.5 of 12.9.

Fix for this lesson: Mini-lesson: delete `teachlist` (the explore has just done "list in order"; Q2 repeats it with 36 cubes) and cut the third item from `try1`, `try2`: mini 12.0. Page 1 in class = Q2 (a, b) and Q3 (Start-here scaffold, a, b): 11.0 min; Q1 and Q3c to take-home. Page 2 in class = Q4 only (5.5 min); delete `teachpaint`, `teachpour` and send Q5, Q6 to take-home (the painted-cube and pouring questions each need their own worked slide, which is why they cannot fit a short block). Opening: keep the stone demonstration but cut the hook SAY to its second paragraph ("Watch this clear box ..."): opening 3.5.

New budgets (min): Opening (inside the 90) 3.5, Sneak-peek 4.5, Warm-up 6.5, Explore 13.5, Mini-lesson 12, Brain break 4.5, WB page 1 pairs 15, WB check p1 3.5, WB teaching 0, WB page 2 alone 7, WB check p2 2, Talk time 5.5, Exit/reflect/close 8.5, Buffer 4 (total 90).

### Lesson 6: Rate Racers

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.1 | 0.5 | 0.0 | 0.4 | 2.0 | +2.0 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.4 | 1.5 | 2.0 | 0.4 | 5.3 | +2.3 | OVER |
| Warm-up 3-9 | 6 | 1.0 | 2.5 | 2.0 | 0.8 | 6.3 | +0.3 | OK |
| Explore 9-21 | 12 | 1.5 | 2.3 | 9.5 | 4.7 | 18.0 | +6.0 | OVER |
| Mini-lesson 21-33 | 12 | 3.6 | 3.7 | 3.5 | 2.9 | 13.6 | +1.6 | TIGHT |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.5 | 0.4 | 5.0 | +1.0 | TIGHT |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 14.0 | 2.9 | 17.7 | +5.7 | OVER |
| WB check p1 49-53 | 4 | 0.4 | 3.0 | 0.0 | 1.2 | 4.6 | +0.6 | OK |
| WB teaching 53-58 | 5 | 1.0 | 1.0 | 0.0 | 0.8 | 2.9 | -2.1 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 8.5 | 0.9 | 9.6 | -4.4 | LOOSE |
| WB check p2 72-76 | 4 | 0.3 | 3.0 | 0.0 | 0.8 | 4.1 | +0.1 | OK |
| Talk time 76-82 | 6 | 0.9 | 2.0 | 4.5 | 1.4 | 8.8 | +2.8 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 5.6 | 1.2 | 9.4 | +1.4 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **106.0** (range 95-117) | **+16.0** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **111.6** | +21.6 | |

Where the time goes:

- Explore 18.0 (+6.0): the largest single over-run after L9/L10: two rate tables of four cells each (1, 2, 4, 10 minutes), "which is faster", then "how long do both take for 430 pages" (18 + 25 = 43 a minute, 10 minutes), 9 min of pair work, 30 s think time and a breakout round trip.
- Mini-lesson 13.6 (+1.6): seven slides (`teach1`, `we1`, `try1`, `teachfree`, `we2`, `try2`, `key`).
- Page 1 content 14.0 min (Q1 5.0, Q2 4.5 without the optional 20-cans part, Q3 4.5) against 8.3. A middle pair completes 3 of 8 parts.
- Page 2: plan set Q4 (a), Q6 (a) and Q5 needs 8.5 of 12.9: LOOSE (-4.4).
- Brain break 5.0 (+1.0): the star-jump predict-then-test uses 150 s of activity.

Fix for this lesson: Explore: cap at 6 minutes (move the 430-page "both together" question to the Go further what-if, which asks the same kind of thing). Page 1 in class = Q1 a, b, Q2 (start line, a, b) and Q3 a: 10.5 min; Q3 b, c to take-home (Q2c is already optional). Mini-lesson: keep `teachfree`, give every `try` two items (12.5). Page 2 in class = Q4 a, b and Q6 a with `teachplans`; delete `teachpark`, Q5 car-park to take-home. Brain break: 60 s of star jumps, count once (4.0).

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4, Warm-up 6, Explore 14, Mini-lesson 12.5, Brain break 4, WB page 1 pairs 14.5, WB check p1 4, WB teaching 1.5, WB page 2 alone 9, WB check p2 3, Talk time 5.5, Exit/reflect/close 8.5, Buffer 1.5 (total 90).

### Lesson 7: Percentage Puzzles

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.3 | 1.5 | 2.2 | 0.4 | 5.5 | +2.5 | OVER |
| Warm-up 3-9 | 6 | 0.6 | 2.5 | 2.0 | 0.8 | 5.9 | -0.1 | OK |
| Explore 9-21 | 12 | 1.6 | 2.3 | 6.5 | 3.2 | 13.6 | +1.6 | TIGHT |
| Mini-lesson 21-33 | 12 | 2.3 | 3.2 | 4.0 | 2.5 | 12.0 | -0.0 | OK |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 19.0 | 2.9 | 22.7 | +10.7 | OVER |
| WB check p1 49-53 | 4 | 0.4 | 3.5 | 0.0 | 1.2 | 5.1 | +1.1 | TIGHT |
| WB teaching 53-58 | 5 | 1.0 | 1.0 | 0.0 | 0.8 | 2.8 | -2.2 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 10.0 | 0.9 | 11.1 | -2.9 | OK |
| WB check p2 72-76 | 4 | 0.3 | 2.5 | 0.0 | 0.8 | 3.5 | -0.5 | OK |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.5 | 1.4 | 9.0 | +3.0 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.4 | 1.2 | 6.1 | 1.2 | 9.8 | +1.8 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **99.6** (range 89-110) | **+9.6** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **110.2** | +20.2 | |

Where the time goes:

- The lightest fixed parts of the level: explore 13.6 (+1.6; 6 min of pair work, no breakouts) and mini-lesson 12.0 (no slack) are close to budget.
- Sneak-peek 5.5 (+2.5), talk 9.0 (+3.0), exit 9.8 (+1.8: three-step $26.16 answer on a slip).
- Page 1 content 19.0: Q1 table (10%, 5%, 1%, 15%, 35%, 99%) 5.5, Q2 two shops with discount and GST 9.0, Q3 4.5. A middle pair completes 5 of 11 parts.
- Page 2: plan set (Q4 a-c and Q5, which now has a Start-here line) 10.0 of 12.9; teaching 2.8.
- `teachchange` and `teachdeal` are labelled 72-76 (the page-2 check minutes) but are "optional, after worksheet page 2, for the Think harder page": they are not in the whole-group flow and are not counted. They compete with the check if a tutor shows them.

Fix for this lesson: Page 1 in class = Q1 (a, b) and Q3 (a-c): 10.0 min. Move Q2 (rice cooker, 9.0) to page 2 where it is the first item (it is exactly `we2`/`try2` applied). Page 2 in class = Q2 a-c and Q4 a-c with `teachrem` only; delete `teachtable` and send Q5 to take-home. Relabel `teachchange` / `teachdeal` "after class" (not 72-76). Sneak-peek and talk-time fixes as for all lessons; the exit ticket keeps its 3.5 minutes.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 5.5, Explore 12.5, Mini-lesson 11, Brain break 4.5, WB page 1 pairs 14, WB check p1 3.5, WB teaching 1.5, WB page 2 alone 11.5, WB check p2 3, Talk time 5.5, Exit/reflect/close 9, Buffer 2 (total 90).

### Lesson 8: Angle Chasers

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.8 | +1.8 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.3 | 1.5 | 1.8 | 0.4 | 5.0 | +2.0 | TIGHT |
| Warm-up 3-9 | 6 | 0.9 | 2.5 | 2.0 | 0.8 | 6.2 | +0.2 | OK |
| Explore 9-21 | 12 | 1.6 | 2.3 | 6.5 | 3.7 | 14.1 | +2.1 | OVER |
| Mini-lesson 21-33 | 12 | 3.1 | 3.7 | 3.6 | 2.9 | 13.2 | +1.2 | TIGHT |
| Brain break 33-37 | 4 | 0.8 | 1.3 | 2.0 | 0.4 | 4.5 | +0.5 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 11.8 | 2.9 | 15.4 | +3.4 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 2.5 | 0.0 | 1.2 | 4.1 | +0.1 | OK |
| WB teaching 53-58 | 5 | 1.6 | 1.5 | 0.0 | 1.2 | 4.3 | -0.7 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 6.2 | 0.9 | 7.3 | -6.7 | LOOSE |
| WB check p2 72-76 | 4 | 0.4 | 3.0 | 0.0 | 0.8 | 4.2 | +0.2 | OK |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.5 | 1.4 | 9.0 | +3.0 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.3 | 1.2 | 5.6 | 1.2 | 9.2 | +1.2 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **101.7** (range 91-112) | **+11.7** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **105.1** | +15.1 | |

Where the time goes:

- Page 1 content 11.8 (Q1 4.25; Q2 parallelogram + rhombus + trapezium 8.0, each with a stated angle fact) against 8.3: OVER by 3.4 on content. The page 2 plan set (Q3 b, c and Q4 a, b) is only 6.2 of 12.9, so this is the clearest LOOSE page 2 (-6.7).
- Sneak-peek 5.0, explore 14.1 (+2.1: tearing triangle corners and a quadrilateral on camera, 6 min plus think time), mini-lesson 13.2 (`teachshapes` plus two worked angle chases), talk 9.0.
- Exit 9.2: the exit ticket demands "write the reason for each step".

Fix for this lesson: This lesson is closest to fitting after L4/L7. Page 1 in class = Q1 (a-d) and Q2 a, b (9.2 min; Q2c trapezium to take-home, already practised in `try2` b). Page 2 in class = Q3 (worked start, b) and Q4 a, b with `teachchain` and `teachcombo`; delete `teachcases` and send Q5 (try every case) to take-home or the Think-harder menu. That leaves 5 minutes of buffer: if you want them used, restore Q5 a with `teachcases` (about 3.5 min). Mini-lesson: one item fewer per `try` slide. Explore: pair work capped at 6.5 min.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4, Warm-up 6, Explore 12.5, Mini-lesson 12, Brain break 4.5, WB page 1 pairs 13, WB check p1 3.5, WB teaching 3, WB page 2 alone 7.5, WB check p2 3, Talk time 5.5, Exit/reflect/close 8.5, Buffer 5 (total 90).

### Lesson 9: Pattern Generalisers

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 1.0 | 0.5 | 0.0 | 0.4 | 1.9 | +1.9 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.4 | 1.5 | 2.5 | 0.4 | 5.8 | +2.8 | OVER |
| Warm-up 3-9 | 6 | 0.7 | 2.5 | 3.0 | 0.8 | 7.0 | +1.0 | TIGHT |
| Explore 9-21 | 12 | 1.6 | 2.3 | 9.5 | 5.2 | 18.6 | +6.6 | OVER |
| Mini-lesson 21-33 | 12 | 2.9 | 4.0 | 5.8 | 2.9 | 15.7 | +3.7 | OVER |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.0 | 0.4 | 4.4 | +0.4 | OK |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 16.0 | 3.9 | 20.7 | +8.7 | OVER |
| WB check p1 49-53 | 4 | 0.3 | 3.0 | 0.0 | 1.8 | 5.1 | +1.1 | TIGHT |
| WB teaching 53-58 | 5 | 1.8 | 1.5 | 0.0 | 1.2 | 4.5 | -0.5 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 11.5 | 0.9 | 12.6 | -1.4 | OK |
| WB check p2 72-76 | 4 | 0.4 | 4.0 | 0.0 | 0.8 | 5.1 | +1.1 | TIGHT |
| Talk time 76-82 | 6 | 1.0 | 2.0 | 4.5 | 1.4 | 8.9 | +2.9 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 6.1 | 1.2 | 9.9 | +1.9 | TIGHT |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **113.1** (range 101-126) | **+23.1** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **121.8** | +31.8 | |

Where the time goes:

- Explore 18.6 (+6.6): High Fives (guess for 8 children, build the table 2, 3, 4, 5 ... children, find the pattern for 8 and for 30) needs 9 min of pair work, 30 s think time, a breakout round trip and toothpicks: the largest explore of the level.
- Mini-lesson 15.7 (+3.7): seven slides including three "Your turn" slides (`try1`, `try2`, `try3`) and a two-way border-tile example (`we2`).
- Warm-up 7.0: the deck text says "3 rounds" of Guess My Rule.
- Page 1 content 16.0 against 7.3 (the lowest availability because of the breakout move): Q1 9.0 (tables and chairs, four parts, one explanation), Q2 7.0 (matchstick houses). A middle pair completes 3 of 7 parts.
- Page 2: plan set Q3 + Q4 (a, b) 11.5 of 12.9, near the limit. The worksheet is left with 2.9 of 26 scheduled minutes if the other parts take what they need.

Fix for this lesson: Mini-lesson: delete `try3` (border-tile items; `we2` already shows both ways) and keep two items on `try1`, `try2` (11.5). Warm-up: one round of Guess My Rule. Explore: pairs get 5.5 min (stop the table at 6 children; the quick rule for 8 and 30 goes to the Go further what-if). Page 1 in class = Q1 a, b (tables and chairs and the rule) and Q2 a, b (9.0 min); Q1 c, d and Q2 c to take-home (they repeat the working-backwards practice of `we1`/`try2`). Page 2 in class = Q3 and Q4 a with `teachgs`, `teachsup`; delete `teachmarks` and send Q5 (marks) to take-home. The buffer is only 1 min: use the typed stamp and cut the reflection to one tick if the clock is behind.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 5.5, Explore 13.5, Mini-lesson 11.5, Brain break 4, WB page 1 pairs 14, WB check p1 4, WB teaching 3.5, WB page 2 alone 9, WB check p2 3, Talk time 5.5, Exit/reflect/close 9, Buffer 1 (total 90).

### Lesson 10: Challenge Day

| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |
|---|---|---|---|---|---|---|---|---|
| Opening (before clock) | 0 | 0.9 | 0.5 | 0.0 | 0.4 | 1.9 | +1.9 | PRE-CLOCK |
| Sneak-peek 0-3 | 3 | 1.6 | 1.5 | 2.5 | 0.4 | 6.0 | +3.0 | OVER |
| Warm-up 3-9 | 6 | 1.2 | 2.5 | 3.3 | 0.8 | 7.9 | +1.9 | TIGHT |
| Explore 9-21 | 12 | 1.8 | 2.3 | 9.5 | 4.7 | 18.3 | +6.3 | OVER |
| Mini-lesson 21-33 | 12 | 3.7 | 3.7 | 4.5 | 2.9 | 14.7 | +2.7 | OVER |
| Brain break 33-37 | 4 | 0.7 | 1.3 | 2.5 | 0.4 | 5.0 | +1.0 | TIGHT |
| WB page 1 pairs 37-49 | 12 | 0.8 | 0.0 | 14.0 | 2.9 | 17.7 | +5.7 | OVER |
| WB check p1 49-53 | 4 | 0.2 | 3.0 | 0.0 | 1.2 | 4.4 | +0.4 | OK |
| WB teaching 53-58 | 5 | 1.5 | 1.5 | 0.0 | 1.2 | 4.3 | -0.7 | OK |
| WB page 2 alone 58-72 | 14 | 0.2 | 0.0 | 15.0 | 0.9 | 16.1 | +2.1 | OVER |
| WB check p2 72-76 | 4 | 0.3 | 3.5 | 0.0 | 0.8 | 4.6 | +0.6 | OK |
| Talk time 76-82 | 6 | 1.1 | 2.0 | 4.5 | 1.4 | 9.0 | +3.0 | OVER |
| Exit/reflect/close 82-90 | 8 | 1.5 | 1.2 | 8.2 | 1.6 | 12.5 | +4.5 | OVER |
| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **114.6** (range 102-127) | **+24.6** | |
| **Total if middle pairs finish page 1** | 90 | | | | | **122.3** | +32.3 | |

Where the time goes:

- Exit 12.5 (+4.5): the exit ticket is a three-step backwards problem plus "say which start you used" (5.5 including reading and showing slips), the reflection 2.6, eight certificates and the last stamp 4.5 min (the `end` slide is also a slide change).
- Explore 18.3 (+6.3): "pick 2 of the 4 puzzle cards", each worth about 4.5 min, plus write how you started, plus be ready to teach one card; 9 min of pair work, 30 s think time, a breakout round trip, cards sent to the rooms.
- Mini-lesson 14.7 (+2.7): seven slides (toolbox, three worked examples, two "Your turn" slides, key). Warm-up 7.9 (+1.9): the relay has eight cards, each answered by a volunteer who then invites the next (the `warmIntro` SAY is 94 words, the longest in the level).
- Page 1 content 14.0 (three medium-long questions: logic grid 5.0, working backwards 4.5, units and an extra 4.5) against 8.3: a middle pair completes 1 of 3 questions. The page 2 plan set (Q4, Q5 and Q6 a) needs 15.0 against 12.9: OVER (+2.1), the only OVER page 2 in the level.
- The script is the longest (439 SAY words, 29 slides). Total 114.6; the worksheet is left with only 1.4 of 26 scheduled minutes if the other parts take what they need.

Fix for this lesson: Explore: send one card per room as images and ask each pair to solve ONE card and teach it (the second card becomes the Go further what-if): pair work 6 min, explore 14.5. Mini-lesson: delete `try2` (squares in a 2 by 2 grid is `teachsq` material anyway): 10.5. Warm-up: shorten `warmIntro` to "Mix-up relay: I read a card, a volunteer answers and invites the next volunteer. You may pass once." and read 6 of the 8 cards (volunteers who have not yet answered first). Page 1 in class = Q1 and Q2 (9.5 min); Q3 (draw a model) is the first item of page 2 with Q4 a (6.0). Page 2 teaching = `teachsq` only; `teachliar`, `teachage`, Q5, Q6 and Q4 b, c to take-home. Certificates: show each for 12 s and send the PDF through the approved channel; last stamp typed in the chat. Exit ticket: keep, 3 min of writing.

New budgets (min): Opening (inside the 90) 2, Sneak-peek 4.5, Warm-up 6.5, Explore 14.5, Mini-lesson 10.5, Brain break 4, WB page 1 pairs 13.5, WB check p1 3, WB teaching 2, WB page 2 alone 7.5, WB check p2 3, Talk time 5.5, Exit/reflect/close 10.5, Buffer 3 (total 90).

## 7. Recommended budgets and where the minutes go

Method: each fix is applied in the helper's fix scenario (`plan()` in `docs/audit/timing_p5.py`), the part needs are recomputed, rounded up to half a minute and set as the new budgets; the standing buffer takes what is left. Same assumptions as in section 2. The new totals are exactly 90.

| Part | Old | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Opening (inside the 90) | 0 | 2 | 2 | 2 | 2 | 3.5 | 2 | 2 | 2 | 2 | 2 |
| Sneak-peek | 3 | 4.5 | 4.5 | 4.5 | 4.5 | 4.5 | 4 | 4.5 | 4 | 4.5 | 4.5 |
| Warm-up | 6 | 6 | 6.5 | 6.5 | 6 | 6.5 | 6 | 5.5 | 6 | 5.5 | 6.5 |
| Explore | 12 | 14 | 14 | 13.5 | 13 | 13.5 | 14 | 12.5 | 12.5 | 13.5 | 14.5 |
| Mini-lesson | 12 | 11 | 11 | 12 | 11 | 12 | 12.5 | 11 | 12 | 11.5 | 10.5 |
| Brain break | 4 | 4.5 | 4 | 4 | 4.5 | 4.5 | 4 | 4.5 | 4.5 | 4 | 4 |
| WB page 1 pairs | 12 | 14.5 | 15.5 | 14 | 12.5 | 15 | 14.5 | 14 | 13 | 14 | 13.5 |
| WB check p1 | 4 | 4 | 4 | 3.5 | 3.5 | 3.5 | 4 | 3.5 | 3.5 | 4 | 3 |
| WB teaching | 5 | 3 | 1.5 | 1.5 | 3 | 0 | 1.5 | 1.5 | 3 | 3.5 | 2 |
| WB page 2 alone | 14 | 8 | 8 | 8 | 10 | 7 | 9 | 11.5 | 7.5 | 9 | 7.5 |
| WB check p2 | 4 | 3 | 3 | 2 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| Talk time | 6 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 | 5.5 |
| Exit/reflect/close | 8 | 8 | 8 | 9.5 | 7 | 8.5 | 8.5 | 9 | 8.5 | 9 | 10.5 |
| Buffer | 0 | 2 | 2.5 | 3.5 | 4.5 | 4 | 1.5 | 2 | 5 | 1 | 3 |
| **Total** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** | **90** |

What changes, in one place:

| Where | Old | New | How the budget is met |
|---|---|---|---|
| Opening | 0 (pre-clock) | 2.0 (L5 3.5) | One-paragraph hook, greeting by wave and chat, one-sentence recording notice, "Today we will..." |
| Sneak-peek | 3 | 4-4.5 | One hold-up for both puzzles, no volunteer round, short intro, answer plus one reason; think time stays about a minute each |
| Warm-up | 6 | 5.5-6.5 | 4 quick questions, one game round (L1, L9: the decks must stop saying "3 rounds") |
| Explore | 12 | 12.5-14.5 | Pair work 5.5-6.5 min, protected 30 s think time kept, regroup two questions not three, materials sent the day before, pairs preassigned to breakout rooms |
| Mini-lesson | 12 | 10.5-12.5 | Two items per "Your turn" slide; L5 `teachlist`, L9 `try3`, L10 `try2` removed |
| Page 1 pairs | 12 | 12.5-15.5 | Longer block, but 8.8-11 minutes of middle-child content instead of 9-23 |
| Check p1 | 4 | 3-4 | One pair explains the heaviest question; others clicked through |
| Teaching | 5 | 0-3.5 | Only the teaching slides for questions that stay in class |
| Page 2 | 14 | 7-11.5 | The plan line names the in-class items only; everything else is "take-home / Think harder" |
| Check p2 | 4 | 2-3 | Only the questions that were set |
| Talk time | 6 | 5.5 | Pairs 2 min, volunteers 1.5, Investigation first step to take-home or the next lesson's opener |
| Exit/reflect/close | 8 | 7-10.5 | Typed stamp; reflection 75 s; L10 certificates 12 s each; L3 and L7 keep the longer exit ticket |
| Buffer | 0 | 1.0-5.0 | see section 8 |

What moves to take-home is in each lesson's fix note above. It is moved, not cut: answers, tier labels and the pass option are untouched, and the Investigation prompt stays on its page; only the in-class minutes go.

Honest caveat on the fix: a lesson that fits 90 minutes by this arithmetic keeps about half of its worksheet in class (page 1 about 9-11 minutes of middle-child work, page 2 about 5.5-10 minutes). The rest moves to take-home. Page 2 was already designed as a menu, but the page-1 parts that move are Core parts. If that is too much to lose, the alternative is to lengthen the session to about 105 minutes (the clock estimates in section 3 are 100-115 minutes).

## 8. Standing buffer

Yes. Recommended: **3 minutes held back, not scheduled** (the plan above leaves 1.0-5.0, average 2.9, depending on the lesson), placed at the end ("stamp and goodbye, typed, plus 2-3 minutes of floating time"). With every fixed part already running at or above its budget, no lesson has any slack today, so every glitch lands on the worksheet, which is the least elastic content. A 3-minute buffer covers normal slippage (late arrivals, a mute, a slow breakout) but not the full estimate range of plus or minus 10 minutes, so also add:

1. A printed cut-first list in each tutor script, in this order: the Investigation first step, quick question 4, the Go further what-if, the last in-class item of page 2, the reflection reduced to a one-tick version. These are all "pass is allowed" or optional items, so no rule is broken.
2. Clock checkpoints in the guide: 21 (explore done), 33 (mini done), 37 (break done), 49 (page 1 done), 58 (teaching done), 76 (page 2 check done). If the tutor is more than 2 minutes behind at 37, cut the first item on the list.
3. Fix the heading in `p5/guide.js`: the workbook segment is labelled `37-72 min` but its text runs to minute 76 and the next segment is `76-82`, so a tutor reading the headings sees a 4-minute gap.

## 9. Inconsistencies found in the sources (timing relevant)

- `p5/guide.js`: `seg('37-72 min', 'Workbook ...')` while the DO text and the `p5/data.js` TIMELINE run to 76 (page-2 check 72-76); the same label is repeated in the rebuilt PDF for all ten lessons.
- `p5/data.js` / decks: L1 and L9 warm-up game text says "Play 3 rounds" while the slide note says "play only 1 or 2 rounds"; three rounds cannot fit in 3 minutes.
- Page-1 question numbers: for L3, L4, L8, L9 page 1 has only two questions, so the printed line "After question 3 you may choose" on page 1 points at a question that is on page 2, and the L3 `ws1` / `ws1ans` slides list Q3 on page 1. The source is already being corrected (`pageOne`, `choiceQ` in `p5/data.js`); recheck after the rebuild.
- L7: `teachchange` and `teachdeal` are labelled 72-76 min (the page-2 check) although they are optional after-page-2 slides.
- The P5 guide's REC cue lines do not exist yet (`levels/reccues.js` is new and not required by `p5/guide.js`); its privacy text says to record, while `p5/guide.js` still says "Do not record lessons (this is in the tutor agreement)". The 1.5-minute REC cost is included here.
- Online set-up text mentions breakout rooms for the explore (and page 1) in L1, L2, L6, L9, L10 only; for L3, L4, L5, L7, L8 children work on camera in the main room. The model charges a 2.5 min round trip in the first group and 1 min in the second group; if all lessons use breakouts for explore and page 1 (as "pairs first" implies), add about 3 minutes to each of L3, L4, L5, L7, L8.

## 10. Caveats

Estimates, not stopwatch timings. Biggest uncertainties: how long a mixed group of 10-12 year olds really takes on the puzzles and Your-turn items (plus or minus 15 percent is applied in the ranges), how quickly a tutor switches slides, and whether the group is 6 or 8 children (the model uses 8 for greetings, hand-ins and stamps). The judgement inputs (seconds per puzzle, per Your-turn slide, minutes per worksheet part) are listed in `LES` and `FIX` in the helper so any can be changed and the audit rerun. Think harder / Go further / Investigation pages are not in the whole-group flow and are not timed. Camera and tech glitches are ignored. The source is moving (see the snapshot note at the top): numbers in this file are from the run recorded there.
