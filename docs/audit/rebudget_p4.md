# Level 4 (P4) re-budget pass: what was applied

Source of the plan: `docs/audit/timing_p4.md` (section 6, per-lesson tables). Plan of record in code: `rebuild/p4_budget.py`, which writes `p4/budget.json` and is read by `rebuild/p4_fix.py` (title-slide Time plan, every slide pill is checked against it at build time) and `p4/guide.js` (segment times, routine table, lesson scripts). Model re-run: `python3 docs/audit/rebudget_p4.py` (uses `timing_p4.py` unchanged).

## 1. Old -> new budget (minutes; every lesson adds to 90)

Old for every lesson: opening 1, sneak-peek 3, warm-up 4, explore 10, mini-lesson 12, brain break 4, worksheet 46 (16 + 3 + 5 + 18 + 4), talk 5, exit 3 (L10: 2), looking back 2 (L10: certificates 1).

| L | Open | Sneak | Warm-up | Explore | Mini | Break | Worksheet (a + b + c + d + e) | Talk | Exit | Looking back |
|--:|--:|--:|--:|--:|--:|--:|---|--:|--:|--:|
| 1 | 1.5 | 5.5 | 5.5 | 12 | 8 | 3.5 | 43.5 (18 + 2.5 + 3.5 + 17 + 2.5) | 3.5 | 3.5 | 3.5 |
| 2 | 1.5 | 5 | 5 | 13 | 5 | 3.5 | 47 (17.5 + 2 + 4 + 20 + 3.5) | 3.5 | 3 | 3.5 |
| 3 | 1.5 | 5 | 5 | 12 | 5 | 4 | 48 (16.5 + 2 + 2.5 + 23 + 4) | 3.5 | 2.5 | 3.5 |
| 4 | 1.5 | 5 | 5 | 12.5 | 8 | 3.5 | 44 (17.5 + 2.5 + 3.5 + 18 + 2.5) | 4 | 3 | 3.5 |
| 5 | 1.5 | 5 | 5 | 13.5 | 8 | 3.5 | 43 (18.5 + 2 + 5 + 15.5 + 2) | 3.5 | 3.5 | 3.5 |
| 6 | 1.5 | 5 | 5 | 11.5 | 7.5 | 3.5 | 46 (17.5 + 1.5 + 2.5 + 22 + 2.5) | 3.5 | 3 | 3.5 |
| 7 | 1.5 | 5 | 5 | 12 | 5.5 | 3.5 | 46 (16 + 2 + 3.5 + 21 + 3.5) | 4 | 4 | 3.5 |
| 8 | 1.5 | 5 | 5 | 14 | 8.5 | 3.5 | 42.5 (19 + 2.5 + 3.5 + 15 + 2.5) | 4 | 2.5 | 3.5 |
| 9 | 1.5 | 5 | 5 | 14.5 | 6.5 | 3.5 | 44 (18 + 2 + 4 + 17.5 + 2.5) | 3.5 | 3 | 3.5 |
| 10 | 1.5 | 5 | 5 | 13 | 6.5 | 3.5 | 41.5 (16.5 + 1.5 + 3.5 + 17 + 3) | 3.5 | 4.5 | 3.5 (+ certificates and goodbye 2.5) |

Standing buffer (last stretch of the page-2 solo block, spent before the choice questions, never from checks, exit ticket or Looking back): L1 3, L2 3, L3 3, L4 2, L5 2.5, L6 3, L7 3, L8 2.5, L9 2, L10 2 minutes. It is named in the title-slide Time plan, the ws2 speaker note, the guide worksheet segment and `budget.json` (`buffer`).

Slide time pills were recomputed for every slide (half-minute windows, contiguous, 0 to 90); `p4_fix.check_times()` fails the build if a pill, or a slide in the plan, is missing or different.

## 2. What was cut or moved

All lessons
- Sneak-peek: 60 s for puzzle 1, 90 s for puzzle 2, ONE hold-up for both papers; the optional "can anyone find another way?" removed (L1 content, slide notes).
- Warm-up: game about 90 s, three quick questions (Q1 to Q3 kept). Q4 and Q5 moved to the Weekly Dose: kept in the content as `deck.warmWeekly`, printed in the guide as "Moved to the Weekly Dose", and appended as "Also try: ..." (with answers) to the tip in `p4/parent_side.json`, so the Weekly Dose PDF carries them (still 25 pages). Warm-up speaker-note ASKs deleted.
- Explore: two debrief questions (third dropped; the answer to the dropped one is in the speaker note, in L1 it is the first mini-lesson slide). Explore described as the only breakout of the first half with a 60 s auto-close; "Pencils down" minute is now computed (explore end minus the debrief).
- Mini-lesson: one "your turn" slide kept (the last one: L1, L4, L5, L6, L8, L9, L10), none in L2, L3, L7; at most three speaker-note ASKs. Dropped slides removed from deck order and the generator code: L1 try1; L2 try1, try2; L3 try1, try2, try3, trytrick; L4 try1, trycompare; L5 try1; L6 try1, tryclock; L7 try1, try2, we3, try3; L8 try1, try3; L9 try1; L10 try1. L3 teachchain moved to the early-finisher (take-home) group instead of being deleted. L7: 4th think-aloud paragraph removed with we3.
- Brain break: 3.5 min (L3 4), water and toilet first, slide reordered, clock check at its end ("more than 1.5 minutes behind: skip the next optional item").
- Worksheet teaching: ASKs limited to three or fewer per block (L1 only on teachriddle and teachtest; L4 only on teachcompare2).
- Talk time: pair talk 1 minute, no breakout; the second discussion question moved to the Weekly Dose (`script.talkWeekly` and `talkWeeklyAns`; L10 keeps both lines because the second is an invitation, not a question). `talkAns` now answers the asked question only.
- Looking back: first SAY paragraph is one sentence; model line and "still stuck" line kept; the child's 2 minutes untouched.
- Optional / early-finisher slides (stretch, challenge, chdiag, chwalk, L3 teachchain): pill "Optional, if you finish early", no clock time. The kept "your turn" slide keeps its window and "OPTIONAL".

Lesson specifics
- L2, L3, L7, L10: Q3 is the first solo question (still printed on page 1). Page-1 line and page-2 "Aim for" line reworded; ws1ans no longer shows Q3, ws2ans does (answers unchanged).
- L6: "after question 3" fixed to "after question 2" (page 1 ends at Q2; same for L9); Q1 pair task (each child measures two angles, then checks the partner's two); Q5, Q6 promoted to "aim for" and a 4-minute Think harder slot before the check, plus buffer (guide plan lines, printed cap line).
- L7: Q1 pair-split (partner A two rectangles, partner B big minus missing piece); exit ticket budget 4.
- L8: families cut the six squares before the lesson (explore note).
- L10: whole-group close (segment "Certificates and goodbye" 87.5-90, with REC cue; `script.farewell`; end-slide note; guide Ending-the-program bullet); explore shows 2 live cards (A, B) and C, D greyed as "take-home"; Q1b starred "take-home"; exit ticket 4.5.
- L3 Q7 starred ("take-home choice") because its teaching slide moved to take-home.

Workbook: only the page-1 choice line, the page-2 "Aim for" line and the star on L10 Q1b and L3 Q7 changed. Every answer and key is unchanged; tiers, pass option and private-paper rules untouched.

## 3. New totals vs the audit's prediction (typical tutor, minutes needed out of 90)

Model: `docs/audit/rebudget_p4.py` (fix switches as in the audit, run on the rebuilt decks).

| L | Audit predicted (best / typ / slow) | Now (best / typ / slow) | Cushion (typ) |
|--:|---|---|--:|
| 1 | 74.7 / 85.8 / 89.8 | 74.6 / 85.8 / 89.8 | 4.2 |
| 2 | 76.8 / 85.8 / 89.8 | 77.4 / 86.4 / 90.4 | 3.6 |
| 3 | 77.5 / 85.4 / 89.2 | 78.3 / 86.2 / 90.1 | 3.8 |
| 4 | 72.4 / 82.6 / 86.7 | 72.5 / 82.1 / 86.2 | 7.9 |
| 5 | 73.5 / 84.9 / 89.0 | 73.5 / 83.7 / 87.8 | 6.3 |
| 6 | 67.7 / 76.2 / 80.2 | 67.7 / 75.6 / 79.6 | 14.4 |
| 7 | 76.4 / 85.9 / 89.8 | 76.7 / 85.6 / 89.6 | 4.4 |
| 8 | 73.2 / 83.5 / 87.5 | 73.2 / 83.6 / 87.5 | 6.4 |
| 9 | 73.3 / 83.3 / 87.3 | 73.4 / 82.8 / 86.8 | 7.2 |
| 10 | 77.3 / 86.6 / 90.8 | 78.0 / 87.3 / 91.5 | 2.7 |

All ten fit at the typical setting. Differences from the prediction come from the page-2 check (WS-e) in L2, L3, L7, L10, which now also carries Q3 (needs 0.5 to 0.7 min more than budgeted; the audit assumed 0.5) and from small text changes. L10 slow is 0.7 over, as the audit expected 0.8 over. L6 keeps a large cushion (14.4) beyond the promoted Q5 and Q6 and the Think harder slot, as the audit proposed.

## 4. Page counts (after rebuild)

Student workbook 64 (unchanged; per lesson L1 6, L2 6, L3 5, L4 5, L5 5, L6 6, L7 5, L8 5, L9 5; first pass overflowed in L7 and L10 and the new lines were shortened). Tutor guide 99 -> 102. Weekly Dose 25, Question Bank 28, Weekly Email Pack 12, Free Taster 5, What Learners Get 1, Scheme of Work 2 (all unchanged). `rebuild/preview.py`: no slide overflows in any of the 10 decks. Slides per deck now 27, 26, 25, 28, 28, 26, 25, 26, 26, 28.

## 5. Not applied, or applied differently

- "Move L4 teachtimes and teachgrow into the idle mini-lesson": those slide ids are P2 L4 (timing_p2.md), not P4. P4 L4 has no idle mini-lesson (audit budget 8); applied the P4 audit plan instead.
- Warm-up budget: the audit text F3 says 5 min; the L1 table says 5.5 (and sneak 5.5). Followed the L1 table.
- REC cue minutes: `levels/reccues.js` reads whole minutes from the first `a-b` in the time string, so a half-minute range would be read wrongly. `p4/guide.js` passes a whole-minute range to `REC.cue` (part length rounded), and overrides the sneak-peek cue to 3 and Looking back to 2 (what the watching child actually pauses for). reccues.js itself was not touched.
- F12 (shorten the four longest REC cue lines and the recording notice) needs `levels/reccues.js`: not done, for the lead.
- L5: the audit keeps ASKs on teach1, we2 and the first ASK of we3; I removed the we2 and we3 ASKs (fewer than the allowed three).
- Warm-up game "one short round": only L5 had an explicit 3 rounds (changed to one); L2 mentions two rounds in the notes, now "stop at about 90 seconds".
- L3 warm-up questions: the guide list differed from the slide (4 800 / 6 vs 48 / 6); the guide now matches the slide, and the two moved questions are the slide's.

## 6. Notes for the lead (shared files, not edited)

- `tutor/build_data.py` PARTS: should read `p4/budget.json` (`parts` = title/start/end; `optional_slides`; extra keys `worksheet_blocks`, `buffer`, `slide_windows`). Part titles are the ones it already uses, plus "Certificates and goodbye" in L10.
- `tutor/build_data.py` detects the slide pill with `border-radius:999px`; after `restyle.py` that works for sec() pills, but the pill text now has halves (`1.5–7 MIN`) so its `re.match(r'\s*(\d+)')` start minute becomes an integer floor; use `slide_windows` instead.
- `levels/reccues.js`: voice rule still says "keep it under ten seconds" (see the audit F12); minute parsing is integer-only (above).
- `levels/mkextras.py` Free Taster and the website quote "about 5 minutes" warm-ups and the old routine; not edited.
