# Independent audit: strategy card and common look-back rollout (Levels 1-6, 60 lessons)

Audit date 23 Oct 2026. Report only; nothing was fixed. Files audited were the CURRENT local files on branch claude/great-fermi-1hv4vc. Tracked decks were not modified: the idempotency test used a temp copy.

## Verdict on republishing the 60 decks

**YES.** All 60 decks (split/l1..l10, p2l1..p6l10) pass every deck check below and none is NOT ready. One caution: if the owner wants any tool re-mapping from M1 below (L1.4, L1.7, L3.9, L5.1, L6.9), make it BEFORE republishing, otherwise the 60 URLs need a second republish. `split/l6s` is the Level 1 lesson 6 trial deck and stays out, as the spec says. `outputs/deck_urls_all.json` has 60 lesson keys plus `l6s` and `_republished`; `outputs/deck_urls_p4_p6.md` has all 30 P4-P6 ids.

## Method

- Static check of all 60 decks (deck.json order vs files, duplicates, chip, tool slide or badge, reflect wording and timer against levels/spine.json, Mi placement, "camera" text).
- Idempotency: copied levels/ and split/ to a temp dir, ran `levels/restyle.py` on all 60 decks twice: 0 files changed on both runs, and the result is identical to the tracked decks (diff -rq empty).
- Playwright and Chromium at 1920x1080, with the repo fonts, on every slide of every deck (about 1,650 slides): per-line text rectangles, SVG and Mi image boxes, overlap and out-of-slide test.
- Tutor data (tutor/data/*.public.json), workbook PDFs (pdftotext and rendered pages), B&W print files (pdfimages, ink per page, check_bw.py), guides (pdftotext), kit cards (rendered).

## Findings

### High

None.

### Medium

**M1. Tool-to-lesson fit (content judgement, the mapping data matches the spec exactly for all 60 lessons).**
- **L1.4 Pattern Inquiry** (main: Try something simpler). The lesson (workbook Q1-Q6) is "find the 8th, 10th, 12th, 30th item of a repeating pattern", which is Spot the pattern; only Q7 (sticks table, 1, 2, 3 triangles) builds small cases. "In content (build 1, 2, 3)" is only half true. The deck chip, tool slide, card and guide all say Try something simpler ("Try it with smaller numbers first"), and "Spot the pattern" appears only as "also". Consider swapping main and also, or adding a "try 3, 4, 5 first" line.
- **L1.7 Shape Safari** (Act it out). Content is counting shapes in a picture, a sides-and-corners table and "who am I" riddles. Nothing is acted out. Make a table or Spot the pattern fits better.
- **L3.9 Measure and Money Masters** (Draw it). Content is unit conversion, ordering masses and a $20 shopping choice; a bar or number line is not the main move. Make a table or Guess and check fits better.
- **L5.1 Million Puzzles** (List every way). Place value and a digit-riddle (clues, check every clue) is closer to Guess and check or Work backwards.
- **L6.9 Data Detectives** (Draw it). Content is mean, balance check, median and mode. Draw it is weak; Work backwards (the 4th score, the 5th score) is in the lesson and is "also".
- L5.9 and L6.5 (Try something simpler) fit reasonably: L5.9 Q1 starts from 1, 2, 3 tables; L6.5 Q1 builds up in stages. Neither tells the child to try 2, 3, 4 friends before the 7-friend handshake problem (Q4), so "in content (2, 3, 4 friends)" is generous.
- Fine: all other 52 lessons are a defensible fit.

**M2. Level 1 tutor guide still describes the old look-back.** `hp/Math_Inquirers_P1_Tutor_Guide.pdf` page 5 (front matter, timing table "Look-back (three minutes, minutes 85 to 88; 87 to 90 in Lesson 10)") still says the box has "Something I did well", "The hardest part ..." (retired rows). The new lesson script is correct; only this table cell is stale. Levels 2-6 guides are clean. (Source: hp/guide.js, probably the old timing-table sentence.)

**M3. Compact strategy cards drop the definition and "Also useful" line in 21 of 60 lessons.** Spec fallback allows it, but the card then no longer matches the deck tool slide and guide. Lessons: L1 3, 6, 7; L2 4; L3 3, 5, 7, 10 (Level 3 lesson 10 is the slim choose row); L4 5, 8, 9; L6 1, 2, 3, 6, 7, 8, 9. Level 6 has 7 of 10 lessons compact; its card for lessons 1-3 and 6-9 also has the Scratch-file note squeezed beside it in tiny type, and the "Start here" pill and hint line are pushed together (visible on L6.1, L6.2). Readable, but cramped.

**M4. `outputs/print/bw/bw_spec.json` has only 4 rows (P2, P3, P5, P6).** P1 and P4 B&W files exist and pass (64 and 76 pages) but are missing from the spec. `outputs/print/print_spec.json` (colour/print) is correct for all six.

### Low

- **L1.10 deck order.** `l10` order ends `... exit, end, reflect`: the trophy "end" slide (with Mi) comes BEFORE the Look back slide, and Mi is on end, reflect, break and title (4 slides). Levels 2-6 lesson 10 end after reflect (p3l10 and p5l10 use the unprefixed id `end`). Looks like the "lesson-10 exception" but check that the ending is intended.
- **Level 1-3 look-back wording by band.** Guide script (spine.json `script.lookback_say`) uses the band A wording for all levels, while Level 5-6 decks and workbooks show the longer band C prompts. Tutor reads "did I answer the question?" while the slide says "...that was asked (with units or a reason)?". Minor mismatch.
- **Tutor timing.** Level 1 Lesson 1 Opening is 4 min and Lessons 2-10 is 2 min; Levels 2-4 are 1.5 min. The Opening tool line (about 20 s) plus the 20 s title cue in 1.5 min is tight; unstopwatched.
- **Look-back box position.** It is on the "Choose, then look back" page, not the physically last page of each lesson (Think harder and Go further pages follow it). This matches the spec wording ("Before you go" page).
- **Pre-existing, not spine:** `p6l5-teachhand` has the yellow "In code (Q6)" bar overlapping the last card; the table slides `l10-we3`, `p2l10-teachgrow`, `p3l3-teachgrid`, `p4l9-we2` and `p5l1-we2` trigger my overlap test because of table cell positions (no visible clash expected); `p4l2-we1` label vs SVG. None involve spine elements.
- Workbook look-back tool icons are about 7 mm, below the spec's 10 mm, but still recognisable in the B&W file (viewed). Level 5 B&W pages are laid out for the 794/850 scale (spacer in `p5/wb_pdf.py`; visible as a slightly narrower page body). Do not remove it.
- 17 extra "Try something simpler" hint lines exist in spine.json (`hint`) but were not added to guide hint ladders (known; build notes).
- `spine.json` (09:57) is newer than the Level 1-5 workbook builds (09:28-09:55). The timer values affect only decks and guides, which were rebuilt after; the workbook look-back has no timer, so no drift found.

## Results by area

### 1. Decks (60)
- Title chip: exactly 1 per deck, name correct for all 60 (L10 shows "choose" with all eight icons).
- Levels 1-3 (30 decks): `<deck>-tool` slide directly after title, correct tool name and band definition in all 30 (checked against spine.json); pill copied from the title. Levels 4-6: one talk-slide badge per deck with the right tool; p6l10 has `showcase` instead of `talk` (no badge, chip only, by design).
- Look back slide: exactly one per deck; three prompts in the right band wording and a timer label match spine.json (120 s L1, 90 s L2/L3/L4/L5, 75 s L6; wait: L3 and L4 use band B 90 s, L2 90 s override, L5 90 s override, L6 75 s). "Something I did well" is gone from all decks and workbooks.
- No duplicate ids, chips, badges, SPINE notes or pills in any deck. Idempotent (see Method).
- Mi: only on title, break and the last slide (reflect, or end in lesson 10: p2l10, p4l10, p6l10 end; p3l10 and p5l10 `end`; l10 has end and reflect).
- Overlap or overflow: 0 problems on any title, tool, talk, reflect, break, exit or end slide in all 60 decks (see Low for the pre-existing teach slides). Rendered and viewed samples: l4 tool and title, p3l9 tool, p4l8 talk, p5l9 reflect, p6l10 title, p2l2 reflect; Mi clear of the look-back card.
- No instruction to hold paper up to the camera in any deck or guide; every match is a negative ("nothing is held up to the camera").
- Slide counts: 23-30 (Levels 1-3 +1 slide for the tool slide; Levels 4-6 unchanged); sensible.

### 2. Tutor data
Every lesson sums to exactly 90 min (60 of 60). `tool` maps to Opening, `reflect` to Look-back / Looking back / Exit-and-close part, and tutor slide ids equal the deck order in all 60 lessons. Level 4: Looking back 2.5 and Talk 4.5 (5.0 in L4, L7, L8, which were 4.0 before), Opening 1.5; deck pills agree (talk 79.5-84, exit 84-87.5, reflect 87.5-90; lesson 10 talk 76-80.5, exit 80.5-85, reflect 85-87.5, end 87.5-90). Correct.

### 3. Workbooks
- Card on the "Start here" page: 10 of 10 per level, tool name matches spine.json for all 60; lesson 10 shows eight icons with "I chose". Look back box on the lesson's Choose/look-back page: 10 of 10 per level with the right band wording.
- Page counts, designed / print / B&W: L1 58/64/64, L2 62/70/70, L3 58/64/64, L4 66/76/76, L5 57/62/62, L6 55/58/58. All print counts are even and equal print_spec.json; quote_request.md Level 2 row is 70 pages and 35 sheets. Level 2 source pages fell 66 to 62 (reflow), noted in the build notes; no lesson lost content.
- No page overflow seen in viewed card and look-back pages for all six levels (contact sheets).
- B&W files: every page is a single 1-bit gray image (pure black and white); `check_bw.py` on P1: non-grey 0, light-tint cells 0.133. Blank pages are only the backs of the cut-out pages at the end (L1 54-64, L2 56-70, L3 54-64, L4 58-76, L5 54-62, L6 54-58; even pages only), counts equal print_spec blank_pages. No content page sits behind a cut-out.
- Icons are legible on viewed B&W pages (L1 p3, L3 p13, L4 p43, L5 p48, L6 p3 and p5); the card icons are about 12 mm, the look-back icons small (see Low).

### 4. Tutor guides
All six guides: "Today's tool is <name>. <band definition>" present 9 times (lesson 10 uses "Today you choose the tool", 1 time), "Where did you use <name> today" 9 times, and the look-back script ("Pick one problem from today") 10 times; the name and definition match spine.json for all 54 non-choose lessons. Page counts L1 94, L2 112, L3 104, L4 103, L5 113, L6 107. Level 2 and 5 add the "check together" line. See M2 for the one stale sentence.

### 5. A5 toolbox cards (outputs/kit)
Three bands (A, B, C), B&W print PDFs (A5, 2 pages, 1-bit) and colour screen PDFs. Colour PDF text for band C matches spine.json definitions and prompts word for word; the code builds directly from spine.json and the files (10:01) are newer than spine.json (09:57). Rendered A and C front and back: legible, eight icons readable, answer lines and tick boxes present. Not checked: B-band render (same builder).

### 6. "Try something simpler" lessons and wording
- L1.4, L5.9, L6.5 are as in the spec; see M1 for fit. Band wording is right: A "Try it with smaller numbers first", C "Solve 1, 2, 3 cases first, find how the answer grows, then handle the real size".
- Ages 6-8: definitions are short and concrete ("Write each way down, in order, so none is missed" is long for age 6 but fine read aloud). Ages 11-13: "Tabulate cases, find the change in each column, extend or generalise", and the Look-back prompt 1 "(with units or a reason)" are correctly more formal. Band B look-back prompt 2 adds "(Is it about the right size?)" which is useful. No wording problems found beyond the guide mismatch in Low.

## Decks NOT ready
None.
