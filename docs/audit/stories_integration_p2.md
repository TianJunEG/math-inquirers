# Stories integration, Level 2 (P2)

Source: `docs/stories/final_p2.json` (10 lessons, one person each). Child-facing text lives in new `p2/stories.json` (story text unchanged, 70-88 words, so no shortening was needed; blurb and legend labels added; x, / and - shown as ×, ÷, − in try-it text).

## Changes
- `p2/stories.json` (new), `p2/data.js` (exports `stories`).
- Decks: `rebuild/p2gaps.py` adds slide `p2lK-story` "Story break: <name>" straight after `p2lK-break` (label 34-36 MIN (OPTIONAL)); story at 38px, legend label shown where the story is a legend/memory (Gauss, Mary Somerville, Thales); try-it is a click-in optional box; answer only in speaker notes with skip, volunteers-only and no-marking instructions. Break slide notes and title-slide time plan mention the optional 2-minute story. All ten `gen_p2lK.py` already call `p2gaps.add/order`, so no per-lesson edits were needed. Regenerated all 10 decks, `levels/restyle.py split/p2lK`, `levels/normfoot.py 2`.
- Workbook (`p2/workbook_html.js`): "Story corner" box (name, country, years, 2-3 sentence blurb, optional try-it, answer line, no answer) on the "Before you go" page of each lesson. Page count unchanged (64).
- Tutor guide (`p2/guide.js`): routine table brain-break row; new page "Level 2 stories: mathematicians" (table Lesson, Person, Country, Years, Link; plus rules); per lesson at the brain break the line "Story break (optional, 2 minutes): ..." with skip instruction; "Story try-it" answer in each lesson's answer key. The stories page sits before "How to use the scripts" so the weekly PDF slicing is unaffected.
- Rebuilt: workbook HTML/PDF, guide docx/PDF, weekly zip (`weekly_level.py`).

## Verification
- All ten try-it answers checked in Python (place value, pairing sum 55, products 35/36/60, ripple pattern mod 4, X=6, $11 and $9, 1/4 and 3/4, cube 6 faces and 12 edges, shadow 9 m / 120 cm, sweets 8 and 4 unique). All correct.
- Story slides: no element below y 920 or outside the 128px margins, no font under 24px, ≤17 elements, notes well under 4000 chars. Longest story (Thales) bottom at y about 864.
- Workbook: story box fits on the Before-you-go page for all 10 lessons, none clipped. Guide: stories table and brain-break lines render without clipping.
- Safeguarding wording and Start here / Think harder / Go further names untouched.

## Left / notes
- Not rerun: `parent_pack_level.py` and `levels/scheme.py` (their content does not change); the rest of build_level.sh was run step by step.
- Stories mention numbers above 1000 (5050, 13-digit numbers) as history only; try-its stay within P2 rules (Shakuntala try-it uses 7×5, 9×4, 6×10, all within the 5, 4 and 10 tables).
- Dates for Aryabhata, Pacioli and Ahmes are approximate ("sources differ"), shown as such.
- Slide decks are source only here; the published Claude Slides artifacts were not updated (no publish tools used). Nothing committed.
- Other uncommitted changes in hp/* and p4/* in the working tree are not from this task.
