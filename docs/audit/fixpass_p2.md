# Fix pass, Level P2 (ages 7-9)

Not committed. Edited: p2/*, rebuild/gen_p2l*.py, rebuild/p2gaps.py (new mechanism), diag/content/p2.json, docs/audit/mk_*_p2.py. Not edited: levels/*, slidekit.py, build_diag.py, website/*, hp/*.

## Page counts (before / after)
- Student workbook: 52 / 64 (+12 over 10 lessons). Each lesson gains one page for the "Before you go" page (Investigation + Looking back, so every child reaches them); two lessons end up +2. The brief's cap of +1 per lesson is therefore slightly exceeded in total. Alternative: shrink Think harder / Go further to one page, at the cost of writing room.
- Tutor guide: 80 / 83. Weekly dose: 24 / 24. Decks: 27-33 slides before, now 28, 29, 29, 28, 29, 29, 30, 30, 29, 34 (+1 "Explore: go further" slide each). All decks previewed: no OVERFLOW. mkextras: "P2 self-check: OK" (key rows still Q1..Qn).

## Cross-lesson changes
1. No public labels: banners now Start here / Think harder / Go further / Investigation. Fast-track box replaced by the neutral line "After question 3 you may choose: carry on, or try Think harder." Script and every deck note say the tutor never announces who is on which page and pairs are not split unless both agree.
2. Safeguarding correction applied: NO private chat to children anywhere. Invitations go to the whole group ("When you have finished Start here you can choose Think harder, Go further or the Investigation"). A child ticking "I am still stuck" gets a check-in in the open session (quick visit to the shared breakout room or hand signal, parent nearby). Guide rule "No private messages to children" kept.
3. Sneak-peek puzzles (1-4 min): Q1 access (objects/drawing/counting), Q2 thinking. Answers on own paper shown to the tutor on camera, never boards before the group. Notes say these are ideas not yet learnt; guessing and "I do not know" welcome; nobody marked. Timeline unified: game 4-6, quick questions 6-8, explore 8-14 (+ go-further slide), exit 80-87, Looking back 87-89 (2 min), close 89-90 (L10: 80-85, 85-87, 87-90).
4. Looking back: small box on the last core page (page every child reaches): did well / hardest part / What helped me ticks incl. "I asked for help", "I am still stuck (my tutor will check in during the session)"; pass always allowed; not collected publicly. Q8 and the old reflect block removed.
5. Talk time: volunteers first, pass allowed, no cold-calling, no tallies.
6. Investigation printed (dashed box, easy first step, model answers kept) on the page every child gets.
7. High child: "Explore: go further" slide from minute 8. Low child: exact review fixes below.

## Per lesson
- L1: leading-zero explanation; Bonus on warm-up (900 and 108); volunteer explains zero.
- L2: exit ticket now 3A4 + 257 = 601 (two unknowns as Bonus); Q2 check header; Q5(b) to Think harder; Q6 bar hint; box/letter note.
- L3: Q7 to Think harder with picture; Q4 dealing tip; Q6 stop at 10 rows.
- L4: Q1(d) to Think harder with shape picture; Q1 tip; Q3 simplified.
- L5: IN/OUT/undo strip; Q2(b) replaced by an x2 then +1 table; scaffolded bars for Q3; old Q2(b) to Think harder; partners swap roles.
- L6: "50c is a coin, $50 is a note"; Q2 "you may not need every row"; Q5(b) to Think harder; play-money fallback.
- L7: softer folding of thirds; notation note (slash on slides, stacked in workbook).
- L8: nets A-D in core, E-F to Think harder; Q4 fold net A with tutor; Q2 table one row per size; Q3 build stack A first; cube fallback.
- L9: ruler-on-pencil backup; Q3 pours start from empty jugs, 6-step answer; Q4(c) to Think harder; Q5(c) 10:45 to 11:30; noon-crossing trip to Think harder.
- L10: relay by volunteers, pass allowed; certificates 87-90 with praise said in the open session.

## Diagnostic (diag/content/p2.json only; all answers verified in Python by docs/audit/mk_diag_p2.py)
Content: 4 warm-up, 6 main, 2 stretch. Flagged questions replaced, undefined vocabulary removed, missing coverage added, work notes neutral ("Listen for..."), stretch preceded by "These last two are tricky on purpose".
Simulation (assumed rates): typical 8-year-old sent down 4% (was 11%); strong child joins 73% (+16% level-up check); weak/guessing child 75-78% chat plus taster.

Build changes needed in diag/build_diag.py (not made):
- Read `childNote` and print under the "Brain stretchers" heading; draw a box for "?"/{box}.
- Score line: "Warm-up __/4, Main __/6, Brain stretchers bonus __/2". Numbering: warm-up 1-4, main 5-10, stretch 11-12 (tie-break and prerequisite text refer to main questions 6, 8, 9 and 7-10).
- Cut on the main six: 5-6 join, 3-4 join with support, 0-2 chat plus taster; warm-up of 2 or less steers down; stretch is only a flag; level-up check only if main 6/6, warm-up 4/4, both stretchers right. Never use the word failure.
- Parent page from `parent` (join, support, down, strongBox, "Want a gentler start?").
- Tutor key as a separate PDF page set from `tutorKey` (header "Print pages 1 and 2 for your child. Keep pages 3 and 4 for yourself.", column "Listen for", tieBreak, prereq).

## Left unfixed (shared files, not mine to edit)
levels/mkextras.py:335 and hp/parent_pack_level.py:44 (also the P2 Weekly Dose PDF, line "Challenge is for strong thinkers") still carry the old label; change to "Go further is open to anyone who would like it".
