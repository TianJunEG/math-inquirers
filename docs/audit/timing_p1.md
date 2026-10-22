# Lesson timing audit, Math Inquirers Level N=1 (Primary 1, ages 6-8)

Analysis only. Nothing in content, guides, decks, builds or outputs was edited. Helper: `docs/audit/timing_p1.py` (re-run with `python3 -I docs/audit/timing_p1.py`; it regenerates every table below from the repo). **All numbers are model estimates, not stopwatch timings.**

Question asked: when a tutor runs each of the 10 lessons live online from the slides and the script, does the lesson fit its 90 minutes?

## 1. Verdict

* **Five lessons land on 88-91 minutes with no slack (L1, L2, L3, L5, L8). Two run long (L9 +6, L10 +15). Three run short (L4 -11, L6 -8, L7 -4).** Likely range for a real class is about plus or minus 6 minutes around each estimate; with every assumption pushed the same way (all fast or all slow) it is plus or minus 11.
* Even the five "fitting" lessons only fit because the **end of the lesson is over-budgeted** (exit ticket scripted 8 min, needs about 5.3) and soaks up a **3 to 4 minute lag that builds up in the first 10 minutes** (warm-up + sneak-peek need 10 to 11.5 min of the 8 scripted; the opening needs 4.6 of 2 in Lesson 1). A tutor reaches "minute 10" at about minute 12 to 13 and "minute 40" at about minute 43 to 45 in those lessons.
* The plan has **no standing buffer**: the scripts add up to exactly 90 and the model total of the "good" lessons is 88.5-91. Any camera/tech glitch, one slow pair or one long answer overruns. A buffer is recommended (section 7).
* The new fixed items cost more than the scripts allow: the **sneak-peek (7-10) needs 4.6-4.9 min, not 3, in every lesson**; the **look-back (88-90) needs 2.6-2.7**; the **REC cue lines as written are 8-20 s each (2.2 min a lesson), not "under ten seconds"**; certificates in Lesson 10 need about 3 to 4 minutes that no part budgets.
* Three structural mismatches drive most of the long/short results: (a) worksheet pages whose question load does not match the minutes (L4 and L6 too light, L9 and L8 too heavy), (b) mini-lessons with 7 slides (L2, L3, L4, L9, L10) versus 4 slides (L6, L7) in the same 10 minutes, (c) Lesson 10's three-part design (cards + re-teach slides + puzzle writing) which fills about 105 minutes.

### Summary table (base case, as scripted today)


| Lesson | Slides (timed) | SAY words | Need (min) | vs 90 | Range fast-slow | Parts OVER | Parts LOOSE | Need after fixes (base; fast-slow) |
|---|---:|---:|---:|---:|---|---|---|---|
| 1 | 28 (25) | 265 | 89.4 | -0.6 | 78.4 - 101.1 | Opening | Worksheet | 82.9 (72.5 - 93.8) |
| 2 | 25 (22) | 235 | 91.0 | +1.0 | 79.6 - 102.7 | - | - | 86.6 (75.9 - 97.6) |
| 3 | 26 (23) | 192 | 89.2 | -0.8 | 78.2 - 100.6 | Mini-lesson | - | 85.7 (75.3 - 96.5) |
| 4 | 24 (21) | 228 | 79.4 | -10.6 | 70.0 - 89.2 | - | Worksheet | 83.3 (74.5 - 92.5) |
| 5 | 27 (24) | 223 | 88.8 | -1.2 | 77.7 - 100.5 | - | - | 84.2 (73.6 - 95.2) |
| 6 | 26 (21) | 232 | 82.2 | -7.8 | 72.1 - 92.7 | - | Mini-lesson, Worksheet | 85.5 (76.0 - 95.5) |
| 7 | 28 (22) | 226 | 86.2 | -3.8 | 75.6 - 97.3 | - | - | 84.2 (74.1 - 94.7) |
| 8 | 27 (24) | 250 | 88.5 | -1.5 | 77.8 - 99.7 | - | - | 85.6 (75.4 - 96.3) |
| 9 | 28 (25) | 188 | 96.2 | +6.2 | 84.2 - 108.7 | Worksheet | - | 86.4 (74.9 - 98.4) |
| 10 | 29 (26) | 331 | 105.0 | +15.0 | 93.0 - 117.6 | Explore, Mini-lesson, Talk time | - | 86.6 (76.2 - 97.5) |

## 2. Sources read and state of the repository

* Budgets: `hp/guide.js` `pushSeg()` calls. They are **identical for all 10 lessons**: 0-2 Opening, 2-7 Warm-up, 7-10 Sneak-peek, 10-25 Explore, 25-35 Mini-lesson, 35-40 Brain break, 40-72 Worksheet, 72-80 Talk time, 80-88 Exit ticket and closing, 88-90 Look-back. Lesson 10 does **not** vary in the segment list; it varies inside the parts (puzzle cards in Explore, Q9 in Talk time, certificates in the closing), and the slide MIN badges differ per lesson inside the worksheet block (for example L5 teaching slides at 40-44 and page 1 at 44-52).
* SAY/DO/ASK/IF STUCK lines: `hp/scripts.js`, `hp/lessons.js`, `deck/data.js`, `hp/gaps.json` (sneak-peek and Investigation), `hp/qbank.json`. REC cues: `levels/reccues.js` (10 cues per lesson, one per part).
* Slides: `split/l1..l10/project` (`deck.json` order, per-slide MIN badges, visible text, speaker notes). Workbook: `hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf` (read as text), cross-checked against `hp/workbook_html.js`.
* **The rebuilt tutor guide PDF (`hp/Math_Inquirers_P1_Tutor_Guide.pdf`, 74 pages) predates the REC edit in `hp/guide.js`** (no REC lines in it; it still says L10 cards "swap at minute 20" while the slide says 21). The model therefore uses `guide.js` plus `levels/reccues.js`. `hp/scripts.js` and `hp/lessons.js` were being edited by other passes while this audit ran; the tables are from the final re-run, and word counts may move by a few words if those files change again.

## 3. The model (identical for every level)

| Item | Assumption |
|---|---|
| Tutor speech | 120 words per minute including natural pauses (SAY lines, think-aloud, intro and rules, closing lines, REC cues) |
| Read-aloud | 110 words per minute (questions and slide text the tutor reads). For mini-lesson slides the tutor reads 70% of the visible text once, plus the scripted think-aloud; for worksheet teaching slides also 40% of the speaker-note words as explanation (those narrations exist only in the slide notes, not in `guide.js`) |
| Wait time | every question put to the group: 10 s think + 20 s to take one or two answers = **30 s**. A "your turn" slide: 45 s of work + 20 s of answers. "Hold up papers/boards" moment: **30 s** |
| Slide change online | **25 s** per slide (20-30 s) |
| Breakout rooms / handing out | **90 s** each way (60-120 s). Applied to Explore (in and out), the worksheet (one return), Talk time (60 s each way) |
| Worksheet start | **2 minutes** to find the page and get started |
| Greeting and camera checks | 4 s per child at the opening; 8 s per child to show the exit ticket to the camera |
| Camera and tech glitches | ignored; parts with no slack are flagged TIGHT |
| REC cue | actual word count of each cue at 120 wpm (35, 19, 30, 34, 22, 15, 39, 28, 19, 26 words = 267 words = **2.2 min a lesson**, 8-20 s per cue). The guide says "under ten seconds"; at that limit the cost would be 1.6 min |
| Child work | judged from the task, per lesson (see `EXPLORE_ACT` and `ITEMS` in the helper): a Core item 1.5-3 min for a middle child aged 6-8 (0.5-1 min for one-line "read the graph" items, 5 min for trial-and-error items like the magic triangle), writing a sentence 1-1.5 min. LOW child = 1.7 times the middle child, HIGH child = 0.65 times. Think harder item 4-6 min for a middle child |
| Flags | difference = scripted minus need. **OVER**: need exceeds scripted by 2 or more. **TIGHT**: need exceeds scripted by under 2, or slack under 1. **OK**: slack 1 to under 3. **LOOSE**: slack 3 or more |
| New fixed items | sneak-peek (7-10), look-back (88-90) and the REC cues are inside every lesson table; Lesson 10 certificates and the `end` slide are inside its Exit row |
| Not modelled | the "teach so the recording works" rules (read every question aloud, repeat every child's answer, read every answer aloud). A tutor who obeys all of them adds about 2.5 to 4 minutes a lesson, mostly in the worksheet and mini-lesson |

Columns in the tables: **REC** = cue line; **Speak** = SAY lines and read-aloud; **Wait** = question cycles, hold-ups, answer-taking, greeting, camera checks; **Activity** = child work, game or break time; **Transit** = slide changes and breakout moves. **Need** = the sum. "Clock end" = scripted end of the part / the minute at which it actually ends when every earlier part runs at its estimated need.

Where the average lesson's 89.5 minutes go: child activity 31.5, waiting for answers 24.2, transitions 17.1 (about 24 slide changes at 25 s is 10 min, plus about 6.5 min of breakout moves), tutor speech 14.5, REC cues 2.2.

### How many items each child finishes (worksheet "Start here")

The workbook has 3 to 10 numbered Start-here questions per lesson, not counting Think harder (T1-T4/5), Go further (C1-C3) and the Investigation, which are not timed. Page times come from the slide badges (page 1 = badge minus 3 for start-up and reading Q1-Q2 when the page slide starts at 40, otherwise minus 1; page 2 = badge minus 1). "Required" excludes the items marked "if you have time".


| Lesson | Required items (Start here) | Page 1 need / have | Page 2 need / have | LOW finishes | MIDDLE finishes | HIGH finishes | HIGH spare min (about Think harder items) |
|---|---:|---|---|---|---|---|---|
| 1 | 5 | 6.5 / 10 | 7.0 / 9 | 3 of 5 | 5 of 5 | 5 of 5 | 10.2 (3) |
| 2 | 6 | 6.2 / 11 | 10.5 / 9 | 4 of 6 | 5 of 6 | 6 of 6 | 9.1 (2) |
| 3 | 10 | 4.3 / 9 | 9.0 / 9 | 7 of 10 | 10 of 10 | 10 of 10 | 9.4 (2) |
| 4 | 3 | 6.0 / 11 | 5.0 / 11 | 3 of 3 | 3 of 3 | 3 of 3 | 14.8 (3) |
| 5 | 5 | 5.1 / 7 | 10.5 / 9 | 2 of 5 | 4 of 5 | 5 of 5 | 5.9 (1) |
| 6 | 4 | 9.0 / 9 | 5.5 / 9 | 2 of 4 | 4 of 4 | 4 of 4 | 8.6 (2) |
| 7 | 6 | 5.5 / 9 | 7.5 / 9 | 3 of 6 | 6 of 6 | 6 of 6 | 9.6 (2) |
| 8 | 4 | 8.0 / 9 | 5.5 / 9 | 2 of 4 | 4 of 4 | 4 of 4 | 9.2 (2) |
| 9 | 5 | 10.0 / 7 | 9.0 / 9 | 2 of 5 | 4 of 5 | 5 of 5 | 3.7 (0) |
| 10 | 8 | 8.5 / 10 | 6.3 / 9 | 6 of 8 | 8 of 8 | 8 of 8 | 9.4 (2) |

## 4. Lesson by lesson, as scripted today

Part names in brackets give the number of slides in the part. "Clock end" shows the scripted end of the part and the estimated minute at which it really ends.

#### Lesson 1: Count with the Frog

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (4) | 2 | 0.3 | 2.1 | 0.5 | 0.0 | 1.7 | **4.6** | -2.6 | OVER | 2 / 4.6 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 1.1 | 2.5 | 2.0 | 0.8 | **6.6** | -1.6 | TIGHT | 7 / 11.2 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.2 | 1.0 | 2.0 | 0.4 | **4.8** | -1.8 | TIGHT | 10 / 16.0 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.5 | 3.5 | 6.5 | 3.8 | **15.6** | -0.6 | TIGHT | 25 / 31.6 |
| Mini-lesson (6) | 10 | 0.2 | 3.1 | 4.2 | 0.0 | 2.5 | **9.9** | 0.1 | TIGHT | 35 / 41.5 |
| Brain break (1) | 5 | 0.1 | 0.3 | 1.5 | 1.0 | 0.9 | **3.9** | 1.1 | OK | 40 / 45.4 |
| Worksheet (Start here) (6) | 32 | 0.3 | 3.6 | 7.5 | 13.5 | 4.0 | **28.9** | 3.1 | LOOSE | 72 / 74.3 |
| Talk time (1) | 8 | 0.2 | 0.4 | 2.2 | 2.0 | 2.4 | **7.3** | 0.7 | TIGHT | 80 / 81.6 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.7 | 1.6 | 2.0 | 0.7 | **5.1** | 2.9 | OK | 88 / 86.8 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 89.4 |
| **Whole lesson** | **90** | 2.2 | 15.0 | 24.5 | 30.0 | 17.7 | **89.4** | **0.6** | TIGHT | |

Workbook (Start here, required items, MID child): page 1 needs 6.5 min of 10 available; page 2 needs 7.0 min of 9 available. Finished in the scripted time: LOW 3/5, MIDDLE 5/5, HIGH 5/5. Spare work minutes: MID 5.5, HIGH 10.2 (about 3 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 265; all lines in scripts.js: 418; slides: 28 (25 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** 28 slides, three of which (`cover`, `routine`, `rules`) exist only in Lesson 1. Opening: four slides at 25 s, the 79-word routine table and the four rules read together, the recording notice, the hook and 8 greetings need 4.6 min for a 2-minute slot. Warm-up: the stomp game (33 numbers counted) plus five quick questions (about 37 s each) gives 6.6 for 5. Sneak-peek needs 4.8. Explore: the child has to **cut out the two rows of the 0-50 strip from the kit and tape them end to end** (about 2.5 min at this age) before hopping 12 + 10 landings; 15.6 for 15. The tutor reaches minute 40 at about 45. The worksheet then has slack (page 1 needs 6.5 of 10 min, page 2 needs 7.0 of 9), so the lesson ends at about 89.4: it fits only because of the loose worksheet and exit. LOW child: 3 of 5 questions.

#### Lesson 2: Number Bond Inquiry

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.9 | 0.5 | 0.0 | 0.4 | **2.1** | -0.1 | TIGHT | 2 / 2.1 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 0.9 | 2.5 | 2.0 | 0.8 | **6.4** | -1.4 | TIGHT | 7 / 8.5 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.2 | 1.0 | 2.0 | 0.4 | **4.9** | -1.9 | TIGHT | 10 / 13.3 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.2 | 3.5 | 5.5 | 3.8 | **14.3** | 0.7 | TIGHT | 25 / 27.7 |
| Mini-lesson (7) | 10 | 0.2 | 3.1 | 5.2 | 0.0 | 2.9 | **11.5** | -1.5 | TIGHT | 35 / 39.1 |
| Brain break (1) | 5 | 0.1 | 0.4 | 1.5 | 1.0 | 0.9 | **3.9** | 1.1 | OK | 40 / 43.0 |
| Worksheet (Start here) (5) | 32 | 0.3 | 3.4 | 8.5 | 16.7 | 3.6 | **32.5** | -0.5 | TIGHT | 72 / 75.5 |
| Talk time (1) | 8 | 0.2 | 0.4 | 2.2 | 2.0 | 2.4 | **7.3** | 0.7 | TIGHT | 80 / 82.8 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.5 | 1.6 | 2.5 | 0.7 | **5.4** | 2.6 | OK | 88 / 88.3 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 91.0 |
| **Whole lesson** | **90** | 2.2 | 13.0 | 26.6 | 32.7 | 16.5 | **91.0** | **-1.0** | TIGHT | |

Workbook (Start here, required items, MID child): page 1 needs 6.2 min of 11 available; page 2 needs 10.5 min of 9 available. Finished in the scripted time: LOW 4/5, MIDDLE 5/6, HIGH 6/6. Spare work minutes: MID 5.8, HIGH 9.1 (about 2 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 235; all lines in scripts.js: 388; slides: 25 (22 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** Mini-lesson is 3 teach + 3 "your turn" slides + key (7 slides): the three "your turn" slides each hold three whiteboard sub-questions in one scripted minute (20 s each), and 11.4 min are needed for 10. Worksheet page 2 has Q4 (5 sub-items including an explanation), **Q5 the magic triangle (trial and error, about 5 min for a 6-year-old)** and Q6 (guess and check, 2.5 min): the middle child needs 10.5 min for the 9 available, so Q6 is the one cut. Page 1 (Q1-Q3, 6.2 min) has 11 available. The tutor reaches minute 40 at about 43 and the lesson ends at 90.9.

#### Lesson 3: Let’s Plan the Fruit Party

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.8 | 0.5 | 0.0 | 0.4 | **2.0** | 0.0 | TIGHT | 2 / 2.0 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 0.9 | 2.0 | 2.0 | 0.8 | **5.9** | -0.9 | TIGHT | 7 / 7.9 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.0 | 1.0 | 2.0 | 0.4 | **4.7** | -1.7 | TIGHT | 10 / 12.6 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.1 | 3.5 | 5.5 | 3.8 | **14.2** | 0.8 | TIGHT | 25 / 26.8 |
| Mini-lesson (7) | 10 | 0.2 | 3.4 | 6.2 | 0.0 | 2.9 | **12.7** | -2.7 | OVER | 35 / 39.5 |
| Brain break (1) | 5 | 0.1 | 0.3 | 1.5 | 1.5 | 0.9 | **4.4** | 0.6 | TIGHT | 40 / 43.9 |
| Worksheet (Start here) (6) | 32 | 0.3 | 2.9 | 9.2 | 13.3 | 4.0 | **29.7** | 2.3 | OK | 72 / 73.6 |
| Talk time (1) | 8 | 0.2 | 0.5 | 2.2 | 2.0 | 2.4 | **7.4** | 0.6 | TIGHT | 80 / 81.0 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.5 | 1.6 | 2.5 | 0.7 | **5.5** | 2.5 | OK | 88 / 86.5 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 89.2 |
| **Whole lesson** | **90** | 2.2 | 12.5 | 27.8 | 29.8 | 16.9 | **89.2** | **0.8** | TIGHT | |

Workbook (Start here, required items, MID child): page 1 needs 4.3 min of 9 available; page 2 needs 9.0 min of 9 available. Finished in the scripted time: LOW 7/8, MIDDLE 10/10, HIGH 10/10. Spare work minutes: MID 4.7, HIGH 9.4 (about 2 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 192; all lines in scripts.js: 333; slides: 26 (23 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** Mini-lesson **7 slides, three "your turn" slides with three sub-questions each**, the third one (missing row, unknown key) is a genuine thinking item: 12.7 min for 10 (OVER). The worksheet is lopsided: page 1 (Q1-Q5 are one-liners: most, fewest, how many more, same, altogether) needs only 4.3 of 9 min, page 2 needs 9.0 of 9 because **Part B asks the group to vote and tally online** (about 3.5 min for 8 children) and Q6-Q9 are all explanations. Note that the slide for page 1 lists Q1-Q5 but the printed workbook page 1 holds Q1-Q4 (Q5 is on page 2). Total 89.1.

#### Lesson 4: Pattern Inquiry

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.7 | 0.5 | 0.0 | 0.4 | **2.0** | 0.0 | TIGHT | 2 / 2.0 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 0.8 | 2.0 | 1.5 | 0.8 | **5.3** | -0.3 | TIGHT | 7 / 7.3 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.0 | 1.0 | 2.0 | 0.4 | **4.7** | -1.7 | TIGHT | 10 / 11.9 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.2 | 3.5 | 5.0 | 3.8 | **13.8** | 1.2 | OK | 25 / 25.7 |
| Mini-lesson (7) | 10 | 0.2 | 3.8 | 4.2 | 0.0 | 2.9 | **11.0** | -1.0 | TIGHT | 35 / 36.8 |
| Brain break (1) | 5 | 0.1 | 0.3 | 1.5 | 1.5 | 0.9 | **4.4** | 0.6 | TIGHT | 40 / 41.2 |
| Worksheet (Start here) (4) | 32 | 0.3 | 1.9 | 6.3 | 11.0 | 3.2 | **22.8** | 9.2 | LOOSE | 72 / 63.9 |
| Talk time (1) | 8 | 0.2 | 0.4 | 2.2 | 2.0 | 2.4 | **7.3** | 0.7 | TIGHT | 80 / 71.2 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.5 | 1.6 | 2.5 | 0.7 | **5.5** | 2.5 | OK | 88 / 76.7 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 79.4 |
| **Whole lesson** | **90** | 2.2 | 11.8 | 22.9 | 26.5 | 16.1 | **79.4** | **10.6** | LOOSE | |

Workbook (Start here, required items, MID child): page 1 needs 6.0 min of 11 available; page 2 needs 5.0 min of 11 available. Finished in the scripted time: LOW 3/3, MIDDLE 3/3, HIGH 3/3. Spare work minutes: MID 11.0, HIGH 14.8 (about 3 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 228; all lines in scripts.js: 389; slides: 24 (21 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** The worksheet has **only three required questions** (Q1 draw two shapes, Q2 four sub-parts including the 30th place, Q3 table of 10 and four sub-parts; Q4 is "if you have time"). A middle child needs 11.0 min of work in a 32-minute block (22.8 min in total with talk and checking); every child type finishes all three and the HIGH child has 14.8 spare minutes. The rest of the lesson is on target (clock at minute 40 is 41.1), so the lesson ends at **79.4: about 10.6 minutes of dead time**, all in the worksheet. Mini-lesson is 7 slides and needs 11.0 for 10.

#### Lesson 5: Mystery Number

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.7 | 0.5 | 0.0 | 0.4 | **1.9** | 0.1 | TIGHT | 2 / 1.9 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 1.2 | 2.0 | 1.5 | 0.8 | **5.7** | -0.7 | TIGHT | 7 / 7.6 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.1 | 1.0 | 2.0 | 0.4 | **4.7** | -1.7 | TIGHT | 10 / 12.3 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.2 | 3.5 | 5.0 | 3.8 | **13.8** | 1.2 | OK | 25 / 26.2 |
| Mini-lesson (6) | 10 | 0.2 | 2.9 | 4.2 | 0.0 | 2.5 | **9.7** | 0.3 | TIGHT | 35 / 35.9 |
| Brain break (1) | 5 | 0.1 | 0.4 | 1.5 | 1.5 | 0.9 | **4.4** | 0.6 | TIGHT | 40 / 40.3 |
| Worksheet (Start here) (8) | 32 | 0.3 | 4.3 | 8.0 | 15.6 | 4.8 | **33.0** | -1.0 | TIGHT | 72 / 73.3 |
| Talk time (1) | 8 | 0.2 | 0.4 | 2.2 | 2.0 | 2.4 | **7.3** | 0.7 | TIGHT | 80 / 80.7 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.5 | 1.6 | 2.5 | 0.7 | **5.5** | 2.5 | OK | 88 / 86.1 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 88.8 |
| **Whole lesson** | **90** | 2.2 | 13.7 | 24.5 | 31.1 | 17.3 | **88.8** | **1.2** | OK | |

Workbook (Start here, required items, MID child): page 1 needs 5.1 min of 7 available; page 2 needs 10.5 min of 9 available. Finished in the scripted time: LOW 2/4, MIDDLE 4/5, HIGH 5/5. Spare work minutes: MID 2.9, HIGH 5.9 (about 1 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 223; all lines in scripts.js: 359; slides: 27 (24 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** Worksheet block has 8 slides (4 teaching slides, two "teach" pairs before each page) so the tutor talks for about 4.2 min and clicks 8 times; page 2 (Q3 bars: 8 + 13 + 7 = 28 boxes to colour, Q4 two queue drawings, **Q5 "make your own story"**) needs 10.5 of 9 min: the middle child does not reach Q5, the LOW child does 2 of 5 questions in the whole block. Everything else is on target; total 88.8.

#### Lesson 6: Coin Combos

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.8 | 0.5 | 0.0 | 0.4 | **2.1** | -0.1 | TIGHT | 2 / 2.1 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 1.0 | 2.0 | 2.5 | 0.8 | **6.5** | -1.5 | TIGHT | 7 / 8.6 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.1 | 1.0 | 2.0 | 0.4 | **4.8** | -1.8 | TIGHT | 10 / 13.3 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.1 | 3.5 | 5.5 | 3.8 | **14.2** | 0.8 | TIGHT | 25 / 27.5 |
| Mini-lesson (4) | 10 | 0.2 | 2.5 | 1.6 | 0.0 | 1.7 | **5.9** | 4.1 | LOOSE | 35 / 33.4 |
| Brain break (1) | 5 | 0.1 | 0.4 | 1.5 | 1.5 | 0.9 | **4.4** | 0.6 | TIGHT | 40 / 37.8 |
| Worksheet (Start here) (7) | 32 | 0.3 | 3.9 | 5.8 | 14.5 | 4.4 | **29.0** | 3.0 | LOOSE | 72 / 66.8 |
| Talk time (1) | 8 | 0.2 | 0.3 | 2.2 | 2.0 | 2.4 | **7.2** | 0.8 | TIGHT | 80 / 74.1 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.5 | 1.6 | 2.5 | 0.7 | **5.5** | 2.5 | OK | 88 / 79.5 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 82.2 |
| **Whole lesson** | **90** | 2.2 | 12.7 | 19.8 | 31.5 | 16.1 | **82.2** | **7.8** | LOOSE | |

Workbook (Start here, required items, MID child): page 1 needs 9.0 min of 9 available; page 2 needs 5.5 min of 9 available. Finished in the scripted time: LOW 2/4, MIDDLE 4/4, HIGH 4/4. Spare work minutes: MID 3.5, HIGH 8.6 (about 2 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 232; all lines in scripts.js: 364; slides: 26 (21 on the timed path, 5 untimed choice/Think harder/Go further slides).

**Walk-through.** Mini-lesson has **only 4 slides** (teach, worked example, one "your turn", key) and needs 5.9 min for 10 (LOOSE, 4.1 min of dead time). Worksheet page 1 is the opposite: Q1 (a five-row coin table plus three explanation parts) and Q2 (find all four ways to make 25c) need 9.0 of the 9 available, while page 2 needs 5.5 of 9. Total 82.1; the lesson ends about 8 minutes early. LOW child: 2 of 4.

#### Lesson 7: Shape Safari

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.7 | 0.5 | 0.0 | 0.4 | **1.9** | 0.1 | TIGHT | 2 / 1.9 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 0.8 | 2.0 | 2.5 | 0.8 | **6.3** | -1.3 | TIGHT | 7 / 8.2 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.0 | 1.0 | 2.0 | 0.4 | **4.6** | -1.6 | TIGHT | 10 / 12.9 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.1 | 3.5 | 6.0 | 3.8 | **14.7** | 0.3 | TIGHT | 25 / 27.6 |
| Mini-lesson (4) | 10 | 0.2 | 2.8 | 2.6 | 0.0 | 1.7 | **7.3** | 2.7 | OK | 35 / 34.9 |
| Brain break (1) | 5 | 0.1 | 0.3 | 1.5 | 1.5 | 0.9 | **4.4** | 0.6 | TIGHT | 40 / 39.2 |
| Worksheet (Start here) (8) | 32 | 0.3 | 5.4 | 7.8 | 13.0 | 4.8 | **31.3** | 0.7 | TIGHT | 72 / 70.6 |
| Talk time (1) | 8 | 0.2 | 0.5 | 2.2 | 2.0 | 2.4 | **7.4** | 0.6 | TIGHT | 80 / 78.0 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.6 | 1.6 | 2.5 | 0.7 | **5.5** | 2.5 | OK | 88 / 83.5 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 86.2 |
| **Whole lesson** | **90** | 2.2 | 14.3 | 22.8 | 30.5 | 16.5 | **86.2** | **3.8** | LOOSE | |

Workbook (Start here, required items, MID child): page 1 needs 5.5 min of 9 available; page 2 needs 7.5 min of 9 available. Finished in the scripted time: LOW 3/5, MIDDLE 6/6, HIGH 6/6. Spare work minutes: MID 5.0, HIGH 9.6 (about 2 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 226; all lines in scripts.js: 378; slides: 28 (22 on the timed path, 6 untimed choice/Think harder/Go further slides).

**Walk-through.** Mini-lesson has 4 slides and needs 7.3 for 10 (OK, 2.7 spare). Explore (fold a paper square corner to corner and cut) needs 14.7 for 15. Worksheet needs 31.3 for 32 with 8 slides (4 teaching slides, 447 words of narration live only in the speaker notes). **Six untimed slides sit between the page-2 check and the Talk time slide** (`stretch`, `we2`, `try2`, `we3`, `challenge`, `chwalk`): a tutor who clicks through in deck order wastes 2.5 min, so the guide should say "skip to Talk time". Total 86.2.

#### Lesson 8: Logic Lab

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.8 | 0.5 | 0.0 | 0.4 | **2.0** | 0.0 | TIGHT | 2 / 2.0 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 0.9 | 1.5 | 2.5 | 0.8 | **5.9** | -0.9 | TIGHT | 7 / 7.9 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.1 | 1.0 | 2.0 | 0.4 | **4.8** | -1.8 | TIGHT | 10 / 12.6 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.1 | 3.5 | 5.5 | 3.8 | **14.2** | 0.8 | TIGHT | 25 / 26.8 |
| Mini-lesson (6) | 10 | 0.2 | 3.7 | 2.7 | 0.0 | 2.5 | **9.1** | 0.9 | TIGHT | 35 / 35.9 |
| Brain break (1) | 5 | 0.1 | 0.4 | 1.5 | 1.0 | 0.9 | **3.9** | 1.1 | OK | 40 / 39.8 |
| Worksheet (Start here) (8) | 32 | 0.3 | 6.5 | 8.0 | 13.5 | 4.8 | **33.2** | -1.2 | TIGHT | 72 / 73.0 |
| Talk time (1) | 8 | 0.2 | 0.4 | 2.2 | 2.0 | 2.4 | **7.3** | 0.7 | TIGHT | 80 / 80.3 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.6 | 1.6 | 2.5 | 0.7 | **5.5** | 2.5 | OK | 88 / 85.8 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 88.5 |
| **Whole lesson** | **90** | 2.2 | 16.4 | 22.5 | 30.0 | 17.3 | **88.5** | **1.5** | OK | |

Workbook (Start here, required items, MID child): page 1 needs 8.0 min of 9 available; page 2 needs 5.5 min of 9 available. Finished in the scripted time: LOW 2/4, MIDDLE 4/4, HIGH 4/4. Spare work minutes: MID 4.5, HIGH 9.2 (about 2 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 250; all lines in scripts.js: 371; slides: 27 (24 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** Worksheet block has 8 slides including **four teaching slides** (ladder, line-ups, number riddles, odd one out) with 462 words of narration only in the notes: 6.6 min of tutor speech in the block. Page 1 (Q1 three ordering puzzles, Q2 two-loop picture) needs 8.0 of 9; page 2 (Q3 logic grid, Q4 line-up) 5.5 of 9, but two of the four teaching slides serve only the optional Q5/Q6 and Think harder T5. Worksheet needs 33.2 for 32 (TIGHT -1.2); total 88.5.

#### Lesson 9: Measure It!

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.7 | 0.5 | 0.0 | 0.4 | **1.9** | 0.1 | TIGHT | 2 / 1.9 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 0.8 | 1.5 | 2.0 | 0.8 | **5.3** | -0.3 | TIGHT | 7 / 7.3 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 1.2 | 1.0 | 2.0 | 0.4 | **4.9** | -1.9 | TIGHT | 10 / 12.1 |
| Explore (pairs, objects) (2) | 15 | 0.3 | 1.1 | 3.5 | 8.0 | 3.8 | **16.7** | -1.7 | TIGHT | 25 / 28.9 |
| Mini-lesson (7) | 10 | 0.2 | 3.8 | 3.2 | 0.0 | 2.9 | **10.1** | -0.1 | TIGHT | 35 / 38.9 |
| Brain break (1) | 5 | 0.1 | 0.4 | 1.5 | 2.0 | 0.9 | **4.9** | 0.1 | TIGHT | 40 / 43.9 |
| Worksheet (Start here) (8) | 32 | 0.3 | 5.6 | 7.0 | 19.0 | 4.8 | **36.8** | -4.8 | OVER | 72 / 80.6 |
| Talk time (1) | 8 | 0.2 | 0.4 | 2.2 | 2.0 | 2.4 | **7.3** | 0.7 | TIGHT | 80 / 88.0 |
| Exit ticket + closing (1) | 8 | 0.2 | 0.6 | 1.6 | 2.5 | 0.7 | **5.5** | 2.5 | OK | 88 / 93.5 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 96.2 |
| **Whole lesson** | **90** | 2.2 | 15.7 | 22.0 | 38.5 | 17.7 | **96.2** | **-6.2** | OVER | |

Workbook (Start here, required items, MID child): page 1 needs 10.0 min of 7 available; page 2 needs 9.0 min of 9 available. Finished in the scripted time: LOW 2/4, MIDDLE 4/5, HIGH 5/5. Spare work minutes: MID 4.0, HIGH 3.7 (about 0 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 188; all lines in scripts.js: 319; slides: 28 (25 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** Explore (cut a cube strip from the kit, estimate and measure pencil, book, shoe, then hand spans with a partner over video) needs 16.7 for 15. Then **worksheet Q2 asks the child to measure the same pencil, book and shoe again** with a guess column: 7 min, so page 1 needs 10.0 of the 7 minutes the slides give it (ws1 40-50 minus start-up). Page 2 has 9.0 of 9 and the teaching slides add 5.5 min of speech and 8 clicks. Worksheet 36.7 for 32 (**OVER 4.7**); the tutor reaches minute 72 at about 80 and ends at **96.1**. LOW child: 2 of 5. (Side note: the teaching slides use 1 clip = 3 erasers, the printed Q4 uses 1 clip = 2 erasers; the slide notes already warn the tutor.)

#### Lesson 10: Challenge Day

| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| Opening (1) | 2 | 0.3 | 0.7 | 0.5 | 0.0 | 0.4 | **1.9** | 0.1 | TIGHT | 2 / 1.9 |
| Warm-up game + quick questions (2) | 5 | 0.2 | 2.1 | 3.6 | 0.0 | 0.8 | **6.7** | -1.7 | TIGHT | 7 / 8.6 |
| Sneak-peek puzzles (1) | 3 | 0.2 | 0.9 | 1.0 | 2.0 | 0.4 | **4.6** | -1.6 | TIGHT | 10 / 13.2 |
| Explore (pairs, objects) (3) | 15 | 0.3 | 2.0 | 5.0 | 8.0 | 5.2 | **20.5** | -5.5 | OVER | 25 / 33.7 |
| Mini-lesson (7) | 10 | 0.2 | 4.5 | 5.2 | 0.0 | 2.9 | **12.7** | -2.7 | OVER | 35 / 46.5 |
| Brain break (1) | 5 | 0.1 | 0.4 | 1.5 | 1.0 | 0.9 | **3.9** | 1.1 | OK | 40 / 50.4 |
| Worksheet (Start here) (7) | 32 | 0.3 | 3.8 | 7.7 | 14.8 | 4.4 | **31.0** | 1.0 | TIGHT | 72 / 81.4 |
| Talk time (1) | 8 | 0.2 | 0.6 | 2.2 | 6.0 | 2.4 | **11.5** | -3.5 | OVER | 80 / 92.9 |
| Exit ticket + closing (+ certificates) (2) | 8 | 0.2 | 4.5 | 1.6 | 2.0 | 1.1 | **9.4** | -1.4 | TIGHT | 88 / 102.3 |
| Look-back (1) | 2 | 0.2 | 1.1 | 0.0 | 1.0 | 0.4 | **2.7** | -0.7 | TIGHT | 90 / 105.0 |
| **Whole lesson** | **90** | 2.2 | 20.5 | 28.3 | 34.8 | 19.1 | **105.0** | **-15.0** | OVER | |

Workbook (Start here, required items, MID child): page 1 needs 8.5 min of 10 available; page 2 needs 6.3 min of 9 available. Finished in the scripted time: LOW 6/8, MIDDLE 8/8, HIGH 8/8. Spare work minutes: MID 4.2, HIGH 9.4 (about 2 Think harder item(s) for a HIGH child).

SAY words (hook, warm-up intro, predict, think-aloud, talk, close): 331; all lines in scripts.js: 430; slides: 29 (26 on the timed path, 3 untimed choice/Think harder/Go further slides).

**Walk-through.** Largest lesson: **29 slides, 331 SAY words (mean of the others 233)**, and four things at once. (1) Warm-up: a 5-question whiteboard round (slide warm1) **and** 5 quick questions (warm2) = ten questions in 7 minutes. (2) Explore: scripted as 10 min on one card + 4 min on a swapped card, but the slide also puts the debrief at 21-25 and online needs a card per breakout room, a swap and four 30-second pair reports: 20.5 for 15. A middle child solves any one card in 2.5-4 min, so the 10-minute round is long for MID but short for LOW (Coins card needs trial and error). (3) Mini-lesson: 7 slides re-teaching "draw it / list it / make a table" (12.7 for 10). (4) Worksheet block re-teaches picture graphs, triangle counting and length on three teaching slides (4 min) before pages that revisit L3, L7 and L9. **Q9 (write a puzzle for a friend) has been moved to Talk time**, which then needs 11.5 (pairs write 3.5, swap and solve 2.5, 2-minute pair talk, volunteers) for 8. Exit: certificates and the `end` slide ("ask each child to name one puzzle they enjoyed", about 8 x 27 s) take the closing to 9.4 for 8. The tutor reaches minute 72 at about 81 and finishes at **104.9**, i.e. the lesson cannot be run as written.


### Running clock

(as scripted today): estimated minute at which each scripted mark is actually reached

| Lesson | min 10 | min 25 | min 40 | min 72 | min 80 | min 88 | end |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 16.0 | 31.6 | 45.4 | 74.3 | 81.6 | 86.8 | 89.4 |
| 2 | 13.3 | 27.7 | 43.0 | 75.5 | 82.8 | 88.3 | 91.0 |
| 3 | 12.6 | 26.8 | 43.9 | 73.6 | 81.0 | 86.5 | 89.2 |
| 4 | 11.9 | 25.7 | 41.2 | 63.9 | 71.2 | 76.7 | 79.4 |
| 5 | 12.3 | 26.2 | 40.3 | 73.3 | 80.7 | 86.1 | 88.8 |
| 6 | 13.3 | 27.5 | 37.8 | 66.8 | 74.1 | 79.5 | 82.2 |
| 7 | 12.9 | 27.6 | 39.2 | 70.6 | 78.0 | 83.5 | 86.2 |
| 8 | 12.6 | 26.8 | 39.8 | 73.0 | 80.3 | 85.8 | 88.5 |
| 9 | 12.1 | 28.9 | 43.9 | 80.6 | 88.0 | 93.5 | 96.2 |
| 10 | 13.2 | 33.7 | 50.4 | 81.4 | 92.9 | 102.3 | 105.0 |

## 5. Fixes and the proposed 90-minute plans

Each plan lists the new budget per part (sum 90, including the standing buffer), the estimated need after the fixes, and the new clock. Most parts show TIGHT after the fixes on purpose: the budgets are the estimated need rounded to a whole minute, and the only deliberate slack is the 2-minute standing buffer at the end plus the 2 to 5 minutes by which the base-case need stays under 90. The estimates after fixes use the same model; the universal fixes (section 6: shorter REC cues, questions 1-3 in the warm-up, one camera moment in the sneak-peek) are included in every "new need".

### Lesson 1

**Fixes for Lesson 1** (OVER: Opening; Explore tight; Worksheet LOOSE)
1. **Opening 0-4 (was 0-2).** Skip the `cover` slide (the title slide repeats it) and show the `routine` slide for 30 s, naming only the four phases (Warm-up, Explore, Teach, Worksheet) instead of reading the table; keep the four inquirer rules read together (22 words). Saves about 1.3 min, leaving 3.2 min of need for 4 scripted.
2. **Explore: parents cut and tape the 0-50 strip before the lesson.** Add one sentence to the "one week before" mail and to the L1 online set-up in `hp/lessons.js` ("cut out the two rows of the number strip and tape them end to end"). Saves 2.5 min of cutting in Explore; Explore budget 14, need 13.0.
3. **Worksheet 42-72 (30 min, was 40-72).** Page 1 needs 6.5 min of work; give it 10 min (42-52), check page 1 52-54, teaching 54-58, page 2 58-68, check 68-72. No question is cut and the answers are unchanged.
4. Universal fixes (section 6): warm-up 6, sneak-peek 4, break 4, talk 7, exit 6, look-back 3, buffer 2.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 4.6 | 3.2 | 4 | 0.8 | TIGHT | 0-4 |
| Warm-up | 5 | 6.6 | 5.3 | 6 | 0.7 | TIGHT | 4-10 |
| Sneak-peek | 3 | 4.8 | 3.9 | 4 | 0.1 | TIGHT | 10-14 |
| Explore | 15 | 15.6 | 13.0 | 14 | 1.0 | OK | 14-28 |
| Mini-lesson | 10 | 9.9 | 9.9 | 10 | 0.1 | TIGHT | 28-38 |
| Brain break | 5 | 3.9 | 3.9 | 4 | 0.1 | TIGHT | 38-42 |
| Worksheet | 32 | 28.9 | 28.8 | 30 | 1.2 | OK | 42-72 |
| Talk time | 8 | 7.3 | 7.2 | 7 | -0.2 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.1 | 5.1 | 6 | 0.9 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **89.4** | **82.9** | **90** | **5.1** (buffer 2 not counted) | | |

### Lesson 2

**Fixes for Lesson 2** (Mini-lesson OVER-ish at 11.4; worksheet page 2 overloaded)
1. **Drop slide `l2-try3`** ("balance it": 7+4=9+__, 3+8=__+6, true/false 4+4=8+1). Its three items repeat worksheet Q4 (5+3=4+__ and so on), and `l2-teach3` already works one example with all steps. Saves 1.8 min: Mini-lesson need 9.6, budget 10.
2. **Re-split the worksheet (still 40-72):** page 1 40-50 (10 min; MID needs 6.2 + start-up), check 50-52, teaching 52-54, **page 2 54-66 (12 min instead of 10)**, check + stretch 66-72. Page 2 needs 10.5 min (Q4 3, Q5 5, Q6 2.5), so the middle child now finishes Q6; Q5b and Q6b stay "if you have time". Do not remove the magic triangle; keep the hint.
3. Universal fixes.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 2.1 | 2.0 | 2 | 0.0 | TIGHT | 0-2 |
| Warm-up | 5 | 6.4 | 5.2 | 6 | 0.8 | TIGHT | 2-8 |
| Sneak-peek | 3 | 4.9 | 3.9 | 4 | 0.1 | TIGHT | 8-12 |
| Explore | 15 | 14.3 | 14.2 | 14 | -0.2 | TIGHT | 12-26 |
| Mini-lesson | 10 | 11.5 | 9.6 | 10 | 0.4 | TIGHT | 26-36 |
| Brain break | 5 | 3.9 | 3.9 | 4 | 0.1 | TIGHT | 36-40 |
| Worksheet | 32 | 32.5 | 32.3 | 32 | -0.3 | TIGHT | 40-72 |
| Talk time | 8 | 7.3 | 7.2 | 7 | -0.2 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.4 | 5.4 | 6 | 0.6 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **91.0** | **86.6** | **90** | **1.4** (buffer 2 not counted) | | |

### Lesson 3

**Fixes for Lesson 3** (Mini-lesson OVER; worksheet pages unbalanced)
1. **Merge `l3-try3` into `l3-teach3`** as a single "your turn" item (a): "15 children voted. Red 6, blue 4, the rest chose green. How many chose green? (5)". Move (b) "the key is lost, cats have 3 pictures = 6 children" and (c) to the Think harder slide / take-home, where they belong (they need the key idea, so they are Think harder, not Core). Also cut the third think-aloud quote in `scripts.js` L3. Saves 1.4 min: Mini-lesson need 11.3 -> **budget 11** (explore stays 14, worksheet 31).
2. **Worksheet 41-72 (31 min):** page 1 (Q1-Q5, 4.3 min of work) gets 9 min: 41-50 including the 2-minute start-up and reading Q1-Q2; check 50-52; teaching 52-55 (`teachwho`, `teachtally`); page 2 55-67 (12 min, it holds Part B vote and tally, Q6-Q9, 9.0 min); check + stretch 67-72. Correct the slide `l3-ws1` text: it lists Q5 on page 1 but the printed workbook page 1 ends at Q4.
3. Universal fixes.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 2.0 | 1.9 | 2 | 0.1 | TIGHT | 0-2 |
| Warm-up | 5 | 5.9 | 5.3 | 6 | 0.7 | TIGHT | 2-8 |
| Sneak-peek | 3 | 4.7 | 3.8 | 4 | 0.2 | TIGHT | 8-12 |
| Explore | 15 | 14.2 | 14.1 | 14 | -0.1 | TIGHT | 12-26 |
| Mini-lesson | 10 | 12.7 | 11.3 | 11 | -0.3 | TIGHT | 26-37 |
| Brain break | 5 | 4.4 | 4.4 | 4 | -0.4 | TIGHT | 37-41 |
| Worksheet | 32 | 29.7 | 29.6 | 31 | 1.4 | OK | 41-72 |
| Talk time | 8 | 7.4 | 7.3 | 7 | -0.3 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.5 | 5.5 | 6 | 0.5 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **89.2** | **85.7** | **90** | **2.3** (buffer 2 not counted) | | |

### Lesson 4

**Fixes for Lesson 4** (Worksheet LOOSE by 9.2 min; Mini-lesson 11.0 for 10)
1. **Add four Core items to Start here** from `hp/qbank.json` L4 `core` (same tier, answers unchanged): core 1 (circle, square, triangle ... 10th = circle, 1.5 min), core 3 (red, red, blue ... 8th = red, 1.0), core 5 (cat, dog, dog ... 12th = dog, 1.5) and core 4 (A, B, C, D ... 11th = C, write the letters in a row, 2.0). Put core 1 and 3 on page 1 after Q1, core 5 and 4 on page 2 before Q3. That is +6 min of work: worksheet need 28.6 for 32, and the HIGH child still has about 8 spare minutes for Think harder T1-T2. Update the printed workbook, the slide `ws1`/`ws2` question lists and the answer key in `hp/lessons.js`.
2. Mini-lesson is 7 slides (two teach + two worked + two "your turn" + key) and needs 11.0: give it **11 (26-37)** and the worksheet 31 (41-72); no content is cut, because the worksheet now has the slack.
3. Universal fixes.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 2.0 | 1.9 | 2 | 0.1 | TIGHT | 0-2 |
| Warm-up | 5 | 5.3 | 4.7 | 6 | 1.3 | OK | 2-8 |
| Sneak-peek | 3 | 4.7 | 3.7 | 4 | 0.3 | TIGHT | 8-12 |
| Explore | 15 | 13.8 | 13.7 | 14 | 0.3 | TIGHT | 12-26 |
| Mini-lesson | 10 | 11.0 | 11.0 | 11 | -0.0 | TIGHT | 26-37 |
| Brain break | 5 | 4.4 | 4.4 | 4 | -0.4 | TIGHT | 37-41 |
| Worksheet | 32 | 22.8 | 28.6 | 31 | 2.4 | OK | 41-72 |
| Talk time | 8 | 7.3 | 7.2 | 7 | -0.2 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.5 | 5.5 | 6 | 0.5 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **79.4** | **83.3** | **90** | **4.7** (buffer 2 not counted) | | |

### Lesson 5

**Fixes for Lesson 5** (Worksheet 33.0 for 32; page 2 needs 10.5 of 9)
1. **Mark Q5 ("make your own mystery number story") "if you have time"**, like Q3d and Q4 in other lessons. The middle child no longer misses a required item and the tutor can say "pass is fine". Answers and tiers unchanged. Worksheet need 30.3 for 32.
2. In `l5-teachq1` and `l5-teachq2` show the "your turn" only once. Optional.
3. Universal fixes.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 1.9 | 1.8 | 2 | 0.2 | TIGHT | 0-2 |
| Warm-up | 5 | 5.7 | 5.0 | 6 | 1.0 | OK | 2-8 |
| Sneak-peek | 3 | 4.7 | 3.8 | 4 | 0.2 | TIGHT | 8-12 |
| Explore | 15 | 13.8 | 13.7 | 14 | 0.3 | TIGHT | 12-26 |
| Mini-lesson | 10 | 9.7 | 9.7 | 10 | 0.3 | TIGHT | 26-36 |
| Brain break | 5 | 4.4 | 4.4 | 4 | -0.4 | TIGHT | 36-40 |
| Worksheet | 32 | 33.0 | 30.4 | 32 | 1.6 | OK | 40-72 |
| Talk time | 8 | 7.3 | 7.3 | 7 | -0.3 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.5 | 5.5 | 6 | 0.5 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **88.8** | **84.2** | **90** | **3.8** (buffer 2 not counted) | | |

### Lesson 6

**Fixes for Lesson 6** (Mini-lesson LOOSE by 4.1 min; Worksheet LOOSE by 3.1)
1. **Add two "your turn" slides to the Mini-lesson** (Question Bank L6 core items, answers unchanged): (a) core 4 "ways to make 20c using only 10c and 5c (3 ways)", core 1 "pay 15c with two coins", core 2 "pay 40c with two coins"; (b) core 5 and 6 "how much money does Ali have (20c+10c+5c = 35c)" and "two 20c and one 5c (45c)". This brings the Mini-lesson to 9.3 min for a budget of 10 and fills the dead time with exactly the skill Q1-Q3 need.
2. **Add core 5 and 6 (count the money) to page 2** of Start here (+2 min). Worksheet need 30.8 for 32.
3. Universal fixes. Explore stays 14.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 2.1 | 1.9 | 2 | 0.1 | TIGHT | 0-2 |
| Warm-up | 5 | 6.5 | 5.9 | 6 | 0.1 | TIGHT | 2-8 |
| Sneak-peek | 3 | 4.8 | 3.8 | 4 | 0.2 | TIGHT | 8-12 |
| Explore | 15 | 14.2 | 14.1 | 14 | -0.1 | TIGHT | 12-26 |
| Mini-lesson | 10 | 5.9 | 9.3 | 10 | 0.7 | TIGHT | 26-36 |
| Brain break | 5 | 4.4 | 4.4 | 4 | -0.4 | TIGHT | 36-40 |
| Worksheet | 32 | 29.0 | 30.8 | 32 | 1.2 | OK | 40-72 |
| Talk time | 8 | 7.2 | 7.2 | 7 | -0.2 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.5 | 5.5 | 6 | 0.5 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **82.2** | **85.5** | **90** | **2.5** (buffer 2 not counted) | | |

### Lesson 7

**Fixes for Lesson 7** (whole lesson 3.8 min under; nothing OVER)
1. **Re-budget instead of cut:** Mini-lesson 8 (need 7.2), Explore 16 (need 14.6, gives the fold-and-cut time a margin; folding with scissors online is the slowest explore in the level), Worksheet 32 unchanged.
2. Add to the guide's Worksheet DO line: "After page 2 is checked, go straight to the Talk time slide. The Think harder, Go further and Investigation slides (6 untimed slides) are shown only on request."
3. Universal fixes.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 1.9 | 1.8 | 2 | 0.2 | TIGHT | 0-2 |
| Warm-up | 5 | 6.3 | 5.7 | 6 | 0.3 | TIGHT | 2-8 |
| Sneak-peek | 3 | 4.6 | 3.7 | 4 | 0.3 | TIGHT | 8-12 |
| Explore | 15 | 14.7 | 14.6 | 16 | 1.4 | OK | 12-28 |
| Mini-lesson | 10 | 7.3 | 7.3 | 8 | 0.7 | TIGHT | 28-36 |
| Brain break | 5 | 4.4 | 4.4 | 4 | -0.4 | TIGHT | 36-40 |
| Worksheet | 32 | 31.3 | 31.2 | 32 | 0.8 | TIGHT | 40-72 |
| Talk time | 8 | 7.4 | 7.3 | 7 | -0.3 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.5 | 5.5 | 6 | 0.5 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **86.2** | **84.2** | **90** | **3.8** (buffer 2 not counted) | | |

### Lesson 8

**Fixes for Lesson 8** (Worksheet 33.2 for 32 is TIGHT/OVER)
1. **Show `l8-teachriddle` and `l8-teachodd` with all steps revealed, 30 s each.** They only serve the optional Q5/Q6 and Think harder T5, and each carries 107-117 words of notes. Saves 1.4 min: worksheet need 31.7 for 32.
2. Page 1 (Q1 three ordering puzzles + Q2 two-loop picture, 8.0 min) and page 2 (Q3 pets grid 3.0, Q4 line-up 2.5) are well matched; keep the split.
3. Universal fixes.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 2.0 | 1.9 | 2 | 0.1 | TIGHT | 0-2 |
| Warm-up | 5 | 5.9 | 5.9 | 6 | 0.1 | TIGHT | 2-8 |
| Sneak-peek | 3 | 4.8 | 3.9 | 4 | 0.1 | TIGHT | 8-12 |
| Explore | 15 | 14.2 | 14.1 | 14 | -0.1 | TIGHT | 12-26 |
| Mini-lesson | 10 | 9.1 | 9.0 | 10 | 1.0 | TIGHT | 26-36 |
| Brain break | 5 | 3.9 | 3.9 | 4 | 0.1 | TIGHT | 36-40 |
| Worksheet | 32 | 33.2 | 31.6 | 32 | 0.4 | TIGHT | 40-72 |
| Talk time | 8 | 7.3 | 7.2 | 7 | -0.2 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.5 | 5.5 | 6 | 0.5 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **88.5** | **85.6** | **90** | **2.4** (buffer 2 not counted) | | |

### Lesson 9

**Fixes for Lesson 9** (Worksheet OVER by 4.7; Explore 16.7 for 15; lesson ends at 96)
1. **Q2: copy the numbers from Explore.** Children already estimated and measured pencil, book and shoe in Explore. Change the Q2 instruction (workbook and slides) to "Use what you measured in Explore. Write your guess, your measure and how far off you were"; the "My choice" row is the only new measurement. Saves about 4 min on page 1 and removes the duplicate measuring. Answers are unchanged (open measurements).
2. **Parents cut out the cube strips before the lesson** ("print the cube strip page and cut out Strip A", added to the L9 materials mail). Explore need 14.6, budget 15.
3. **Drop slide `l9-tryconv`** (it serves only the optional Q4 and Think harder T3/T4, which still have `teachconv` and `teachunit`). Saves 1.7 min. Worksheet need 30.7, budget **31 (41-72)**.
4. Brain break: "giant steps" in place, not across the room (saves 0.5 min).
5. Correct the teaching/printed mismatch (1 clip = 3 erasers on slides, 2 on the page) so that Q4 does not cost an explanation.
6. Universal fixes.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 1.9 | 1.8 | 2 | 0.2 | TIGHT | 0-2 |
| Warm-up | 5 | 5.3 | 5.3 | 6 | 0.7 | TIGHT | 2-8 |
| Sneak-peek | 3 | 4.9 | 4.0 | 4 | 0.0 | TIGHT | 8-12 |
| Explore | 15 | 16.7 | 14.6 | 15 | 0.4 | TIGHT | 12-27 |
| Mini-lesson | 10 | 10.1 | 10.0 | 10 | -0.0 | TIGHT | 27-37 |
| Brain break | 5 | 4.9 | 4.4 | 4 | -0.4 | TIGHT | 37-41 |
| Worksheet | 32 | 36.8 | 30.8 | 31 | 0.2 | TIGHT | 41-72 |
| Talk time | 8 | 7.3 | 7.3 | 7 | -0.3 | TIGHT | 72-79 |
| Exit ticket | 8 | 5.5 | 5.5 | 6 | 0.5 | TIGHT | 79-85 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 85-88 |
| Standing buffer | 0 | | | 2 | | | 88-90 |
| **Total** | 90 | **96.2** | **86.4** | **90** | **1.6** (buffer 2 not counted) | | |

### Lesson 10

**Fixes for Lesson 10** (OVER by 15 min: Explore, Mini-lesson, Talk time, and Warm-up/Exit tight)
1. **Warm-up 2-6 (4 min): drop slide `l10-warm2`.** The five whiteboard questions on `l10-warm1` already come from the nine lessons; the second set of quick questions repeats the idea. Need 3.1.
2. **Explore 10-28 (18 min).** Round 1 on one card **6 min** (not 10: a middle child solves any card in 2.5-4 min; a LOW child may need up to 7 on the Coins card, and a pair that is still stuck keeps its card in round 2), swap 1 min, round 2 **4 min**, then ONE debrief question (Q3 "what helped you when you were stuck?") and 20-second pair reports. Pairs read their own card; the tutor does not read all four aloud. Need 17.3.
3. **Mini-lesson 28-37 (9 min): drop the two "your turn" slides `l10-try1` and `l10-try2`.** The Explore cards are the practice; keep teach1, we1, we2, we3 and key. Need 9.1.
4. **Worksheet 41-71 (30 min): skip the three re-teach slides `l10-teachgraph`, `l10-teachtri`, `l10-teachlen`** (they re-teach L3, L7 and L9; keep them for "I need a reminder" only) and **put Q9 (write a puzzle for a friend) back on page 2**, which the time freed (about 3.6 min) pays for. Need 28.9.
5. **Talk time 71-79 (8 min)** = swap puzzles, solve, 2-minute pair talk, volunteers. Need 7.9.
6. **Exit and closing 79-87 (8 min) with certificates:** certificate line said once to the group, then 10 s per child with one specific thing they did well; the `end` slide's "name one puzzle you enjoyed" is asked as a thumbs-up question or only of volunteers. Need 8.2.
7. Look-back 87-90 (3). **No standing buffer in Lesson 10**; the slack is in the worksheet (30 for 28.9). This is the one lesson where the tutor must follow the shortened plan.

| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |
|---|---:|---:|---:|---:|---:|---|---|
| Opening | 2 | 1.9 | 1.8 | 2 | 0.2 | TIGHT | 0-2 |
| Warm-up | 5 | 6.7 | 3.1 | 4 | 0.9 | TIGHT | 2-6 |
| Sneak-peek | 3 | 4.6 | 3.7 | 4 | 0.3 | TIGHT | 6-10 |
| Explore | 15 | 20.5 | 17.3 | 18 | 0.7 | TIGHT | 10-28 |
| Mini-lesson | 10 | 12.7 | 9.1 | 9 | -0.1 | TIGHT | 28-37 |
| Brain break | 5 | 3.9 | 3.9 | 4 | 0.1 | TIGHT | 37-41 |
| Worksheet | 32 | 31.0 | 29.0 | 30 | 1.0 | OK | 41-71 |
| Talk time | 8 | 11.5 | 7.9 | 8 | 0.1 | TIGHT | 71-79 |
| Exit ticket | 8 | 9.4 | 8.2 | 8 | -0.2 | TIGHT | 79-87 |
| Look-back | 2 | 2.7 | 2.6 | 3 | 0.4 | TIGHT | 87-90 |
| Standing buffer | 0 | | | 0 | | | 90-90 |
| **Total** | 90 | **105.0** | **86.6** | **90** | **3.4** (buffer 0 not counted) | | |

## 6. Level-wide fixes (apply to all ten lessons, then the lesson-specific ones)

**U1. Re-budget the parts to the model, keeping the worksheet anchored at 40-72.** The parts before the worksheet take 40 min, the parts after take 18:

| Part | Today | Proposed | Why (middle estimate across L2-L9) |
|---|---|---|---|
| Opening | 0-2 | 0-2 (L1: 0-4) | need 1.8-2.1; L1 needs 3.2 after trimming |
| Warm-up game + quick questions | 2-7 | **2-8** | need 5.3-6.6 as written, 4.7-5.9 with questions 1-3 only |
| Sneak-peek puzzles | 7-10 | **8-12** | need 4.6-4.9 as written, 3.7-4.0 after U3 |
| Explore | 10-25 | **12-26** (14) | need 13.7-14.7 |
| Mini-lesson | 25-35 | **26-36** (10) | need 9-11 after lesson fixes |
| Brain break | 35-40 | **36-40** (4) | need 3.9-4.9 |
| Worksheet | 40-72 | 40-72 (32) | unchanged except L1, L3, L9, L10 |
| Talk time | 72-80 | **72-79** (7) | need 7.2-7.4 |
| Exit ticket + closing | 80-88 | **79-85** (6) | need 5.1-5.5 |
| Look-back | 88-90 | **85-88** (3) | need 2.6-2.7 |
| Standing buffer / goodbye | none | **88-90** (2) | see section 7 |

Edit points: the ten `pushSeg()` calls in `hp/guide.js` (and the "minute 22", "minutes 5 to 7", "minutes 33 to 35", "minute 40" DO lines), the MIN badges on about 10 slides per deck, the `routine` slide table, and the time plan in each `*-title` slide's notes. REC cue durations ("about N minutes") are computed from the seg ranges, so they update by themselves.

**U2. Warm-up quick questions: ask questions 1-3 of the slide as the default** (the slide notes already allow it), and ask 4-5 only if the clock at minute 6 is on time. Saves about 0.6 min per question dropped.

**U3. Sneak-peek in 4 minutes with ONE camera moment.** Say a single shorter line: "Two sneak-peek puzzles: ideas we have not learnt yet. A guess is a great start, and I do not know is welcome. Nobody is marked." (26 words instead of 70). Children try both on their own paper (about a minute each), then **everyone holds the paper to the camera once, after the second question** (30 s instead of two hold-ups), then click the two answers and say "Lots of us had a different idea, and that is fine." Saves 0.9 min and keeps the privacy rule (nothing is shown to the group).

**U4. Shorten the REC cue lines to 10 seconds (about 20 words).** The longest are the worksheet cue (39 words, 20 s), opening (35, 18 s), explore (34, 17 s), sneak-peek (30, 15 s) and talk time (28, 14 s). Suggested replacements: opening "Recording: get a pencil, paper, your workbook and materials, then press play."; sneak-peek "Recording: pause. Try both puzzles on your own paper. Guessing is fine."; explore "Recording: pause, get your objects and try this. Press play when you have an answer."; worksheet "Recording: pause and do your workbook, page 1 first. Press play for each checking part."; talk "Recording: pause. Tell someone at home your answer and why."; close "Recording: well done! Show your journal to a grown-up." Saves 0.6 min a lesson.

**U5. Pre-lesson preparation by parents** (cutting is the clearest Explore time sink in L1 and L9): add to the "one week before" mail "cut out and tape the number strip (L1)" and "cut out the cube strip (L9)", and to every lesson's mail a one-line "have your materials on the table before we start". Not needed for L2-L8 if counters are loose.

**U6. A skip list printed in the guide** (section 7).

## 7. Standing buffer

**Yes: a standing buffer of 2 minutes at the end (88-90) in every lesson, plus a declared skip list.** Evidence: the base model puts L1, L2, L3, L5 and L8 at 88.5 to 90.9 minutes with each early part running 1 to 2 minutes over, and the corner cases (all assumptions slow) are 100 to 103. After the fixes the lessons need 83 to 87 minutes in the base case, i.e. 3 to 7 minutes under 90 (that includes the 2-minute buffer), which covers the base case but **not** the slow case (92 to 98): the tutor still needs permission to drop things. Proposed rules, printed once in the guide and on the `routine` slide's notes:

1. **Clock checks** at minute 12 (end of sneak-peek), minute 40 (start of worksheet) and minute 72. If more than 2 minutes behind at 40, apply the skip list; do not shorten the worksheet below 28.
2. **Skip list, in order:** quick questions 4-5; Q "if you have time" items; the last "your turn" slide of the Mini-lesson; the second `expAsk` debrief question; the Talk time pair-talk (go straight to volunteers); only then the exit-ticket reveal.
3. **Never** drop: the camera/privacy hold-up, the look-back (pass is allowed) or the "no pressure/pass" lines.
4. L10 has no buffer: use the shortened plan in its fix list.

## 8. Other findings noticed while walking the lessons

* **Slide count / words:** L10 is the outlier (29 slides, 331 SAY words, 7-slide mini-lesson, 3 re-teach slides). L1 28 slides (3 only used in L1). L7 and L9 28 slides. L4 has the fewest (24). Mini-lessons run 4 slides in L6 and L7 but 6-7 slides in L1, L2, L3, L4, L5, L8, L9, L10 (about 85 seconds a slide including each question cycle). Worksheet blocks have 4 to 8 slides, and **100-460 words of narration for the worksheet teaching slides exist only in the speaker notes** (L7 447, L8 462, L9 346), so a tutor who follows `guide.js` alone has no script for them.
* **Untimed choice slides in deck order:** after the page-2 check every deck has 3-6 slides (Think harder, Go further, walk-through, extra worked examples in L6/L7) before Talk time. The guide should say "skip to Talk time".
* **Online breakout moves** cost about 6.5 minutes a lesson (Explore in/out 3, worksheet return 1.5, Talk time 2). If the platform cannot run breakouts smoothly, those are the first minutes to lose; a "pairs in the main room with mics off, partner talk by chat/gesture" variant is not modelled.
* **LOW children:** in L1, L2, L5, L6, L7, L8, L9 a LOW child finishes 2 to 4 of 4 to 6 required Start-here questions (40-60%), and in L2, L5 and L9 the middle child misses the last question. The pass option and the "after question 3 you may choose" rule keep this from being a pressure point, but the check-together slides run at fixed minutes, so LOW children are checked on work they have not finished. The model's fixes do not change this; they stop it getting worse.
* **Workbook/slide mismatches affecting timing:** L3 `ws1` lists Q5 on page 1 (printed page 1 ends at Q4); L9 teaching slides use 1 clip = 3 erasers while printed Q4 uses 2; L10 PDF guide says swap at minute 20, the slide says 21.
* **The new fixed items:** sneak-peek 4.6-4.9 min needed (3 scripted); look-back 2.6-2.7 (2 scripted); REC cues 2.2 min a lesson (not budgeted); certificates + `end` slide in L10 3 to 4 min (not budgeted).

## 9. Limits of this audit

Estimates, not timings: no tutor was timed. The largest uncertainties are (i) minutes per workbook question for a 6-year-old (the dictionaries `ITEMS` and `EXPLORE_ACT` in `timing_p1.py` are explicit, change them and re-run), (ii) how long online breakout moves really take, (iii) how much of each teaching slide a tutor reads, and (iv) the 30-second answer-taking cycle, which a talkative group can double. Corner cases (all assumptions fast or all slow together) are shown in the summary table; the likely range is plus or minus 6 minutes. Camera and tech glitches, late arrivals and parent questions are ignored: they all add to the time.


## 10. Re-running the helper

`python3 -I docs/audit/timing_p1.py` prints every table in this document (base case), the child completion table, the running clock and the after-fix plans. The fast and slow scenarios are `SCENARIOS` in the same file.
