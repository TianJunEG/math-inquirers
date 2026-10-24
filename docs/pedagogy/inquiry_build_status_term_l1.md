# Inquiry habits: build status (Level 1 term lessons 1-40, non-print parts)

24 Oct 2026, branch `claude/great-fermi-1hv4vc`. Design: `inquiry_skills_explicit.md`. Assignment: `inquiry_coverage.md` sections 6.8 to 6.11 (each term has all six habits; no habit leads two consecutive lessons; each habit is the focus of 6 or 7 of the 40 lessons). Nothing was sent, published or deployed. Wording is process-based: children practise the habit; nothing promises a result.

## What was built

- `levels/habits.json`: new key `term_l1_lessons` (lesson 1-40 to habit). Wording, icons and the rule come from the same shared data as the 60 holiday lessons (`levels/habit_icons/*.svg`).
- `term/l1/tools/habit_term.py` (new): the slide badge, tutor-guide box and six-habit table, and the online item insert. Called from `b_deck.py`, `b_guide.py` and `b_practice.py` (a few lines each). `b_print.py` and the lesson JSON files are NOT changed.
- `term/l1/habit_items.json` (new): the 40 online self-check items (open, textarea, "Show me an example" button, skill "Inquiry habit: <habit>").

## Per lesson

1. Guide: a box under the cover ("Focus habit: <habit> - teaching move. Say: ... rule: do not give the answer first") and a front-matter section "Focus habit (every lesson): the six inquiry habits" (table with icon, child phrase, teaching move, scripted prompt; today's habit marked).
2. Slides: badge ("Focus habit: <habit>" with the shared icon) on the title slide (top left, above the lesson line) and on the look-back slide (top right, left of the minute pill); a `HABIT:` line is added to both speaker notes. Checked on all 40 decks at 1920 by 1080: exactly 2 badges per deck, none clipped, none overlapping any text or Mi; the builder's own layout check shows no new problem.
3. Online practice: one new self-check item `hab` (tier core, after the last core item) per lesson. Where the audit said "tag item X and add a self-check explain follow-up" (lessons 1, 2, 14, 17, 35, 39) the existing item was left as it is and the new item serves as the follow-up. Verified for all 40: existing ids, questions, answers, options and hints are unchanged, and the new item renders and shows its example in the runner. The new items use small self-contained tasks (all numbers in the question), not the lesson's own numbers; the 40 model answers need a tutor or owner read.

| Lesson | Focus habit | Guide | Slide badges | Online practice | Build + test |
|---|---|---|---|---|---|
| T1 L1 (lesson 1) | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| T1 L2 (lesson 2) | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| T1 L3 (lesson 3) | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| T1 L4 (lesson 4) | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| T1 L5 (lesson 5) | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| T1 L6 (lesson 6) | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| T1 L7 (lesson 7) | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| T1 L8 (lesson 8) | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| T1 L9 (lesson 9) | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| T1 L10 (lesson 10) | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| T2 L1 (lesson 11) | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| T2 L2 (lesson 12) | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| T2 L3 (lesson 13) | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| T2 L4 (lesson 14) | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| T2 L5 (lesson 15) | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| T2 L6 (lesson 16) | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| T2 L7 (lesson 17) | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| T2 L8 (lesson 18) | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| T2 L9 (lesson 19) | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| T2 L10 (lesson 20) | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| T3 L1 (lesson 21) | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| T3 L2 (lesson 22) | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| T3 L3 (lesson 23) | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| T3 L4 (lesson 24) | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| T3 L5 (lesson 25) | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| T3 L6 (lesson 26) | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| T3 L7 (lesson 27) | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| T3 L8 (lesson 28) | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| T3 L9 (lesson 29) | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| T3 L10 (lesson 30) | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| T4 L1 (lesson 31) | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| T4 L2 (lesson 32) | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| T4 L3 (lesson 33) | Look back | done | done | new self-check item `hab` (label "Look back") | OK |
| T4 L4 (lesson 34) | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| T4 L5 (lesson 35) | Notice | done | done | new self-check item `hab` (label "Notice it") | OK |
| T4 L6 (lesson 36) | Try | done | done | new self-check item `hab` (label "Try it") | OK |
| T4 L7 (lesson 37) | Wonder | done | done | new self-check item `hab` (label "Wonder") | OK |
| T4 L8 (lesson 38) | Explain | done | done | new self-check item `hab` (label "Explain") | OK |
| T4 L9 (lesson 39) | Check | done | done | new self-check item `hab` (label "Check it") | OK |
| T4 L10 (lesson 40) | Look back | done | done | new self-check item `hab` (label "Look back") | OK |

## Tests run

- `bash term/l1/build.sh NN` for all 40 lessons: 39 exit 0. Lesson 9 exits 1 only because of `LAYOUT slide s-m4 overflows (bottom 1056)`, which was already there before this work (same result when the habit code is taken out); not touched.
- `python3 term/l1/tools/validate.py NN` for all 40: 0 FAIL (27 to 30 passes each).
- Online practice: Playwright smoke on all 40 lessons (open item `hab`, type, press "Show me an example", model answer shown, no page errors): 40 of 40 OK.
- `python3 term/l1/tools/test_copy_check.py`: ok. `python3 print/check_bw.py` (reads outputs/print/bw): rc 0, every file ok, nothing changed.

## Not done on purpose

- Printed term books and workbooks, `outputs/print`, `term_books_spec`: untouched (owner has not approved habit tags in print). The printed workbook does not yet show the habit. `term/l1/out/` is git-ignored, so the rebuilt outputs are not part of any commit; no printed-book file was rebuilt or committed.
- Website, `website/dist`, `mi_signup.html`, `level_pages`: untouched. No Artifact republished, nothing sent.
- Report field (design point 7) and parent packs / weekly zips for term: not built.
- Lesson 9 `s-m4` overflow (pre-existing) left for the lesson owner.
