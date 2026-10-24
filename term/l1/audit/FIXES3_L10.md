# Third fix pass, Lesson 10 (Term 1): Mi's Challenge Quest and the L11 hand-off

Changed: `lessons/l10.json`, `verify/l10_checks.py`, `AUDIT_L10.md`, `out/l10/` (old `L10_Check_*` files and `html/check_*.html` removed; `L10_Quest_*` added), new shared-by-copy builder `assets/quest_build.py`.

| Item | Action |
|---|---|
| End-of-term check to Mi's Challenge Quest | Block renamed `challenge_quest` (no `end_of_term_check`, so `build.py` skips `tools/b_check.py`). Gates 1 to 8 plus an optional secret cave, same questions and answers. Quest partner beside the child (pairs) or group quest with Mi; private paper; no score, mark, ranking or visible timer; photo return unchanged (business WhatsApp). Slides `s-check1/2` became `s-quest1/2` (`no_record`), part title, script, rec cue, guide text, tutor prep, safeguarding, parent summary/next/report line, materials updated. Make-up: plays before the recording. |
| Tutor private notes | `L10_Quest_Tutor_Notes.pdf`: gates and answers, what to look for (no R/P/N, no points, no bands), private notes sheet per child, group advice sheet for next term, one-line "what we saw" templates. |
| Parent page | `L10_Quest_Parent_Note.pdf` and the Parent Summary name the quest and promise one line from the tutor's private notes. |
| Cut-out: L10 to L11 hand-off | Goodbye script, `s-end` slide and `parent.next_materials` list the Lesson 11 cards page (cut out, in an envelope), ten small things, a coin or button, FRONT paper. |
| Validator | 0 FAIL. Verify script checks: no bands or progress words, test-like wording absent from child and parent text, quest named, slides `no_record`. |

Template changes needed (shared tools not edited):
1. `tools/b_check.py` hard-codes test-like labels (TERM n CHECK, "End-of-term check", R/P/N marks, point bands, percent rule, `L1x_Check_*` names); `build.py` should call a quest-aware generator (`assets/quest_build.py` can be promoted to `tools/b_quest.py`) and `validate.check_term_check` should check the Quest files.
2. `validate.BANNED_CHILD` bans `\bchallenge\b`, so the quest name is written with a soft hyphen (Chal­lenge) in slide and parent strings; allow "Challenge Quest" and remove the workaround.
3. `b_guide.py` prints "while the check sheet is on screen" in the no-record box (tutor page only).
4. Brand strings "Notice it. Test it. Explain why." (mascot line, parent footer) and the "63-83 MIN" tag on every slide are template-wide and were not changed.
