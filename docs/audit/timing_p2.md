# Lesson timing audit, Primary 2 (Level N=2, ages 7-9)

*Analysis only. Nothing in content, guides, decks, builds or outputs was edited. Estimates, not stopwatch timings.*
*Model and numbers are reproducible: `python3 -I docs/audit/timing_p2.py` (`--summary`, `--tables`, `--fixed`). Content read live from `p2/data.js`, `split/p2l*/project/slides`, `p2/guide.js` and the rebuilt `p2/Math_Inquirers_P2_Tutor_Guide.pdf` (101 pages, with REC lines) as it stood at about 02:06 UTC on 22 Oct 2026; other jobs were editing `p2/content` and rebuilding PDFs while this audit ran, so a few word counts moved by a few words during the work.*

## 1. Verdict

**No P2 lesson fits its 90 minutes when a tutor really runs it live online from the slides and script.** Walking each lesson slide by slide with the model below, the central estimate is **96.8 to 110.1 minutes** (a fast tutor 87 to 99; a slow one 107 to 123). The sums of the scripted part budgets are all exactly 90, so the plan is not arithmetically wrong. It is wrong because the budgets are *activity* times and leave nothing for the 24 to 30 slide changes, the breakout rooms, the waits after questions and the read-aloud, and because several parts contain more task than the window.

| Lesson | Scripted | As scripted: fast / **central** / slow (time-boxed) | If the MIDDLE child is allowed to finish the Core pages | Over / Loose parts (central) | Slides (shown) | SAY words |
|---|--:|--:|--:|---|--:|--:|
| 1 Digit Detectives | 90 | 88 / **98.5** / 109 | 99.5 | 2 OVER, 0 LOOSE | 28 (24) | 530 |
| 2 Missing Digit Mysteries | 90 | 92 / **101.8** / 113 | 110.3 | 5 OVER, 0 LOOSE | 29 (25) | 542 |
| 3 Legs, Wheels and Arrays | 90 | 91 / **104.0** / 117 | 104.0 | 5 OVER, 0 LOOSE | 29 (25) | 596 |
| 4 Pattern Machines | 90 | 87 / **96.8** / 107 | 101.1 | 4 OVER, 1 LOOSE | 28 (24) | 453 |
| 5 Mystery Number Machines | 90 | 88 / **98.8** / 110 | 99.9 | 4 OVER, 0 LOOSE | 29 (25) | 552 |
| 6 Market Day | 90 | 92 / **103.3** / 115 | 108.6 | 6 OVER, 0 LOOSE | 29 (25) | 516 |
| 7 Fair Shares | 90 | 94 / **104.7** / 116 | 107.2 | 3 OVER, 0 LOOSE | 30 (26) | 469 |
| 8 Shape Builders | 90 | 96 / **106.9** / 119 | 113.2 | 6 OVER, 0 LOOSE | 30 (26) | 484 |
| 9 Measure Masters | 90 | 99 / **110.1** / 122 | 112.7 | 5 OVER, 0 LOOSE | 29 (25) | 549 |
| 10 Challenge Day | 90 | 95 / **106.7** / 119 | 111.3 | 5 OVER, 0 LOOSE | 34 (30) | 524 |

- **All 10 lessons run long: 10 of 10 OVER, 0 whole-lesson LOOSE.** Only one part anywhere is genuinely loose: L4 mini-lesson (8.4 min of need against 12). Talk time (about 6.6 against 8) and the exit ticket (about 5.4 against 7) carry 1 to 2 minutes of slack each, which is the only give in the plan, and it does not cover the overruns.
- **Closest to fitting:** L4 (about +7), L1 and L5 (about +9). **Furthest:** L9 (about +20), L8 and L10 (+17), L7 (+15), L3 (+14).
- **Part by part (central):** sneak-peek OVER in 10 of 10 (+2.4 to +2.7); explore OVER in 10 of 10 (+2.1 to +7.6); mini-lesson OVER in 7, TIGHT in 2, LOOSE in 1; warm-up OVER in 5 (L3, L5, L6, L9, L10); the 52-57 "short teaching" block OVER in 5 (L3, L4, L7, L8, L9, +3.2 to +6.8); worksheet page 1 content OVER in 5 (L2, L4, L6, L8, L10) and page 2 OVER in 3 (L2, L6, L8). Brain break, talk time, looking back and closing are fine.
- **After the fixes in section 6** the expected need is **77 to 85 minutes (central)** inside a 90-minute budget with a named 3 to 5 minute buffer (fast tutor 68 to 74, slow tutor 88 to 96; see section 8 for what that means for the buffer).

## 2. Model (identical for every level; assumptions stated)

| Item | Value used (central) | Fast / slow case |
|---|---|---|
| Tutor speech to 7-9s | 125 words per minute including pauses (SAY lines counted word by word from the guide) | 140 / 110 |
| Questions read aloud | 115 wpm (puzzles, warm-up questions, exit question, talk question, "Your turn" slide text) | 130 / 100 |
| Wait after a group question | 10 s + 20 s to take one or two answers = **30 s** | 20 / 40 |
| "Hold up boards / papers" | 30 s (plus 20 s to click the answer) | 20 / 40 |
| Slide change online | **25 s** each (24 to 30 slides are shown per lesson; stretch, challenge and the two challenge-diagram slides are not shown to the group) | 20 / 30 |
| Breakout rooms (explore only; the guide's online column puts pairs in rooms) | 90 s in + 90 s out | 60 / 120 each way |
| Finding / handing out materials | 20 to 150 s per lesson, set by the actual kit (L2 pencils only 20 s; L9 coat-hanger balance 150 s) | x0.7 / x1.3 |
| Worksheet start | 2 min (find the page, read the title, pairs set up) | same |
| REC cue lines | 10 s said at the start of each of the 11 guide segments (1.8 min per lesson) | 8 / 10 |
| Activity time | scripted time for the break (3 min of movement + water inside the 4); explore pair work and worksheet judged from the actual task content (below) | x0.92 / x1.10 |
| Worksheet demand | minutes per numbered Core question, set by me from the printed page: 2.5 to 3 for a short multi-part item, 4 to 6 for a 3-4 part item with a table or an explanation, 7.5 to 9 for the two heavy L8 items. MIDDLE child, working alone. Pairs x1.15 (talk before write). LOW x1.7, HIGH x0.65. | |
| Flags | diff = needed - scripted. **OVER** >= +2.0; **TIGHT** +0.5 to +2.0; **OK** -3.0 to +0.5; **LOOSE** <= -3.0 (dead time) | |

Two totals are given. **Time-boxed** (headline) assumes the tutor stops the two worksheet work windows on the clock (14 min pairs, 12 min alone) even when the MIDDLE child has not finished. **Content-complete** lets the MIDDLE child finish all Core questions; the worksheet rows then show the demand against the window. Camera and tech glitches, late arrivals, toilet breaks beyond the 4-minute break and parents' questions are ignored; so every "OK" row has no give for them. **Not counted, and real:** the REC lines are about 14 s each as actually written (290 words over 11 lines, about 2.3 min, so about +0.5 min on the model); the guide's recording rules (say the page and question number aloud every time, read each question aloud as well as showing it, repeat each child's answer in your own words, show a timer) are not costed and could add 2 to 4 minutes; the tutor circulating during pairs/alone work is parallel time and is not added.

**Walk-through per part (what is counted).** *Opening:* hook SAY, "Today we will..." read, title slide, greeting 8 children (16 s). *Sneak-peek:* `common.preSay` (57 words), the two puzzle texts read aloud, 60 s + 120 s of child work (as scripted), 20 s papers shown privately, answer slide. *Warm-up:* intro SAY, the game (6 cards or 3 rounds, timed per game), three quick questions (1, 3, 5) at 30 s each, two slides. *Explore:* predict + setup + debrief questions read, 3 or more slides, 2 breakout moves, materials, pair work, 3 debrief questions at 30 s wait + 30 s discussion. *Mini-lesson:* the `think` SAY paragraphs + key-idea SAY + half of each worked-example slide's text, one group question per teach/worked slide, 3-item "Your turn" slides at 35-70 s per item + hold-up. *Worksheet:* 2-min start, page 1, check slide (8 s per lettered answer, 15 s per question, 30 s per "how do you know"), 52-57 teaching slides (their on-slide text as narration, one question each, any "Your turn" tasks), page 2, check slide. *Talk:* talk SAY, question, 2 min pairs, three 45 s shares, closing 45 s. *Exit:* question read, the child's work (75 to 150 s by task), 8 children x 15 s to show the tutor, answer reveal. *Looking back:* `refSay` + 75 s of writing. *Close:* closing SAY + stamps.

## 3. Level-wide findings

**Where a typical lesson's 106 minutes go (central, content-complete, mean of 10):** children working about 60 min; slide changes, rooms, materials and worksheet start about 18 min (of which slide changes alone are 10 to 12.5 min); waiting after questions about 11 min; tutor speech about 16 min; REC lines 1.8 min. The tutor's *speech* is not the problem (SAY lines total 453 to 596 words, about 3.6 to 4.8 minutes; L4 smallest, L3 largest). The problem is the number of small steps and the practice duplicated on slides.

**Mean excess over the scripted budget, by part (minutes, central, time-boxed):** explore +4.9; sneak-peek +2.5; mini-lesson +2.4; 52-57 teaching +2.3; warm-up +2.0; check page 1 +0.9; opening/looking back/closing +0.3 to +0.4 each; brain break 0; worksheet pages 0 (time-boxed); exit ticket -1.2; talk time -1.4.

**The three biggest time sinks across the level**
1. **Explore (8-20): +4.9 min on average, OVER in all ten.** About 5 to 7 of its 15 to 19 needed minutes are not mathematics: two breakout moves (3 min), finding materials (0.3 to 2.5 min), three slides (explore1, goexp, explore2; seven in L10) and 30 s waits on three debrief questions. L7, L9, L8, L10, L5 and L6 also have too much task for six minutes of pair work (folding and labelling 15 strip parts; hanging a coat-hanger balance and testing two objects; cutting two circles; two station cards; a two-role machine game; a toy-stall list to $10).
2. **Practice slides that duplicate the worksheet: mini-lesson "Your turn" slides and the 52-57 teaching block.** Every lesson has 2 to 3 three-item whiteboard slides in the mini-lesson and, in L3, L4, L7, L8, L9, more "Your turn" slides before page 2. They cost 1.5 to 3 min each (slide change, read, work, hold up, click) and then the child does the same type of question again on the worksheet. Mini-lesson +2.4 average (L2 +7.3, L10 +4.2, L9 +4.0) and 52-57 teaching +2.3 average (L8 +6.8, L9 +5.5, L3 +4.4, L4 +3.7, L7 +3.2).
3. **Fixed overhead that is the same in every lesson:** the sneak-peek (3 min scripted, about 5.4 needed: 3 min of child work leaves no room for the instructions, reading two puzzles and revealing answers) and the warm-up (4 scripted, 4.6 to 8.1 needed: game plus three quick questions plus two slide changes). Together +4.5 min in every lesson before the lesson has started.

**Slide and script size.** 28 to 30 slides in nine lessons and **34 in L10 (30 shown; the four station cards are four slides in one 5-minute window)**. L7 and L8 have 30 and L2, L3, L5, L6, L9 have 29. At 25 s a change, shown slides cost 10.0 min (L1, L4) to 12.5 min (L10) per lesson. The speaker notes are far larger than the SAY lines (2,670 to 3,710 words of notes per lesson against 450 to 600 SAY words); a tutor who reads the notes aloud is lost, so the SAY lines are what was timed. Largest on-slide text: L9 `we2` (jug table, 131 words), L5 `teachrule` (120), L1 `teachriddle` (116), L9 `we1` (100).

**No slack anywhere (every "OK" has none to spare for a glitch):** opening, brain break, looking back (needs 2.2 of 2), closing (needs 1.4 of 1). Looking back and closing are fixed items; in L10 certificates (3 min for 8 children) and the exit ticket (5 min scripted, 6.4 needed) are the same.

**Source consistency found while walking the lessons**
- L2 `key` slide is tagged "35 MIN" (should be 31-32). L10 `reflect` slide is tagged "87-89 MIN" but the script and notes say 85-87.
- L3 deck text (`ws2`) says page 2 includes "Q7 bicycles and tricycles"; in the printed workbook Q7 is Go further 7, and the Core is Q1-Q6.
- The guide says "one slide or two for each part". The decks show 24 to 30 slides per lesson; `goexp` shares the 8-14 window with `explore1`.
- Nothing in the guide says whether worksheet pairs are in breakout rooms; I assumed they stay in the main room (only explore uses rooms). If worksheet pairs also use rooms, add 3 min to each lesson.
- The guide table says Looking back is "a small box on the last core page"; the rebuilt guide now says the box is on the "Before you go" page after page 2, so children turn a page during the 2 minutes.

## 4. Worksheet block: what children can actually do

Per-question minutes are for a MIDDLE child alone (pairs x1.15 on page 1). Windows: page 1 has 14 min including the 2-min start (12 usable; 10 usable in L5, L6, L10 where a 2-min teach slide precedes it); page 2 has 12.

| Lesson | Page 1 Core (min) | pairs | Page 2 Core (min) | Core items finished in class as scripted (page 1 + page 2 = of Core): LOW / MIDDLE / HIGH | HIGH spare time for Think harder (min) |
|---|---|--:|---|---|--:|
| 1 | 2.5 + 4 + 3 = 9.5 | 10.9 | 4 + 3 + 6 = 13.0 | 1+2=3 / 3+2=5 / 3+3=6 (of 6) | 8 |
| 2 | 4 + 4 + 6 = 14.0 | 16.1 | 5.5 + 6 + 4 = 15.5 | 1+1=2 / 2+2=4 / 3+3=6 (of 6) | 3 |
| 3 | 2.5 + 3 + 4 = 9.5 | 10.9 | 3.5 + 2.5 + 5 = 11.0 | 2+2=4 / 3+3=6 / 3+3=6 (of 6) | 10 |
| 4 | 4.5 + 4.5 + 3.5 = 12.5 | 14.4 | 4 + 5 + 4 = 13.0 | 1+1=2 / 2+2=4 / 3+3=6 (of 6) | 6 |
| 5 | 5.5 + 3.5 = 9.0 | 10.3 | 3.5 + 4 + 4 = 11.5 | 0+1=1 / 2+3=5 / 2+3=5 (of 5) | 8 |
| 6 | 5 + 5 = 10.0 | 11.5 | 3.5 + 4.5 + 2 + 5 = 15.0 | 1+1=2 / 1+3=4 / 2+4=6 (of 6) | 5 |
| 7 | 3 + 2 + 5.5 = 10.5 | 12.1 | 6 + 3.5 + 4 = 13.5 | 2+1=3 / 3+2=5 / 3+3=6 (of 6) | 7 |
| 8 | 5 + 7.5 = 12.5 | 14.4 | 6 + 9 = 15.0 | 1+1=2 / 1+1=2 / 2+2=4 (of 4) | 5 |
| 9 | 5 + 6 = 11.0 | 12.6 | 4 + 4 + 5 = 13.0 | 1+1=2 / 1+2=3 / 2+3=5 (of 5) | 7 |
| 10 | 4.5 + 3.5 + 4 = 12.0 | 13.8 | 4 + 3.5 + 4 = 11.5 | 1+1=2 / 2+3=5 / 3+3=6 (of 6) | 6 |

Reading it: a HIGH child finishes every Core item in every lesson. A MIDDLE child finishes all Core only in L3 and L5; he or she misses one item in L1, L7 and L10 and two items in L2, L4, L6, L8 and L9. L8 is the extreme (MIDDLE 2 of 4: Q2 "count every square by size" and Q4 "cut out four nets and fold them" are 7.5 and 9 min each on their own). A LOW child finishes 1 to 4 items (L5: 1 of 5). That is acceptable under the no-pressure rule as long as the check-together slides do not assume completion, but it means the "choose Think harder" invitation after question 3 is effectively used only by HIGH children, who have about 3 to 10 spare minutes, enough for one Think harder item (4 to 6 min). The seven Think harder / Go further items and the Investigation per lesson are therefore a take-home resource, not an in-class one.

## 5. Per-lesson walk-through (as scripted)

### Lesson 1: Digit Detectives

**Total 98.5 (fast 88, slow 109).** Closest to fitting after L4. Sneak-peek +2.4, explore +3.3 (15.3: 5.2 min of transitions: 3 slides, two rooms, cards found; the pair task itself, 3 cards -> 6 numbers, is fine at 4.5 min), warm-up TIGHT (+1.3: 3 rounds of Place It Right at about 45 s plus 3 quick questions), check-together page 1 TIGHT (+1.7: 10 lettered answers), 52-57 teaching TIGHT (+1.4: three slides; `teachriddle` has 116 words), page 2 content 13.0 min for 12 (Q6b "find ALL numbers whose digits add to 3" is 3 to 4 min alone). Worksheet items: LOW 3, MIDDLE 5, HIGH 6 of 6.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.6 | 0.0 | 0.0 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| Sneak-peek 1-4 | 3 | 1.2 | 0.0 | 3.3 | 0.7 | 0.17 | **5.4** | +2.4 | OVER |
| Warm-up 4-8 | 4 | 0.6 | 1.5 | 2.2 | 0.8 | 0.17 | **5.3** | +1.3 | TIGHT |
| Explore 8-20 | 12 | 1.1 | 3.4 | 5.5 | 5.2 | 0.17 | **15.3** | +3.3 | OVER |
| Mini-lesson 20-32 | 12 | 2.7 | 3.4 | 3.8 | 2.5 | 0.17 | **12.5** | +0.5 | TIGHT |
| Brain break 32-36 | 4 | 0.3 | 0.0 | 3.2 | 0.4 | 0.17 | **4.2** | +0.2 | OK |
| WS page 1 pairs 36-50 | 14 | 0.4 | 0.0 | 10.9 | 2.4 | 0.17 | **13.9** | -0.1 | OK |
| WS check page 1 50-52 | 2 | 3.2 | 0.0 | 0.0 | 0.4 | 0.00 | **3.7** | +1.7 | TIGHT |
| WS teaching 52-57 | 5 | 1.7 | 1.5 | 1.9 | 1.2 | 0.00 | **6.4** | +1.4 | TIGHT |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 13.0 | 0.0 | 0.00 | **13.0** | +1.0 | TIGHT |
| WS check page 2 69-72 | 3 | 2.5 | 0.0 | 0.0 | 0.4 | 0.00 | **2.9** | -0.1 | OK |
| Talk time 72-80 | 8 | 0.5 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-87 | 7 | 0.4 | 0.0 | 3.8 | 0.9 | 0.17 | **5.2** | -1.8 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.2 | 0.0 | 0.3 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| **Total** | **90** | 15.9 | 10.3 | 54.3 | 17.3 | 1.8 | **99.5** (time-boxed 98.5) | +9.5 | |

**Fixes for L1** (on top of the level-wide changes in section 6a):

- `warm1`: play **two** rounds (biggest, smallest) instead of three. `warm2`: ask questions 1 and 3 only (5 is spare).
- `try1`: items a and b only; drop c ("what is the 6 worth in 461?", already asked in warm-up question 2).
- **Page 2:** move **Q5 (count on and back, four items)** and **Q4(b)** to a take-home star and take the `teachcount` slide (54-55) with them. Page-2 demand 13.0 -> 9.5 min; 52-57 block 3.4 min.
- `ws1ans`: read the answer lines only (10 lettered answers); `ws2ans` likewise. Talk time: first question only (401 or 399); the "second question if time" line in the `talk` note is removed.

**Core items done in class after the fixes (in-class Core = 5 of 6):** LOW 1+1=2 / MIDDLE 3+2=5 / HIGH 3+2=5. Expected need after fixes: **81 (fast 71, slow 91)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.2 | +0.3 | 1.0 / 1.3 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.2 | +0.3 | 3.8 / 4.6 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.2 | +0.3 | 3.5 / 4.9 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 12.7 | +0.3 | 10.3 / 15.1 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 12.0 | +0.0 | 10.0 / 14.0 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.9 | +0.1 | 2.6 / 3.2 |
| 38.5-52.5 | WS page 1 pairs 36-50 | 14 | 14.0 | 13.9 | +0.1 | 12.8 / 15.1 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 2.7 | -0.2 | 2.6 / 2.8 |
| 55-59.5 | WS teaching 52-57 | 5 | 4.5 | 3.4 | +1.1 | 2.8 / 4.1 |
| 59.5-71 | WS page 2 alone 57-69 | 12 | 11.5 | 9.5 | +2.0 | 8.7 / 10.4 |
| 71-73.5 | WS check page 2 69-72 | 3 | 2.5 | 1.8 | +0.8 | 1.7 / 1.8 |
| 73.5-76.5 | Standing buffer | - | 3.0 | 0.0 | +3.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.0 / 5.3 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 4.4 | +0.6 | 4.1 / 4.6 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.4 | +0.1 | 1.3 / 1.5 |
| 0-90 | **Total** | 90 | 90.0 | 80.9 | +9.1 | 71.2 / 91.4 |

### Lesson 2: Missing Digit Mysteries

**Total 101.8 (fast 92, slow 113); content-complete 110.3.** The mini-lesson is the problem: seven slides (`teach1`, `try1`, `we2`, `try2`, `teach3`, `try3`, `key`) with three 3-item missing-digit "Your turn" slides at 45-60 s per item: **19.0 min against 12**. Page 1 is 14.0 min of Core alone (16.1 in pairs) in a 12-minute window (Q1 three missing-digit sums, Q2 two subtractions with borrowing, Q3 four balance items including an explanation), and page 2 is 15.5 (Q5 magic triangle is 5 to 6 min of trial and error on its own). Both worksheet pages OVER. Worksheet items: LOW 2, MIDDLE 4, HIGH 6 of 6. Also: `key` slide is tagged "35 MIN".

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.5 | 0.0 | 0.0 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| Sneak-peek 1-4 | 3 | 1.2 | 0.0 | 3.3 | 0.7 | 0.17 | **5.4** | +2.4 | OVER |
| Warm-up 4-8 | 4 | 0.3 | 1.5 | 1.8 | 0.8 | 0.17 | **4.6** | +0.6 | TIGHT |
| Explore 8-20 | 12 | 1.0 | 3.4 | 5.0 | 4.6 | 0.17 | **14.1** | +2.1 | OVER |
| Mini-lesson 20-32 | 12 | 3.7 | 4.2 | 8.2 | 2.9 | 0.17 | **19.3** | +7.3 | OVER |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.1** | +0.1 | OK |
| WS page 1 pairs 36-50 | 14 | 0.4 | 0.0 | 16.1 | 2.4 | 0.17 | **19.0** | +5.0 | OVER |
| WS check page 1 50-52 | 2 | 3.2 | 0.0 | 0.0 | 0.4 | 0.00 | **3.7** | +1.7 | TIGHT |
| WS teaching 52-57 | 5 | 1.9 | 1.5 | 1.0 | 1.2 | 0.00 | **5.6** | +0.6 | TIGHT |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 15.5 | 0.0 | 0.00 | **15.5** | +3.5 | OVER |
| WS check page 2 69-72 | 3 | 2.2 | 0.0 | 0.0 | 0.4 | 0.00 | **2.6** | -0.4 | OK |
| Talk time 72-80 | 8 | 0.5 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-87 | 7 | 0.3 | 0.0 | 3.5 | 0.9 | 0.17 | **4.9** | -2.1 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.2 | 0.0 | 0.3 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| **Total** | **90** | 16.1 | 11.1 | 64.3 | 17.0 | 1.8 | **110.3** (time-boxed 101.8) | +20.3 | |

**Fixes for L2** (on top of the level-wide changes in section 6a):

- **Mini-lesson 19.0 -> 11.5:** merge `we2` into `teach1` (one slide: start at the ones; for subtraction turn it round into an addition; the SAY paragraphs stay), **delete `try3`** (its three items are the same as worksheet Q3 a-c), `try1` items a and b, `try2` item a only; keep `teach3` and `key`.
- **Page 1 (16.1 -> 11.3 min pairs):** move **Q3 c and d** and the "check one of your answers by adding the full numbers" line of Q1 to take-home.
- **Page 2 (15.5 -> 9.5):** move **Q5 (magic triangle)** to take-home and post `teachtri` with it; the 52-57 block keeps `teachsq` and `teachtwo` (3.7 min).
- Correct the `key` slide tag from "35 MIN" to 31-32.

**Core items done in class after the fixes (in-class Core = 5 of 6):** LOW 1+1=2 / MIDDLE 3+2=5 / HIGH 3+2=5. Expected need after fixes: **79 (fast 70, slow 89)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.1 | +0.4 | 0.9 / 1.3 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.2 | +0.3 | 3.8 / 4.6 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.0 | +0.5 | 3.3 / 4.7 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 11.9 | +1.1 | 9.6 / 14.4 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 11.5 | +0.5 | 9.8 / 13.4 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.8 | +0.2 | 2.5 / 3.1 |
| 38.5-52.5 | WS page 1 pairs 36-50 | 14 | 14.0 | 14.2 | -0.2 | 13.2 / 15.5 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 2.2 | +0.2 | 2.2 / 2.3 |
| 55-59.5 | WS teaching 52-57 | 5 | 4.5 | 3.7 | +0.8 | 3.0 / 4.4 |
| 59.5-71 | WS page 2 alone 57-69 | 12 | 11.5 | 9.5 | +2.0 | 8.7 / 10.4 |
| 71-73.5 | WS check page 2 69-72 | 3 | 2.5 | 1.8 | +0.8 | 1.7 / 1.8 |
| 73.5-76.5 | Standing buffer | - | 3.0 | 0.0 | +3.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.0 / 5.2 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 4.1 | +0.9 | 3.8 / 4.3 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.4 | +0.1 | 1.2 / 1.5 |
| 0-90 | **Total** | 90 | 90.0 | 79.1 | +10.9 | 69.6 / 89.3 |

### Lesson 3: Legs, Wheels and Arrays

**Total 104.0 (fast 91, slow 117).** Biggest SAY text of the level (596 words). Warm-up OVER (+2.5): six picture cards counted in 2s, 3s, 4s and 5s at about 35 s each is 3.5 min for a 2-minute game. Mini-lesson +2.2 (six slides, two 3-item "Your turn" slides). **52-57 block 9.4 for 5 min (+4.4):** `teachshare`, `teachround`, `teachall` and `try3` (three 20-60 s items). The worksheet itself **fits** (page 1 10.9 pairs, page 2 11.0): L3 is the only lesson where a MIDDLE child finishes all six Core items. Exit ticket (hens and goats, 5 animals, 14 legs) needs a table: about 2.5 min of child work. Deck `ws2` text mentions a Q7 that is a Go further item.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.7 | 0.0 | 0.0 | 0.7 | 0.17 | **1.5** | +0.5 | TIGHT |
| Sneak-peek 1-4 | 3 | 1.4 | 0.0 | 3.3 | 0.7 | 0.17 | **5.5** | +2.5 | OVER |
| Warm-up 4-8 | 4 | 0.5 | 1.5 | 3.5 | 0.8 | 0.17 | **6.5** | +2.5 | OVER |
| Explore 8-20 | 12 | 1.1 | 3.4 | 6.0 | 5.2 | 0.17 | **15.8** | +3.8 | OVER |
| Mini-lesson 20-32 | 12 | 3.6 | 3.4 | 4.5 | 2.5 | 0.17 | **14.2** | +2.2 | OVER |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.1** | +0.1 | OK |
| WS page 1 pairs 36-50 | 14 | 0.4 | 0.0 | 10.9 | 2.4 | 0.17 | **13.9** | -0.1 | OK |
| WS check page 1 50-52 | 2 | 2.2 | 0.0 | 0.0 | 0.4 | 0.00 | **2.6** | +0.6 | TIGHT |
| WS teaching 52-57 | 5 | 2.1 | 2.3 | 3.3 | 1.7 | 0.00 | **9.4** | +4.4 | OVER |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 11.0 | 0.0 | 0.00 | **11.0** | -1.0 | OK |
| WS check page 2 69-72 | 3 | 2.2 | 0.0 | 0.0 | 0.4 | 0.00 | **2.6** | -0.4 | OK |
| Talk time 72-80 | 8 | 0.5 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-87 | 7 | 0.4 | 0.0 | 5.0 | 0.9 | 0.17 | **6.5** | -0.5 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.3 | 0.0 | 0.3 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| **Total** | **90** | 16.0 | 11.1 | 57.4 | 17.7 | 1.8 | **104.0** (time-boxed 104.0) | +14.0 | |

**Fixes for L3** (on top of the level-wide changes in section 6a):

- `warm1`: show **three** of the six picture cards (cars, hens, bicycles) and count in 2s and 4s; `warm2`: questions 1 and 3.
- **Mini-lesson 14.2 -> 10.0:** **delete `try1`** (arrays: worksheet Q1 and Q2 are the same tasks), `try2` items a and b only (hens and goats, bicycles and tricycles).
- **52-57 block 9.4 -> 4.6:** **delete `try3`** (three items that repeat Q4-Q6); keep `teachshare`, `teachround`, `teachall`.
- Exit ticket: allow 2 min of child work (the child has already built the same table in explore, `teach2` and Q3).
- The worksheet needs no cut: all six Core items fit. Correct `ws2` text ("Q7 bicycles and tricycles" is Go further 7).

**Core items done in class after the fixes (in-class Core = 6 of 6):** LOW 2+2=4 / MIDDLE 3+3=6 / HIGH 3+3=6. Expected need after fixes: **82 (fast 72, slow 93)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.2 | +0.3 | 1.1 / 1.4 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.3 | +0.2 | 3.9 / 4.8 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.2 | +0.3 | 3.5 / 4.9 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 12.2 | +0.8 | 9.8 / 14.7 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 10.0 | +2.0 | 8.4 / 11.8 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.8 | +0.2 | 2.5 / 3.1 |
| 38.5-52.5 | WS page 1 pairs 36-50 | 14 | 14.0 | 13.9 | +0.1 | 12.8 / 15.1 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 2.1 | +0.4 | 2.0 / 2.2 |
| 55-59.5 | WS teaching 52-57 | 5 | 4.5 | 4.6 | -0.1 | 3.7 / 5.6 |
| 59.5-71 | WS page 2 alone 57-69 | 12 | 11.5 | 11.0 | +0.5 | 10.1 / 12.1 |
| 71-73.5 | WS check page 2 69-72 | 3 | 2.5 | 2.1 | +0.4 | 2.0 / 2.2 |
| 73.5-76.5 | Standing buffer | - | 3.0 | 0.0 | +3.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.0 / 5.3 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 5.1 | -0.1 | 4.8 / 5.5 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.4 | +0.1 | 1.3 / 1.6 |
| 0-90 | **Total** | 90 | 90.0 | 81.9 | +8.1 | 72.0 / 92.7 |

### Lesson 4: Pattern Machines

**Total 96.8 (fast 87, slow 107): the closest to 90.** It is also the only lesson with a LOOSE part: **the mini-lesson needs 8.4 of 12 (-3.6)**: five slides and one 3-item "Your turn" (`try1`, bead colours). While the 52-57 block is overloaded (+3.7: `teachtimes`, `teachgrow`, `teachboth` and `try2`, 8.7 min) and page 1 is OVER (+3.3: Q1c "how do you know", Q2c "30 letters, how many Ts, show how", Q3 bead string 12.5 min alone, 14.4 in pairs). Page 2 13.0 for 12. Worksheet items: LOW 2, MIDDLE 4, HIGH 6 of 6. Smallest SAY text (453 words).

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.5 | 0.0 | 0.0 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| Sneak-peek 1-4 | 3 | 1.2 | 0.0 | 3.3 | 0.7 | 0.17 | **5.4** | +2.4 | OVER |
| Warm-up 4-8 | 4 | 0.3 | 1.5 | 2.0 | 0.8 | 0.17 | **4.8** | +0.8 | TIGHT |
| Explore 8-20 | 12 | 0.9 | 3.4 | 5.0 | 5.8 | 0.17 | **15.2** | +3.2 | OVER |
| Mini-lesson 20-32 | 12 | 2.1 | 2.6 | 1.5 | 2.1 | 0.17 | **8.4** | -3.6 | LOOSE |
| Brain break 32-36 | 4 | 0.1 | 0.0 | 3.2 | 0.4 | 0.17 | **4.0** | -0.0 | OK |
| WS page 1 pairs 36-50 | 14 | 0.4 | 0.0 | 14.4 | 2.4 | 0.17 | **17.3** | +3.3 | OVER |
| WS check page 1 50-52 | 2 | 3.0 | 0.0 | 0.0 | 0.4 | 0.00 | **3.4** | +1.4 | TIGHT |
| WS teaching 52-57 | 5 | 1.9 | 2.3 | 2.8 | 1.7 | 0.00 | **8.7** | +3.7 | OVER |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 13.0 | 0.0 | 0.00 | **13.0** | +1.0 | TIGHT |
| WS check page 2 69-72 | 3 | 3.4 | 0.0 | 0.0 | 0.4 | 0.00 | **3.8** | +0.8 | TIGHT |
| Talk time 72-80 | 8 | 0.6 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-87 | 7 | 0.4 | 0.0 | 4.0 | 0.9 | 0.17 | **5.4** | -1.6 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.2 | 0.0 | 0.3 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| **Total** | **90** | 15.4 | 10.3 | 55.9 | 17.8 | 1.8 | **101.1** (time-boxed 96.8) | +11.1 | |

**Fixes for L4** (on top of the level-wide changes in section 6a):

- **Use the loose 3.6 min in the mini-lesson:** move **`teachtimes` and `teachgrow`** (the "pattern machine / times table" and "growing pattern: find the rule" slides, now at 52-55) into the mini-lesson after `teachcount`. The mini-lesson then needs 10.7 of 12 and the key slide already names both ideas.
- **52-57 block 8.7 -> 1.8:** keep only `teachboth`; **delete `try2`** (three items repeating Q4-Q6). Budget 2.5; the freed 2 min go to the buffer.
- **Page 1 (14.4 -> 11.3 min in pairs):** move **Q2(c)** (30 letters, count the Ts) and **Q3(b)** (beads altogether) to take-home. **Page 2 (13.0 -> 11.2):** move **Q4(d)** (23 petals, flowers and left over) and **Q5(d)** (why does it go up by 2) to take-home.

**Core items done in class after the fixes (in-class Core = 6 of 6):** LOW 1+2=3 / MIDDLE 3+3=6 / HIGH 3+3=6. Expected need after fixes: **79 (fast 69, slow 89)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.1 | +0.4 | 0.9 / 1.3 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.2 | +0.3 | 3.8 / 4.6 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 3.8 | +0.7 | 3.1 / 4.5 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 12.0 | +1.0 | 9.6 / 14.5 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 10.7 | +1.3 | 8.7 / 12.8 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.7 | +0.3 | 2.4 / 3.0 |
| 38.5-52.5 | WS page 1 pairs 36-50 | 14 | 14.0 | 14.2 | -0.2 | 13.2 / 15.5 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 2.1 | +0.4 | 2.0 / 2.2 |
| 55-57.5 | WS teaching 52-57 | 5 | 2.5 | 1.8 | +0.7 | 1.5 / 2.2 |
| 57.5-69 | WS page 2 alone 57-69 | 12 | 11.5 | 11.2 | +0.3 | 10.3 / 12.3 |
| 69-71.5 | WS check page 2 69-72 | 3 | 2.5 | 2.3 | +0.2 | 2.2 / 2.4 |
| 71.5-76.5 | Standing buffer | - | 5.0 | 0.0 | +5.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.1 / 5.3 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 4.6 | +0.4 | 4.3 / 4.9 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.4 | +0.1 | 1.2 / 1.5 |
| 0-90 | **Total** | 90 | 90.0 | 79.0 | +11.0 | 69.4 / 89.4 |

### Lesson 5: Mystery Number Machines

**Total 98.8 (fast 88, slow 110).** Explore is the worst part (+5.2, 17.2 min): two roles (one partner runs a secret two-step machine, the other works backwards), then swap roles, then swap the order of the two cards (7 min of pair work) plus 5.2 min of transitions. Warm-up OVER (+2.3: "Guess my machine", five rounds plus OUT -> IN rounds at about 30 s). Mini-lesson +2.3 (six slides, two 3-item "Your turn"; `we1` and `we2` are the long ones). A 2-minute teach slide (`teachrule`, 120 words, "find a two-step rule") precedes page 1, so pairs have 10 usable minutes against 10.4 needed. Only five Core questions, which is why page 2 fits (11.5). 52-57 block is fine (3.7 of 5). Worksheet items: LOW 1, MIDDLE 5, HIGH 5 of 5.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.5 | 0.0 | 0.0 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| Sneak-peek 1-4 | 3 | 1.2 | 0.0 | 3.3 | 0.7 | 0.17 | **5.4** | +2.4 | OVER |
| Warm-up 4-8 | 4 | 0.8 | 1.5 | 3.0 | 0.8 | 0.17 | **6.3** | +2.3 | OVER |
| Explore 8-20 | 12 | 1.4 | 3.4 | 7.0 | 5.2 | 0.17 | **17.2** | +5.2 | OVER |
| Mini-lesson 20-32 | 12 | 3.2 | 3.4 | 5.0 | 2.5 | 0.17 | **14.3** | +2.3 | OVER |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.0** | +0.0 | OK |
| WS teach slide 36-38 | 2 | 0.9 | 0.5 | 0.7 | 0.4 | 0.17 | **2.7** | +0.7 | TIGHT |
| WS page 1 pairs 38-50 | 12 | 0.4 | 0.0 | 10.3 | 2.4 | 0.00 | **13.1** | +1.1 | TIGHT |
| WS check page 1 50-52 | 2 | 1.5 | 0.0 | 0.0 | 0.4 | 0.00 | **1.9** | -0.1 | OK |
| WS teaching 52-57 | 5 | 1.3 | 1.0 | 0.5 | 0.8 | 0.00 | **3.7** | -1.3 | OK |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 11.5 | 0.0 | 0.00 | **11.5** | -0.5 | OK |
| WS check page 2 69-72 | 3 | 2.2 | 0.0 | 0.0 | 0.4 | 0.00 | **2.6** | -0.4 | OK |
| Talk time 72-80 | 8 | 0.6 | 0.5 | 5.0 | 0.4 | 0.17 | **6.7** | -1.3 | OK |
| Exit ticket 80-87 | 7 | 0.4 | 0.0 | 4.0 | 0.9 | 0.17 | **5.5** | -1.5 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.2 | 0.0 | 0.3 | 0.7 | 0.17 | **1.3** | +0.3 | OK |
| **Total** | **90** | 15.4 | 10.3 | 55.2 | 17.3 | 1.8 | **99.9** (time-boxed 98.8) | +9.9 | |

**Fixes for L5** (on top of the level-wide changes in section 6a):

- `warm1` ("Guess my machine"): three rounds (two IN -> OUT guesses, one OUT -> IN), `warm2` questions 1 and 3.
- **Explore 17.2 -> 12.2:** drop step 4 of the setup ("swap the order of the two cards") and debrief question 3 ("does it matter which card goes first?"): slide `teachorder` (55-57) and worksheet Q5 are exactly that question. Pairs 5.5 min.
- **Mini-lesson 14.3 -> 11.8:** `try1` item a only (b and c repeat Q1), `try2` items a and b.
- **Page 1:** move **Q1(d)** (x 4, then take away 15) to take-home. Pairs then need 8.7 min against 9.4 usable.

**Core items done in class after the fixes (in-class Core = 5 of 5):** LOW 1+1=2 / MIDDLE 2+3=5 / HIGH 2+3=5. Expected need after fixes: **83 (fast 72, slow 93)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.1 | +0.4 | 0.9 / 1.3 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.2 | +0.3 | 3.8 / 4.6 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.7 | -0.2 | 3.9 / 5.5 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 12.2 | +0.8 | 10.0 / 14.6 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 11.8 | +0.2 | 9.9 / 13.8 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.8 | +0.2 | 2.5 / 3.1 |
| 38.5-41 | WS teach slide 36-38 | 2 | 2.5 | 2.7 | -0.2 | 2.3 / 3.1 |
| 41-52.5 | WS page 1 pairs 38-50 | 12 | 11.5 | 11.5 | -0.0 | 10.7 / 12.5 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 1.3 | +1.2 | 1.2 / 1.4 |
| 55-59.5 | WS teaching 52-57 | 5 | 4.5 | 3.7 | +0.8 | 3.0 / 4.4 |
| 59.5-71 | WS page 2 alone 57-69 | 12 | 11.5 | 11.5 | +0.0 | 10.6 / 12.7 |
| 71-73.5 | WS check page 2 69-72 | 3 | 2.5 | 2.1 | +0.4 | 2.0 / 2.2 |
| 73.5-76.5 | Standing buffer | - | 3.0 | 0.0 | +3.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.7 | +0.3 | 4.1 / 5.3 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 4.6 | +0.4 | 4.4 / 4.9 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.3 | +0.2 | 1.2 / 1.4 |
| 0-90 | **Total** | 90 | 90.0 | 82.5 | +7.5 | 72.4 / 93.4 |

### Lesson 6: Market Day

**Total 103.3 (fast 93, slow 115).** Warm-up **OVER +4.0**: six items with price tags from 85c to $57.20, each paid exactly with play notes and coins, "who can pay with the fewest pieces": 5 min for a 2-minute game. Explore +5.0 (play-money kit, toy-stall list to $10: 6.5 min of pair work). Mini-lesson +2.5. Page 1 is Q1 (four prices, $1.65 to $76, notes and coins each) and Q2 (every way to pay $8, a table of up to 8 rows): 11.5 min in pairs against 10 usable (+2.3 after the 2-min teach slide). **Page 2 demand 15.0 for 12 (+3.0):** Q3b, Q4b and Q6 are each "find all" lists. Worksheet items: LOW 2, MIDDLE 4, HIGH 6 of 6.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.5 | 0.0 | 0.0 | 0.7 | 0.17 | **1.3** | +0.3 | OK |
| Sneak-peek 1-4 | 3 | 1.2 | 0.0 | 3.3 | 0.7 | 0.17 | **5.4** | +2.4 | OVER |
| Warm-up 4-8 | 4 | 0.5 | 1.5 | 5.0 | 0.8 | 0.17 | **8.0** | +4.0 | OVER |
| Explore 8-20 | 12 | 1.3 | 3.4 | 6.5 | 5.8 | 0.17 | **17.0** | +5.0 | OVER |
| Mini-lesson 20-32 | 12 | 3.5 | 3.4 | 5.0 | 2.5 | 0.17 | **14.5** | +2.5 | OVER |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.0** | +0.0 | OK |
| WS teach slide 36-38 | 2 | 0.6 | 0.5 | 0.7 | 0.4 | 0.17 | **2.4** | +0.4 | OK |
| WS page 1 pairs 38-50 | 12 | 0.4 | 0.0 | 11.5 | 2.4 | 0.00 | **14.3** | +2.3 | OVER |
| WS check page 1 50-52 | 2 | 2.1 | 0.0 | 0.0 | 0.4 | 0.00 | **2.5** | +0.5 | TIGHT |
| WS teaching 52-57 | 5 | 1.8 | 1.5 | 0.5 | 1.2 | 0.00 | **5.0** | +0.0 | OK |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 15.0 | 0.0 | 0.00 | **15.0** | +3.0 | OVER |
| WS check page 2 69-72 | 3 | 2.5 | 0.0 | 0.0 | 0.4 | 0.00 | **2.9** | -0.1 | OK |
| Talk time 72-80 | 8 | 0.6 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-87 | 7 | 0.3 | 0.0 | 4.5 | 0.9 | 0.17 | **5.9** | -1.1 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.2 | 0.0 | 0.3 | 0.7 | 0.17 | **1.3** | +0.3 | OK |
| **Total** | **90** | 16.0 | 10.8 | 61.8 | 18.2 | 1.8 | **108.6** (time-boxed 103.3) | +18.6 | |

**Fixes for L6** (on top of the level-wide changes in section 6a):

- **Warm-up 8.0 -> 4.4:** pay exactly for **two** price tags only (the 85c one and the $57.20 one); `warm2` questions 1 and 3.
- **Explore 17.0 -> 13.1:** send the play-money cut-outs with the workbook (kit in hand at minute 0); pairs 5.5 min: find the three baskets that cost exactly $10 (6+4, 6+3+1, 4+3+2+1) and say how they know there are no more.
- **Mini-lesson 14.5 -> 12.0:** `try1` item a only, `try2` items a and b.
- **Page 1:** move the last row of **Q1 (bicycle, $76)** and **Q2(b)** to take-home. **Page 2 (15.0 -> 11.0):** move **Q3(b)** (change from $50, fewest notes) and **Q4(b)** (pairs with exactly $3 change) to take-home; Q3(a), Q4(a), Q5, Q6 stay. The 52-57 slides stay, without discussion of the cut parts.

**Core items done in class after the fixes (in-class Core = 6 of 6):** LOW 1+3=4 / MIDDLE 2+4=6 / HIGH 2+4=6. Expected need after fixes: **85 (fast 74, slow 96)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.1 | +0.4 | 0.9 / 1.2 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.2 | +0.3 | 3.8 / 4.6 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.4 | +0.1 | 3.6 / 5.1 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 13.1 | -0.1 | 10.6 / 15.8 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 12.0 | -0.0 | 10.1 / 14.1 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.8 | +0.2 | 2.5 / 3.1 |
| 38.5-41 | WS teach slide 36-38 | 2 | 2.5 | 2.4 | +0.1 | 2.0 / 2.8 |
| 41-52.5 | WS page 1 pairs 38-50 | 12 | 11.5 | 11.7 | -0.2 | 10.9 / 12.7 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 1.9 | +0.6 | 1.8 / 2.0 |
| 55-59.5 | WS teaching 52-57 | 5 | 4.5 | 4.5 | -0.0 | 3.6 / 5.5 |
| 59.5-71 | WS page 2 alone 57-69 | 12 | 11.5 | 11.0 | +0.5 | 10.1 / 12.1 |
| 71-73.5 | WS check page 2 69-72 | 3 | 2.5 | 2.2 | +0.3 | 2.1 / 2.2 |
| 73.5-76.5 | Standing buffer | - | 3.0 | 0.0 | +3.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.1 / 5.3 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 5.1 | -0.1 | 4.7 / 5.4 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.3 | +0.2 | 1.2 / 1.4 |
| 0-90 | **Total** | 90 | 90.0 | 84.6 | +5.4 | 74.0 / 96.0 |

### Lesson 7: Fair Shares

**Total 104.7 (fast 94, slow 116).** **Explore +7.1 (19.1)**: fold four strips into whole, halves, quarters, eighths, write a fraction on each of 15 parts, line them up, then try to fold a strip into three equal parts: 8 min for a 6-minute pair slot, plus 1 to 2 min cutting strips and three rooms/slides. Mini-lesson TIGHT (+2.0: seven slides, two 3-item "Your turn", fraction notation on slide). **52-57 block 8.2 for 5 (+3.2):** five slides (`teachadd`, `tryadd` four items, `teachstory`, `teachsame`). Page 2 content 13.5 for 12 (Q4 five add/take-away items with bars, 6 min). Worksheet items: LOW 3, MIDDLE 5, HIGH 6 of 6.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.5 | 0.0 | 0.0 | 0.7 | 0.17 | **1.3** | +0.3 | OK |
| Sneak-peek 1-4 | 3 | 1.2 | 0.0 | 3.3 | 0.7 | 0.17 | **5.4** | +2.4 | OVER |
| Warm-up 4-8 | 4 | 0.5 | 1.5 | 2.0 | 0.8 | 0.17 | **5.0** | +1.0 | TIGHT |
| Explore 8-20 | 12 | 1.3 | 3.4 | 8.0 | 6.2 | 0.17 | **19.1** | +7.1 | OVER |
| Mini-lesson 20-32 | 12 | 3.2 | 3.9 | 3.8 | 2.9 | 0.17 | **14.0** | +2.0 | TIGHT |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.0** | -0.0 | OK |
| WS page 1 pairs 36-50 | 14 | 0.4 | 0.0 | 12.1 | 2.4 | 0.17 | **15.0** | +1.0 | TIGHT |
| WS check page 1 50-52 | 2 | 3.0 | 0.0 | 0.0 | 0.4 | 0.00 | **3.4** | +1.4 | TIGHT |
| WS teaching 52-57 | 5 | 2.2 | 2.3 | 2.0 | 1.7 | 0.00 | **8.2** | +3.2 | OVER |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 13.5 | 0.0 | 0.00 | **13.5** | +1.5 | TIGHT |
| WS check page 2 69-72 | 3 | 2.6 | 0.0 | 0.0 | 0.4 | 0.00 | **3.0** | +0.0 | OK |
| Talk time 72-80 | 8 | 0.5 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-87 | 7 | 0.3 | 0.0 | 3.8 | 0.9 | 0.17 | **5.1** | -1.9 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.1 | 0.0 | 0.3 | 0.7 | 0.17 | **1.3** | +0.3 | OK |
| **Total** | **90** | 16.4 | 11.6 | 58.2 | 19.1 | 1.8 | **107.2** (time-boxed 104.7) | +17.2 | |

**Fixes for L7** (on top of the level-wide changes in section 6a):

- **Explore 19.1 -> 12.5:** fold **three** strips (halves, quarters, eighths), write the fraction on **one** part of each (not all 15); **move "fold a strip into 3 equal parts" to the `goexp` card and take-home**; strips cut before the lesson (kit, 60 s); debrief questions 1 and 2 only (the thirds question goes with the card).
- **Mini-lesson 14.0 -> 11.8:** merge `we3` (same bottom number) into `we2`; `try1` and `try2` items a and b.
- **52-57 block 8.2 -> 4.5:** **delete `tryadd`** (four items = worksheet Q4); keep `teachadd`, `teachstory`, `teachsame`.
- **Page 1:** move **Q1(a)** explanation ("how do you know it is not cut into quarters") to take-home. **Page 2 (13.5 -> 11.1):** move **Q4(d) and Q4(e)** to take-home.

**Core items done in class after the fixes (in-class Core = 6 of 6):** LOW 2+2=4 / MIDDLE 3+3=6 / HIGH 3+3=6. Expected need after fixes: **84 (fast 73, slow 94)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.1 | +0.4 | 0.9 / 1.2 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.2 | +0.3 | 3.8 / 4.6 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.1 | +0.4 | 3.4 / 4.8 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 12.5 | +0.5 | 10.2 / 15.0 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 11.8 | +0.2 | 9.9 / 13.9 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.7 | +0.3 | 2.4 / 3.0 |
| 38.5-52.5 | WS page 1 pairs 36-50 | 14 | 14.0 | 14.2 | -0.2 | 13.2 / 15.5 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 2.7 | -0.2 | 2.6 / 2.8 |
| 55-59.5 | WS teaching 52-57 | 5 | 4.5 | 4.5 | +0.0 | 3.5 / 5.5 |
| 59.5-71 | WS page 2 alone 57-69 | 12 | 11.5 | 11.1 | +0.4 | 10.2 / 12.2 |
| 71-73.5 | WS check page 2 69-72 | 3 | 2.5 | 2.2 | +0.3 | 2.1 / 2.2 |
| 73.5-76.5 | Standing buffer | - | 3.0 | 0.0 | +3.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.0 / 5.2 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 4.3 | +0.7 | 4.1 / 4.6 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.3 | +0.2 | 1.2 / 1.4 |
| 0-90 | **Total** | 90 | 90.0 | 83.5 | +6.5 | 73.4 / 94.4 |

### Lesson 8: Shape Builders

**Total 106.9 (fast 96, slow 119); content-complete 113.2.** The Core is only four questions but each is heavy. Explore +6.0 (cutting two paper circles, folding, building shapes; 7 min of work, 2 min of materials). Mini-lesson +2.4 (seven slides, counting squares and triangles). Page 1 demand 14.4 (pairs) for 14 (+3.3): Q1 robot pieces 5 min, Q2 count every square by size in a 4x4 grid and triangles 7.5 min. **52-57 block 11.8 for 5 (+6.8):** `teachcube`, `trycube` (three stacks), `teachnet` (102 words), `trynet` (three nets folded in your head) all in five minutes. **Page 2 demand 15.0 for 12 (+3.0):** Q3 count cubes 6 min; Q4 cut out four nets, fold, circle, then draw a missing square on a grid 9 min. Worksheet items: LOW 2, **MIDDLE 2**, HIGH 4 of 4.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.6 | 0.0 | 0.0 | 0.7 | 0.17 | **1.5** | +0.5 | OK |
| Sneak-peek 1-4 | 3 | 1.4 | 0.0 | 3.3 | 0.7 | 0.17 | **5.6** | +2.6 | OVER |
| Warm-up 4-8 | 4 | 0.5 | 1.5 | 2.5 | 0.8 | 0.17 | **5.5** | +1.5 | TIGHT |
| Explore 8-20 | 12 | 1.2 | 3.4 | 7.0 | 6.2 | 0.17 | **18.0** | +6.0 | OVER |
| Mini-lesson 20-32 | 12 | 3.2 | 3.9 | 4.2 | 2.9 | 0.17 | **14.4** | +2.4 | OVER |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.0** | +0.0 | OK |
| WS page 1 pairs 36-50 | 14 | 0.4 | 0.0 | 14.4 | 2.4 | 0.17 | **17.3** | +3.3 | OVER |
| WS check page 1 50-52 | 2 | 1.8 | 0.0 | 0.0 | 0.4 | 0.00 | **2.2** | +0.2 | OK |
| WS teaching 52-57 | 5 | 2.0 | 2.7 | 5.5 | 1.7 | 0.00 | **11.8** | +6.8 | OVER |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 15.0 | 0.0 | 0.00 | **15.0** | +3.0 | OVER |
| WS check page 2 69-72 | 3 | 1.7 | 0.0 | 0.0 | 0.4 | 0.00 | **2.1** | -0.9 | OK |
| Talk time 72-80 | 8 | 0.6 | 0.5 | 5.0 | 0.4 | 0.17 | **6.7** | -1.3 | OK |
| Exit ticket 80-87 | 7 | 0.4 | 0.0 | 4.0 | 0.9 | 0.17 | **5.5** | -1.5 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.2 | 0.0 | 0.3 | 0.7 | 0.17 | **1.3** | +0.3 | OK |
| **Total** | **90** | 14.5 | 11.9 | 65.8 | 19.1 | 1.8 | **113.2** (time-boxed 106.9) | +23.2 | |

**Fixes for L8** (on top of the level-wide changes in section 6a):

- **Explore 18.0 -> 12.8:** ask parents to cut the two paper circles before the lesson (kit message and opening slide), pairs 5.5 min; debrief unchanged.
- **Mini-lesson 14.4 -> 11.8:** **delete `we3`** (triangles) and post it with the take-home; `try1` and `try2` items a and b.
- **52-57 block 11.8 -> 3.1:** **delete `trycube` and `trynet`** (worksheet Q3 and Q4 are those tasks); keep `teachcube` and `teachnet`.
- **Page 1 (14.4 -> 10.1 pairs):** move **Q1(c)** and **Q2(b)** (triangles) to take-home. **Page 2 (15.0 -> 10.0):** ask parents to cut nets A to D out beforehand and move **Q4(b)** (add one square to make a cube net) to take-home.
- L8 remains the heaviest Core: even after this the MIDDLE child finishes 4 items, not 4 + extension.

**Core items done in class after the fixes (in-class Core = 4 of 4):** LOW 1+1=2 / MIDDLE 2+2=4 / HIGH 2+2=4. Expected need after fixes: **80 (fast 70, slow 90)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.2 | +0.3 | 1.0 / 1.4 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.4 | +0.1 | 4.0 / 4.8 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.1 | +0.4 | 3.3 / 4.8 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 12.8 | +0.2 | 10.4 / 15.4 |
| 23.5-35.5 | Mini-lesson 20-32 | 12 | 12.0 | 11.9 | +0.1 | 10.0 / 13.9 |
| 35.5-38.5 | Brain break 32-36 | 4 | 3.0 | 2.8 | +0.2 | 2.5 / 3.1 |
| 38.5-52.5 | WS page 1 pairs 36-50 | 14 | 14.0 | 13.1 | +0.9 | 12.1 / 14.2 |
| 52.5-55 | WS check page 1 50-52 | 2 | 2.5 | 1.8 | +0.8 | 1.7 / 1.8 |
| 55-59.5 | WS teaching 52-57 | 5 | 4.5 | 3.1 | +1.4 | 2.5 / 3.8 |
| 59.5-71 | WS page 2 alone 57-69 | 12 | 11.5 | 10.0 | +1.5 | 9.2 / 11.0 |
| 71-73.5 | WS check page 2 69-72 | 3 | 2.5 | 1.7 | +0.8 | 1.6 / 1.8 |
| 73.5-76.5 | Standing buffer | - | 3.0 | 0.0 | +3.0 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.7 | +0.3 | 4.1 / 5.3 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 4.7 | +0.3 | 4.4 / 4.9 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.3 | +0.2 | 1.2 / 1.4 |
| 0-90 | **Total** | 90 | 90.0 | 79.6 | +10.4 | 69.8 / 90.1 |

### Lesson 9: Measure Masters

**Total 110.1 (fast 99, slow 122): the longest.** Explore **+7.6 (19.6)**: hang two cups from a coat hanger, check it is level, guess and test how many 20c coins balance a glue stick, then a spoon (8 min of work and 2.5 min of finding things). Mini-lesson **+4.0 (16.0)**: `we2` is a 131-word jug table, then `try2` (a 2 l and a 5 l jug, three items at 70 s). Warm-up OVER +2.1 (six "which unit?" prompts at 30 s). **52-57 block 10.5 for 5 (+5.5):** four slides (`teachlen`, `teachclock`, `teachdur`, `trytime` with three time items). Pages TIGHT (12.6 pairs; 13.0 alone). Worksheet items: LOW 2, MIDDLE 3, HIGH 5 of 5. Q2 (jug puzzles a and b) and Q3 are 3 min each for a 7 to 9 year old.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.5 | 0.0 | 0.0 | 0.7 | 0.17 | **1.4** | +0.4 | OK |
| Sneak-peek 1-4 | 3 | 1.5 | 0.0 | 3.3 | 0.7 | 0.17 | **5.7** | +2.7 | OVER |
| Warm-up 4-8 | 4 | 0.6 | 1.5 | 3.0 | 0.8 | 0.17 | **6.1** | +2.1 | OVER |
| Explore 8-20 | 12 | 1.3 | 3.4 | 8.0 | 6.8 | 0.17 | **19.6** | +7.6 | OVER |
| Mini-lesson 20-32 | 12 | 3.9 | 3.4 | 6.0 | 2.5 | 0.17 | **16.0** | +4.0 | OVER |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.0** | +0.0 | OK |
| WS page 1 pairs 36-50 | 14 | 0.4 | 0.0 | 12.6 | 2.4 | 0.17 | **15.6** | +1.6 | TIGHT |
| WS check page 1 50-52 | 2 | 2.0 | 0.0 | 0.0 | 0.4 | 0.00 | **2.4** | +0.4 | OK |
| WS teaching 52-57 | 5 | 2.4 | 2.3 | 4.2 | 1.7 | 0.00 | **10.5** | +5.5 | OVER |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 13.0 | 0.0 | 0.00 | **13.0** | +1.0 | TIGHT |
| WS check page 2 69-72 | 3 | 2.2 | 0.0 | 0.0 | 0.4 | 0.00 | **2.6** | -0.4 | OK |
| Talk time 72-80 | 8 | 0.5 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-87 | 7 | 0.3 | 0.0 | 4.0 | 0.9 | 0.17 | **5.4** | -1.6 | OK |
| Looking back 87-89 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Closing + stamps 89-90 | 1 | 0.3 | 0.0 | 0.3 | 0.7 | 0.17 | **1.5** | +0.5 | OK |
| **Total** | **90** | 16.6 | 11.1 | 64.0 | 19.2 | 1.8 | **112.7** (time-boxed 110.1) | +22.7 | |

**Fixes for L9** (on top of the level-wide changes in section 6a):

- **Warm-up 6.1 -> 4.3:** three of the six "which unit?" prompts (door, bag of rice, brushing teeth); `warm2` questions 1 and 3.
- **Explore 19.6 -> 13.2:** hang the balance and test it level **before** the lesson (kit message plus 30 s at minute 0), glue stick only in class (spoon moves to take-home), pairs 5.5 min.
- **Mini-lesson 16.0 -> 9.9:** `try1` items a and b; **delete `try2`** (the 2 l and 5 l jug puzzle is worksheet Q2 and Q3). Keep `we2` (the 131-word jug table) but say it from the SAY lines, not the slide text.
- **52-57 block 10.5 -> 3.4:** **delete `teachlen` and `trytime`** (ribbon overlap and time-problem items repeat Q4 and Q5; `teachlen` goes with the take-home); keep `teachclock`, `teachdur`.
- **Page 1 (12.6 -> 9.2):** move **Q2(b)** (exactly 1 l) to take-home. **Page 2 (13.0 -> 9.3):** move **Q4(b)** (ribbon with a 5 cm overlap) and **Q5(c)** (journey time) to take-home.

**Core items done in class after the fixes (in-class Core = 5 of 5):** LOW 1+2=3 / MIDDLE 2+3=5 / HIGH 2+3=5. Expected need after fixes: **77 (fast 68, slow 87)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.1 | +0.4 | 0.9 / 1.3 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.5 | +0.0 | 4.1 / 4.9 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.3 | +0.2 | 3.5 / 5.0 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 13.2 | -0.2 | 10.6 / 15.8 |
| 23.5-34 | Mini-lesson 20-32 | 12 | 10.5 | 9.9 | +0.6 | 8.3 / 11.6 |
| 34-37 | Brain break 32-36 | 4 | 3.0 | 2.8 | +0.2 | 2.5 / 3.1 |
| 37-51 | WS page 1 pairs 36-50 | 14 | 14.0 | 12.1 | +1.9 | 11.3 / 13.2 |
| 51-53.5 | WS check page 1 50-52 | 2 | 2.5 | 1.8 | +0.7 | 1.8 / 1.9 |
| 53.5-58 | WS teaching 52-57 | 5 | 4.5 | 3.4 | +1.1 | 2.8 / 4.1 |
| 58-69.5 | WS page 2 alone 57-69 | 12 | 11.5 | 9.3 | +2.2 | 8.6 / 10.2 |
| 69.5-72 | WS check page 2 69-72 | 3 | 2.5 | 1.9 | +0.6 | 1.8 / 2.0 |
| 72-76.5 | Standing buffer | - | 4.5 | 0.0 | +4.5 | 0.0 / 0.0 |
| 76.5-81.5 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.0 / 5.3 |
| 81.5-86.5 | Exit ticket 80-87 | 7 | 5.0 | 4.6 | +0.4 | 4.3 / 4.9 |
| 86.5-88.5 | Looking back 87-89 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 88.5-90 | Closing + stamps 89-90 | 1 | 1.5 | 1.5 | +0.0 | 1.3 / 1.6 |
| 0-90 | **Total** | 90 | 90.0 | 77.3 | +12.7 | 67.8 / 87.5 |

### Lesson 10: Challenge Day

**Total 106.7 (fast 95, slow 119).** 34 slides (30 shown), the most. Warm-up **OVER +4.1**: relay review of six cards, each read, thought about, answered, then the volunteer chooses a friend (45 to 50 s a card). Explore +6.1 (four station cards each shown as a slide, two rooms, 6 min of pair work on two cards). Mini-lesson **+4.2 (16.2)**: three worked strategies (draw, list, table) in seven slides and two 3-item "Your turn" slides; `teach1` ("how to start a puzzle") and `key` say the same thing. A 2-minute teach slide (`teachgraph`) precedes page 1 and page 1 demand is 13.8 in pairs for 10 usable (**+4.6**: picture graph, digit cards, a coins table). Exit ticket TIGHT (+1.4: 5 min scripted, needs 6.4: "5 bicycles and tricycles have 13 wheels, how did you start?" is 2.5 min of thinking). Certificates (8 children in 3 min) are OK. `reflect` slide is tagged 87-89 but the script says 85-87. Worksheet items: LOW 2, MIDDLE 5, HIGH 6 of 6.

| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Opening 0-1 | 1 | 0.4 | 0.0 | 0.0 | 0.7 | 0.17 | **1.3** | +0.3 | OK |
| Sneak-peek 1-4 | 3 | 1.4 | 0.0 | 3.3 | 0.7 | 0.17 | **5.6** | +2.6 | OVER |
| Warm-up 4-8 | 4 | 0.6 | 1.5 | 5.0 | 0.8 | 0.17 | **8.1** | +4.1 | OVER |
| Explore 8-20 | 12 | 1.2 | 3.4 | 7.0 | 6.4 | 0.17 | **18.1** | +6.1 | OVER |
| Mini-lesson 20-32 | 12 | 4.0 | 3.9 | 5.2 | 2.9 | 0.17 | **16.2** | +4.2 | OVER |
| Brain break 32-36 | 4 | 0.2 | 0.0 | 3.2 | 0.4 | 0.17 | **4.1** | +0.1 | OK |
| WS teach slide 36-38 | 2 | 0.6 | 0.5 | 0.7 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| WS page 1 pairs 38-50 | 12 | 0.4 | 0.0 | 13.8 | 2.4 | 0.00 | **16.6** | +4.6 | OVER |
| WS check page 1 50-52 | 2 | 2.4 | 0.0 | 0.0 | 0.4 | 0.00 | **2.8** | +0.8 | TIGHT |
| WS teaching 52-57 | 5 | 1.2 | 1.0 | 1.0 | 0.8 | 0.00 | **4.0** | -1.0 | OK |
| WS page 2 alone 57-69 | 12 | 0.0 | 0.0 | 11.5 | 0.0 | 0.00 | **11.5** | -0.5 | OK |
| WS check page 2 69-72 | 3 | 2.2 | 0.0 | 0.0 | 0.4 | 0.00 | **2.6** | -0.4 | OK |
| Talk time 72-80 | 8 | 0.5 | 0.5 | 5.0 | 0.4 | 0.17 | **6.6** | -1.4 | OK |
| Exit ticket 80-85 | 5 | 0.3 | 0.0 | 5.0 | 0.9 | 0.17 | **6.4** | +1.4 | TIGHT |
| Looking back 85-87 | 2 | 0.4 | 0.0 | 1.2 | 0.4 | 0.17 | **2.3** | +0.3 | OK |
| Certificates + close 87-90 | 3 | 0.3 | 0.0 | 1.6 | 0.8 | 0.17 | **2.8** | -0.2 | OK |
| **Total** | **90** | 16.1 | 10.8 | 63.6 | 18.9 | 1.8 | **111.3** (time-boxed 106.7) | +21.3 | |

**Fixes for L10** (on top of the level-wide changes in section 6a):

- **Warm-up 8.1 -> 4.5:** relay review with **three** cards (digits, change, fractions) instead of six; `warm2` questions 1 and 3.
- **Explore 18.1 -> 13.2:** put the four station cards on **one** slide (-4 slide changes), pairs 4.5 min (two cards each); the debrief keeps all three questions.
- **Mini-lesson 16.2 -> 9.8:** **delete `teach1`** (the `key` slide says the same), **delete `try1`**, `try2` items a and b (`we1`, `we2`, `we3` stay).
- **Page 1 (13.8 -> 9.2 min in pairs; 10 usable after the 2-min `teachgraph`):** move **Q3 (coins table)** to take-home (same skill as L6 Q2).
- Exit ticket: 2 min of child work; certificates stay at 3 min. Correct `reflect` tag to 85-87.

**Core items done in class after the fixes (in-class Core = 5 of 6):** LOW 1+1=2 / MIDDLE 2+3=5 / HIGH 2+3=5. Expected need after fixes: **83 (fast 73, slow 94)** against 90.

| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |
|---|---|--:|--:|--:|--:|--:|
| 0-1.5 | Opening 0-1 | 1 | 1.5 | 1.0 | +0.5 | 0.8 / 1.1 |
| 1.5-6 | Sneak-peek 1-4 | 3 | 4.5 | 4.4 | +0.1 | 4.0 / 4.8 |
| 6-10.5 | Warm-up 4-8 | 4 | 4.5 | 4.5 | +0.0 | 3.7 / 5.3 |
| 10.5-23.5 | Explore 8-20 | 12 | 13.0 | 13.2 | -0.2 | 10.7 / 15.7 |
| 23.5-33.5 | Mini-lesson 20-32 | 12 | 10.0 | 9.5 | +0.5 | 8.0 / 11.2 |
| 33.5-36.5 | Brain break 32-36 | 4 | 3.0 | 2.8 | +0.2 | 2.5 / 3.1 |
| 36.5-39 | WS teach slide 36-38 | 2 | 2.5 | 2.3 | +0.2 | 1.9 / 2.7 |
| 39-51 | WS page 1 pairs 38-50 | 12 | 12.0 | 12.0 | +0.0 | 11.1 / 13.0 |
| 51-53.5 | WS check page 1 50-52 | 2 | 2.5 | 1.8 | +0.7 | 1.8 / 1.9 |
| 53.5-57 | WS teaching 52-57 | 5 | 3.5 | 3.0 | +0.5 | 2.4 / 3.7 |
| 57-68.5 | WS page 2 alone 57-69 | 12 | 11.5 | 11.5 | +0.0 | 10.6 / 12.7 |
| 68.5-71 | WS check page 2 69-72 | 3 | 2.5 | 2.1 | +0.4 | 2.0 / 2.2 |
| 71-75 | Standing buffer | - | 4.0 | 0.0 | +4.0 | 0.0 / 0.0 |
| 75-80 | Talk time 72-80 | 8 | 5.0 | 4.6 | +0.4 | 4.0 / 5.2 |
| 80-85 | Exit ticket 80-85 | 5 | 5.0 | 5.1 | -0.1 | 4.8 / 5.4 |
| 85-87 | Looking back 85-87 | 2 | 2.0 | 2.3 | -0.3 | 2.0 / 2.5 |
| 87-90 | Certificates + close 87-90 | 3 | 3.0 | 2.8 | +0.2 | 2.6 / 3.1 |
| 0-90 | **Total** | 90 | 90.0 | 82.9 | +7.1 | 72.9 / 93.8 |

## 6. Fixes

### 6a. Level-wide changes (all ten lessons; they carry most of the saving)

| # | Change | Where | Minutes |
|---|---|---|--:|
| W1 | **Sneak-peek**: shorten the SAY to about 28 words ("Two sneak-peek puzzles on ideas we have not learnt yet. Guessing is welcome, so is I do not know. Nobody is marked. Show your paper to me only."); child work 45 s for Q1 and 90 s for Q2 (was 60 s + 120 s). Both puzzles stay; answers are still revealed as "one way to think about it". | `p2/gaps.json` `common.preSay`; guide segment 1-4 | budget **3 -> 4.5** (need 4.2) |
| W2 | **Warm-up**: ask quick questions 1 and 3 only (2, 4, 5 spare; the guide already calls 2 and 4 spare); games trimmed to what fits two minutes (per lesson below). | `warm2` note, guide warm-up segment | budget **4 -> 4.5** |
| W3 | **Explore logistics**: kit out at minute 0 (opening message "have everything on the desk"; 30 s check); **one** breakout round with an auto-timer, 60 s each way; fold the `goexp` slide into `explore1` as a corner box; "how do you know" only on debrief question 2 (15 s discussion on the others). | explore segment, `goexp` slides | budget **12 -> 13** |
| W4 | **Mini-lesson "Your turn" slides** carry two items, not three, and a slide that repeats a worksheet question is deleted (per lesson below). | `try*` slides | mini 12 (10 in L10) |
| W5 | **Brain break** 3 minutes: 2 min movement, 1 min water ("Keep it to three minutes"). | guide break segment | **4 -> 3** |
| W6 | **Check-together slides**: tutor reads only the answer line and the child self-marks; one "how do you know" per page; budgets 2.5 and 2.5. | `ws1ans`, `ws2ans` | 2 + 3 -> 2.5 + 2.5 |
| W7 | **Talk time**: 90 s pairs, two volunteers, no second question. | `talk` note | **8 -> 5** |
| W8 | **Exit ticket**: slips held up one child at a time, answer on the next click. Looking back unchanged (2 min). Closing 1.5 min (stamps and goodbye). | exit segment | **7 -> 5**; close 1 -> 1.5 |
| W9 | **Standing buffer** 3 minutes, named "Flex", placed after the second check (see section 8). | new segment | +3 |

Standard timeline after the changes (L1-L3, L7-L9): Opening 0-1.5, Sneak-peek 1.5-6, Warm-up 6-10.5, Explore 10.5-23.5, Mini-lesson 23.5-35.5, Brain break 35.5-38.5, Worksheet page 1 (with start) 38.5-52.5, Check 52.5-55, Teaching 55-59.5, Page 2 59.5-71, Check 71-73.5, **Flex 73.5-76.5**, Talk 76.5-81.5, Exit 81.5-86.5, Looking back 86.5-88.5, Closing 88.5-90. L4 (teaching 2.5) and L10 (certificates, mini 10, teaching 3.5) differ; L5, L6, L10 begin the worksheet with a 2-minute teach slide and a 12-minute page 1. Every minute label on the slides and in `guide.js` (`seg()` calls, the `R` routine table, "Minutes 36 to 50" in slide notes) must be regenerated if these budgets are adopted.

### 6b. What the fixes do not touch
Answers, answer keys, the tier principle (Core approachable; Think harder needs the taught idea; Go further and the Investigation need the completed topic) and the no-pressure rules are unchanged. Every Core item moved out of class is marked as a take-home star on the same page, stays Core (not Think harder), and keeps its check-together answer on the answer slide so a child can self-mark at home. No item was moved that carries the lesson's key idea (list in order, missing digit, hens and goats table, etc.); items moved are the second or third part of a question that repeats the skill, or the explanation sub-part (which is still asked in talk time and the exit ticket). Think harder, Go further and the Investigation remain open choices; the take-home stars give a HIGH child something to do with spare minutes.

## 7. Re-budgeted totals

| Lesson | Old total | New budgets (sum) | Expected need: fast / **central** / slow | Buffer | Core items in class (of total) |
|---|--:|--:|--:|--:|--:|
| 1 Digit Detectives | 99 (as scripted, time-boxed central) | 90 | 71 / **81** / 91 | 3.0 | 5 of 6 |
| 2 Missing Digit Mysteries | 102 (as scripted, time-boxed central) | 90 | 70 / **79** / 89 | 3.0 | 5 of 6 |
| 3 Legs, Wheels and Arrays | 104 (as scripted, time-boxed central) | 90 | 72 / **82** / 93 | 3.0 | 6 of 6 |
| 4 Pattern Machines | 97 (as scripted, time-boxed central) | 90 | 69 / **79** / 89 | 5.0 | 6 of 6 |
| 5 Mystery Number Machines | 99 (as scripted, time-boxed central) | 90 | 72 / **83** / 93 | 3.0 | 5 of 5 |
| 6 Market Day | 103 (as scripted, time-boxed central) | 90 | 74 / **85** / 96 | 3.0 | 6 of 6 |
| 7 Fair Shares | 105 (as scripted, time-boxed central) | 90 | 73 / **84** / 94 | 3.0 | 6 of 6 |
| 8 Shape Builders | 107 (as scripted, time-boxed central) | 90 | 70 / **80** / 90 | 3.0 | 4 of 4 |
| 9 Measure Masters | 110 (as scripted, time-boxed central) | 90 | 68 / **77** / 87 | 4.5 | 5 of 5 |
| 10 Challenge Day | 107 (as scripted, time-boxed central) | 90 | 73 / **83** / 94 | 4.0 | 5 of 6 |

Reading the table: the central case leaves 5 to 13 minutes unspent (the budgets are rounded up and the buffer is on top); that is deliberate headroom, because the model may be generous in places (see caveats). The slow-tutor case (every parameter 10 to 30% worse at once) still needs 88 to 96 minutes, i.e. it overruns 90 in 7 of the 10 lessons by up to 6 minutes; the 3-minute buffer plus the elastic page 2 (section 8) covers about half of that, and a new tutor should expect to drop one take-home star in a slow week. The first live run of each lesson should be timed and the budgets trimmed or restored accordingly.

## 8. Does the plan need a standing buffer? Yes.

- **Size: 3 minutes named in every lesson (5 in L4, 4.5 in L9, 4 in L10 on the current numbers), placed after check-together page 2 (about minute 73.5-76.5).** It is the one place a tutor can absorb a late start, a camera problem or a slow page 2 without cutting talk time or the fixed items (looking back, certificates, stamps). If unused, spend it on the Investigation share or a second talk-time volunteer; do not add content to it.
- **Plus the elastic block:** page 2 (11.5 min) and the 52-57 teaching are the only places where time can be recovered safely, because moved items are already marked take-home. Rule for tutors: at minute 59.5 (start of page 2), if the clock is more than 2 min late, drop the last Core question of page 2 to take-home; do not shorten talk time, exit ticket, looking back or closing.
- **Checkpoints (standard timeline):** 10.5 explore starts; 23.5 mini-lesson starts; 38.5 worksheet starts; 52.5 page 1 finished; 59.5 page 2 starts; 73.5 flex; 76.5 talk time; 86.5 looking back.
- **Why not more:** the scripted lessons are 10 to 20 minutes over, not 3. The sums in section 7 already hold 5 to 13 minutes of slack in the central case; a 3-minute named buffer on top covers the slow-tutor case without taking minutes from the children's thinking time.
- **Re-time after the first live run:** this is a desk model. Run L1, L4 and L9 (the shortest, the loosest mini-lesson, the longest) with a stopwatch and re-set the per-part budgets in section 6a from the measured numbers before the full program is locked.

## 9. Caveats

- Per-question minutes are my judgement from the printed pages and the key; there are no pilot timings. Page-2 and page-1 results move by about 20% with the LOW/HIGH multipliers (x1.7 / x0.65).
- Breakout rooms are assumed for explore only. If the tutor works with pairs in rooms for worksheet page 1 as well, add about 3 min.
- Recording rules (read every question aloud, repeat each answer, timers) and the real length of the REC lines (about 14 s, not 10) add 2 to 4 minutes that are not in the totals above.
- Fast / slow cases move all parameters together; real variance is likely to be narrower for an experienced tutor and wider on the first week.
- Content changed during the audit (other jobs editing `p2/content`, rebuilding PDFs). Figures use the state of the repository at about 02:06 UTC.

## 10. Files

- `docs/audit/timing_p2.md` (this report).
- `docs/audit/timing_p2.py`: the model; reads `p2/data.js` through `node` and the slide HTML, writes nothing. `python3 -I docs/audit/timing_p2.py --summary | --tables | --fixed | --json`.
