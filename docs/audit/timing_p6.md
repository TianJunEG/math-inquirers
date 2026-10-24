# Lesson timing audit: Math Inquirers Level N=6 (P6), ten lessons of 90 minutes

Analysis only. Nothing in content, guides, decks, builds or outputs was edited, committed or published. Written by `docs/audit/timing_p6.py` (the model) plus hand-written findings. Snapshot: working tree on 2026-10-22 (HEAD was `00847c1` when I started; other people's WIP commits landed while this audit ran), so re-run `python3 docs/audit/timing_p6.py` before acting on any number. These are estimates from word counts and judged task times, not stopwatch timings, so every total comes with a range.

## 1. Answer

**No lesson fits its 90 minutes as written.** Run live from the slides and script, Lessons 1 to 9 need about **96 to 110 minutes** (central estimate; plausible range 86 to 122) and Lesson 10 needs about **126 minutes** (112 to 139). Lesson 3 (95.7) and Lesson 6 (96.9) come closest; a fast tutor with a quick group could finish them in about 86 minutes. No part of any lesson is LOOSE: the only slack anywhere is Talk time (about 1.2 minutes in each of Lessons 1-9), and it is nowhere near enough.

| Lesson | Scripted | As written, central (fast to slow) | Worksheet held to 35 | Parts OVER / TIGHT / LOOSE | Biggest sink | After fixes | Flex |
|---|---:|---|---:|---|---|---:|---:|
| 1 Code the Pattern | 90 | **105.5** (95 to 116) | 97.7 | 3 / 2 / 0 | worksheet +7.8, warm-up +3.7 | 87.3 | 2.5 |
| 2 Prime Hunters | 90 | **108.8** (98 to 120) | 98.3 | 4 / 1 / 0 | worksheet +10.4, warm-up +3.2 | 88.5 | 1.5 |
| 3 Below Zero | 90 | **95.7** (86 to 105) | 93.2 | 2 / 1 / 0 | worksheet +2.5, warm-up +2.9 | 86.8 | 3.0 |
| 4 Algebra Machines | 90 | **109.9** (99 to 121) | 100.4 | 4 / 0 / 0 | worksheet +9.5, explore +5.1 | 86.5 | 3.5 |
| 5 Every Possible Way | 90 | **110.5** (99 to 122) | 99.9 | 4 / 1 / 0 | worksheet +10.6, warm-up +3.8 | 86.9 | 3.0 |
| 6 Fair or Unfair? | 90 | **96.9** (87 to 107) | 96.5 | 2 / 0 / 0 | warm-up +3.1, sneak +2.5 | 87.1 | 2.5 |
| 7 Turtle Geometry | 90 | **107.7** (97 to 119) | 102.3 | 5 / 0 / 0 | explore +5.3, worksheet +5.4 | 87.7 | 2.5 |
| 8 Secret Codes | 90 | **105.4** (95 to 116) | 100.2 | 5 / 0 / 0 | worksheet +5.2, mini +4.2 | 86.0 | 4.0 |
| 9 Data Detectives | 90 | **108.5** (97 to 120) | 101.6 | 5 / 1 / 0 | worksheet +6.9, mini +3.3 | 88.3 | 1.5 |
| 10 Showcase Challenge | 90 | **125.7** (112 to 139) | n/a | 8 / 2 / 0 | challenge +7.1, exit/certificates +5.7 | 87.3 | 2.5 |

Reading the table: "Worksheet held to 35" is the total if the tutor stops the worksheet at minute 75 whatever happens and lets every other part take what it needs (the children then finish fewer questions). "Parts OVER / TIGHT / LOOSE" counts parts of the lesson (9 in L1-L9, 11 in L10) by the flag rules in section 3. "After fixes" is the same model applied to the fixes proposed in section 6; "Flex" is the unscripted buffer left in a 90-minute plan after the fixes.

**Where the time goes, across the level (L1-L9 means).**

| Part (L1-L9) | Scripted | Needed, mean of 9 | Over, mean | Range of Diff |
|---|---:|---:|---:|---|
| Opening | 2 | 2.0 | +0.0 | -0.0 to +0.2 |
| Sneak-peek puzzles | 3 | 5.3 | +2.3 | +1.7 to +2.5 |
| Warm-up | 5 | 8.1 | +3.1 | +2.3 to +3.8 |
| Explore | 15 | 17.5 | +2.5 | +0.4 to +5.3 |
| Mini-lesson | 10 | 11.7 | +1.7 | -0.2 to +4.2 |
| Brain break | 5 | 5.0 | +0.0 | -0.3 to +0.4 |
| Worksheet | 35 | 41.5 | +6.5 | +0.4 to +10.6 |
| Talk time | 7 | 5.8 | -1.2 | -1.3 to -1.1 |
| Exit slip, looking back, close | 8 | 8.5 | +0.5 | -0.4 to +1.3 |

1. **Worksheet block (+6.5 on average, up to +10.6).** The 35 minutes contain 13 to 18 minutes of tutor-led slides (6 to 9 slide changes, 5 to 7 check-together questions, 2 to 5 teaching waits) and only 15 to 20 minutes of independent work, against 20 to 28 minutes that a MIDDLE child needs for the Start-here questions. A MIDDLE child finishes 3.4 to 6.2 of the 5 to 7 questions; LOW finishes 2.2 to 3.7; HIGH finishes all or nearly all (5.0 to 7.0) but has at most 1 or 2 Think Harder items of time left.
2. **Warm-up (+3.1, every lesson).** A game of 6 items (about 3.5 min at 10 s + 20 s each) plus 5 quick questions (about 2.8 min) cannot fit in 5 minutes.
3. **Explore (+2.5, up to +5.3).** Three moves (find materials / open Scratch, out to breakout rooms, back) cost about 4 minutes before any child works; L4 and L7 add a long Scratch set-up on top.
4. **Sneak-peek (+2.3, every lesson).** Two puzzles read aloud, 2 minutes of real thinking and two hold-up moments are about 5 minutes, not 3.
5. Slide changes alone are about 11 to 12 minutes a lesson (24 to 26 whole-group slides at 25 s). Lesson 10 is different: the showcase, the build and the certificates have no slack at all.

**Top fixes (detail and exact budgets in section 6).** (a) Re-budget the routine: sneak 4, warm-up 6, a 2 to 3 minute flex buffer; (b) cut each warm-up to 3 or 4 game items and 3 quick questions; (c) take the Go further slide out of the group flow, ask 2 explore questions, and remove the duplicated Scratch build in Explore (L1, L5, L9) or shrink it (L4, L7); (d) move one worksheet question per lesson to take-home (L1 Q5, L2 Q5, L4 Q7, L5 Q5, L7 Q5, L8 Q5, L9 Q6) and shorten check-together to 35 s a question by showing all answers at once; (e) rebuild Lesson 10 around a 2:15 showcase, no relay, no separate talk time and PDF certificates.

## 2. What was read, and what I found about the sources

Read in full: `p6/guide.js` (the `pushSeg` calls give the budgets: 0-2 opening, 2-5 sneak-peek, 5-10 warm-up, 10-25 explore, 25-35 mini-lesson, 35-40 brain break, 40-75 worksheet, 75-82 talk, 82-90 exit/looking back/closing; Lesson 10 has its own plan line), `p6/content/l1.js` to `l10.js` through `p6/data.js` (script, deck, lesson, qbank, gaps, workbook), `p6/workbook_html.js`, all ten decks in `split/p6l1` to `split/p6l10` (slide text and speaker notes), `levels/reccues.js`, the rebuilt tutor guide PDF and the workbook PDF. The tutor guide is built from the same data, so SAY / DO / ASK / IF STUCK lines are the generator's text. Findings that matter for timing:

- **The PDF changed under me.** When this audit started, `p6/Math_Inquirers_P6_Tutor_Guide.pdf` was a Primary 3 guide ("Math Inquirers P3 Tutor Guide", 88 pages, no REC lines) even though the HTML next to it was P6. It was rebuilt at 01:59 and is now the P6 guide (102 pages, REC lines present, Lesson 10 plan with 2 min 30 s showcase slots). Check the file you send to tutors.
- **Early-finisher slides are out of order.** `stretch`, `challenge`, `chdiag` and `chwalk` are labelled 40-72 min but sit in the deck after `ws2ans` (minute 75) and before `talk`. A tutor stepping through the deck in order meets four extra slides (about 100 s) at minute 75. Hide them, or move them before `ws1`.
- **Lesson 10 headings.** The L10 section still prints the default segment headings (10-25 Explore, 25-35 Mini-lesson, 40-75 Worksheet, 75-82, 82-90) under a plan line that says to ignore them. The REC cue minutes and the "Recording chapters" table are built from those headings, so they are wrong for L10.
- **Page time labels do not match the workload.** For example L2 page 2 needs 17.5 min against 11 on `ws2` while page 1 needs 9.5 against 14; L3 page 2 needs 8.5 against 15; L5 page 2 needs 15.5 against 11; L9 page 1 needs 15 against 11. Overlapping or missing labels: L8 `we2` 29-31 overlaps `try1` 29-30; L2 `key` has no label.
- **Files the lessons assume but the repository does not hold.** A printed 1-100 grid for L2 (the cut-out kit has code cards and a square grid only), and tutor-built Scratch start files for L4 (Machine), L7 (Turtle) and L10 (four starters); the notes say "no .sb3 exists in this repository". That is prep time, not lesson time, but the timings below assume the files exist.
- **Stray wording.** L5 `warm1`/`warmGame` mentions "pages 15 to 40", which belongs to another level.

## 3. Model and assumptions (same for every level)

| Item | Value used |
|---|---|
| Tutor speech | 140 words per minute, pauses included: SAY lines, think-aloud and slide narration (narration counted as 80% of the printed words of a worked-example slide) |
| Read-aloud | 130 wpm: questions, answers read from a check slide, task slides; "your turn" prompts counted at 60% |
| Waiting | 10 s after each question put to the group + 20 s to take one or two answers (30 s a question); hold-up-your-paper moments 30 s; "your turn" slide 75 s of whiteboard work + 30 s show; greeting the children 30 s; recording notice 15 s |
| Check-together | 60 s per numbered question as written (volunteer explains, answer shown, children mark in a different colour); 35 s after the fix |
| Slide change | 25 s each (fast run 20 s, slow run 30 s), counted for every whole-group slide, including reveal-click slides. Slides shown only while children work alone (Think harder, Go further, see-it, walk-through) cost no group time |
| Moves | 90 s to find materials / open the Scratch window, 90 s out to breakout rooms, 60 s back (fast 60/40, slow 120/80); 2 min to get started on the worksheet; worksheet pairs stay in the main room (30 s + 30 s) |
| Child activity | Scripted explore, brain-break and worksheet time are not trusted; each is re-estimated from the task. Fast run x0.85, slow run x1.15 |
| REC cue | 10 s at the start of each of 9 parts plus looking back and closing: 11 cues, 110 s a lesson. The real cue texts total 290 words (2.1 min); they range from 15 to 39 words each, so the model is slightly kind |
| Tech | Camera and tech glitches are ignored; every part flagged OK (no slack) has no room for even one |
| Group | 8 children (the maximum); with 6 only L10 changes materially (117.7 instead of 125.7) |
| Worksheet minutes per question (MIDDLE child, age 11-13) | 0.5 to read, 0.25 per table cell to compute, 0.6 to 0.8 per short answer part, 1.0 per "explain", 3 to 4 for planning code or tracing a table. Whole numbered questions come out at 1.5 to 7 min (Core 2 to 5; the 6 x 6 table in L6 Q4 is the longest at 7). LOW x1.6, HIGH x0.65. Think Harder 4 to 6 min |

**What would make these numbers wrong.** In order of size: (1) child activity (46 to 60 minutes of each lesson; +-15% is about +-8 minutes, and the worksheet items are my judgement of what an 11- to 13-year-old needs, not measured); (2) the 25 s per slide change (24 to 26 slides, so 20 s or 30 s moves a lesson by about 2 minutes); (3) breakout moves (3 per Explore, +-1.5 minutes); (4) speech, the best-known part (12 to 14 minutes a lesson, +-1 minute). Even the fast run (20 s slides, 60 s moves, activity x0.85) stays above 90 in seven of Lessons 1-9 (94.7 to 99.1) and falls under 90 only in L3 (86.4) and L6 (87.2); the slow run is 105 to 122. So the conclusion that the plan does not fit does not depend on the central assumptions, but the size of the overrun does.

Flags: **OVER** needed minus scripted of 2 or more; **TIGHT** 1 to 2; **OK** less than 1 over and less than 3 spare ("no slack" when within half a minute); **LOOSE** 3 or more spare.

Judgement inputs per lesson (central run; every one can be changed in the `INP` dictionary of the helper):

| Lesson | Sneak thinking (s, puzzle 1 / 2) | Warm-up game (s) | Explore task (min) | Live code in mini-lesson (s) | Break game (s) | Exit slip (min) | Scratch minutes inside the lesson |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 45 / 60 | 240 | 8.5 | 180 | 90 | 3.0 | 6.5 |
| 2 | 60 / 75 | 210 | 6.5 | 240 | 120 | 3.0 | 4.0 |
| 3 | 40 / 50 | 180 | 6.5 | 0 | 90 | 1.5 | 5.5 |
| 4 | 40 / 75 | 240 | 11.0 | 0 | 120 | 2.0 | 9.0 |
| 5 | 60 / 75 | 240 | 8.5 | 180 | 90 | 2.0 | 6.0 |
| 6 | 45 / 90 | 210 | 6.5 | 60 | 90 | 2.5 | 1.0 |
| 7 | 60 / 75 | 150 | 11.0 | 135 | 120 | 2.0 | 11.3 |
| 8 | 40 / 90 | 180 | 8.5 | 150 | 90 | 2.0 | 2.5 |
| 9 | 60 / 75 | 150 | 9.0 | 240 | 120 | 2.5 | 7.0 |
| 10 | 40 / 90 | relay 20 s a child | challenge 11.6 (teams) | 4 starters x 45 s | 90 | 2.0 | 17.0 |

Scratch time is counted as follows: first opening 1.0 min (tab, new project), making a variable 0.5, each block 0.4 to 0.5, run and read 0.3 to 0.5; the live demos by the tutor are the "live code" column. L6 uses Scratch only to run the coin program 2-3 times. L10 counts loading a starter (1.5), the one change (8) and testing (6) in the 17.

## 4. Size of the lessons

| Lesson | Slides | Whole-group slides | Reveal clicks | Words on group slides | Speaker-note words | SAY words | Mini-lesson slides | Workbook Qs / sub-lines |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | 29 | 25 | 53 | 1573 | 2395 | 497 | 5 | 6 / 7 |
| 2 | 29 | 25 | 59 | 1667 | 2741 | 496 | 6 | 6 / 8 |
| 3 | 28 | 24 | 45 | 1389 | 2559 | 486 | 7 | 7 / 10 |
| 4 | 29 | 25 | 51 | 1605 | 2642 | 497 | 7 | 7 / 10 |
| 5 | 29 | 25 | 55 | 1593 | 3313 | 534 | 6 | 6 / 2 |
| 6 | 30 | 26 | 54 | 1510 | 3232 | 495 | 8 | 5 / 4 |
| 7 | 30 | 26 | 61 | 1582 | 3360 | 465 | 7 | 5 / 7 |
| 8 | 30 | 26 | 57 | 1690 | 3406 | 437 | 8 | 5 / 13 |
| 9 | 29 | 25 | 51 | 1535 | 3307 | 617 | 7 | 6 / 13 |
| 10 | 28 | 24 | 46 | 1387 | 3832 | 599 | 6 | 6 / 14 |

No lesson is unusually large in slide count (28 to 30 slides, 24 to 26 whole-group), but three things stand out. (1) **Eight slides in the 10-minute mini-lesson** in L6 and L8, seven in L3, L4, L7 and L9; at 25 s a slide change that is 2.9 to 3.3 minutes of the 10 gone before anyone says a word. (2) **SAY words:** L9 (617) and L10 (599) are the longest scripts, L5 (534) next, L8 the shortest (437); the SAY text is not the problem, the slide narration and question-and-answer are. (3) **Speaker notes:** L10 has 3,832 words (title notes 464, showcase notes 328), L8 3,406 and L7 3,360; the title-slide notes hold the objective and the time plan and are not spoken, but a tutor reading them live loses time. Reveal clicks (45 to 61 a lesson) are inside the slide-change allowance.

Where the minutes go, by kind of time (central run, whole lesson):

| Lesson | Speaking | Waiting | Child activity | Transitions | Total |
|---|---:|---:|---:|---:|---:|
| 1 | 13.2 | 22.4 | 54.5 | 15.4 | 105.5 |
| 2 | 13.7 | 21.2 | 58.5 | 15.4 | 108.8 |
| 3 | 12.5 | 22.4 | 45.8 | 15.0 | 95.7 |
| 4 | 13.4 | 22.9 | 58.2 | 15.4 | 109.9 |
| 5 | 13.7 | 21.9 | 59.5 | 15.4 | 110.5 |
| 6 | 13.1 | 20.4 | 47.5 | 15.8 | 96.9 |
| 7 | 13.2 | 21.4 | 57.2 | 15.8 | 107.7 |
| 8 | 13.8 | 21.4 | 54.4 | 15.8 | 105.4 |
| 9 | 13.9 | 21.2 | 58.0 | 15.4 | 108.5 |
| 10 | 11.5 | 24.1 | 77.9 | 12.2 | 125.7 |

## 5. Standing buffer, cut-first ladder, REC lines

**Yes, the plan needs a standing buffer.** As written there is none (the 90 minutes are fully allocated), and the fast to slow range is about +-10 minutes. After the fixes in section 6 the central estimate is 86 to 88.5 minutes, so the plan keeps **1.5 to 4 minutes of flex** (4.0 in L8, 3.5 in L4, 1.5 in L2 and L9). Recommend a flex of at least 2 minutes in every lesson, placed right after the worksheet check, where overruns arrive, labelled in the guide as "Flex: use for Think harder or catch-up, lose first". Even after the fixes the slow run is 95 to 98 minutes, so the tutor also needs this ladder, in this order, to recover time without touching the fixed items:

1. Skip the Go further what-if (already out of the group flow after the fix).
2. Ask one quick question fewer in the warm-up, then one explore discussion question fewer.
3. Check-together: explain only the starred question on each page.
4. Second talk question to the next lesson's opener.
5. Never cut: the sneak-peek puzzles, the exit slip, the looking-back 2 minutes, the stamp, and in L10 the certificates and the last stamp.

New budgets at a glance, Lessons 1-9 (minutes; Lesson 10 has its own table in section 6). In every lesson the flex sits right after the worksheet and the other parts keep their usual order:

| Lesson | Opening | Sneak | Warm-up | Explore | Mini | Break | Worksheet | Flex | Talk | Exit and close | Sum |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 4 | 6.5 | 12.5 | 11 | 4.5 | 33.5 | 2.5 | 5 | 8.5 | 90 |
| 2 | 2 | 4.5 | 6 | 14 | 8.5 | 5 | 35.5 | 1.5 | 5 | 8 | 90 |
| 3 | 2 | 3.5 | 6 | 15 | 10 | 5 | 33 | 3 | 6 | 6.5 | 90 |
| 4 | 2 | 4 | 6.5 | 14 | 8 | 5.5 | 34.5 | 3.5 | 5 | 7 | 90 |
| 5 | 2 | 4.5 | 6.5 | 13 | 9.5 | 5 | 34.5 | 3 | 5 | 7 | 90 |
| 6 | 2 | 4.5 | 6 | 14.5 | 10.5 | 5 | 31.5 | 2.5 | 6 | 7.5 | 90 |
| 7 | 2 | 4.5 | 6.5 | 14.5 | 12.5 | 5.5 | 30 | 2.5 | 5 | 7 | 90 |
| 8 | 2 | 4 | 5.5 | 14.5 | 11 | 5 | 31 | 4 | 6 | 7 | 90 |
| 9 | 2 | 4.5 | 5.5 | 14 | 11.5 | 5.5 | 32.5 | 1.5 | 5 | 8 | 90 |

**Shorter Looking-back line** (keeps the pass option, the "nobody marks this" promise and the still-stuck box; 50 words instead of 83, saves 15 s): "Two minutes, just for you, in the Looking back box: something I did well, the hardest part, and what helped. You can write pass. Nobody marks this. If you are still stuck, tick that box and I will check in with you in the open session."

**REC cue lines.** The cues add about 2 minutes a lesson (11 cues; the texts are 15 to 39 words each) and are counted in every table. The longest are Opening (35 words, 15 s), Worksheet (39 words, 17 s) and Explore (34 words, 15 s). The worksheet cue says "this takes about 35 minutes" and the explore cue "about 15 minutes", so any change of budget in section 6 changes the number the cue prints (they are generated from the `pushSeg` minutes), and the L10 headings need the correction in section 2.

## 6. Lesson by lesson

For each lesson: the table as written (central run; Speaking, Waiting, Activity and Transit. are minutes; Needed = their sum; Diff = Needed minus Scripted), then where the time goes, then the fixes with a new budget that sums to 90. "Need after fixes" is the same model applied to the fixed lesson. All fixes keep the answers, the tier principle (Core approachable, Think Harder needs the taught idea, Challenge needs the completed topic) and every "pass is fine / no cold-calling / no rankings" rule. Moving a question to take-home means it moves to the Finish page / next-lesson opener list; it is not deleted and its answer stays in the key.

### Lesson 1: Code the Pattern

Size: 29 slides (25 whole-group, 53 reveal clicks), 1573 words on the group slides, 2395 speaker-note words, about 497 SAY words. Workbook: 6 numbered questions, 7 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 0.9 | 0.7 | 0.0 | 0.4 | 2.0 | +0.0 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.3 | 1.5 | 1.8 | 0.4 | 4.9 | +1.9 | TIGHT |
| Warm-up | 5 | 1.0 | 2.8 | 4.0 | 0.8 | 8.7 | +3.7 | OVER |
| Explore | 15 | 1.6 | 2.0 | 8.5 | 5.2 | 17.4 | +2.4 | OVER |
| Mini-lesson | 10 | 1.8 | 3.0 | 3.0 | 2.1 | 9.9 | -0.1 | OK (no slack) |
| Brain break | 5 | 0.3 | 0.0 | 4.0 | 0.4 | 4.7 | -0.3 | OK (no slack) |
| Worksheet | 35 | 3.8 | 9.8 | 24.5 | 4.8 | 42.8 | +7.8 | OVER |
| Talk time | 7 | 0.8 | 0.8 | 3.8 | 0.4 | 5.8 | -1.2 | OK |
| Exit slip, looking back, close | 8 | 1.6 | 1.8 | 5.0 | 0.8 | 9.3 | +1.3 | TIGHT |
| **Whole lesson** | **90** | **13.2** | **22.4** | **54.5** | **15.4** | **105.5** | **+15.5** | |

Estimated total **105.5 min** (fast 94.9 / slow 116.2); with the worksheet held to its 35 minutes **97.7**. Over 90 by 15.5.

Start-here questions finished in the 35-minute block as written: LOW 2.2, MIDDLE 3.8, HIGH 6.0 of 6 (about 15 min of independent work after the tutor-led slides). After the fixes (33.5-minute block): LOW 3.0, MIDDLE 5.0, HIGH 5.0 of 5, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 5.0; Q2 3.5; Q3 3.0; Q4 4.0; Q5 4.0; Q6 3.0. Page 1 needs 11.5 min against 10 scripted on the ws1 slide; page 2 needs 11.0 against 13 on the ws2 slide.

**Where the time goes**

- Warm-up (+3.7). `warm1` has six sequence cards; at the 10 s + 20 s rule that is about 3.5 min, then `warm2` asks five quick questions (2.8 min of waiting): 6.4 min of question-and-answer inside a 5-minute part.
- Explore (+2.4). Step 4 on `explore1` (check pattern 10 in Scratch: open the window, make `sticks`, four blocks, run, about 3.5 min) is done again live in `we2` (30-33). Finding matchsticks and the two breakout moves cost 4 min before any child builds anything.
- Worksheet (+7.8). Nine group slides, six check-together questions (6 min) and the teaching waits leave about 15 min of independent work; a MIDDLE child needs 22.5 min. `trywhich` (42-44) needs 3 min for its three whiteboard items, and page 1 needs 11.5 min against the 10 on `ws1`.
- Sneak-peek +1.9 and exit +1.3 are TIGHT. Total with the worksheet held to 35 min: 97.7 min.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4 min).** One "show" moment after both puzzles (not one per puzzle), reveal the answers by click and move on with no reaction round, say each answer in 15 words or fewer. Saves about 1.1 min.
- **Warm-up (6.5).** `warm1`: keep cards 1, 2, 3 and 5 (add 4, take away 6, squares, Fibonacci); drop card 4 (doubling) and card 6 (decimals, move to the chat). `warm2`: ask Q2, Q3 and Q4 only (the two seed questions and the $12 + $5 x 6 fence-post question); drop Q1 and Q5. Saves about 2.3 min.
- **Explore (12.5).** Delete step 4 on `explore1` and the "Finished early: in Scratch..." hint. Scratch first appears in `we2`, where the tutor builds it live; add "open scratch.mit.edu, make a variable" to that demo (240 s instead of 180 s). Take the `go` slide out of the group flow (paste the what-if in the chat). Ask discussion Q2 and Q3 only (Q1 is read from the table). Saves about 4.8 min.
- **Mini-lesson (11).** Unchanged slides; the demo now includes opening Scratch.
- **Worksheet (33.5).** Move Q5 (plan the code, 4 min) to the take-home list and take `teachplan` out of the live flow; fold `teachbug` into `teachtrace` as a second panel (one slide change fewer each). Do not read `ws1`/`ws2` aloud (show only). In `ws1ans` and `ws2ans` show all answers at once, children self-mark in a different colour, and the tutor asks one volunteer to explain only the question that carries the idea (Q2 rule on page 1, Q6 repeat 49 on page 2): 35 s a question instead of 60.
- **Talk (5) and exit (8.5).** Ask only the first talk question ("Is Ali right?"). Everyone holds the exit slip to the camera at the same moment (as in the sneak-peek) instead of one by one, and use the short Looking-back line (see section 5).
- **Relabel the page slides.** After the fixes page 1 needs 11.5 min of child work and page 2 needs 7.0; `ws1` and `ws2` say 10 and 13 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 12, `ws2` 7) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.0 |
| Sneak-peek puzzles | 3 | 4.0 | 2 to 6 | 3.8 |
| Warm-up | 5 | 6.5 | 6 to 12.5 | 6.4 |
| Explore | 15 | 12.5 | 12.5 to 25 | 12.6 |
| Mini-lesson | 10 | 11.0 | 25 to 36 | 10.9 |
| Brain break | 5 | 4.5 | 36 to 40.5 | 4.7 |
| Worksheet | 35 | 33.5 | 40.5 to 74 | 33.5 |
| **Flex buffer (unscripted, lost first)** | 0 | 2.5 | 74 to 76.5 | |
| Talk time | 7 | 5.0 | 76.5 to 81.5 | 5.0 |
| Exit slip, looking back, close | 8 | 8.5 | 81.5 to 90 | 8.3 |
| **Total** | 90 | **90.0** | | **87.3** (fast 78.2 / slow 96.5) |


### Lesson 2: Prime Hunters

Size: 29 slides (25 whole-group, 59 reveal clicks), 1667 words on the group slides, 2741 speaker-note words, about 496 SAY words. Workbook: 6 numbered questions, 8 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 0.9 | 0.7 | 0.0 | 0.4 | 2.0 | -0.0 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.3 | 1.5 | 2.2 | 0.4 | 5.5 | +2.5 | OVER |
| Warm-up | 5 | 1.0 | 2.8 | 3.5 | 0.8 | 8.2 | +3.2 | OVER |
| Explore | 15 | 1.6 | 2.0 | 6.5 | 5.2 | 15.4 | +0.4 | OK (no slack) |
| Mini-lesson | 10 | 2.3 | 3.5 | 4.0 | 2.5 | 12.3 | +2.3 | OVER |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 5.2 | +0.2 | OK (no slack) |
| Worksheet | 35 | 4.1 | 8.0 | 29.0 | 4.3 | 45.4 | +10.4 | OVER |
| Talk time | 7 | 0.7 | 0.8 | 3.8 | 0.4 | 5.7 | -1.3 | OK |
| Exit slip, looking back, close | 8 | 1.4 | 1.8 | 5.0 | 0.8 | 9.1 | +1.1 | TIGHT |
| **Whole lesson** | **90** | **13.7** | **21.2** | **58.5** | **15.4** | **108.8** | **+18.8** | |

Estimated total **108.8 min** (fast 97.5 / slow 120.0); with the worksheet held to its 35 minutes **98.3**. Over 90 by 18.8.

Start-here questions finished in the 35-minute block as written: LOW 2.2, MIDDLE 3.4, HIGH 5.6 of 6 (about 17 min of independent work after the tutor-led slides). After the fixes (35.5-minute block): LOW 2.8, MIDDLE 5.0, HIGH 5.0 of 5, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 6.0; Q2 3.5; Q3 5.5; Q4 3.5; Q5 4.5; Q6 4.0. Page 1 needs 9.5 min against 14 scripted on the ws1 slide; page 2 needs 17.5 against 11 on the ws2 slide.

**Where the time goes**

- Sneak-peek +2.5: puzzle 2 (could 31 counters make equal rows?) needs 75 s of real thought after puzzle 1 (every way to arrange 12 counters, 60 s).
- Warm-up +3.2: six factor-pair cards plus five remainder questions.
- Mini-lesson +2.3: six slides in 10 minutes; `we3` builds the prime checker live in Scratch (about 4 min with children copying) and `try1` needs 3 min for three prime tests on whiteboards.
- Worksheet +10.4, the biggest in the level with L5. The pages are unbalanced: page 1 (Q1 factor table and prime circling, Q2 factor trees) needs 9.5 min against 14 min on `ws1`; page 2 (Q3 trace of 6 rows, Q4 Goldbach, Q5 exactly 3 factors, Q6 order the blocks) needs 17.5 min against 11. A MIDDLE child finishes 3.4 of 6 questions in the time left.
- Risk not in the table: the workbook kit has no 1-100 grid (only code cards and a square grid). If children draw their own 10 x 10 grid it costs about 3 min before the sieve starts (`explore1`).

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4.5).** As L1 (one show, no reaction round, short answers).
- **Warm-up (6).** Play four of the six factor-pair cards (keep the card with only one pair) and ask three quick questions (17 ÷ 5, 100 ÷ 7 and "a remainder of 0 means...?").
- **Explore (14).** Add the 1-100 grid to the weekly pack so it is printed; drop the `go` slide from the group flow; ask discussion Q1 and Q3 only ("how many primes", "is 1 prime, is 2 prime"); Q2 (why stop at 7) moves to the mini-lesson where `we1` already says it.
- **Mini-lesson (8.5).** Drop `try1` (the workbook Q1 asks for the same six prime tests). Pre-build the prime checker so the demo is 150 s instead of 240 s.
- **Worksheet (35.5).** Move Q5 (exactly 3 factors) to take-home; fold `teachsq` and `teachplan` into `teachgold`/`teachtrace`. Shorter check-together as L1.
- **Talk (5), exit (8).** One talk question first ("why does 36 have an odd number of factors?"), the primes question stays as a take-home.
- **Relabel the page slides.** After the fixes page 1 needs 9.5 min of child work and page 2 needs 13.0; `ws1` and `ws2` say 14 and 11 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 10, `ws2` 13) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.0 |
| Sneak-peek puzzles | 3 | 4.5 | 2 to 6.5 | 4.3 |
| Warm-up | 5 | 6.0 | 6.5 to 12.5 | 5.9 |
| Explore | 15 | 14.0 | 12.5 to 26.5 | 14.0 |
| Mini-lesson | 10 | 8.5 | 26.5 to 35 | 8.4 |
| Brain break | 5 | 5.0 | 35 to 40 | 5.2 |
| Worksheet | 35 | 35.5 | 40 to 75.5 | 35.5 |
| **Flex buffer (unscripted, lost first)** | 0 | 1.5 | 75.5 to 77 | |
| Talk time | 7 | 5.0 | 77 to 82 | 5.0 |
| Exit slip, looking back, close | 8 | 8.0 | 82 to 90 | 8.1 |
| **Total** | 90 | **90.0** | | **88.5** (fast 78.8 / slow 98.2) |


### Lesson 3: Below Zero

Size: 28 slides (24 whole-group, 45 reveal clicks), 1389 words on the group slides, 2559 speaker-note words, about 486 SAY words. Workbook: 7 numbered questions, 10 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 0.7 | 0.0 | 0.4 | 2.1 | +0.1 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.2 | 1.5 | 1.5 | 0.4 | 4.7 | +1.7 | TIGHT |
| Warm-up | 5 | 1.2 | 2.8 | 3.0 | 0.8 | 7.9 | +2.9 | OVER |
| Explore | 15 | 1.7 | 2.0 | 6.5 | 5.2 | 15.4 | +0.4 | OK (no slack) |
| Mini-lesson | 10 | 2.2 | 4.8 | 0.0 | 2.9 | 9.8 | -0.2 | OK (no slack) |
| Brain break | 5 | 0.4 | 0.0 | 4.0 | 0.4 | 4.9 | -0.1 | OK (no slack) |
| Worksheet | 35 | 2.5 | 8.0 | 23.5 | 3.5 | 37.5 | +2.5 | OVER |
| Talk time | 7 | 0.8 | 0.8 | 3.8 | 0.4 | 5.8 | -1.2 | OK |
| Exit slip, looking back, close | 8 | 1.4 | 1.8 | 3.5 | 0.8 | 7.6 | -0.4 | OK (no slack) |
| **Whole lesson** | **90** | **12.5** | **22.4** | **45.8** | **15.0** | **95.7** | **+5.7** | |

Estimated total **95.7 min** (fast 86.4 / slow 104.9); with the worksheet held to its 35 minutes **93.2**. Over 90 by 5.7.

Start-here questions finished in the 35-minute block as written: LOW 3.7, MIDDLE 6.2, HIGH 7.0 of 7 (about 19 min of independent work after the tutor-led slides). After the fixes (33.0-minute block): LOW 4.1, MIDDLE 7.0, HIGH 7.0 of 7, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 2.5; Q2 3.5; Q3 2.5; Q4 4.5; Q5 3.0; Q6 2.5; Q7 3.0. Page 1 needs 13.0 min against 12 scripted on the ws1 slide; page 2 needs 8.5 against 15 on the ws2 slide.

**Where the time goes**

- Closest to fitting: 95.7 min as written, 93.2 with the worksheet held to 35.
- Warm-up +2.9 (five quick questions plus the city line-up, 3 min) and sneak +1.7. Explore and mini are at their limit with no slack.
- Worksheet +2.5: seven questions (10 sub-lines, about 26 answers) is the largest count in the level, but each answer is short. Page 1 (Q1-Q4) needs 13 min against 12; page 2 (Q5-Q7) needs 8.5 against 15, so page 2 is 6 min LOOSE and page 1 TIGHT.
- Risk: `explore1` notes warn that pasting the minus sign from the slide makes Scratch reject the number. Budget one extra minute if several children paste.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (3.5).** As L1. **Warm-up (6).** Keep the city line-up but shorten it to ordering the five cities plus Tokyo vs Seoul (150 s); ask three quick questions (keep "3 °C falls 5", "which is colder", "lift at B1 goes down 2").
- **Explore (15).** Take the `go` slide out of the group flow; keep all three discussion questions (this lesson has the room).
- **Worksheet (33).** Fold `teachbug` into `teachtrace`. Do not read the preview slides. Faster check-together as L1. No question moves to take-home.
- **Talk (6), exit (6.5).** Keep both talk questions. Exit slip held up together.
- **Relabel the page slides.** After the fixes page 1 needs 13.0 min of child work and page 2 needs 8.5; `ws1` and `ws2` say 12 and 15 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 13, `ws2` 9) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.1 |
| Sneak-peek puzzles | 3 | 3.5 | 2 to 5.5 | 3.5 |
| Warm-up | 5 | 6.0 | 5.5 to 11.5 | 6.2 |
| Explore | 15 | 15.0 | 11.5 to 26.5 | 14.8 |
| Mini-lesson | 10 | 10.0 | 26.5 to 36.5 | 9.8 |
| Brain break | 5 | 5.0 | 36.5 to 41.5 | 4.9 |
| Worksheet | 35 | 33.0 | 41.5 to 74.5 | 33.0 |
| **Flex buffer (unscripted, lost first)** | 0 | 3.0 | 74.5 to 77.5 | |
| Talk time | 7 | 6.0 | 77.5 to 83.5 | 5.8 |
| Exit slip, looking back, close | 8 | 6.5 | 83.5 to 90 | 6.6 |
| **Total** | 90 | **90.0** | | **86.8** (fast 77.8 / slow 95.8) |


### Lesson 4: Algebra Machines

Size: 29 slides (25 whole-group, 51 reveal clicks), 1605 words on the group slides, 2642 speaker-note words, about 497 SAY words. Workbook: 7 numbered questions, 10 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 0.7 | 0.0 | 0.4 | 2.0 | +0.0 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.2 | 1.5 | 1.9 | 0.4 | 5.0 | +2.0 | OVER |
| Warm-up | 5 | 1.1 | 2.8 | 4.0 | 0.8 | 8.7 | +3.7 | OVER |
| Explore | 15 | 1.8 | 2.0 | 11.0 | 5.2 | 20.1 | +5.1 | OVER |
| Mini-lesson | 10 | 2.5 | 4.8 | 0.0 | 2.9 | 10.2 | +0.2 | OK (no slack) |
| Brain break | 5 | 0.4 | 0.0 | 4.5 | 0.4 | 5.4 | +0.4 | OK (no slack) |
| Worksheet | 35 | 3.1 | 8.5 | 29.0 | 3.9 | 44.5 | +9.5 | OVER |
| Talk time | 7 | 0.9 | 0.8 | 3.8 | 0.4 | 5.9 | -1.1 | OK |
| Exit slip, looking back, close | 8 | 1.5 | 1.8 | 4.0 | 0.8 | 8.1 | +0.1 | OK (no slack) |
| **Whole lesson** | **90** | **13.4** | **22.9** | **58.2** | **15.4** | **109.9** | **+19.9** | |

Estimated total **109.9 min** (fast 98.8 / slow 121.1); with the worksheet held to its 35 minutes **100.4**. Over 90 by 19.9.

Start-here questions finished in the 35-minute block as written: LOW 2.5, MIDDLE 4.6, HIGH 7.0 of 7 (about 18 min of independent work after the tutor-led slides). After the fixes (34.5-minute block): LOW 3.3, MIDDLE 6.0, HIGH 6.0 of 6, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 4.5; Q2 4.0; Q3 5.0; Q4 2.5; Q5 2.5; Q6 4.0; Q7 4.5. Page 1 needs 13.5 min against 12 scripted on the ws1 slide; page 2 needs 13.5 against 15 on the ws2 slide.

**Where the time goes**

- Explore +5.1 (the largest single explore overrun with L7): open Scratch, build `ask IN? and wait / set out to (answer * 3) + 2 / say out` (the nested operator is slow for 11-year-olds), change it to a secret rule, then two screen-share rounds (one each way) is 11 min of task plus 4 min of moves. The `explore1` notes say "screen-share Scratch for 2 minutes and build the machine together" and that no .sb3 starter exists in the repository, so the tutor must build it beforehand.
- Warm-up +3.7: four "guess my rule" rounds (about 4 min) plus five quick questions.
- Worksheet +9.5: seven questions. Page 1 (Q1 four tables, Q2 two machines, Q3 four backwards equations with checks) needs 13.5 min against 12; Q7 (the number trick with algebra and an explanation) is the longest single item on page 2 at 4.5 min.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4).** As L1. **Warm-up (6.5).** Three rounds of guess-my-rule (5n, 2n - 1, 3n + 2; drop n + 5) and three quick questions.
- **Explore (14).** The tutor builds the machine live for 2 minutes as the notes say; each pair then does ONE direction (one child shares, the partner calls IN numbers) and the swap becomes the Go further what-if. Task time 6.5 min instead of 11. Drop the `go` slide from the group flow; ask Q2 and Q3 only.
- **Mini-lesson (8).** Drop `try1` (find the rule): workbook Q1 has four such tables. `try2` stays.
- **Worksheet (34.5).** Move Q7 (number trick) to take-home; fold `teachsearch` and `teachtrick` into `teachcode` (Q7 leaves the room, so `teachtrick` is not needed live). Shorter check-together.
- **Talk (5), exit (7).** First talk question only ("Ravi or Mei: which way is better?"); exit slips up together.
- **Relabel the page slides.** After the fixes page 1 needs 13.5 min of child work and page 2 needs 9.0; `ws1` and `ws2` say 12 and 15 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 14, `ws2` 9) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.0 |
| Sneak-peek puzzles | 3 | 4.0 | 2 to 6 | 4.0 |
| Warm-up | 5 | 6.5 | 6 to 12.5 | 6.6 |
| Explore | 15 | 14.0 | 12.5 to 26.5 | 14.2 |
| Mini-lesson | 10 | 8.0 | 26.5 to 34.5 | 7.8 |
| Brain break | 5 | 5.5 | 34.5 to 40 | 5.4 |
| Worksheet | 35 | 34.5 | 40 to 74.5 | 34.3 |
| **Flex buffer (unscripted, lost first)** | 0 | 3.5 | 74.5 to 78 | |
| Talk time | 7 | 5.0 | 78 to 83 | 5.2 |
| Exit slip, looking back, close | 8 | 7.0 | 83 to 90 | 7.1 |
| **Total** | 90 | **90.0** | | **86.5** (fast 77.3 / slow 95.8) |


### Lesson 5: Every Possible Way

Size: 29 slides (25 whole-group, 55 reveal clicks), 1593 words on the group slides, 3313 speaker-note words, about 534 SAY words. Workbook: 6 numbered questions, 2 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 0.7 | 0.0 | 0.4 | 2.1 | +0.1 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.2 | 1.5 | 2.2 | 0.4 | 5.4 | +2.4 | OVER |
| Warm-up | 5 | 1.1 | 2.8 | 4.0 | 0.8 | 8.8 | +3.8 | OVER |
| Explore | 15 | 2.3 | 2.0 | 8.5 | 5.2 | 18.0 | +3.0 | OVER |
| Mini-lesson | 10 | 2.0 | 4.2 | 3.0 | 2.5 | 11.7 | +1.7 | TIGHT |
| Brain break | 5 | 0.4 | 0.0 | 4.0 | 0.4 | 4.9 | -0.1 | OK (no slack) |
| Worksheet | 35 | 3.3 | 8.0 | 30.0 | 4.3 | 45.6 | +10.6 | OVER |
| Talk time | 7 | 0.9 | 0.8 | 3.8 | 0.4 | 5.9 | -1.1 | OK |
| Exit slip, looking back, close | 8 | 1.5 | 1.8 | 4.0 | 0.8 | 8.1 | +0.1 | OK (no slack) |
| **Whole lesson** | **90** | **13.7** | **21.9** | **59.5** | **15.4** | **110.5** | **+20.5** | |

Estimated total **110.5 min** (fast 99.1 / slow 121.9); with the worksheet held to its 35 minutes **99.9**. Over 90 by 20.5.

Start-here questions finished in the 35-minute block as written: LOW 2.7, MIDDLE 4.1, HIGH 5.8 of 6 (about 17 min of independent work after the tutor-led slides). After the fixes (34.5-minute block): LOW 3.3, MIDDLE 5.0, HIGH 5.0 of 5, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 1.5; Q2 5.0; Q3 6.0; Q4 4.0; Q5 6.0; Q6 5.5. Page 1 needs 12.5 min against 13 scripted on the ws1 slide; page 2 needs 15.5 against 11 on the ws2 slide.

**Where the time goes**

- Worst of L1-L9: 110.5 min (99.9 with the worksheet held to 35).
- Worksheet +10.6. Page 2 (Q4 handshakes with Ali's error, Q5 grid routes with a puddle, Q6 plan the nested-loop code) needs 15.5 min against 11, and page 1 needs 12.5 (Q3, a 6-row trace of nested loops, is 6 min). Q5 (fill about 16 circles, then redo with a puddle) is 6 min alone.
- Explore +3.0: list the 6 orders on paper, predict the size change, then open the "Every Order" starter and add a second loop (about 3 min); the same nested loop is built live again in `teachcode` (30-32, "share your screen and build it live").
- Sneak +2.4 (chess clubs: "is it 5 x 4?" needs 75 s) and warm-up +3.8 (six counting puzzles). The warm-up game text on `warm1` mentions "pages 15 to 40", which does not match this level and will make the tutor hesitate.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4.5).** As L1. **Warm-up (6.5).** Four of the six counting puzzles and three quick questions (drop "1 + 2 + ... + 10" and "6 x 5 / 2", which reappear as handshakes); remove the stray "pages 15 to 40" wording.
- **Explore (13).** Do the bubble-tea list and the size prediction on paper only; the nested loop is built once, live, in `teachcode`. Drop the `go` slide from the group flow, ask Q1 and Q2 only.
- **Mini-lesson (9.5).** Drop `try2` (count the says): workbook Q3 asks the same thing with a trace table.
- **Worksheet (34.5).** Move Q5 (grid routes) to take-home and take `teachroute` out of the live flow; fold `teachhandcode` into `teachhand`. Shorter check-together.
- **Talk (5), exit (7).** First talk question only; exit slips up together.
- **Relabel the page slides.** After the fixes page 1 needs 12.5 min of child work and page 2 needs 9.5; `ws1` and `ws2` say 13 and 11 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 13, `ws2` 10) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.1 |
| Sneak-peek puzzles | 3 | 4.5 | 2 to 6.5 | 4.3 |
| Warm-up | 5 | 6.5 | 6.5 to 13 | 6.4 |
| Explore | 15 | 13.0 | 13 to 26 | 13.2 |
| Mini-lesson | 10 | 9.5 | 26 to 35.5 | 9.3 |
| Brain break | 5 | 5.0 | 35.5 to 40.5 | 4.9 |
| Worksheet | 35 | 34.5 | 40.5 to 75 | 34.6 |
| **Flex buffer (unscripted, lost first)** | 0 | 3.0 | 75 to 78 | |
| Talk time | 7 | 5.0 | 78 to 83 | 5.1 |
| Exit slip, looking back, close | 8 | 7.0 | 83 to 90 | 7.1 |
| **Total** | 90 | **90.0** | | **86.9** (fast 77.6 / slow 96.3) |


### Lesson 6: Fair or Unfair?

Size: 30 slides (26 whole-group, 54 reveal clicks), 1510 words on the group slides, 3232 speaker-note words, about 495 SAY words. Workbook: 5 numbered questions, 4 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 0.9 | 0.7 | 0.0 | 0.4 | 2.0 | -0.0 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.4 | 1.5 | 2.2 | 0.4 | 5.5 | +2.5 | OVER |
| Warm-up | 5 | 1.0 | 2.8 | 3.5 | 0.8 | 8.1 | +3.1 | OVER |
| Explore | 15 | 1.9 | 2.0 | 6.5 | 5.2 | 15.6 | +0.6 | OK (no slack) |
| Mini-lesson | 10 | 2.3 | 4.2 | 1.0 | 3.3 | 10.9 | +0.9 | OK (no slack) |
| Brain break | 5 | 0.5 | 0.0 | 4.0 | 0.4 | 4.9 | -0.1 | OK (no slack) |
| Worksheet | 35 | 2.9 | 6.5 | 22.0 | 3.9 | 35.4 | +0.4 | OK (no slack) |
| Talk time | 7 | 0.9 | 0.8 | 3.8 | 0.4 | 5.9 | -1.1 | OK |
| Exit slip, looking back, close | 8 | 1.5 | 1.8 | 4.5 | 0.8 | 8.7 | +0.7 | OK (no slack) |
| **Whole lesson** | **90** | **13.1** | **20.4** | **47.5** | **15.8** | **96.9** | **+6.9** | |

Estimated total **96.9 min** (fast 87.2 / slow 106.5); with the worksheet held to its 35 minutes **96.5**. Over 90 by 6.9.

Start-here questions finished in the 35-minute block as written: LOW 3.5, MIDDLE 4.9, HIGH 5.0 of 5 (about 20 min of independent work after the tutor-led slides). After the fixes (31.5-minute block): LOW 3.5, MIDDLE 4.9, HIGH 5.0 of 5, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 3.5; Q2 3.5; Q3 2.0; Q4 7.0; Q5 4.0. Page 1 needs 9.0 min against 12 scripted on the ws1 slide; page 2 needs 11.0 against 13 on the ws2 slide.

**Where the time goes**

- Second best: 96.9 min (96.5 with the worksheet held to 35). Worksheet fits (35.4): five questions, page 1 needs 9 min against 12, page 2 needs 11 against 13.
- But the mini-lesson has eight slides in 10 minutes (3.3 min of slide changes) and the sneak-peek puzzle 2 (list every way two coins can land) needs 90 s. Sneak +2.5, warm-up +3.1.
- Longest single item: Q4 (the 6 x 6 difference table, about 24 cells to fill, then two probabilities and "is it fair?") at 7 min.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4.5).** As L1. **Warm-up (6).** Four of the six events on the probability line; three quick questions.
- **Explore (14.5).** Take the `go` slide out of the group flow; ask Q1 and Q2 only.
- **Mini-lesson (10.5).** Fold `teachwhy` ("close but not exact") into `teachcode` (they are one idea: run it 2-3 times, then say why it wobbles). Keeps all content, saves one slide change.
- **Worksheet (31.5).** No question moves. Fold `teachplan` into `teachfair`; faster check-together. The block can shrink to 31.5 min because the fixes remove about 4 min of tutor-led time, and a HIGH child still has time for about 2 Think Harder items.
- **Exit (7.5).** Exit slips up together.
- **Relabel the page slides.** After the fixes page 1 needs 9.0 min of child work and page 2 needs 11.0; `ws1` and `ws2` say 12 and 13 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 9, `ws2` 11) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.0 |
| Sneak-peek puzzles | 3 | 4.5 | 2 to 6.5 | 4.4 |
| Warm-up | 5 | 6.0 | 6.5 to 12.5 | 5.9 |
| Explore | 15 | 14.5 | 12.5 to 27 | 14.3 |
| Mini-lesson | 10 | 10.5 | 27 to 37.5 | 10.5 |
| Brain break | 5 | 5.0 | 37.5 to 42.5 | 4.9 |
| Worksheet | 35 | 31.5 | 42.5 to 74 | 31.7 |
| **Flex buffer (unscripted, lost first)** | 0 | 2.5 | 74 to 76.5 | |
| Talk time | 7 | 6.0 | 76.5 to 82.5 | 5.9 |
| Exit slip, looking back, close | 8 | 7.5 | 82.5 to 90 | 7.7 |
| **Total** | 90 | **90.0** | | **87.1** (fast 77.9 / slow 96.4) |


### Lesson 7: Turtle Geometry

Size: 30 slides (26 whole-group, 61 reveal clicks), 1582 words on the group slides, 3360 speaker-note words, about 465 SAY words. Workbook: 5 numbered questions, 7 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 0.7 | 0.0 | 0.4 | 2.0 | +0.0 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.4 | 1.5 | 2.2 | 0.4 | 5.5 | +2.5 | OVER |
| Warm-up | 5 | 1.2 | 2.8 | 2.5 | 0.8 | 7.4 | +2.4 | OVER |
| Explore | 15 | 1.7 | 2.0 | 11.0 | 5.7 | 20.3 | +5.3 | OVER |
| Mini-lesson | 10 | 2.3 | 5.2 | 2.2 | 2.9 | 12.7 | +2.7 | OVER |
| Brain break | 5 | 0.4 | 0.0 | 4.5 | 0.4 | 5.3 | +0.3 | OK (no slack) |
| Worksheet | 35 | 3.0 | 6.5 | 27.0 | 3.9 | 40.4 | +5.4 | OVER |
| Talk time | 7 | 0.9 | 0.8 | 3.8 | 0.4 | 5.9 | -1.1 | OK |
| Exit slip, looking back, close | 8 | 1.4 | 1.8 | 4.0 | 0.8 | 8.1 | +0.1 | OK (no slack) |
| **Whole lesson** | **90** | **13.2** | **21.4** | **57.2** | **15.8** | **107.7** | **+17.7** | |

Estimated total **107.7 min** (fast 96.6 / slow 118.9); with the worksheet held to its 35 minutes **102.3**. Over 90 by 17.7.

Start-here questions finished in the 35-minute block as written: LOW 2.5, MIDDLE 4.1, HIGH 5.0 of 5 (about 20 min of independent work after the tutor-led slides). After the fixes (30.0-minute block): LOW 2.4, MIDDLE 4.0, HIGH 4.0 of 4, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 6.5; Q2 3.5; Q3 5.0; Q4 4.0; Q5 6.0. Page 1 needs 10.0 min against 10 scripted on the ws1 slide; page 2 needs 15.0 against 17 on the ws2 slide.

**Where the time goes**

- Explore +5.3: the `setup` slide (10-11) offers two routes (add the Pen extension and build the four set-up blocks, or open the start file the tutor shares); the notes tell the tutor to build the start file beforehand because no .sb3 exists in the repository. With the build route the task is square, triangle, pentagon, hexagon and a table, about 11 min, plus 4 min of moves and four slides.
- Mini-lesson +2.7: seven slides, two whiteboard "your turn" slides (3 min each with the show moment), two live runs in Scratch.
- Worksheet +5.4: the inside-angle table in Q5 (10 cells, then a formula) is 6 min and Q1 (a 7-row table with forwards and backwards rows) is 6.5 min.
- Sneak +2.5 (turn 40-degree corners: 360 / 40 = 9 corners needs 75 s) and warm-up +2.4.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4.5).** As L1. **Warm-up (6.5).** Three quick questions; the "turtle says" game stays at 150 s.
- **Explore (14.5).** Make the start file the default route (the slide already offers it; the tutor builds it before the lesson) so children load it in 60 s instead of building the four set-up blocks, and test the triangle and the hexagon only (the pentagon becomes the Go further what-if). Merge `setup` into `explore1`. Drop the `go` slide; ask Q1 and Q3.
- **Mini-lesson (12.5).** Unchanged; this is the only one of L1-L9 that keeps a mini-lesson above 11 min (the star is the centre of the lesson). If it overruns, drop `try1` first (saves about 2.3 min).
- **Worksheet (30).** Move Q5 (inside-angle sums) to take-home and take `teachsum` out of the live flow. Shorter check-together.
- **Talk (5), exit (7).** First talk question only; exit slips up together.
- **Relabel the page slides.** After the fixes page 1 needs 10.0 min of child work and page 2 needs 9.0; `ws1` and `ws2` say 10 and 17 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 10, `ws2` 9) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.0 |
| Sneak-peek puzzles | 3 | 4.5 | 2 to 6.5 | 4.4 |
| Warm-up | 5 | 6.5 | 6.5 to 13 | 6.3 |
| Explore | 15 | 14.5 | 13 to 27.5 | 14.6 |
| Mini-lesson | 10 | 12.5 | 27.5 to 40 | 12.7 |
| Brain break | 5 | 5.5 | 40 to 45.5 | 5.3 |
| Worksheet | 35 | 30.0 | 45.5 to 75.5 | 30.1 |
| **Flex buffer (unscripted, lost first)** | 0 | 2.5 | 75.5 to 78 | |
| Talk time | 7 | 5.0 | 78 to 83 | 5.1 |
| Exit slip, looking back, close | 8 | 7.0 | 83 to 90 | 7.1 |
| **Total** | 90 | **90.0** | | **87.7** (fast 78.4 / slow 97.0) |


### Lesson 8: Secret Codes

Size: 30 slides (26 whole-group, 57 reveal clicks), 1690 words on the group slides, 3406 speaker-note words, about 437 SAY words. Workbook: 5 numbered questions, 13 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 0.9 | 0.7 | 0.0 | 0.4 | 2.0 | +0.0 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.2 | 1.5 | 2.2 | 0.4 | 5.3 | +2.3 | OVER |
| Warm-up | 5 | 1.0 | 2.8 | 3.0 | 0.8 | 7.6 | +2.6 | OVER |
| Explore | 15 | 1.6 | 2.0 | 8.5 | 5.2 | 17.3 | +2.3 | OVER |
| Mini-lesson | 10 | 3.1 | 5.2 | 2.5 | 3.3 | 14.2 | +4.2 | OVER |
| Brain break | 5 | 0.4 | 0.0 | 4.0 | 0.4 | 4.8 | -0.2 | OK (no slack) |
| Worksheet | 35 | 3.3 | 6.5 | 26.5 | 3.9 | 40.2 | +5.2 | OVER |
| Talk time | 7 | 0.8 | 0.8 | 3.8 | 0.4 | 5.8 | -1.2 | OK |
| Exit slip, looking back, close | 8 | 1.4 | 1.8 | 4.0 | 0.8 | 8.1 | +0.1 | OK (no slack) |
| **Whole lesson** | **90** | **13.8** | **21.4** | **54.4** | **15.8** | **105.4** | **+15.4** | |

Estimated total **105.4 min** (fast 94.7 / slow 116.1); with the worksheet held to its 35 minutes **100.2**. Over 90 by 15.4.

Start-here questions finished in the 35-minute block as written: LOW 2.2, MIDDLE 3.9, HIGH 5.0 of 5 (about 19 min of independent work after the tutor-led slides). After the fixes (31.0-minute block): LOW 2.2, MIDDLE 4.0, HIGH 4.0 of 4, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 4.0; Q2 7.0; Q3 5.0; Q4 3.5; Q5 5.0. Page 1 needs 11.0 min against 10 scripted on the ws1 slide; page 2 needs 13.5 against 16 on the ws2 slide.

**Where the time goes**

- Mini-lesson +4.2, the worst mini-lesson in the level: eight slides (`teach1` 104 words, `we1` 92, `we2` 82, `we3` 96, plus two whiteboard slides and `teachloop` 43 words) with a live Scratch build from the starter.
- Explore +2.3: writing out the alphabet twice (A to Z and D to C) is 3 min before any coding happens; then code a name, swap, decode a message.
- Worksheet +5.2: Q2 (code PIZZA, decode the nine letters of MYNO SC PEX, a forward shift) is 7 min and Q3 (trace W, A, Y through three formulas) is 5 min. Page 1 needs 11 min against 10.
- Sneak +2.3: puzzle 2 ("what day in 100 days?") needs 90 s unless the child knows remainders.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4).** As L1. **Warm-up (5.5).** Four clock-jump calls and three quick questions.
- **Explore (14.5).** Show the shifted alphabet strip on the slide instead of having every child write it (saves 1.5 min of copying); the rest stays.
- **Mini-lesson (11).** Drop `try1` (clocks and days: the workbook Q1 is five such puzzles); fold `teachloop` (the whole code machine) into `we3`; demo 120 s because the starter project already has the list.
- **Worksheet (31).** Move Q5 (two shifts in a row) to take-home and fold `teachcomb` away. Shorter check-together.
- **Exit (7).** Exit slips up together. Keep both talk questions (this lesson has 4 min of flex).
- **Relabel the page slides.** After the fixes page 1 needs 11.0 min of child work and page 2 needs 8.5; `ws1` and `ws2` say 10 and 16 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 11, `ws2` 9) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.0 |
| Sneak-peek puzzles | 3 | 4.0 | 2 to 6 | 4.2 |
| Warm-up | 5 | 5.5 | 6 to 11.5 | 5.5 |
| Explore | 15 | 14.5 | 11.5 to 26 | 14.6 |
| Mini-lesson | 10 | 11.0 | 26 to 37 | 10.9 |
| Brain break | 5 | 5.0 | 37 to 42 | 4.8 |
| Worksheet | 35 | 31.0 | 42 to 73 | 31.0 |
| **Flex buffer (unscripted, lost first)** | 0 | 4.0 | 73 to 77 | |
| Talk time | 7 | 6.0 | 77 to 83 | 5.8 |
| Exit slip, looking back, close | 8 | 7.0 | 83 to 90 | 7.1 |
| **Total** | 90 | **90.0** | | **86.0** (fast 76.8 / slow 95.1) |


### Lesson 9: Data Detectives

Size: 29 slides (25 whole-group, 51 reveal clicks), 1535 words on the group slides, 3307 speaker-note words, about 617 SAY words. Workbook: 6 numbered questions, 13 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 1.1 | 0.7 | 0.0 | 0.4 | 2.2 | +0.2 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.4 | 1.5 | 2.2 | 0.4 | 5.5 | +2.5 | OVER |
| Warm-up | 5 | 1.2 | 2.8 | 2.5 | 0.8 | 7.3 | +2.3 | OVER |
| Explore | 15 | 2.0 | 2.0 | 9.0 | 5.2 | 18.3 | +3.3 | OVER |
| Mini-lesson | 10 | 2.4 | 4.0 | 4.0 | 2.9 | 13.3 | +3.3 | OVER |
| Brain break | 5 | 0.3 | 0.0 | 4.5 | 0.4 | 5.3 | +0.3 | OK (no slack) |
| Worksheet | 35 | 3.0 | 7.5 | 27.5 | 3.9 | 41.9 | +6.9 | OVER |
| Talk time | 7 | 0.8 | 0.8 | 3.8 | 0.4 | 5.8 | -1.2 | OK |
| Exit slip, looking back, close | 8 | 1.9 | 1.8 | 4.5 | 0.8 | 9.0 | +1.0 | TIGHT |
| **Whole lesson** | **90** | **13.9** | **21.2** | **58.0** | **15.4** | **108.5** | **+18.5** | |

Estimated total **108.5 min** (fast 97.4 / slow 119.7); with the worksheet held to its 35 minutes **101.6**. Over 90 by 18.5.

Start-here questions finished in the 35-minute block as written: LOW 3.2, MIDDLE 4.6, HIGH 6.0 of 6 (about 19 min of independent work after the tutor-led slides). After the fixes (32.5-minute block): LOW 3.5, MIDDLE 5.0, HIGH 5.0 of 5, and a HIGH child has time for about 2 Think Harder item(s).

MIDDLE-child minutes per item: Q1 3.0; Q2 3.0; Q3 4.5; Q4 4.5; Q5 6.0; Q6 4.5. Page 1 needs 15.0 min against 11 scripted on the ws1 slide; page 2 needs 10.5 against 14 on the ws2 slide.

**Where the time goes**

- Highest SAY word count of L1-L9 (617). Mini-lesson +3.3 (seven slides, `code1` builds the mean machine live with a list, about 4 min).
- Worksheet +6.9: page 1 is the longest page in the level: Q1 to Q4 need 15 min against 11 (Q3 asks four predict-then-compute items; Q4 asks mean, median, mode, a count and an explanation).
- Explore +3.3: names are posted in the chat, the mean is estimated, worked by hand, then typed into a Scratch list (8 values) and run, then 30 is added: 9 min of task.
- Sneak +2.5 (puzzle 2 about a $38 outlier needs 75 s). Exit +1.0 TIGHT.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4.5).** As L1. **Warm-up (5.5).** Two rounds of quick-eye mean and three quick questions.
- **Explore (14).** Drop the typing of the data into the Scratch list and the program run (the same program is built in `code1`); keep the by-hand mean and the "add a value of 30" prediction. Drop the `go` slide; ask Q1 and Q2.
- **Mini-lesson (11.5).** Pre-build the list program so the live demo is 150 s; fold `change` into `key`.
- **Worksheet (32.5).** Move Q6 (temperatures, plan the code) to take-home; fold `teachif` away.
- **Talk (5), exit (8).** First talk question only; exit slips up together. Buffer is only 1.5 min here, so this lesson needs the cut-first ladder in section 5.
- **Relabel the page slides.** After the fixes page 1 needs 15.0 min of child work and page 2 needs 6.0; `ws1` and `ws2` say 11 and 14 minutes as written. Set the two labels in proportion to those numbers (for example `ws1` 15, `ws2` 6) and keep the teaching and check slides inside the rest of the block.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.2 |
| Sneak-peek puzzles | 3 | 4.5 | 2 to 6.5 | 4.4 |
| Warm-up | 5 | 5.5 | 6.5 to 12 | 5.4 |
| Explore | 15 | 14.0 | 12 to 26 | 13.9 |
| Mini-lesson | 10 | 11.5 | 26 to 37.5 | 11.4 |
| Brain break | 5 | 5.5 | 37.5 to 43 | 5.3 |
| Worksheet | 35 | 32.5 | 43 to 75.5 | 32.7 |
| **Flex buffer (unscripted, lost first)** | 0 | 1.5 | 75.5 to 77 | |
| Talk time | 7 | 5.0 | 77 to 82 | 5.0 |
| Exit slip, looking back, close | 8 | 8.0 | 82 to 90 | 8.0 |
| **Total** | 90 | **90.0** | | **88.3** (fast 78.9 / slow 97.6) |


### Lesson 10: Showcase Challenge

Size: 28 slides (24 whole-group, 46 reveal clicks), 1387 words on the group slides, 3832 speaker-note words, about 599 SAY words. Workbook: 6 numbered questions, 14 lettered sub-lines.

**As written (central run)**

| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Opening | 2 | 1.0 | 0.7 | 0.0 | 0.4 | 2.1 | +0.1 | OK (no slack) |
| Sneak-peek puzzles | 3 | 1.1 | 1.5 | 2.2 | 0.4 | 5.2 | +2.2 | OVER |
| Warm-up (lightning relay) | 3 | 1.0 | 0.5 | 2.7 | 0.4 | 4.6 | +1.6 | TIGHT |
| Challenge round (teams of 2) + check | 15 | 1.8 | 4.5 | 11.6 | 4.2 | 22.1 | +7.1 | OVER |
| Starter projects (A-D) | 7 | 1.7 | 4.8 | 3.0 | 2.5 | 11.9 | +4.9 | OVER |
| Brain break | 2 | 0.4 | 0.0 | 4.0 | 0.4 | 4.8 | +2.8 | OVER |
| Plan and build | 30 | 1.4 | 1.5 | 30.5 | 1.8 | 35.2 | +5.2 | OVER |
| Showcase (8 children) | 23 | 0.7 | 4.7 | 20.0 | 0.4 | 25.8 | +2.8 | OVER |
| Talk time | 1 | 0.5 | 1.3 | 0.0 | 0.4 | 2.3 | +1.3 | TIGHT |
| Exit slip | 2 | 0.3 | 1.3 | 2.0 | 0.4 | 4.1 | +2.1 | OVER |
| Looking back + certificates | 2 | 1.5 | 3.3 | 2.0 | 0.8 | 7.7 | +5.7 | OVER |
| **Whole lesson** | **90** | **11.5** | **24.1** | **77.9** | **12.2** | **125.7** | **+35.7** | |

Estimated total **125.7 min** (fast 112.0 / slow 139.4). Over 90 by 35.7. With 6 children instead of 8 the total is 117.7.

Challenge round team work (teams of 2, x0.8 for sharing): Q1 4.5, Q2 6.0, Q3 4.0 MIDDLE-child minutes; plan and build 28.5 min of child work.

**Where the time goes**

- Longest by far: 125.7 min (range 112-139). The plan in the guide (and the deck) has 11 parts and no part has slack.
- Challenge round (8-23) +7.1: three puzzles with 11 answers in teams of 2 need about 11.6 min of team work, plus the rules slide, two breakout moves, a 3-question check-together and the "how we started" slide, against 15.
- Starter projects (23-30) +4.4: six slides and four starters (A, B, C, then D in `teachplan`) run on screen with predictions.
- Brain break (30-32) +2.8: the break is 2 min on paper but a stretch game plus water is 4 min. Plan and build (32-62) +5.2: Q4, Q5, Q6 on paper (13 min), load a starter, make a change, run three tests, fix one bug.
- Showcase (62-85) +2.8 with 8 children: 8 x (2 min 30 s + 20 s switch) is 22 min 40 s on paper, so any spoken stars or reply over 20 s breaks it; with 6 children the same part needs 19.5 min. Exit slip (+2.1) and looking back with certificates (+5.7): looking back is 2 min and a certificate with one specific praise for each of 8 children is another 3.3 min, in a 2-minute slot.
- The L10 section of the tutor guide still prints the default segment headings (10-25 Explore, 25-35 Mini-lesson, 40-75 Worksheet, 82-90 Exit) under the plan line, and the REC cue minutes and the recording chapter list are built from those headings, so a child watching the recording is told "about 15 minutes" for parts that do not exist.

**Fixes** (answers, the tier principle and every "pass is fine" rule unchanged)

- **Sneak (4) and warm-up (0).** One show; drop the lightning relay (5-8). The challenge round is the review; the quick questions on `warm1` were already marked "spare".
- **Challenge round (13.5).** Teams do Q1 and Q3; Q2 (prime hunters) moves to take-home. Drop `explore2` ("how we started"; ask it as the first line of the check-together). Do not read `ws1`. Check-together 35 s a question.
- **Starter projects (7).** Run only Starter A live; B, C and D are one line each on `we2`/`we3` and are run by the children when they load the file. Drop `try1` (beat the machine).
- **Brain break (3.5).** Stretch game 90 s, water at the desk, no toilet round (say so at the start).
- **Plan and build (28).** Q4: only the part for the starter the child picked (2 min, not 5); Q5: three cells (idea, answer, twist); Q6: three test rows written before running. Keep "a working copy of one starter with one change is full marks".
- **Showcase (22).** Per child 2 min 15 s (show 25 s, run 30 s, prove 35 s, explain 45 s) plus the 20 s switch; stars are typed in the chat, not spoken. 8 x 2:35 = 20.7 min plus set-up.
- **Talk (0), exit slip (3.5), looking back and certificates (4).** Fold the talk question into the exit slip ("what was the hardest bug you fixed?" as the last line). Send certificates as a PDF with the praise already written (the rubric asks for it); on the `end` slide say one sentence to the whole group. Looking back stays 2 min. Slips held up together.
- **Guide fix.** Make `pushSeg` in `p6/guide.js` use the L10 plan (11 segments) so the headings, REC minutes and chapter list match.

**New budget (sums to 90)**

| Part | Was | Now | Minute marks | Need after fixes |
|---|---:|---:|---|---:|
| Opening | 2 | 2.0 | 0 to 2 | 2.1 |
| Sneak-peek puzzles | 3 | 4.0 | 2 to 6 | 4.1 |
| Warm-up (lightning relay) | 3 | 0 | dropped (see fixes) | 0.0 |
| Challenge round (teams of 2) + check | 15 | 13.5 | 6 to 19.5 | 13.3 |
| Starter projects (A-D) | 7 | 7.0 | 19.5 to 26.5 | 7.1 |
| Brain break | 2 | 3.5 | 26.5 to 30 | 3.3 |
| Plan and build | 30 | 28.0 | 30 to 58 | 28.2 |
| **Flex buffer (unscripted, lost first)** | 0 | 2.5 | 58 to 60.5 | |
| Showcase (8 children) | 23 | 22.0 | 60.5 to 82.5 | 21.8 |
| Talk time | 1 | 0 | dropped (see fixes) | 0.0 |
| Exit slip | 2 | 3.5 | 82.5 to 86 | 3.3 |
| Looking back + certificates | 2 | 4.0 | 86 to 90 | 4.1 |
| **Total** | 90 | **90.0** | | **87.3** (fast 76.6 / slow 98.0) |


## 7. How to check these numbers

Run one lesson with a stopwatch and a group of 6 to 8 and compare part by part with the "Needed" column; the five numbers most worth timing are (1) minutes from "show" to the answers click in the sneak-peek, (2) the warm-up game and quick questions together, (3) the Explore moves (materials, out, back), (4) the length of one check-together slide, and (5) how many Start-here questions a LOW, MIDDLE and HIGH child have written when the check slide for page 2 appears. Edit the `INP` and `FX` dictionaries in `docs/audit/timing_p6.py` and re-run (`--fixed` for the after-fix tables, `--stats` for sizes, `--json` for raw numbers).
