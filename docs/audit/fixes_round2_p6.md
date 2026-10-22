# Round 2 fixes, Math Inquirers P6 (ages 11-13)

Date 2026-10-22. Source: docs/audit/reaudit/reaudit_p6.md. Nothing committed or pushed. No shared file touched (levels/mkextras.py, levels/scheme.py, hp/*); mkextras.py and build_level.sh were only run. No Scratch .sb3 created. No private-message wording added (the only mentions left are the existing prohibitions "never private chat / never by private message").

## Fixes

| # | Finding | Fix | Files |
|---|---|---|---|
| 1 | N1 "you you" in every p6lN-reflect note and the Tutor Guide | `reflectEx` in gaps.json already begins with "you"; both templates added a second "you". Template now inserts `reflectEx` alone. grep for "you you" over split/p6l*, p6/*.html: 0 hits | rebuild/p6_gaps.py, p6/guide.js |
| 2 | N3 L7 wb p1 Q1 15-gon at move 80 runs off stage | Q1 now says "move 80 up to 10 sides, 50 for 12 to 15, 30 for 24" (matches deck notes). Stage simulation from (-50, 100), heading 90: 6, 9, 10-gon at 80, 12 and 15-gon at 50, 24-gon at 30 all inside x ±240, y ±180; 15-gon at 80 confirmed OFF | p6/content/l7.js |
| 3 | N1b Think Harder slide differs from printed page | New `rebuild/p6_th.py` reads `lessons[n-1].th` from p6/data.js (the same array the workbook prints). gen_p6l1..l10 build the stretch slide (now titled Think harder) and its answer notes from it, 4 items, smaller type. Checked by script: all 4 questions and all 4 answers of every lesson appear on the slide of every lesson (10 of 10 match). The old slide lists were wrong in L1, L2, L3, L4, L9, L10 and used items not on the page in L5-L8 | rebuild/p6_th.py (new), rebuild/gen_p6l1-l10.py |
| 4 | N2 L3 Think Harder repeats Core | Replaced three items with step-ups: TH1 unknown start (sprite: change x by -8 then 5 ends at -1, so a = 2); TH3 use -2, 3, 5 once each in __ - __ - __ (biggest 4, smallest -10); TH4 relationship chain (C = -4, B = -1, A = -6). TH2 (diver and seagull, 23 m) kept. All answers checked in Python (itertools for TH3) | p6/content/l3.js |
| 5 | N5 Looking back timing | One rule: Looking back is always the 2 minutes straight after the exit slip. Lessons 1-9: exit slip 82-86, Looking back 86-88, close 88-90 (was already so in the decks). Lesson 10 (showcase): exit slip 86-88, Looking back 88-90 with the certificates. The Tutor Guide contradicted this for L10 (said showcase 62-87, exit and certificates 87-90, Looking back "86 to 88"): corrected to the deck times and the heading is now lesson-aware | p6/guide.js |
| 6 | L7 LOW (weakest cell) | Page 1 Q1: dropped the 36-sided row (move 10) and added row 2 = the hexagon the child already drew in explore (turn 60, inside 120): an early guaranteed win; Q1 stem shortened to two lines; vocabulary box and Q3 stem shortened. Key and ws1ans slide updated. Page still fits (workbook stays 55 pages; an earlier longer wording pushed Q2 to a new page and was cut back) | p6/content/l7.js, rebuild/gen_p6l7.py |
| 7 | L10 LOW | Page 1 Q1(a) is now a counting win: the picture shows 6, 11 and 16 sticks, "sticks for 4 hexagons? (count on)" = 21, then 10 hexagons = 51. Q1 stem points to (a) first; (d) shortened to "The code says __. It checks a chain of __ hexagons." Key, ws1ans slide and notes updated; stale "Q3e" note replaced | p6/content/l10.js, rebuild/gen_p6l10.py |
| 8 | L9 HIGH revision-heavy | TH2 (another total = mean x n item) replaced with a new-idea item: 5 whole numbers with mean 8, median 10, mode 12 (three answers, brute-force checked: 0,6,10,12,12; 1,5,10,12,12; 2,4,10,12,12; 3,3 would make a second mode). Combines median and mode with the mean | p6/content/l9.js |
| 9 | Skip-ahead route | Self-chosen, whole-group, no label: page-1 line now reads "Know this idea already? You may start with Think harder. Or after question N choose: carry on, or try Think harder."; sneak-peek slide notes and the Tutor Guide add the minute-40 invitation to everyone ("if you already know today's idea and can say it in your own words, start on Think harder; tell me the idea in one sentence in the open session"), same follow-up for all, never testing one child in front of others; everyone still does exit slip and Looking back | p6/workbook_html.js, rebuild/p6_gaps.py, p6/guide.js |

## Rebuilt
All 10 decks (gen_p6lN.py, then levels/restyle.py split/p6lN), overflow check 291 slides, 0 overflow. `bash levels/build_level.sh 6` and `python3 levels/mkextras.py 6` (self-check OK). Rendered and viewed: L7 p1, L10 p1, L3 Think harder, L1 p1, Think harder slides L5, L6, L7. Page counts (before -> after): workbook 55 -> 55; Tutor Guide 88 -> 89 (skip-ahead paragraph in each lesson plus lesson-10 timing text); Weekly Dose 25 -> 25; Question Bank 28 -> 29 (the three replaced bank items are longer); Email Pack 12; Free Taster 5; What Learners Get 1; slides 291 -> 291.

## Left and why
- Starter .sb3 files (L5, L8, L10 A-D, L7 start file): not created (unverified Scratch files forbidden). The notes still tell the tutor to build them. Open.
- Scratch primer for children new to Scratch: not added (needs a new slide set and page; out of scope of a wording/defect pass). Open.
- L2 ws2, L5 ws2, L6 Q4-Q5, L4 ws2 load, L10 relay "name someone else": not changed (design reductions, risk to answer keys and slide numbering); L10 LOW got the early win and less reading instead.
- L9 maths familiarity (inherent), brain breaks, "dice" wording: cosmetic, left.
- Re-audit suggested "invite whole group at minute 12 instead of 40": done only as the skip-ahead line at minute 40 plus the existing minute-12 Go further slide; the teach block length is unchanged.
- L7 set-up (about 10 minutes): unchanged apart from stage sizes already in the notes.
- L9 Go further slide answer mentions "instead of 30" (the explore data); not verified against the explore task here, flag for the next review.

## Shared-file issues (not touched)
- Parent-facing "Challenge for strong thinkers" (Weekly Dose, What Learners Get, per re-audit N4): not present in the current P6 PDFs I rebuilt (grep of p6 Weekly Dose text finds only plain "Challenge"); the string in the repo is in rebuild/p2gaps.py (P2). If it still appears in a P6 parent file, the source is in levels/mkextras.py or hp/parent_pack_level.py: change to "Challenge: for anyone who wants more".
- Weekly Dose "Challenge" label is generic and unchanged.
