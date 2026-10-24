# Holiday program final audit (Levels 1-6), independent

Auditor: independent, no stake in the builders' conclusions. Audited at commit 81ff07c (branch claude/great-fermi-1hv4vc, 23 Oct 2026). Source files for the holiday program (hp/, p2..p6/, split/, outputs/print, outputs/designed) were unchanged by other agents during the audit (print PDFs 03:50/04:15, designed 03:32-04:10, decks published 04:20-04:35).
Required reading done: docs/terms/owner_decisions.md (decisions 6, 9, "Puzzle Day for holiday levels 1-4", prices), the five claimed-fix documents.

## Verdict: READY AFTER MINOR FIXES

2 High, 7 Medium, 6 Low. Both Highs are small mechanical fixes (rebuild one print PDF; remove one instruction family). No wrong maths found.

## What I verified independently (claims that held)

| Claim | Method | Result |
|---|---|---|
| Print PDFs match print_spec.json | pdfinfo + text per page | 64/74/64/76/62/58 pages, A4, blank backs after every cut-out page (P1,P2,P3,P5,P6), certificate has blank back |
| Gutters | rendered all pages, measured ink margins | Correct on all six: recto left margin ~2x right, verso mirrored (30 vs 15 px at 30 dpi) |
| L2 Q5(b) line | viewed print p11 | "Each side adds up to 420. Fill in the second triangle..." present |
| L2 Fraction strips heading | viewed print p62-64 | Heading sits on top of the strips page (63), blank back |
| L1 Lesson 5 layout | viewed print p23-27 | Hints/clue lines inside question boxes; no text outside boxes; answers checked (L5 Q2, Q3, Q4, C1, C2 solved) |
| L5/L6 Start-here load | viewed L5 L8 p38-39, L6 L7 p33-34, L6 L10 p48 | Dense but workable; L8 fact strip gone; L6 answers re-solved (49, 15 sides, 1 o'clock, 3 prime pairs) |
| L1 30-second reset | live deck l1-ws1ans read from the artifact and byte-compared with split/ | Present on slide and in notes; byte-identical to repo |
| Live decks match repo | Artifact read of 6 decks (l1, p2l10, p3l9, p4l10, p5l10, p6l7): file counts consistent, deck.json byte-identical (l1, p6l7, p4l10), 7 slide files byte-identical (l1-title, l1-ws1ans, p6l7-explore1, p6l7-exit, p4l10-title, p2l10-challenge) | Live = repo. P5 L10 populated (28 slides, 50 files) |
| Recording cues in all six guides | grep | 44-45 "recording" mentions each |
| L4 "stretch beyond P4" notes | guide text | present, 3 mentions |
| L5 week-5 note | compared to website/data/beta_schedule.json | Wed 23 Dec 16:45 / Sun 27 Dec 16:15 matches the schedule |
| L6 .sb3 files | re-ran p6/scratch/verify/editor_check.js in the REAL Scratch editor (headless Chromium, scratch.mit.edu) | "ALL PASSED (26 files, 39 runs)"; check_structure.py 26 files, 0 problems; families zip holds the 13 starters |
| Question banks | solved 30 random bank items per level (180 total, seed 20261023) by hand | 180/180 correct, no ambiguous or multi-answer item found |
| Go further L1 (30 items) and L4 (30 items) | solved all, compared with the guide keys | All correct and unique where claimed (incl. L4 riddle 30 261, lockers 1,4,9,16, 15 five-digit numbers digit sum 3) |
| Cube nets F/E/D (P2 bank) | viewed the cut-out page | Answers match the drawn nets |
| Deck structure, all 60 decks (1,612 slides) | script | order = files; every deck has check and exit slides; no aside over 4,000 characters; no scripts/styles |

## Findings

### High

**H1. P4 print workbook backs the first cut-out page with a content page.** `outputs/print/Math_Inquirers_P4_Workbook_PRINT.pdf`, sheet 29 = print pages 57 (recto: Lesson 10 Go further No.5-7) and 58 (verso: "Cut-outs"). The source has 57 pages before the cut-outs (odd), so `print/make_print_pdfs.py` (lines ~46-55, no parity padding) puts every cut-out page on a verso with its blank on the following recto. Cutting the Cut-outs sheet destroys the Lesson 10 Go further page; the other eight cut-outs have blank fronts (works, but wastes a sheet) and the file ends with two blank pages. print_spec.json (76 pages, 38 sheets) is therefore wrong for the quote. Fix: insert one blank page before the first cut-out page when its print position is even (or move the Go further page), rebuild P4 (and the bw/ copy, not examined), update print_spec.json. Other five levels are correct.

**H2. Holiday decks and guides still tell children to hold paper up to the camera of a recorded class.** Owner decision 9 (docs/terms/owner_decisions.md line 49): "no paper hold-ups to the camera at all". Only the Level 1 trial deck was fixed. Slides containing "to the camera"/"hold up": l: 25, p2l: 33, p3l: 39, p4l: 29, p5l: 30, p6l: 26 slide files (e.g. split/p6l7/project/slides/p6l7-exit.html "hold it to the camera"; live decks identical); tutor guides: 17 to 42 hits each (g1 "everyone holds their paper to the camera at the same moment", repeated per lesson). Workbook pages carry the child's name. The L1 guide also contradicts itself: "take a photo and send it through the approved channel" vs "Do not make your own recordings or photos" (P1 guide, "Hold up the answer page to the camera at the end of each lesson"). Fix: apply the same wording as the Term 1 fix (tick against the answer slide, choral answers, fingers; private route via parent WhatsApp), regenerate decks and republish. Owner to confirm the rule is meant to cover the holiday program (the decision is written "at all", under the term pre-flight list).

### Medium

**M1. "Challenge Day" still on Level 1 printed pages and elsewhere despite the claimed rename.** (a) `hp/workbook_html.js:344` and `hp/workbook.js:345` `hdr(10,'Mixed Puzzles','CHALLENGE DAY!')`: the printed L1 workbook page 48 reads "CHALLENGE DAY!" while its own kit card (print p61) says "Puzzle Day"; also in hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf and the .docx. (b) `outputs/designed/Math_Inquirers_Weekly_PDFs.zip` Week5_Student_Pages.pdf (L1 parent-facing). (c) Website, listed only (not audited): website/data/level_lessons.json:50,102,154,206,258 (levels 1-5; 1-4 should be Puzzle Day), website/level_pages/ages-6-8, 7-9, 8-10, 9-11 .html and website/dist copies, website/weekly_dose_online.html:136, website/lp_build.py, website/mi_signup.html, website/referral.html, website/syllabus/index.html, extension/config/levels.json:214 ("Challenge day"). (d) Published deck titles for Levels 2-4 (known, cosmetic). Level 5 "Challenge Day" and Level 6 "Showcase Challenge" are as decided (owner_decisions.md line 129). Fix: hdr text to 'PUZZLE DAY!' and rebuild L1 workbook, weekly PDFs, print; fix website data.

**M2. Level 1 parent sheet shows a price that contradicts the website.** `outputs/designed/Math_Inquirers_What_Learners_Get.pdf` ("Planned price (to confirm)": S$650 per child, S$65 a lesson, intro S$500). website/data/beta_schedule.json: S$25 a lesson, S$250 for all 10 ("confirmed by Jasmine"). P2-P6 versions carry no price. Fix: remove the price line or take it from beta_schedule.json.

**M3. Level 1 Free Taster for Parents ships with unfilled placeholders** ("[Sign-up link or QR code]", "[Dates, fee and sign-up link]", "[Name, email or phone]", last page). Parent-facing; cannot be sent as is. (The P2-P6 tasters have none.) Weekly Email Packs: "[Your name]", "[Contact number]" are intended template fields (Low).

**M4. K2 Readiness Check reintroduces ability tiers the program says it does not use.** Decision bands tell the tutor to "set Core questions first, with Think Harder only when Core is done" and, for 22+, "offer Challenge questions early", plus "Group A". The workbook policy is that nobody is placed in a tier and every child may choose any section. Fix: reword to "offer every child the choice; point a child who needs support to Start here".

**M5. Slide-format violations in published decks.** (a) All ten P2 decks: `split/p2lN/project/slides/p2lN-challenge.html` has `<section id="p2lN-go-further">` (file name and section id differ; the slide-file contract requires id = file name; live copy identical, so the slide may not show or may be addressed wrongly). (b) `split/p3l2/project/slides/p3l2-exit.html` and `p3l2-chdiag.html` use `data:image/png;base64` image sources (not allowed in the Slides format; may render blank). I could not render the live deck to confirm either; open the live decks p2l1 and p3l2 and check before the first class.

**M6. L4 guide numbers Go further 1-3, workbook prints No.5-7.** A tutor looking for "Go further 3" will not find it on the page (guide section "Think harder and Go further questions" in each lesson; workbook pages 8, 14, ... 57). L1 uses C1-C3 in both, so only L4 (check L2, L3, L5, L6, same style) mismatches. Fix: print "Go further No.5" or relabel guide.

**M7. Live decks' speaker notes hold answers and are readable by anyone who opens the link.** Per the Slides contract the notes are readable by anyone with access; the weekly Tutor Email in the Email Packs links decks (claude.ai/artifact/...). Fine while private and sent to tutors only; do not share a deck link with families. The decks are private artifacts today (parents cannot open them).

### Low

- L1. Duplicate pill markup: split/l1 title, routine and rules slides each contain the same time pill three times (stacked, invisible but sloppy; live identical).
- L2. About 30% of each Question Bank (234 items L1; 62-78 per level) repeats workbook Think harder / Go further items word for word. Bank is described as "more" practice; say so or dedupe. (Same material, so keys are correct.)
- L3. 319 of 1,601 slides have no time pill (title/check slides carry it in the heading line, e.g. "LESSON 10 - WEEK 5 - 0-1.5 MIN" on p4l10; fine).
- L4. P4 print has two trailing blank pages (see H1).
- L5. Taster/Email pack for P2-P6 reuse the same template (not otherwise checked).
- L6. P5 L1 start-here page still carries about 250-290 words a page (Level 3 parity claimed; viewed, acceptable).

## Challenge Day vs Puzzle Day: where it remains (complete list from grep of the repo)

Correct as decided (Level 5 only): split/p5l10, p5/content/l10.js, p5 guide, p5 workbook, P5 question bank, weekly email pack, what-learners-get, scheme, tutor/data/p5l10.*.
Wrong or stale for Levels 1-4: hp/workbook_html.js:344, hp/workbook.js:345, hp/workbook_body.html, hp/workbook_full.html, hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf, hp/P1_Holiday_Program_Student_Workbook.docx, outputs/print/Math_Inquirers_P1_Workbook_PRINT.pdf (p48), outputs/designed/Math_Inquirers_Weekly_PDFs.zip (Week5_Student_Pages.pdf), plus the website and extension files in M1(c). Level 2-4 outputs (guides, workbooks, print, decks, schemes, diagnostics) are clean.

## Score per level (10 = ready to deliver as is)

| Level | Score | Notes |
|---|---|---|
| 1 | 7.5 | Content correct; stale "CHALLENGE DAY!" printed page, taster placeholders, wrong price sheet, K2 tiers, camera hold-ups |
| 2 | 8.0 | Q5(b) and strips fixes landed; go-further section id mismatch; camera hold-ups |
| 3 | 8.0 | Clean content; p3l2 data: images; camera hold-ups |
| 4 | 7.0 | Print PDF misaligned (H1); Go further numbering mismatch; camera hold-ups |
| 5 | 8.0 | Week-5 note correct; L9/L10 decks populated live; Challenge Day is intended; camera hold-ups |
| 6 | 8.5 | Scratch files all pass in the real editor; guide and workbook name the files; camera hold-ups |

## Top 10 (ranked)

1. H1 P4 print: first cut-out page backed by Lesson 10 Go further; rebuild with parity padding and refresh print_spec.json.
2. H2 Paper hold-ups to the camera still in ~180 slides and all six guides against owner decision 9.
3. M1 "CHALLENGE DAY!" still printed on L1 workbook p48 (and L1 weekly PDF, website data and pages for Levels 1-4).
4. M2 L1 What Learners Get shows S$650/S$500 vs website S$25/S$250.
5. M3 L1 Free Taster has three unfilled placeholders.
6. M5 Ten P2 decks with mismatched slide id; two P3 slides with data: URIs; verify live render.
7. M4 K2 Readiness Check reintroduces Core/Think harder/Challenge tiers and Group A.
8. M6 L4 guide "Go further 1-3" vs workbook "No.5-7".
9. M7 Speaker notes carry answers; keep deck links tutor-only.
10. L2 Banks repeat ~30% of workbook items.

## NOT audited

Colour-vs-bw print files outputs/print/bw (only page counts); term-time lessons, books, shop, soft-copy delivery, school books, extension workbooks; website pages other than grepping for "Challenge Day" and reading beta_schedule.json; Weekly Dose of Thinking Math (25 pp per level; only L1 skimmed by grep for claims/prices); Weekly Email Packs beyond placeholders; the diagnostics/placement checks beyond the Challenge Day grep; tutor console; remaining 54 live decks (only 6 read, 3 compared in full by hash; counts consistent); slide-by-slide render of any deck (live render not possible from here); Think harder and Core workbook items (only bank and Go further solved); timing realism (no child has used any material); Scratch on desktop app or tablets; L2-L6 Free Tasters and What Learners Get beyond the price/placeholder grep.
