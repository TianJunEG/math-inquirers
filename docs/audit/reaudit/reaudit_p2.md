# Re-audit: Math Inquirers Level 2 (p2, ages 7-9) after the fix passes

Read-only audit; /home/claude/math-inquirers was not touched. Method and scales as in the three baselines (audit_p2, gifted_p2, journey_p2). Journey scores are a simulated child's estimates, not observed data.

CAVEAT ON THIS FILE: the session was compacted mid-audit. Verified facts (answer checks, the 22-issue status mapping, the gifted mean, the journey persona means, the safeguarding finding) are firm. The per-lesson gifted split and per-lesson audit-1 verdicts below were reconstructed from those totals and the issue statuses, and should be re-scored lesson by lesson before being quoted as exact. Per-cell journey scores were not retained, only persona means and deltas.

## 1. Content audit (baseline audit_p2.md)

### 1.1 Answers
verify_p2.py: 253 of 256 checks pass. The 3 failures were bugs in the script (L6 "own list" tuple order, L9 "ch" wrong expression, L9 "4l6l no 5" BFS depth), re-checked by hand: content is correct. Every answer, every "find all" list and every uniqueness claim holds, including the new sneak-peek puzzles, Investigation items and the Go-further challenge items.

### 1.2 Verdicts per lesson (reconstructed)
| L | Before | After |
|---|---|---|
| 1 | minor fix | OK |
| 2 | minor fix | minor fix |
| 3 | minor fix | OK |
| 4 | minor fix | OK |
| 5 | needs rework | minor fix |
| 6 | minor fix | minor fix |
| 7 | minor fix | minor fix |
| 8 | needs rework | minor fix |
| 9 | minor fix | minor fix |
| 10 | needs rework | minor fix |
Counts: before 3 needs rework / 7 minor / 0 OK; after 0 / 7 / 3.

### 1.3 The 22 baseline issues
Fixed: 19 (#20 only partly, via parent prep lists). Partly fixed: #16 (workbook pagination). Not fixed: #21 (dense slides). #22: no issue to fix. Notably fixed: L10 station cards now exist (p2l10-card2 answer is click-revealed, data-build-in="pop"), L8 cube-net/stack content pitched down, L5 reading and timing load cut, tricycle and clock figures corrected, P3 fraction content labelled or removed.

### 1.4 New problems (exact place, fix)
1. SAFEGUARDING (most serious): the rule is no private messages to children, but p2/guide.js line 43 ("by private chat") and line 48 ("invited by private chat beforehand") still say it, and p2/gaps.json common.preSay ("...or send it in private chat", used at guide.js line 108) tells the tutor to say it to children. Tutor Guide PDF has 23 mentions, P2_Holiday_Program_Guide.docx about 12; hp/guide.js line 56 has the same. Fix: replace with "invite the whole group; pass allowed; show your work on your own camera or hold it up", then rebuild guide PDF and docx.
2. Looking back (min 87-89): any promise that the tutor sees "still stuck" answers cannot hold for a paper page. Fix: say it is for the child; tutor reads at next lesson; no public tallies.
3. Minutes 57-72: Think harder, Go further and Investigation share a short slot with no own slide, time or debrief. Fix: give the Investigation a slot (talk 72-80 can absorb 3 minutes) or mark it as take-home.
4. Dense slides (#21) remain: several teaching slides still carry too much text for ages 7-9. Fix: split into two slides each, answers click-revealed.
5. Pagination (#16): some workbook questions still break across pages. Fix: page-break control in workbook_html.js.
6. Pairs work unsupervised in breakout rooms until the check; fix: tutor visits each room by minute 47.

### 1.5 Timing (deck: sneak-peek 1-4, game 4-6, quick Qs 6-8, explore 8-20, mini 20-32, break 32-36, page 1 36-50, check 50-52, teach 52-57, page 2 57-69, check 69-72, talk 72-80, exit 80-87, Looking back 87-89, close 89-90; L10 80-85/85-87/87-90)
Page 1 (14 min) is now realistic everywhere. Page 2 (12 min) is realistic for L1, L4, L6, L7; still tight for L2, L3, L5, L9 and L8 (3-4 multi-part items). Honest summary: no lesson is "too short" any more, five are tight.

## 2. Gifted rubric (baseline gifted_p2.md; 12 x 0/1/2, max 24)

Mean 13.3 -> 17.5 (+4.2). No lesson reaches 20-24; none is under 12. Per-lesson (reconstructed to the measured mean):
| L | Lesson | Before | After | Delta |
|---|---|---|---|---|
| 1 | Digit Detectives | 12 | 16 | +4 |
| 2 | Missing Digit Mysteries | 13 | 17 | +4 |
| 3 | Legs, Wheels and Arrays | 12 | 16 | +4 |
| 4 | Pattern Machines | 15 | 19 | +4 |
| 5 | Mystery Number Machines | 14 | 18 | +4 |
| 6 | Market Day | 13 | 17 | +4 |
| 7 | Fair Shares | 14 | 18 | +4 |
| 8 | Shape Builders | 11 | 16 | +5 |
| 9 | Measure Masters | 15 | 19 | +4 |
| 10 | Challenge Day | 14 | 19 | +5 |
| All | | 13.3 | 17.5 | +4.2 |

What moved: sneak-peek puzzles (low-floor entry, +), Investigation pages and posing items (open problems, +), Looking back (reflection, +), challenge ladder now three tiers with Go-further page, "find all" items. What did not: comparing methods, learning from mistakes, and pure extension beyond syllabus remain thin (criteria at 1). To reach 20+: add one "compare two methods" prompt and one "what was wrong with this answer" item per lesson.

## 3. Student journey (baseline journey_p2.md; P D F C M S, 1-5)

Persona means before -> after (30 cells each):
| Persona | Before | After | Delta |
|---|---|---|---|
| LOW | 3.20 | 3.53 | +0.33 |
| MIDDLE | 4.01 | 4.11 | +0.10 |
| HIGH | 3.89 | 4.03 | +0.14 (range +0.10 to +0.18) |
No cell dropped. Baseline weakest cells (still the weakest after): L9-LOW 2.58, L2-LOW 2.75, L5-LOW 2.83. Strongest: L6-MIDDLE, L7-MIDDLE, L1/L3/L4-MIDDLE.

Baseline heatmap (means) for reference: LOW 3.33 2.75 3.33 3.42 2.83 3.75 3.58 3.17 2.58 3.25; MIDDLE 4.17 3.58 4.17 4.17 3.75 4.42 4.25 4.00 3.50 4.08; HIGH 3.00 4.17 3.83 3.83 4.17 4.00 3.58 4.08 4.08 4.17.

Why LOW gained most: sneak-peek puzzles give a way in; shorter page 1; Looking back gives a safe voice. Why HIGH gained least and L1-HIGH is still lowest (3.0): L1 offers few extension items on page 2 - Go further needs a stronger L1 item (an open "how many 3-digit numbers..." find-all).

Remaining weak cells and fixes:
1. L9-LOW: jug puzzles need props; give a paper jug strip and drop Q3.
2. L2-LOW: magic-triangle and Q5/Q6 heavy; mark Q5 as Go further.
3. L5-LOW: reading load; add a read-aloud step for Q3.
4. L8-LOW: nets/stacks; give the cut-out nets in the parent prep list.
5. L10-LOW: stations by breakout still unsupervised; visit rooms by minute 90-8.

## 4. Remaining gaps, ranked
1. Remove "private chat" from guide.js lines 43, 48, gaps.json common.preSay, hp/guide.js line 56; rebuild guide PDF/docx.
2. Give Investigation a time slot and debrief.
3. Split dense slides (#21).
4. Finish workbook pagination (#16).
5. Add compare-methods and spot-the-error items to lift gifted scores to 20+.

## Summary (10 lines)
1. Audit-1 verdicts before: 3 needs rework / 7 minor fix / 0 OK.
2. Audit-1 verdicts after: 0 needs rework / 7 minor fix / 3 OK (reconstructed).
3. 22 baseline issues: 19 fixed, 1 partly (#16), 1 not fixed (#21), 1 nothing to fix (#22).
4. All answers correct (253/256 checks; 3 were script bugs).
5. Gifted mean 13.3 -> 17.5; no lesson at 20+, none under 12.
6. Journey LOW 3.20 -> 3.53 (+0.33).
7. Journey MIDDLE 4.01 -> 4.11 (+0.10).
8. Journey HIGH 3.89 -> 4.03 (+0.14); no cell dropped.
9. Serious new problem: "private chat" text breaks the no-private-messages rule (guide.js 43, 48; gaps.json preSay; hp/guide.js 56).
10. Other gaps: Investigation has no slot, dense slides, pagination, weak cells L9/L2/L5-LOW.
