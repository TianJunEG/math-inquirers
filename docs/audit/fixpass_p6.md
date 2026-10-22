# Fix pass P6 (ages 11-13)

Date 2026-10-22. Nothing committed. Shared files (`levels/*`, `rebuild/slidekit.py`, `diag/build_diag.py`, `website/*`, `hp/*`) untouched. Diagnostic change is in `diag/content/p6.json` only.

## All lessons
- Neutral names: Start here, Think harder, Go further, Investigation. No printed fast-track box; page 1 says "After question N you may choose: carry on, or try Think harder." Tutor invites privately only, never announces pages, never splits a pair unless both agree.
- Sneak-peek puzzles (2-5 min) replace the warm-up check: one access puzzle, one thinking puzzle, answers private, "ideas we have not learnt yet, guessing welcome, nobody is marked". Data in `p6/content/gaps.json`, slides from `rebuild/p6_gaps.py`.
- Timeline made consistent in deck, script, guide and workbook: 0-2 opening, 2-5 sneak-peek, 5-8 warm-up game, 8-10 quick questions, 10-25 explore (Go further what-if on a slide from minute 12), 25-35 teach, 35-40 break, 40-75 worksheet, 75-82 talk, 82-86 exit slip, 86-88 Looking back, 88-90 close. Lesson 10 keeps its own plan (showcase 62-85).
- New Finish page in every workbook (all children reach it): Investigation with an easy first step, exit slip, "Looking back" (did well / hardest part / what helped, tick options incl. "I asked for help" and "I am still stuck (my tutor will check in privately)", pass always allowed). 2 minutes. Never collected publicly; tutor may read privately.
- Talk time: pass allowed, volunteers first, no cold-calling, no tallies.
- Sentences like "you you" fixed. Low-child scaffolds (drawn tables, prefilled rows) and cap on the solo page; core questions moved to Think harder where the review said so.

## Per lesson
1. No race wording; Q2 cut to (a)(b), rest moved to Think harder.
2. "Factor pair hunt"; exit uses 111 (133 optional); Q5(a) up to 30; Q4(b) moved.
3. "No level 0" note on the challenge item.
4. Q1 gets a one-step first row; Q7(b) prefilled; Machine starter note; page 1 tightened to fit.
5. Q1(c), Q4(c) moved; race wording out of warm-up.
6. Timer removed; Q1(d) hint; Q3(c), Q4(d) moved; difference table rows 1-2 prefilled.
7. Vocabulary box; trace rows prefilled; 20-point row moved; setup slide cut to 2 steps (detail in notes); "use your arm as the turtle's nose".
8. Q1(f), Q4(c) reduced and moved; Python corner grey and optional.
9. PSLE phrase removed; no points in warm-up; Python box optional.
10. Relay by volunteers; Q3 cut to (a)-(d) (digit cards and probability moved); showcase "two stars and a question", 2:30 turns.

## Page counts (before, after)
| File | Before | After |
|---|---|---|
| Student workbook | 45 | 55 (+1 per lesson: the Finish page, by design) |
| Tutor guide | 82 | 85 |
| Weekly Dose | 25 | 25 |
| Question Bank | 28 | 28 |
| Email Pack | 12 | 12 |
| Free Taster | 5 | 5 |
| What Learners Get | 1 | 1 |
| Slides | 291 | 291 (checked: 0 overflow, baseline 0) |

`bash levels/build_level.sh 6` and `python3 levels/mkextras.py 6` run, self-check OK. Overflow check: `python3 docs/audit/fixpass_p6_overflow.py`.

## Diagnostic (`diag/content/p6.json`)
Warm-up now: factors of 24 (8 factors), 6/36 = 1/6, triangle 65, loop code n = 17. C2 defines prime, C4 defines probability, C5 says "average", S1 is the pattern 4, 7, 10, 13 (50th term 151). All answers checked in Python. Word "failure" not used. New keys (`notes`) hold the child reassurance, time note, placement table, "guide, not a grade" box, topics title, easy line and key fix.

### Build changes needed in `diag/build_diag.py` (not made)
1. Split the PDF: child sheet (pages 1-2) and a separate tutor/parent page set (pages 3-4), so answers do not print with the child pages.
2. Page 1: replace the header with `notes.childHeader`; add `notes.childReassurance` and `notes.timeNote` under "How it works".
3. Scoring: warm-up (4) decides; use rows from `notes.placement`; main (6) uses `notes.mainNote` with no level change; stretch is tick-box flags, not marks. Change the totals line to "Warm-up __/4, Main __/6, Stretch flags __/2".
4. Remove the "Strong?" and "Not yet?" boxes; use one box with `notes.guideBox`. Drop the "8 of 8, try the level up" line.
5. Retitle "Skills covered" to `notes.topicsTitle`; add `notes.easyLine`.
6. Replace the key's "$2.05 and 2.05" example with `notes.keyFix`.
7. Section headers: "Warm-up (4 marks)", "Main questions (6 marks)", "Brain stretchers (flags)".

## Notes for the owner
- Review asked for "(c) steps IN by 2" in L4 Q1; no table steps IN by 2, so it was skipped.
- No .sb3 starter files exist in the repo; lesson notes tell the tutor to build them.
- Guide checklist "No private messages to children" now allows short in-platform private chat for lesson messages. Please confirm this safeguarding wording.
