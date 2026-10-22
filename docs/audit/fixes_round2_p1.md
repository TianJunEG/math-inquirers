# Math Inquirers Level 1 (p1): round-2 fixes from the re-audit

Date 2026-10-22. Source: docs/audit/reaudit/reaudit_p1.md. Nothing committed or published. p2-p6 and the shared files were not touched. hp/qbank.py was not regenerated (qbank.json edited directly).

## How the fixes are applied
- New P1-only module `rebuild/p1round2.py` (text fixes applied to the final slide HTML of each deck). It is called at the end of every `rebuild/gen_l1.py` to `gen_l10.py`, so regenerating the decks keeps the fixes.
- Deck rebuild used: `python3 rebuild/gen_lK.py` then `python3 levels/restyle.py split/lK` for K = 1 to 10. No overflow on any slide (`rebuild/preview.py`, all 10 decks).
- Printed files rebuilt with the hp/ README commands (not build_level.sh): workbook HTML/PDF and DOCX, tutor guide DOCX and PDF, question bank (`node qbank_doc.js` then `docx2pdf_designed.py`), weekly PDFs zip (`weekly.py`), scheme (`levels/scheme.py p1`, run only). Copies placed in outputs/workbook, outputs/designed, outputs/schemes.
- Page counts: workbook 58 (unchanged), tutor guide 74 -> 75 (the Think harder T1-T4 answer rows are now in every lesson key), question bank 32, scheme 2.
- Verification: `python3 docs/audit/verify_fixes_round2_p1.py` (24 checks, all OK).

## Fixes made (priority order)
| # | Finding | Fix | Files |
|---|---|---|---|
| 1 | N1 "After question 3 you may choose" on pages that end at Q2 | Now "When you finish this page you may choose: carry on, or try Think harder." (all ten lessons, workbook, guide, ws1 slide notes) | hp/workbook_html.js, hp/workbook.js, hp/guide.js, rebuild/p1neutral.py |
| 2 | N2 stale T-labels, L6 | l6-key T2 -> T1; l6-teachexact T2 -> T1; l6-ws2ans T3 (Sam) -> T2 (matches workbook: T1 70c/4 coins, T2 Sam, T4 30c) | rebuild/p1round2.py |
| 3 | N3 L1 key "2) 6" vs slide | Cause was the Think harder slide differing from the workbook. Slide now shows workbook T1-T4 and the key rows are rebuilt from the bank (L1 T2 = 34 and 22) | rebuild/p1gifted.py, hp/lessons.js |
| 4 | N8 l10-key "3 small triangles" | "2 small triangles" (picture is split by one line: 2 small + 1 whole = 3) | rebuild/p1round2.py |
| 5 | N6 L9 clip/eraser | Q4 now uses the taught 1 clip = 3 erasers, with new numbers so it is not a copy of the Your-turn slide: (a) 6 clips = 18 erasers, (b) 15 erasers = 5 clips. Workbook, key, ws2ans slide and note, ws2 note, script think-aloud (also 3 erasers) | hp/workbook_html.js, hp/workbook.js, hp/lessons.js, hp/scripts.js, rebuild/p1round2.py |
| 6 | N7 L2 teachpage2 vs worksheet | Step 1 now says "12 is a big total, so big corners"; note ties it to the worksheet totals 9 and 10 (small totals, small corners) and to the hint printed on the page. Example total kept at 12 because 9, 10 and 11 are worksheet or Go-further answers | rebuild/p1round2.py |
| 7 | N9 whiteboards "held up together" | 6 try1 notes said so; about 14 more try notes just said "Whiteboards". All now: "Children write on whiteboards or paper, and may show their tutor on camera or keep it to share if they want." (L1-L10 try slides) | rebuild/p1round2.py |
| 8 | N11 / #7 L7 exit "hexagon" | Exit now asks the rectangle (4 sides, 2 long, 2 short, square corners: what is it called, how many corners). Q3c "I have 6 sides" -> "I have 3 sides and 3 corners" (triangle) in workbook, key and ws2ans. Think harder T3 (duplicated the talk-time question) swapped with the rectangles-in-a-strip item (answer 6). L10 bank core item "How many sides does a hexagon have" -> rectangle sides and corners. pentagon, hexagon, octagon stay only in the Q2 table, where the names are printed under the pictures and on the teaching slide | hp/lessons.js, hp/workbook*.js, hp/qbank.json, rebuild/p1neutral.py, rebuild/p1round2.py |
| 9 | N12 L3 C1 | "24 children voted for three fruits: apple, banana and orange." (answer banana 6, orange 12, unique) | hp/qbank.json |
| 10 | #29 / P-5 Think harder slide vs workbook | Slide now shows T1-T4 exactly as printed, labelled T1-T4; Go further slide labelled C1-C3; notes answers labelled the same. Key rows "Think harder slide" replaced by "Think harder T1 to T4" in L1-L5, L7-L10 (L6 already had T1-T5; its slide row removed). Guide text no longer says the slide has three more questions | rebuild/p1gifted.py, hp/lessons.js, hp/guide.js |
| 11 | N10 Look-back promise | Tick now "I am still stuck (my tutor will look at this after class)" in workbook, slide, guide; guide and slide notes say the tutor looks after class and checks in at the start of the next lesson in the open session | hp/workbook*.js, hp/guide.js, rebuild/p1gaps.py |
| 12 | Private-message wording | Removed "There are no private chat messages", "never a direct message", "Never send a direct message", "No private messages to children" (now "Speak with children only in the lesson itself, with a parent nearby"). Paper-to-camera practice unchanged. No new channel added | hp/guide.js, rebuild/p1gaps.py, rebuild/p1round2.py |
| 13 | Minor: "who sends the photo" | Guide: "the parent takes a photo and sends it to the tutor through the approved parent channel (the tutor never asks a child to send anything)" | hp/guide.js |
| 14 | Minor: L3 "thumbs and chat" | "thumbs up, no typing needed" on l3-title and l3-explore1 | rebuild/p1round2.py |
| 15 | Minor: l3-explore1 Pear vs workbook Watermelon | Row label now Watermelon (slightly smaller font so it fits) | rebuild/p1round2.py |
| 16 | N4 stale Question Bank | Rebuilt from current qbank.json (the stale L1 S4 "Start at 50 take away 7" wording is gone; L6 S4 current) | hp/Math_Inquirers_P1_Question_Bank.*, outputs/designed |
| 17 | N5 stale Scheme of Work | Rebuilt from current lessons.js (L6 "30c with 20, 10, 5", L7 new exit, no stale "3 by 3 grid") | outputs/schemes/Math_Inquirers_P1_Scheme_of_Work.pdf |
| 18 | Side bug found | `p1neutral.SUBS` appended " together" every run (l8-warm1 read "together together together"). Entry made idempotent, slide cleaned | rebuild/p1neutral.py, rebuild/p1round2.py |

Also refreshed from the new workbook and guide: weekly PDFs zip.

## Left, and why
- #10 L3 (keys of 3, tally, half pictures on one page): a lesson-structure change (moving half-pictures to Go further reshuffles pages and the page map). Needs a design decision.
- #27 / P-2 movement break at about minute 55: timing change across lessons; the 1-minute stand-up at 68 stays.
- P-3 Look-back reduction to 4 ticks and one sentence stem: redesign touching workbook, slide, guide script and keys; the promise and wording defects are fixed (items 11, 12).
- N13 L8 riddles and odd-one-out taught for the optional Q5/Q6: teaching-time decision.
- Online sneak-peek option "everyone holds paper to the camera at the same moment" (answers visible in gallery view): left as is, per the instruction to keep the paper-to-camera practice unchanged. Worth a safeguarding check by the lead.
- Gifted-rubric gaps (multiple methods, student-led, "next time I will", compacting): not content defects, not attempted.
- Stale published decks: the Claude Slides artifacts need republishing from split/l1 to split/l10 (lead's step).

## Shared-file issues (not edited)
- `hp/parent_pack.py` (Weekly Dose of Thinking Math, reads qbank.json): hp/Math_Inquirers_Weekly_Dose_of_Thinking_Math.pdf and outputs copy are stale; re-run after this pass (L3 C1, L7 T3 swap, L10 core hexagon item changed in the bank).
- `hp/weekly_level.py`, `levels/mkextras.py`, `levels/scheme.py`: not edited. scheme.py ran fine for p1 and shows the current exit tickets. mkextras.py builds P2-P6 banks only.
- Readiness tracker and weekly email pack were not rebuilt: mk_pack picks challenge[...] items by index and none of the picked items changed (checked: (3,2), not the L3 C1 slot at index 4).
- Concurrent work by other sessions: other agents committed WIP to this branch while this pass ran (git log shows "WIP: round-2 content audit fixes"); my edits were swept into those commits. I did not commit.
