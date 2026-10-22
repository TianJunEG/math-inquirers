# Fix pass, Level P5 (ages 10-12)

Status: applied, not committed. Rebuilt with the gen scripts + restyle, `levels/build_level.sh 5`, `levels/mkextras.py 5`. No slide overflow in any of the 10 decks.

## Page counts
| Item | Before | After |
|---|---|---|
| Student workbook | 57 | 57 (5 pages per lesson kept) |
| Tutor guide | 81 | 86 (new sneak-peek, choice, reflection, talk-time and Investigation text) |
| Weekly dose | 26 | 26 |

## Safeguarding correction (applied after the first pass)
No private one-to-one messages from tutor to child anywhere. Invitations go to the WHOLE group ("when you have finished Start here you can choose Think harder, Go further or the Investigation"). A child who ticks "I am still stuck (my tutor will check in with me)" gets a check-in in the open session (a quick visit to the shared breakout room or a hand signal, parent nearby). Sneak-peek answers: own paper shown only to the tutor on camera, or everyone holds paper to the camera at the same moment. The guide checklist keeps "No private messages to children".

## All lessons (shared changes)
- Labels: Core = "Start here", Think harder, Go further, Investigation. Removed the fast-track criterion and every "strong thinkers / early finishers / gifted" label (workbook, slides, notes, guide, disclaimer). Page 1 carries the line "After question 3 you may choose: carry on, or try Think harder." The tutor never announces who is on which page; pairs are not split unless both agree.
- Warm-up check became "Sneak-peek puzzles" (0-3 min): an access puzzle then a thinking puzzle; guessing and "I do not know" welcome; nobody is marked; answers never on public boards.
- Reflection: 2 minutes (86-88) in a small box on the Investigation and reflection page every child gets ("Something I did well", "The hardest part was...", "What helped me" ticks incl. "I asked for help" and "I am still stuck", Pass allowed). Never collected publicly; tutor may read it privately. "you you" typos fixed.
- Talk time: pass allowed, volunteers first, no cold-calling by name, no public tallies or rankings.
- Investigation printed on the page every child gets, with an easy first step; model answers kept (p5/content/inv.js).
- Go further what-if on the second explore slide of every lesson (L1 billion seconds; L2 n pizzas among n+1; L3 odd total of 25; L4 three triangles of area 12; L5 which number to 30 gives most cuboids; L6 split 430 pages 180/250; L7 up 50% then down 50%; L8 five-sided shape 540; L9 12 children, 66 high fives; L10 tripled/minus 4/halved gives 6). All verified in Python.
- One timeline in deck, script, guide, workbook: 0-3 sneak-peek, 3-9 warm-up, 9-21 explore, 21-33 teach, 33-37 break, 37-49 page 1, 49-53 check, 53-58 teach, 58-72 page 2, 72-76 check, 76-82 talk, 82-86 exit, 86-88 reflect, 88-90 stamp. Minute labels added to slides that lacked them; optional slides labelled "37-72 MIN OPTION".

## Per lesson (review fixes)
- L1: check C1 now "cards 3, 6, 7, 9, closest to 7000" (both sides asked as a question).
- L2: Q1(b) fraction/mixed note, Q1(c) shortfall hint, Q2 "Start here" tenths line, empty 3-part bar on check C2 (drawn). Optional Q1(d) removed to keep page 1 whole.
- L3: Q1 restructured (a) $60 first try, with key $20/$10/$30, (b) $72, (c) $12, (d) 1/6 as stretch; check C1 replaced with the (a)(b) version; Q5 shows 5 equal parts to draw; third jar card moved to tutor extension.
- L4, L5: typos, page breaks and materials per the review; L5 "Missing Edge Match" (no shouting), "draw the tank and shade the water" on C2; L5 Q5 hint no longer gives answers.
- L6: pair "4 pens $2.00 or 10 pens $4.00"; C2 12 pages/4 min v 20 pages/5 min; Q2 "Start here" 4.20 / 6; Q5 printed half-hour time line; `figTimeline()` added.
- L7: reading load cut; drawn 100-square scaffold on the sneak-peek.
- L8: line "Angle BOC means ..." on page 1; sentence frame on Q2; C2 now straight-line 38 / 142; parallelogram "3 times" question moved to Think harder; Reasons A-F on page 1.
- L9: "first child to say the rule wins" removed (nobody races); drawn stick-triangle picture; Q5(b) scaffold (scores 100, 93, 86, 79 ...).
- L10: logic grid is now Q1, backwards puzzle Q2; relay is volunteers-first with pass and green/orange cards; talk frame "I started by ... I know it is right because ..."; "heuristic" replaced by "strategy" and "Mixed Strategies".

## Diagnostic (diag/content/p5.json only; every answer checked in Python)
- Replaced W3 (24 x 35) with "What is 3/4 of 48?" (36; watch 12 or 192; skill Fraction of a set).
- Replaced M6 with "In triangle ABC, AB = AC and angle BAC = 50 degrees. What is angle ABC?" (65; watch 130 or 50). Topics line now "Angles in triangles" and "Fractions of a set and fraction word problems".
- W1 skill re-tagged "Subtract fractions (related denominators)"; M1 accepts 4 400 000, 4,400,000, 4.4 million; "How did you start? Write one line or draw a quick picture." added (unscored) to M2 and M4.
- S1 and S2 unchanged (answers 101 and 162 verified).

### Changes needed in diag/build_diag.py (not made, shared file)
1. Child sheet intro: add "There are 12 questions and about 30 minutes. Stop when time is up; questions you did not reach count as zero. If you finish early, check each answer a second way."
2. Brain stretchers heading line: "These are meant to be tricky. Many children skip some. Skipping is fine." Stretch questions unscored for placement; show "Main (out of 6)" and a separate "challenge-ready" flag.
3. Cut rows (main out of 6): 5-6 join Ages 10-12 (6 of 6 plus warm-up 4 of 4 plus a stretch right: also offer the free P6 check); 3-4 join with support (warm-up 2 or less: P4 or a chat); 0-2 P4, except warm-up 3 or 4 means offer a free 10-minute chat first. Score line "Main marks ____ / 6" and "Challenge-ready: yes / no".
4. Parent text: replace "Strong?" with "A high score? ... The Think harder pages in class give a strong child plenty to chew on."; replace "Not yet? ... not a failure ..." with "A lower score? A score is one snapshot on one day. It tells us where to start. ... book a free 10-minute chat"; 0-3 row: "Ages 9-11 (P4) is likely to be the more comfortable start ... if the warm-up score was 3 or 4, or your child was tired or distracted, book a free 10-minute chat"; 6-8 row ending "Your child is ready for the pace of this level."; add "Please do not mark in front of your child ... Say 'Let's look at that together in class'."
5. Key note: "Accept equivalent forms (for example 4 400 000 and 4,400,000, or 4.4 million, or 0.4 and 2/5)." Print the tutor key as a separate "tutor and parent" PDF page set so the child cannot turn to the answers.

## Outside my remit (shared files still carrying old wording)
levels/mkextras.py, levels/scheme.py, hp/parent_pack_level.py and possibly hp/weekly_level.py still print "strong thinkers", "gifted-education-type" and the old Think Harder / Challenge tier names.
