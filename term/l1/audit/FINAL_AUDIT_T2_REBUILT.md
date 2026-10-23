# Independent audit: Level 1 Term 2 (lessons 11-20) and rebuilt term books 1-4 (commit 9f7231a)

Report only; nothing fixed. Method: every workbook, exit, home-practice, investigation, talk and Quest item solved independently from the lesson JSON (not from the verify scripts); built answer keys and workbooks checked against the JSON by text match (0 mismatches); all pages of Books 3 and 4 (colour and B&W) rendered and viewed; samples of every home pack and answer key viewed; Term 1 books 1-2 covers and contents viewed; page counts, blank backs, kit scale, image hashes checked by script.

## Verdict: YES AFTER LISTED FIXES

Arithmetic and answer keys are correct, the FINAL_FIXES_T2 claims hold in the built files, and the books are structurally sound. Release is blocked only by the two Medium items marked "before release" (numbering on covers and contents, and the L16 B&W shading), plus the Term 1 recording-order inconsistency (compliance wording). Everything else is cosmetic.

## What checked out
- All items in L11-L20 recompute (workbook, exit, home practice, investigations, talks, Quest gates 1-8 and secret cave). Built answer keys match the lesson data. L20 Quest Gate 6 answers 15 and 11 (book 4 key p24 and L20_Quest_Tutor_Notes.pdf).
- Lesson timings sum to 90 in all ten; Quest sits after the break in L20 (and L10); no "test"/"exam"/score wording on child or parent pages; no prices; no MOE/GEP/SASMO claims (the GEP/exam words appear only as "words to avoid" in tutor notes); beyond-syllabus items are stated (odd/even, times, 3 and 4 tables, money, picture equations with x).
- Mi: every built HTML, deck, guide and book uses the no-calculator image (hash 9bea0496); "calculator" appears once, in the L20 Quest tutor rules (not Mi).
- Parent summary L11-L20: each one page. Recording notice identical in L11-L20 and in the correct order (greet, notice, then "Start the recording now"); parent sentence agrees with website/privacy.html on mute-at-registration and a private link.
- L19 kit page 7 is 15 drawn shapes, three of each. L14 S3 chart is a 2 x 10 table with large numerals. L17 S1 hint says 8, G1 stem has (a)(b)(c). L19 shape items, L20 tokens page present.
- Books: covers, all ten lesson titles in contents, contents page numbers match actual pages, book page numbers run on, every kit page on a recto with a truly blank back (colour and B&W), kit pages print at 100% (content width identical to the source kit PDF; other pages at 94.29%), B&W page counts equal colour counts for all 12 books (46/22/12, 46/30/14, 44/22/12, 48/28/14). B&W files are 1-bit 600 ppi images: no colour, no grey pixels.

## Findings

### High
None.

### Medium
M1 (before release). Numbering mismatch on covers and contents. Cover and contents of Books 3 and 4 (and home pack and answer key covers) say "Lessons 11 to 15" / "Lesson 11..." but every page header, footer and answer-key title reads "Term 2 - Lesson 1" (Book 3 p3 onward; Book 4 p3 shows "Term 2 - Lesson 6"). A family looking for "Lesson 11" finds "Lesson 1". Confirms the known open item. Related: Term 1 L10 goodbye slide, next-materials and parent text say "Lesson 11" for the first Term 2 lesson (lessons/l10.json, "Next term starts with Lesson 11"; "Cut out the cards on the Lesson 11 workbook kit page"). Quest notes also mix "L13" and "Term 2 Lesson 3".
M2 (before release). L16 T1, Book 4 workbook p5, B&W: text says "the top 2 rows are shaded" but the pale-yellow shading was dropped in B&W, so the dots are uniform and the cue is gone (colour p5 shows it). It is the only pale-yellow highlight in the books (checked by pixel search). Needs hatching or a bracket.
M3 (compliance, before release). Term 1 lessons 1-10 still start the recording before the notice (script order SLIDE, REC, then the "this lesson is recorded" line, in l01-l10.json; the T2 fix reversed this for L11-L20). Book 2 contains L6-L10. Same defect the T2 audit fixed; Term 1 and Term 2 are now inconsistent and privacy.html says the group is told at the start.
M4. Quest Log (3 pages, L20_Quest_Log.pdf) is not in any printed book; the Book 4 home pack note says "we send you the Quest Log a week before" and the L20 opening needs "your closed Quest Log". Fine if tutors send it, but the paid printed set is not self-sufficient on the one lesson that needs it.
M5. L14 T3(c) (Book 3 p29): "Odd + odd is odd. Circle one: Always / Sometimes / Never." The printed sentence asserts the false claim; reads better as "Odd + odd is ___ odd." Answer is Never.

### Low
L1. Start here timing: L11 about 18 of 17 minutes, L12 18.5 of 16.5 (timing notes state it; buffer absorbs it; confirm in a live class). Not blocking.
L2. L20 Investigation (tutor look_for, answer key p. L20 investigation): says "a child who finds $3 for both packs" but the answer is $4 for both. Also L20 G2 guide hint: "then what is left from $20" but Mei has $30 (guide and key hint only; workbook is correct).
L3. L20 T3 "Wei pays $24 for 6 such cups" follows T1 (4 cups for $12 = $3 each); "such cups" can read as the T1 cups. Page header "Such cups are cups the same" is awkward.
L4. B&W books use halftone stipple/hatch fills (tier chips, No. tags, table headers, bar fills, shape cards). Technically 1-bit, but a visual grey; bold text on stipple chips is busy. Cues survive in words and shapes (tier names printed, counters R/Y letters and solid vs dotted, shapes distinct), and L16 aside, no colour cue is lost. The cover is a large solid-black block (toner).
L5. Kit page text "Print this page on its own sheet, or on one side only" is wrong for a bound book with blank backs (shared tool b_print.py; also "Nothing to cut ... print on its own sheet" on mats). Contents note on every contents page is clipped at the right edge ("keep them in an e..."). Book 2 contents L6 subtitle reads "Hop" (truncated strand). Cover tagline unchanged.
L6. L19 shape-card page says each shape "is big enough to hold 3 counters"; the shapes are about 18 mm and the kit counters about 12.5 mm, so three do not fit. Kit pages are mostly empty below the cards (L11, L13/L14 cards, L19).
L7. L17 G1(c): six answer blanks render as three ragged dashed lines (Book 4 p14). L12 kit and L18 kit alternate yellow/blue strips; in B&W alternate stipple/white (fine).
L8. print/bw_spec.json lists only Book 4 workbook (overwritten); no record of the other 11 B&W files.
L9. L15 and later: parent page omits the retention sentence and the "cameras and names are not recorded" line (owner open item, privacy.html still a draft); privacy.html does not say outright that unmuted voices are recorded.
L10. Look-back checkbox text is very small on all workbooks (shared template).

## Owner-decision checks
90-minute lessons: yes. Quest in L10/L20, after break, no scores: yes. No end-of-term check: yes (no test wording). Beyond-syllabus item named in every lesson: yes. Originals only: items are plain original stories; no copied contest items found. No prices, no MOE/GEP/SASMO claims: confirmed.
