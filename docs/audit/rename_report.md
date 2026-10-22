# Level rename report: "P1".."P6" become "Level 1".."Level 6"

Branch audit-fixes. Nothing committed or pushed. Date: 2026-10-22.

## Rule

1. Every user-visible level name is "Level N" (never a bare "L3": lessons keep "Lesson N" or "L1" to "L10").
2. Output file names are `Math_Inquirers_Level{N}_...` (workbook, tutor guide, question bank, weekly email pack, what-learners-get, free taster, scheme of work, weekly PDFs zip, Weekly Dose of Thinking Math, diagnostics, and the .docx versions). Intermediate guide docx files are `Math_Inquirers_Level{N}_Holiday_Program_Guide.docx`.
3. Kept unchanged: internal names `p1`..`p6`, `hp/`, `split/pN*`, `rebuild/gen_pN*`, JSON keys (for example `"level": "P3"` in `diag/content`), slide ids, folder names.
4. Kept unchanged: school-year hints ("covers P3 topics", "Primary 3 topics", "going into P4", "Primary 6 students after the PSLE") and syllabus references ("a P3 topic", "P6 preview", "Seven P6 pupils", "See you in Primary 5!").
5. Not touched (historical): `docs/audit/*`, `docs/stories/*` (dates, codes, old file names in their verify scripts), `p1/` and `outputs/older/` (the older P1 enrichment worksheet set, whose "P1-1" codes and "Class: P1-" are school-year/worksheet codes).

How level names were rewritten (regex rules, then manual edits):
- `Math Inquirers P3` becomes `Math Inquirers Level 3` (decks footers, deck titles, workbook footers, tutor guide cover, content comments).
- `PRIMARY 3` (covers, title slides, badges) becomes `LEVEL 3`; `Primary 3 Holiday Program` (certificate) becomes `Level 3 Holiday Program`; `P2  •  LESSON 3` (title slides) becomes `LEVEL 2  •  LESSON 3`.
- File names `Math_Inquirers_P3_...`, `P3_Holiday_Program_Guide.docx` become `Math_Inquirers_Level3_...`.
- Level 1 generic names (no P in the name) also gained the level: `Weekly_Email_Pack`, `What_Learners_Get`, `Weekly_PDFs.zip`, `Weekly_Dose_of_Thinking_Math`, `Free_Taster_for_Parents` became `Math_Inquirers_Level1_...`.
- Extras (`levels/mkextras.py`): short name is "Level 3 (ages 8-10)"; the label that was "Ages 8-10 (covers P3 topics)" is now "Level 3 (ages 8-10, covers P3 topics)" (hint kept verbatim). Level 6: "Level 6 (ages 11-13, after the PSLE)". The taster sentence "Lesson 1 of the Primary 3 holiday program" is now "of the Level 3 holiday program". Two nested bracket sentences in the weekly email pack were flattened.
- Website: sign-up page list and level select, footer and sample-puzzle tag now read "Level N (ages X-Y, covers PN topics)"; hub FAQ "Levels are named by age" now says levels are numbered Level 1 to Level 6 with an age band; referral page tags read "Holiday program · Level 1", the share text reads "Level 1 holiday program", and the "P2 · P3 · ?" tile reads "Level 2 · Level 3 · ?".
- Diagnostics content: "Ages 7-9 (P2)" became "Ages 7-9 (Level 2)", matching the "(Level N)" wording `diag/build_diag.py` already used.
- `docs/levels_and_placement.md` rewritten to Level 1 to Level 6 with the age band and typical school year columns; README gained a "Level names" note.

## Counts

- Regex pass: 1,896 replacements in 1,724 files (Math Inquirers PN: 1,781; PRIMARY N: 49; file names: 35; Primary N Holiday Program: 19; title-slide codes: 12), plus about 60 manual edits in 43 files.
- 1,764 files modified (1,515 of them slide html or deck.json under `split/` and `deck/`), 76 old-named outputs deleted, 6 renamed (Level 1 weekly email pack html/docx/pdf in `hp/` and `outputs/designed/`), 70 new Level-named files created.
- Rebuilt: all 6 workbooks (pdf), 5 tutor guides (docx + pdf + html), 5 Weekly PDFs zips plus the Level 1 zip, 6 Weekly Dose PDFs, 6 schemes, 5 sets of extras (question bank, weekly email pack, free taster, what-learners-get for Levels 2 to 6), 12 diagnostics, Level 1 workbook/guide/question bank/trial lesson/taster/what-learners-get, brand style PDFs (`outputs/brand`), website pages (`website/lp_build.py` and `website/hub/build.py`).

## Files changed (by area)

- Scripts: `hp/` (guide.js, workbook.js, workbook_html.js, qbank_doc.js, trial6.js, wb_pdf.py, weekly.py, mk_pack.py, parent_pack.py, parent_pack_level.py, lessons.js comment), `p2` to `p6` (data.js, guide.js, kit.js, wb_pdf.py, workbook_html.js, SPEC.md, content/*), `levels/` (mkextras.py, scheme.py, build_level.sh, mklevel.py, normfoot.py), `rebuild/` (gen_pNlM.py footers, titles, title-slide text; p4_pagecheck.py path), `taster/`, `wbstyles/`, `diag/` (content json, build_diag.py docstring), `deck/gen2.js`, `website/` (lp_build.py, hub/qa.py, referral.html, built mi_signup.html and parent_questions.html), `docs/levels_and_placement.md`, `review/lesson_review.md` title, `outputs/deck_urls_p4_p6.md` headers (the reader regex in mkextras was updated to match).
- Decks: every slide html and deck.json under `split/pNlM` (footers "Math Inquirers Level N Holiday Program", deck titles, title-slide kickers), `deck/project/deck.json`, plus one slide text ("from our Level 3 lessons").
- Outputs: new names under `outputs/designed`, `outputs/schemes`, `outputs/workbook`, `outputs/diagnostics`, `outputs/brand`, `hp/`, `p2` to `p6`.

## Verification

- `pdftotext` over every PDF, docx and zip member in the repo (excluding docs/audit, docs/stories, p1, outputs/older): no level-name "P1".."P6" or "Primary N" remains; the hits left are the kept school-year and syllabus items listed below.
- Page counts are unchanged for all rebuilt PDFs. Covers, tutor guide title (wraps to two lines, not clipped), taster covers, what-learners-get (still one page for Levels 2 to 6), workbook badge, scheme headers and sample title slides were rendered and checked: nothing clipped.
- All modified json parse, all modified python compiles, all modified js passes `node --check`. mkextras self-check is OK for Levels 2 to 6.

## Notes and caveats

- Decks were updated in place (same text substitution applied to the `rebuild/gen_*` sources and to the built slides) rather than regenerated. Reason: the p3 gen scripts no longer run from source (`rebuild/p3_stories.py` fails with `KeyError: 'try_it'`), so regenerating would lose the later fix-pass edits. The change is text-only, so `levels/restyle.py` output is unaffected. The gen sources carry the same text, so a future regeneration gives the same wording.
- `outputs/designed/Math_Inquirers_Level1_Weekly_Dose_of_Thinking_Math.pdf` was copied from the fresh `hp/` build. The old `outputs/designed` copy was stale (older than `hp/qbank.json`); the question picks differ slightly from the old copy, which is the current qbank content.
- The Level 1 Scheme of Work now uses the current script wording ("children whose school year covers Primary 1 topics"); the old pdf was built from an older script.
- Level 1 "What Learners Get" has no generator in the repo: the docx header line was edited ("Primary 1" to "Level 1") and the pdf regenerated with `hp/docx2pdf_designed.py`. The Level 1 weekly email pack has no level text, so its files were renamed only. Level 1 question bank cover subtitle is "Level 1".
- Level 1 arguments used for `docx2pdf_designed.py`: tutor guide `"Math Inquirers Level 1 Tutor Guide" "Holiday program for Level 1" "Math Inquirers Level 1 • Tutor guide"`; question bank `"Math Inquirers Question Bank" "Level 1" "Math Inquirers • Question bank"`.
- Files with no P in their name and no level wording were left as they are: K2 Readiness Check, Lesson Review, Progress Notes, Lesson 6 Trial (its header now says LEVEL 1).

## Ambiguous hits kept (school year or syllabus, not the level name)

- "Children whose school year covers Primary N topics", "covers P1 topics" style hints (guides, scheme, diagnostics sub-line "Covers Primary 3 topics", website, hub), "going into P4" (guides, specs).
- "Primary 6 students after the PSLE" (Level 6 guide audience row and subtitle).
- "Level: P2 adds and subtracts money in dollars only..." (`rebuild/gen_p2l6.py` tutor note: syllabus statement; changing it would read "Level: Level 2").
- "Equivalent fractions are a P3 topic", "division with a remainder, which is a P3 topic" (Level 2 notes); "P6 preview", "a P6 skill", "Primary 6 skill", "before P6" (Level 5 content, decks, workbook banners "preview of P6"); "Seven P6 pupils" (Level 6 question); "Would the Primary 6 pupils choose the same fruit?" (Level 1 lesson); "See you in Primary 3/5/6!" (closing slides, next school year).
- "Nets are not in the P1 to P3 syllabus", "P1 syllabus", "P1 children" (specs, review, hub FAQ about school Primary 1 maths).
- K2 Readiness Check: "before starting Primary 1", "Primary 1 syllabus", "like a Primary 1 child", "a term of Primary 1" (school year).
- Website `referral.html`: child school-year selector (`Primary 1` to `Primary 6`, `Secondary`), puzzle tiers "Primary 1/2/3/4-6", "K2 to Primary 6", "curious Primary 1 children", "Primary maths, P1–P4" (tutor subjects); hub page titles "Starting Primary 1", "Primary 1 maths" (topic content).
- `website/data/site_seed_example.json` (`"level": "Primary 1"` is the child's school year in sample data).
- `docs/gifted_research.md` (MOE GEP "Primary 3 identification", "P3", "P5"; suggested copy "curious, capable P1 children").
- Code identifiers and comments: `P1`, `P2` variables in `rebuild/gen_p5l5.py`, `gen_p3l8.py`, `p4_fix.py`; "same look as the P1 decks" comments; `kit.js` `const P2 = ...`; `diag/content/*.json` `"level": "P3"` keys.
- `docs/levels_and_placement.md` "Typical school year" column ("Primary 1" to "Primary 6").
