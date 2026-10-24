# Inquiry habits: build status (holiday Levels 1-6, non-print parts)

24 Oct 2026, branch `claude/great-fermi-1hv4vc`. Design: `inquiry_skills_explicit.md`. Assignment: `inquiry_coverage.md` section 6 (each habit is the focus of exactly 10 of the 60 holiday lessons). Nothing was sent, published or deployed. Wording is process-based: children practise the habit; nothing promises a result.

## What was built (shared)

- `levels/habits.json`: single source for the six habits (child phrase, teaching move, scripted prompt), the rule "do not give the answer first", the badge label and the 60-lesson assignment. Edit wording here only.
- `levels/habit_icons/*.svg` + `levels/habit_icons.py`: six stroke icons (eye, speech bubble with ?, flask, tick in circle, speech bubble with lines, back arrow). The same icon and the words "Focus habit: <habit>" every time.
- `levels/habit_guide.js`: builds the one-line guide text "Focus habit: <habit> - <teaching move> Say: "<prompt>" <rule>".
- `levels/spine_deco.py` (called by `levels/restyle.py`, idempotent): habit badge on the title slide and the look-back (`reflect`) slide of all 60 decks, plus a `HABIT:` line in both speaker notes.
- `tutor/build_data.py`: the same line goes into `notes.json` (`habit`, `habit_line`) and into the Opening part's DO list on the tutor phone.
- `practice/holiday/hlib.py` (`habit_item`, `habit_tag`) and `build_holiday.py` (`added=True` items need no printed source line).

## Per lesson

1. Guide: front-page line under the lesson heading (`hp/guide.js`, `p2` to `p6/guide.js`), plus a front-matter section "Focus habit (every lesson)" with the six-habit table. Guide PDFs, HTML and Word files rebuilt for all six levels (`outputs/designed` copy updated for Level 1).
2. Slides: badge on the title slide (inside the "Today we will" card, right end of the tool-chip row, so it adds no height) and on the look-back slide (top left, clear of the time pill and the heading). Checked at 1920 by 1080 for all 60 decks: no overlap, no overflow, content bottom unchanged (max 910 px), second `spine_deco.py` run changes 0 files.
3. Online practice: in 45 lessons a new Start-here self-check item `hab` (open, `marking_mode='self'`, skill "Inquiry habit: <habit>", short label unique in the lesson) is inserted after the last core item; in 15 lessons the audit named an existing self-check item as the carrier, so that item's skill text gets "(habit: <habit>)" and nothing else changes. No existing id, answer, printed number or label was changed. Where the audit said "add the habit prompt to core item X" a separate new item was added instead, because editing the existing question text would change a printed question.

| Lesson | Focus habit | Guide line | Slide badges | Online practice | Build + test |
|---|---|---|---|---|---|
| 1.1 | Notice | done | done | tagged existing item `4b` | OK |
| 1.2 | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| 1.3 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 1.4 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 1.5 | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| 1.6 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 1.7 | Notice | done | done | tagged existing item `2a` | OK |
| 1.8 | Explain | done | done | tagged existing item `2b` | OK |
| 1.9 | Try | done | done | tagged existing item `2` | OK |
| 1.10 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 2.1 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 2.2 | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| 2.3 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 2.4 | Notice | done | done | tagged existing item `6d` | OK |
| 2.5 | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| 2.6 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 2.7 | Explain | done | done | tagged existing item `1x` | OK |
| 2.8 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 2.9 | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| 2.10 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 3.1 | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| 3.2 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 3.3 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 3.4 | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| 3.5 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 3.6 | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| 3.7 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 3.8 | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| 3.9 | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| 3.10 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 4.1 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 4.2 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 4.3 | Check | done | done | tagged existing item `4b` | OK |
| 4.4 | Explain | done | done | tagged existing item `4c-why` | OK |
| 4.5 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 4.6 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 4.7 | Notice | done | done | tagged existing item `5c-why` | OK |
| 4.8 | Explain | done | done | tagged existing item `3c` | OK |
| 4.9 | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| 4.10 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 5.1 | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| 5.2 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 5.3 | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| 5.4 | Explain | done | done | tagged existing item `2c` | OK |
| 5.5 | Check | done | done | tagged existing item `5c` | OK |
| 5.6 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 5.7 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 5.8 | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| 5.9 | Notice | done | done | tagged existing item `1dw` | OK |
| 5.10 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 6.1 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 6.2 | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| 6.3 | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| 6.4 | Check | done | done | tagged existing item `2c-why` | OK |
| 6.5 | Try | done | done | tagged existing item `6b-why` | OK |
| 6.6 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| 6.7 | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| 6.8 | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| 6.9 | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| 6.10 | Look back | done | done | new self-check item `hab` (label "Look back") | OK |

All 60 lessons: `python3 practice/holiday/build_holiday.py pN NN` then `python3 practice/holiday/test_holiday.py pN NN` (with `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`) gave RESULT: OK.

## What remains (not done on purpose)

- Printed workbook: habit tags on the workbook pages (the lines "Notice it: ...", "Look back: ..." in the audit table, the look-back box and the Start-here page). Held back by the print freeze (content freeze Mon 2 Nov, print order Fri 6 Nov) and because the owner has not approved habit tags in print. No file under `outputs/print`, `hp/workbook_html.js`, `pN/workbook_html.js`, qbank or gaps was touched. The online items are not printed questions; the printed workbook does not yet show the habit.
- Term Level 1 (40 lessons): not started (slides, guide, online items, workbook). Section 6.8 to 6.11 of the audit has the assignment.
- Website claims and `website/dist`, `website/mi_signup.html`, `website/level_pages`: untouched, waiting for the lawyer.
- Report field (design point 7: habit practised plus one observed example per term): not built.
- Not rebuilt: weekly PDF zips and parent packs (they slice the tutor guide and workbook), `levels/scheme.py` sentence. Republishing the 60 deck Artifact URLs needs the owner's go-ahead.
- Test proof screenshots under `practice/holiday/pN/NN/proof/` were regenerated by the test runs and are not part of this work (they were already modified before it started); the habit item is not shown in them yet.
- The audit's section 6 "Now (focus habit)" tags were found automatically; the new online items use a small self-contained task per lesson (all numbers in the question), not the lesson's own numbers. A tutor or the owner may want to review the 45 model answers.
