# Final fixes, Level 1 Term 1 (Lessons 1 to 10)

Fix pass of 23 Oct 2026 against `FINAL_AUDIT_T1.md`. Lessons 1 to 10 rebuilt with `bash term/l1/build.sh NN`; `validate.py 01..10` all 0 FAIL (10 also passes the Quest checks: Quest Log 4 pages, 100 mm bar). Embedded Mi image in all ten guides and decks is hash `5d7658` (no calculator). Not touched by this pass: shared tools (`term/l1/tools/*`, runner, schema), the website, `outputs/print/`, Term 3 lessons, `school/`.

## High

| # | Finding | Action |
|---|---|---|
| 1 | L3 and L10 outputs (and Book 1 and Book 2) show the old Mi with a calculator | Both lessons now rebuild (the copy check was fixed in commit eaa9340); L3 and L10 outputs rebuilt, all ten lessons carry Mi `5d7658`. **Open, not mine:** the print books under `outputs/print/` must be rebuilt with `print/make_term_books.py` from these outputs. |
| 2 | Validator and L10 verify script fail on a false positive | Already fixed in eaa9340 (copy check compares only external source text; L10 verify fixed). Confirmed: `validate.py 03` and `10` 0 FAIL, verify scripts pass inside the validator. |

## Medium

| # | Finding | Action |
|---|---|---|
| 3 | Paper to camera in speaker notes | L9 and L10 `s-sneak` notes now say nobody holds paper up; children keep their own answer and check at Talk time. L1 and L3 "may show their bundles / a pair to the camera" (Explore DO line and note) replaced by "keep them on the table and say the number aloud; nobody holds anything up". "Hands up on camera is fine" notes changed to "Fingers or a thumbs up are fine" (L1, L4, L5, L7). Tutor-only "show on camera" kit items (the tutor's own tray or cards) are kept: they are the tutor's objects, not children's papers. |
| 4 | Recording, greeting and camera script differs L1-5 vs L6-10 | L1 to L5 opening now use the exact L6 to L10 three SAY lines ("Cameras can be on or off, as you like"; recording sentence; "Microphone off until I ask you to speak ... Nobody holds paper up to the camera") and the same DO line ("Greet the whole group warmly. Do not use children's first names on the recording."). Removed "so I can see your page and hands" and the "check hands can be seen" DO sentences (L1, L2, L5; L3 and L4 did not have them). Wording matches `privacy.html` (tutor, shared screen and unmuted voices recorded; children may mute and keep cameras off; no first names). |
| 5 | L8 T1 repeats the class example and shows the answer | T1 now uses 56 + 17 and 54 + 19 (both 73); `verify/l08_checks.py`, answer, hint, solution and mistakes updated. Class slide (47 + 18 / 45 + 20) unchanged; the T2 near-copy of the slide's NOT THE SAME pair was checked: T2 (a) is 29 + 14 and 30 + 13, a different pair from the slide's 29 + 14 and 30 + 15 (it is a same-total case, the slide shows a different total), so it was kept. |
| 6 | Privacy notice, terms, website not updated for the term programme | **Not done (outside lessons 1 to 10; website files).** Needs an owner or website-agent pass: a term paragraph in `website/privacy.html` naming the still-stuck and Quest photo flow to the business WhatsApp with 90-day retention, a Term 1 page, and the terms fee. The lesson wording was aligned to what `privacy.html` already says (finding 4). |
| 7 | Parent story: overview, workload, practice route, pasted term line | L1 Parent Summary now has a "Term 1 at a glance" sentence (topics, Quest as a game with no marks, honest beyond-P1 statement, what to do if Start here is hard). L1 to L10 summaries end with "Each week we suggest Home Practice (about 15 minutes); pages 3 to 5 and online practice are optional." L9 `term_line` names length. L1 to L5 `next` now carry the recording and privacy sentence (also Low 22). **Not done:** "ask your tutor for the practice link" is printed by `tools/b_print.py` (shared tool); a real link route needs the tool or the owner. |
| 8 | L9 ruler is a hard dependency | L8 `next_materials` and L9 materials: "No ruler? Tell your tutor now/before the lesson, we will help you make a paper strip ruler, or a grown-up can measure your lines" (owner decision of no printed ruler kept). L9 `home_hint` no longer tells a family to ask "before the lesson" on a sheet used after it. |
| 9 | Slow-class timing uses the whole buffer | Not changed by design: needs a trial with children before cutting warm-ups. Slow totals unchanged (86:17 to 89:52 of 90; workbook 3 to 4 minutes over in the slow model, covered by the flex buffer stated in the guide). Left for the first live term. |
| 10 | L9 says ruler pictures are real size; books print at 94.3% | L9 materials, tutor notes, slide note and tutor prep no longer say children can lay a ruler on the picture; they now say read the marks on the picture, print at 100% if you can, do not measure the picture. This is true for the loose print and the book. **Open, not mine:** `term_books_spec.json` still scales pages (shared). |
| 11 | "Nobody sees your answers" in the Quest Log | Quest Log rule now: "Not a race. Skip a gate if you like. Only your grown-up and tutor see your answers." (kept the same length so the log stays 4 pages). Deck slide text "Nothing is shown to the group" is true and kept. |
| 12 | Entry profile "only counting to 20", no spiral review | `joining_cold.assumes` of L7 and L8 now state the honest entry profile (counting in tens to 100, pairs that make 10, add and take away small numbers within 10); L10 updated; L9 changed to "counting to 20 and comparing two numbers" (true for a measuring lesson). **Not done:** a review item from lesson n minus 2 in Home Practice and the 5-minute entry check: `validate.py` fixes Home Practice at exactly 5 questions with at least 3 Start here, so a review item would replace a current-lesson item; needs an owner decision and the plan open question 2. |
| 13 | Hand-off gap L7 to L8, kit duplication | L7 `next_materials` now says to keep the bars and squares from the first lesson; L3, L5, L7 and L10 kit-page text says "the same cut-outs as Lesson 1, keep them all term, cut a new set only if you lost some" (L6 and L8 already did). The seven repeated kit pages in the workbooks are a tool/book layout matter and are left. |
| 14 | Build-process wording printed in the L10 guide and quest notes | Removed the "owner decision ... built as the block challenge_quest by assets/quest_build.py" clause from `moe.note`, the "Build the quest files with: bash ..." sentence from `tutor_prep`, and "Owner decisions of 22 Oct 2026" from the Quest `plan_note`. |

## Low

| # | Finding | Action |
|---|---|---|
| 15 | "Bigger puzzles", "work out" | "Bigger puzzles" is now "Harder puzzles" (L1, L2, L3, L4, L9 choice slides; L6 and L9 own text checked); "Work out" in hints, spare menu and the L9 WORK OUT card changed to "Find" / "FIND IT" (L1, L6, L7, L8, L9). "Bigger clips" (L9) is about physical size and is kept. |
| 16 | L10 S4(d) wraps | Reworded to "12 children stand in a line. 6 more join. 12 [] 6 = 18"; page checked, the equation sits on one line. |
| 17 | Book 2 contents page | Not done (print tool). |
| 18 | Two page numbers on book pages | Not done (print tool). |
| 19 | L9 Home Practice "tell your tutor before the lesson" | `home_hint` reworded (see 8). Materials line keeps the "before the lesson" ask, which is correct there. |
| 20 | Stale wording | README status updated; L6 `moe.note` "owner or a tutor should check the placement" removed; L4 `tutor_prep` has the beyond-P1 reminder. **Not done:** "papers to the camera 30 s" in the guide's timing line is printed by `tools/b_guide.py` (shared tool). |
| 21 | L7 T1 number line labels overlap | `label_every` 20 so only 30, 38, 50, 62 and 70 are labelled; page checked. |
| 22 | No recording sentence on L1 to L5 parent summary | Added to `parent.next` (see 7). |
| 23 | Spare-time menu titles repeat | Left: the repeated titles are a deliberate routine; not a defect to change in a fix pass. |

## Numbering

"Term 1 • Lesson N" appears in the workbook, key, home and parent headers of all ten lessons with N equal to the lesson number (checked on the built PDFs, headers of lessons 1, 5, 10 read directly). Lesson 10's parent summary correctly says "Term 2 • Lesson 1" only for the next lesson.

## Needs a shared-tool or owner step (list)

1. Rebuild the print books (`outputs/print/make_term_books.py`) so Book 1 (L3) and Book 2 (L10) show the new Mi, and decide the 94.3% scaling for the L9 ruler page.
2. `tools/b_guide.py`: remove "papers to the camera 30 s" from the timing assumptions line.
3. `tools/b_print.py`: replace "ask your tutor for the practice link" once a route exists.
4. Website: term privacy paragraph (photo flow), Term 1 page, terms fee.
5. Owner: review item in Home Practice (needs the exactly-5 rule relaxed) and the entry check.
