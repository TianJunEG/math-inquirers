# Independent audit: Level 1 Term 4, lessons 36-40

Auditor: independent (did not write these). Method: AUDIT_BRIEF / AUDIT2_BRIEF / AUDIT_T3_BRIEF (the T2/T3 briefs are .txt). Every workbook, key, home, kit, parent page and the Quest Log was rendered and viewed; every question was solved from the printed pages; all five decks were viewed as contact sheets; guides were read (L36 in full, others by section); practice runners were checked for external requests only (none). Not done: line-by-line read of the middle of guides 37-40, interactive Playwright run of the practice runners, a B&W print test (Books 5-8 are not built, see M1).

## Verdicts

| Lesson | Ready to release? |
|---|---|
| 36 Count Everything | Yes after listed fixes (M2, L1) |
| 37 Make Your Own Graph | Yes after listed fixes (M3, M4) |
| 38 Graph Detectives | Yes after listed fixes (M3) |
| 39 The Problem-Solving Toolbox | Yes after listed fixes (M5) |
| 40 Inquirers' Showcase + Quest Log | Yes after listed fixes (M6, M7, M8) |

Maths: all workbook items, keys, home practice and Quest gates solve correctly. No High findings. Owner-decision checks (90 minutes, beyond-syllabus item labelled at Think harder/Go further, Quest rules, no end-of-term check, no MOE/GEP/SASMO claim, no price, recording notice before recording, no paper hold-up to camera, 5 minute-class hand-offs 35-36 to 39-40) pass, with the exceptions below.

## High
None.

## Medium

M1. Books 5-8 not built. outputs/print/term holds only T1 and T2 books (term_books_spec.json). Parent pages for 36-40 say "Your Term 4 book (Book 8)" and the Quest Log lives in it. B&W conversion of yellow-highlight items (L36 S6, kit people) cannot be verified; the converter maps gold to dots so it should survive, but run `make_term_books.py` and `make_bw_print.py` and check L36 S6 and L36 T3/G2 yellow squares before release.

M2. L36 sneak-peek puzzle 1 (deck slide 5, key "8 squares") shows a 4 by 2 grid and asks "How many squares are in the picture?". After Explore teaches "small squares and a bigger one", the same grid holds 3 more 2 by 2 squares (11). The answer 8 contradicts the lesson's own idea, and "Back to the sneak-peek" reveals 8. Fix: say "small squares" or use a grid with no bigger squares.

M3. Quest gate numbers reuse lesson pages (owner rule: fresh examples). Gate 6 (3 stars and 5 stars, key 2, answers 6 and 4) is identical to L38 T2 (Pearl 3, Reef 5, key 2, "4 more") and L38 sneak-peek 2 (3 pictures, key 2, 6). Gate 5 is the L36 S3 four-dot A-B-C-D picture plus one line (answer 6 = L36 T1 handshakes; L36 optional slide shows the same figure). Gate 1 rectangle is "2 rows of 3" as in L36 T3; gate 7 uses "3 more each row" as in L39 S3. Tutor notes claim "numbers chosen so they do not repeat a lesson page": false for gates 6 and 5. Fix: change gate 6 to e.g. 4 and 7 pictures, key 2 (8 and 14, 6 more); gate 5 a 5-dot or different layout; gate 1 a 3 by 3 or 2 by 4 rectangle. Files: L40_Quest_Log.pdf pp.1, 3, 4; L40_Quest_Tutor_Notes.pdf section 4; lessons/l40.json.

M4. L37 graph mat is a vertical graph (5 columns by 8 rows, slide "use one column for each kind"), but every graph in the workbook and slides is horizontal rows, and the parent page glossary says "a row for each kind". Children will draw columns on the mat and read rows elsewhere. Fix: make the mat 8 columns by 5 rows (rows = kinds) or change slide/parent wording; remove the five stray tally-like bars under the mat (L37 workbook p.6).

M5. L39 parent page (family-facing) says "Book 8 not here? Tell us on the business WhatsApp and we will send a PDF." This promises the parcel fallback that owner_decisions.md still marks as a draft policy. L40 grown-up note says "we will find another way" instead (inconsistent). The tutor-only parcel notes (L36 guide p.2, L39 guide p.2, L40 guide p.3) are consistent with owner_decisions (printing and postage included in the fee; policy draft; 30-day address deletion) and the word parcel/postage appears on no family page. Fix: use the same neutral line on both pages ("Tell us on the business WhatsApp a week before"), leave the PDF promise to the tutor note.

M6. "Keep the Quest Log closed, in an envelope" (L39 and L40 parent pages, L40 guide, grown-up note) cannot be done: the Quest Log is bound inside Book 8 (make_term_books EXTRAS), not a loose sheet. Same wording as T3. Fix: "keep those 4 pages closed" or make the log tear-out/perforated. Quest Log footers still say "Print at 100% (actual size)" (known shared-tool item `b_quest.py`), which contradicts the posted-book model.

M7. L40 guide chapter note says "Do not record these slides ... s-quest1", but the script has s-quest1 shown from 35:00 and recording paused only at 36:14, so about 70 seconds of Quest intro are recorded; also the 35:08 REC line is spoken before the pause. Fix: pause the recording at 35:00, and say once at restart (55:00) that recording has started again.

M8. L40 Quest Log gate 4 (page 2): tile C has 3 smaller triangles, A, B, D have 2 larger ones, so "size" is as defensible as "number" for part b. Gate 1 picture shows the circle already cut into 4 (gives away part a). Gate 3 folded-paper picture shows no fold line; the answer 2 holes holds, but the figure does not show the fold. Fix: equal-size triangles in C; draw fold edge.

## Low

L1. L36 optional slide "which handshake is missing" is correct (A and D), but the lines cross at the centre like a node; the workbook E3 uses C and D. Fine, but different from the slide: say so in notes.
L2. L36 kit page asks for 8 paper people while the lesson needs at most 6 (coins fallback says 6). Fine, note only.
L3. L37 S2/T1 tally marks at Start here are not in the syllabus (guide flags as activity). Acceptable; keep wording that tally marks are not tested.
L4. L37 guide beyond item says "4 lollies" and 4,3,2 pictures; the workbook G1 uses mints/toffees/gums (4, 3, 3.5 pictures). Update guide text.
L5. L38 workbook labels are S1-S6 but stems say "questions 1 to 3 / 4 to 6 / question 5". Use the printed labels.
L6. L39 S6: a large "PLAY MONEY" caption under the coin pictures looks like a stray label; kit page has no play money. T4 asks 5 cent coins first but the table lists 10 cent first. Home answer 5 uses "14 - 5" (hyphen) instead of "take away". Kit-page "Work backwards" card label tight; deck slide 6 table clips "Work backwards".
L7. L40 workbook S2 says "tick" but has no tick boxes (words only); "Nobody sees your ticks except your grown-up and your tutor" overstates, since the tutor sees only what is photographed. S5(b) "7 take away that is ___" reads awkwardly. Page 5 exit ticket says "at the end of the lesson" but the guide says it is for home. Tutor notes first line says "one from each lesson of the year" but gates cover lessons 31-40.
L8. Quest Log answer lines are about 2 cm; "quarter" in a 6-year-old hand is tight.
L9. Deck "Workbook page" slides show unreadable thumbnails of the workbook figures (all five decks); questions are read aloud so low severity.
L10. L36-L39 parent pages all say photos are kept 90 days after the program ends: consistent with privacy.html. Recording statement on parent pages matches guide wording. No hold-paper-to-camera wording anywhere ("Nobody holds paper up to the camera" only).

## Checks passed (evidence)

- Maths: L36 S1-S6 10,15,5,7/6/5,20,5; T1 2,1,6; T2 8; T3 6,2,8; T4 11,9,8; G1 10,15; G2 9,4,1,14; G3 8,9; E 15,9,CD. L37 4/6/2, 6/8, 3/17, 2/5/3 drawn, chess/13, F T T F; T1 9,5,6=20; T2 (2); T3 11,5; G1 3,7; G2 7,5; E 3,5,(1). L38 Mei/Siti, 5/25, T T F F, 4/oranges, 2/11, 21/apples, T1 5/6, T2 6/4, T3 No/8, G1 15/3, G2 5/8, G3 (2), E Siti/16/True. L39 7/19, 18/9, 15/18, 25/17, 5/35, 15/25/30/3 pairs, $25, $9/$3, 3/6, 4 and 3 coins, 9/27/Yes, 12/3, day 7, work backwards, 7/18, False. L40 (2), Wrong/13, 1/6/16, 4/20, B/4, 5 and 7, No/2/3 and 7, 14, (2), Wrong; Quest 4/quarter/6, 3/3, 6/2, C/number, 6/12, 6/4, Table/17, No/8, 25/75. All match the keys and home answers (home sheets solved too).
- Quest rules: 20 minutes after the break (35-55), game, no scores/rank/timer, private notes, WhatsApp-only photo return, make-up before recording, no "test/exam/score" on child or parent pages.
- Timing: scripts 64:47, ~65, ~65, ~66, 69:58 of 90; slow class 76:49 and 82:18 (L40) fit. Beyond-syllabus item named in every guide, parent page and tied to Think harder/Go further. No prices, no MOE/GEP/SASMO claims. Recording notice precedes "Start the recording now" in all guides. Mi has no calculator.
- Hand-offs: 35-36 (checked via L36 guide), 36 to 37 (graph mat plus about 12 things: true), 37 to 38 (pencil and paper: true), 38 to 39 (15 cards cut: kit has 7 tool and 8 problem cards: true), 39 to 40 (Quest Log, partner, favourite page: true except the envelope wording, M6), 40 to Level 2 or holiday program (neutral, promises nothing).
- Online practice: no external requests in index.html or practice.js; data files present.
- Overlap with Terms 1-3 and the holiday course: topics (strips, find one first, work backwards, tens) are deliberate spiral review in warm-ups; no holiday lesson content reused.
