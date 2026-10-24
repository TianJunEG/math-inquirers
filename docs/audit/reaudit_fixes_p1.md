# Level 1 re-audit fix pass (content and wording)

Scope: Level 1 (ages 6-8) only. Source of the findings: `docs/audit/reaudit_p1.md` (2.3, 2.5, 2.8, Summary). Nothing committed; no diagnostic, `levels/*`, `rebuild/slidekit.py`, `website/*` or `docs/levels_and_placement.md` file was edited. Every new or changed answer was checked in Python (`verify.py`, brute force; results at the end).

## 1. "Next time I will try" restored to the Look-back

| Where | Old | New |
|---|---|---|
| Workbook Look-back box (PDF `hp/workbook_html.js`, Word `hp/workbook.js`), on the Choose and look-back page every child reaches | rows: did well / hardest part / what helped me / still stuck + pass | new row **Next time I will try:** drawing it, using objects, checking my answer, asking a question. Box title still says "There are no right answers. You can pass. Nobody reads it out." The pass tick stays. Row layout re-flowed so wrapped options line up. |
| Look-back slide `lN-reflect` (`rebuild/p1gaps.py`) | no next-step row | same row; notes: optional, never marked, tutor may say to the whole group at the next opening "Today you could try drawing it, using objects or checking your answer" (no names) |
| Tutor guide (`hp/guide.js`) | script and policy paragraph without the row | both mention the optional row ("If you like, tick one thing you will try next time. You can pass.") |

## 2. Label and safeguarding leaks

| Item | Old | New |
|---|---|---|
| Readiness Tracker (`hp/mk_pack.py`) | "Spot children ready for olympiad-style work" (cover), "Who is ready to go further?", "Solved a Challenge question alone", "invite to the Challenge Group", "olympiad-style problems", "Challenge Screening Set" headings, "later maths olympiad papers reward" | cover: "Tutor notes on how each child thinks: four signs to track and an 8-question Go further puzzle set"; "How is each child thinking?" plus "tutor only, never shown to children or shared between families"; "Solved a Go further question alone"; "remind the child that Go further and the Investigation are theirs to choose, and invite the whole group to a short challenge session open to all"; headings "Go further puzzle set"; olympiad sentences removed; "use this only to decide what to offer next, never to label or group a child". File name kept. |
| Weekly Email Pack (`hp/mk_pack.py`) | tutors told to "try the Challenge questions yourself"; parents told "we may invite them to a short challenge session ... We will contact you if so" | "try the Go further questions yourself"; "there will be a short challenge session open to all children in the next holiday. We will send the details to every family" |
| Question Bank (`hp/qbank_doc.js`) | ten "CHALLENGE (after the topic ...)" headings; intro "moves up when they are ready ... Challenge questions" | headings "GO FURTHER (...)"; intro: any child may choose Think harder or Go further at any time, nobody is placed in a level; Core described as "a confident start for every child" |
| Tutor guide (`hp/guide.js`), key (`hp/lessons.js`) | "use the Challenge or Extension question" for early finishers; L2 key "Challenge: 4 and 8"; L10 extension "challenge puzzle"; `scripts.js` "Finished early:" x10 | "point to Think harder, Go further or the Investigation (any child may choose them)"; "If you have time: 4 and 8"; "Write a puzzle"; "For pairs who want more:" |
| Slides (`rebuild/p1neutral.py`, applied by every `gen_lN.py`) | notes "Answers are in the Challenge slide notes", "after pairs have tried the Challenge" (9 decks) | "Go further slide notes", "tried Go further" |
| Parent pack "What Learners Get" (`outputs/designed/..._What_Learners_Get.docx/.pdf`, patched in place; no generator exists for the Level 1 file) | "a Challenge for strong thinkers", "signs of readiness for harder work", "olympiad-style Challenge Screening Set and a Challenge Group", stale "45 printable pages" | "Start here / Think harder / Go further, any child may choose, nobody is placed in a group"; signs of "how the child is thinking", tutor only; "a short challenge session open to all children"; "58 printable pages" |
| Free Taster for parents (`taster/gen.py`) | tier headings Core / Think Harder / Challenge | Start here / Think harder / Go further |
| Public boards, 10 decks | 7 slide titles "Your turn: whiteboards"; notes "Whiteboards up together" (l2, l3, l7, l9), "hold them up together" (l1, l5); "Whiteboards." answer notes; "Ask a child to show ..." (l9-try1); "Ask a child who got b right to explain" (l5-try2); "Draw it on your whiteboard" (l7, l8); "take answers on whiteboards" (l8-warm2) | titles "Your turn: write it"; notes say each child writes on own paper and shows only the tutor (face to face: hold the paper low; online: hold it to the camera at the same moment, or show only the tutor), "Never ask for boards up in front of the group"; volunteers for any explaining; L10 whiteboard round says boards stay low. Also `hp/scripts.js` (L10 warm-up script) and `hp/guide.js` (L10 round) now say nobody holds a board up. |
| Guide wording conflict (re-audit 2.5 item 9) | "Never write scores down" next to "Quietly note who found question 2 easy" (guide and every sneak-peek slide) | "Look for good ideas to praise in a later lesson. Do not write scores or keep a list of who found the second question easy" |

## 3. Tier items (Core approachable untaught; answers re-verified)

| Item | Old | New | Answer |
|---|---|---|---|
| L2 Q5 magic triangle (sum 9) | needs the corner insight; 720 arrangements | corners 1, 2, 3 given, "use counters or number cards, find the number between each pair"; (a) now asks for the middles; (b) "if you have time: sides of 10, you choose the corners" keeps the discovery. Go further C1 (sum 11, corners to find) now genuinely needs the insight. Slide `l2-ws2`, `l2-teachpage2`, `l2-ws2ans` and key updated | 6, 4, 5; sides of 10: corners 1, 3, 5 (only set) |
| L5 Q1c, Q2b | two-step undo and rule plus inverse in Core; page intro stated the taught method | intro now "Find each mystery number. Try a number and check it."; Q1c is a guess-and-check item; Q2b "what does it do?" with the table as data; "OUT 30 means IN __" marked "if you have time"; slide and key updated | 8; add 4; 26 |
| L6 Q3a | "fewest coins" needs biggest-first | tip: "use play coins, pay 85¢ any way you can, then try to use fewer coins"; slide note matches | 4 coins |
| L6 bank Core #7, #8 | dollar notes "fewest notes" in Core, workbook had moved dollars to Think harder | #7 60¢ with the fewest coins (play coins); #8 35¢ with 3 coins from 20¢, 10¢, 5¢. Dollar items stay in the Think harder list | 50¢ + 10¢; 20¢ + 10¢ + 5¢ |
| L9 Q3 (hand spans) | text only, hint was an experiment with paper clips | picture `hp/desk_spans.png` (same desk, 6 big boxes against 8 small boxes), hint removed; slide Q3 text now matches the page (re-audit 2.5 item 7) | Ali (fewer spans, longer span) |
| L9 Q4 (clips and erasers) | text only; slide said "draw the bars" | "(Draw it or count in 2s.)" on the page; slide wording matches | 10 erasers; 6 clips |
| L10 Q7 | two-step backwards in Core | marked "if you have time" with "try a number and check"; slide matches | 5 |
| L7 Go further C1 | text only, unlabelled "3, 6, 10" | printed figure `hp/tri_lines.png` (1, 2, 3 lines with counts) and text "With 1 line there are 3 triangles, with 2 lines 6, with 3 lines 10. How many with 4 lines? With 5 lines? Draw it to check." Also in the bank and on the l7 slide | 15 and 21 (formula and count) |
| L7 Go further C2 | text only | figure `hp/nested_sq.png` and "Draw a square, cut it into 4 equal squares, cut ONE of them into 4 smaller ... count small first" | 9 (brute-forced on a lattice) |
| Lesson keys | L9 key said "Difference column" (page says "How far off my guess was"); L2 Q6 key "Challenge: 4 and 8" | both updated | |

Tools added: `hp/gapkit.py` functions `spans`, `trilines`, `nested` (`python3 gapkit.py spans` / `figs`). `extra()` in both workbook generators now draws an optional picture stored on a bank item (`img` field in `hp/qbank.json`).

## 4. LOW-child load (words on each Core page; pdftotext count including the lesson header, footer excluded)

| Page | Old | New |
|---|---|---|
| L5 p23 | 156 | 147 |
| L5 p24 | 142 | 142 |
| L8 p38 | 158 | 149 |
| L8 p39 | 171 | 148 |
| L9 p43 | 150 | 150 |
| L9 p44 | 238 | 150 (despite adding the picture and the starters) |
| L10 p48 | 134 | 134 |
| L10 p49 | 138 | 144 (Q7 tip; Q7 is now "if you have time") |

Answers unchanged except where listed in section 3. The Choose-and-look-back pages grew by about 17 words (the new row): L1 150 to 167, L9 170 to 187.

## 5. Stale text

* Scheme of Work p1 re-run (`python3 levels/scheme.py p1`) from `hp/lessons.js`.
* Weekly PDFs re-sliced (`hp/weekly.py`) from the new workbook and guide.
* "45 printable pages" (What Learners Get) corrected to 58; L9 key wording; guide "early finishers" line.

## Rebuilt

Decks `split/l1..l10` (`rebuild/gen_lN.py`, then `levels/restyle.py`; no slide overflow in a render check), workbook PDF and Word, tutor guide docx and PDF, question bank, Weekly Dose, Weekly Email Pack, Readiness Tracker, What Learners Get, Free Taster, Weekly PDFs zip, scheme. PDFs copied to `outputs/workbook/` and `outputs/designed/`.

Final page counts: workbook 58 (unchanged), tutor guide 90 (was 89 in `hp/`, 74 in the old `outputs/` copy, which had not been refreshed since the recording cues), question bank 32, Weekly Dose 25, Weekly Email Pack 7, Readiness Tracker 6, What Learners Get 3, Free Taster 8, scheme 2. Weekly slices: student 12/10/12/10/13, tutor 15/15/15/16/16.

## Not fixed, and why

* Bank Think harder and Challenge residue (re-audit 1A table: L1 #8-9, L2 #1-3 and #8-12, L3 #8, L5 #8-10, L6 #8, L9 #10, L10 #9; Challenge L3 #1, L9 #2, L2 #5; Think harder L1 T1, L2 T1/T3, L9 T1, L6 T5): needs new items designed and re-verified, and the printed T1-T4 and slide items read the first entries of those lists, so a reorder shifts workbook pages and slides. Left for a content pass.
* L2 Go further C1 is still "magic triangle with another total" (it now needs the corner idea because Core gives the corners, but it is one technique).
* Lesson 10 is still titled "Challenge Day" (a lesson name for everyone, not a label on children). Renaming touches titles in every document and deck, so I left it; say if you want a new name.
* `hp/trial6.js` (Lesson 6 trial script) still says "Show me ... hold up their whiteboard" (pair level); not rebuilt. L1 explore prediction uses a public thumbs up/sideways/down (low stakes).
* Pacing, lockstep teach slides and the single 5-minute break (separate timing audit).
* Word counts for the Choose-and-look-back page rose slightly (Investigation plus Look-back is about 150-190 words).

## Shared or diagnostic issues found (not edited)

* `levels/mkextras.py` line 340 ("a short Challenge Screening Set and Challenge Group for children who show the signs") is the P2-P6 "What Learners Get" template; same label leak as I fixed by hand for Level 1.
* `levels/scheme.py` says "two Think Harder pages (stretch and challenge)" in the Assessment paragraph of every scheme; the printed pages are now Think harder, Go further and the Investigation.
* `hp/docx2pdf_designed.py` turns a paragraph that reads exactly "Challenge" into a coloured level tag; harmless now for Level 1, but still the old name.
* Diagnostic items from the re-audit 2.4 remain: `diag/build_diag.py` never prints `childNote`, `tutorKey` (rushing prompt), the `$2.05` header, the cross-check sentence or the stretch rule; "not learnt yet" ticks unused; `docs/levels_and_placement.md` still shows 70% / 40-69% / under 40%.

## Python checks

Magic triangle sum 9 only with corners 1, 2, 3 (middles 6, 4, 5); sum 10 only corners 1, 3, 5; sum 11 only 2, 4, 6; sum 13 impossible. L5 Q1c: 8 only; machine rule +4; OUT 30 from IN 26. L6: 60¢ fewest = 2 coins (50 + 10); 35¢ with 20, 10, 5 = 3 coins; 85¢ fewest = 4 coins. L7: triangles with k apex lines = (k+1)(k+2)/2 = 3, 6, 10, 15, 21 (28 for 6 lines, used by the screening extension); nested squares = 9 (lattice brute force). L9: 5 clips = 10 erasers, 12 erasers = 6 clips, 11 / 6 / 25 cubes, 12 cm, 5 cm. L10 Q7: 5.
