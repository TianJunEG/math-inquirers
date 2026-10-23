# X10 Quest v2 and Term 1 reframe: hand-off to the books job

23 Oct 2026 (night). Owner decisions: X10-BEFORE, T1-REFRAME-NOW, PRIVACY-REWORD, three-word scale in private tutor notes only. Nothing pushed; books NOT rebuilt.

## What changed (this job)
- `term/l1/tools/b_quest.py`: Quest v2, opt-in per lesson through `challenge_quest.tool_row` (list of tool ids from `levels/spine.json`, or `"term"` for the default row of tools met by that term). Details in `term/l1/AUTHORING.md` ("Quest v2").
  - Quest Log: tool row under every gate (card names + small icons, plus "In my head"), "I checked" tick, a Mi-says rule line, optional because line in the secret cave (`optional.because: true`).
  - Quest Tutor Notes: Tool column, the four habits with the PRIVATE three-word scale (with help / with a prompt / on their own), tool-words patterns for the line to the grown-up, "tools that fit" per gate (`questions[].tools`), words-to-avoid list extended.
  - Grown-up note: one sentence about the tool row. No scale words anywhere on child or parent pages (`BAN_FAMILY` now bans "with a prompt" and "independence scale"; `validate.check_quest` uses the same list).
  - `lesson: "mixed"` gates are supported (label "mixed").
  - Privacy: any `privacy_checklist` line with "no tally ... not even in your own notes" is replaced at build by `PRIVACY_TALLY_LINE` (prints a NOTE until the lesson file is reworded). `build_quest(d, pw, out_root=None)` can build to a scratch folder.
- Lesson 10 (Story Steps) reframed (option B): Quest moved to minutes 35 to 55, Remember tool slide s-rem5, Explore/Mini/Talk/Look-back tool words, Quest v2 on (tool row, gate 8 mixed, cave because line, quest map off), reworded privacy line. `verify/l10_checks.py` updated (mixed gate counts as lesson 10; minutes 35 to 55; 24 min slow limit). Lesson 9: three next-lesson lines now say "choose a tool". Lesson 4: no change (the plan lists lesson 4 changes only for option A).
- Docs: plan section 1 privacy bullet, term_review 9/11 notes, AUTHORING.md, AUDIT_L10.md.

## What the books job must change
1. Rebuild Book 2 (lessons 6 to 10): lesson 10 workbook, Quest Log (still 4 pages, 10 cm bar 100.00 mm), Quest Tutor Notes (now 9 pages, was 7: key book page count and the even-page check change), Quest Parent Note (1 page), Home Answers, Parent Summary, Tutor Guide, Deck. Lesson 9 parent summary and guide changed (hand-off lines): Book 2 again.
2. Re-run the quote page counts (`outputs/print/term/term_books_spec.json`, `docs/printing/quote_request.md`): Book 2 key-book pages +2 (tutor notes); Quest Log unchanged at 4.
3. Loose `L10_Quest_Log.pdf` and `L10_Quest_Parent_Note.pdf` for families are regenerated (tool row added).
4. Other Quests (L20, L30, L40) still build as before (checked 4/3/4 pages) and print the NEW privacy line and scale strip? NO: the scale strip, tool row and parent sentence appear only when `challenge_quest.tool_row` is set. Only the privacy line is replaced for them automatically. The Term 2 and Terms 3-4 agents must add `"tool_row": "term"` (and rewrite the old privacy line in their JSON; builder output is already right).
5. Page budget warning for them: tested on the current L20, L30, L40 with `tool_row: "term"`: Quest Logs grow to 5, 6 and 7 pages (rows of 6 to 8 tools take about 14 mm per gate and the pages are 95%+ full). Re-tag gate pages (`questions[].page`, `page_instructions`, `sheet_pages`) when writing the v2 Quests; a 4-page log needs about two gates per page, quest_map false and a shorter Mi-says list. Cost if a log needs one more page: one sheet (two pages) in Book 4, 6 or 8.
6. Quest Tutor Notes have loose page breaks (pages at 6% and 21% fill); fine for tutors, but check the key-book layout.

## Dependencies and open points
- Tool names: Term 1 tool row is Draw it, Act it out, Spot the pattern, List every way (plan section 1). The spine design agent's `spine_term.json` also uses Work backwards (lessons 6, 7) and Try something simpler as "also"; the row shows four only, as the plan says. The strategy card (apply_spine_term.py) must reach lessons 1 to 9 so children have met the names; lesson 10 is marked "choose" there.
- Workbook: no "tool I used" tick yet (spine routine's common look-back covers it); lesson 10's look-back "helped" list now shows the four tools and "I checked".
- Only one mixed gate in Term 1 (gate 8): a second would unvisit lessons 6 and 7 (gate 5). Owner may want a second.
- The scale strip says it is deleted with the child's notes sheet; carrying words across blocks (the "direction over the year" idea) is not set up. Owner question.
- `build.sh 09` exits 1 on a pre-existing layout warning (slide s-m4 overflow, a diagram agent's area), outputs are built.
- Quest timing: lesson 10 slow-class script is 89:48 of 90:00 (tight); first trial run should check the Quest pace with tool circling.
