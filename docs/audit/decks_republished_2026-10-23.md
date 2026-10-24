# Holiday decks: local verification and republish status (2026-10-23)

## Result: NOT republished. All 60 decks stay local.
The first Artifact publish (l1, in place at its existing URL) was denied by the permission classifier ("Unauthorized Persistence"). I did not retry or work around it. No live deck was changed. Owner can allow the Artifact tool (settings permission rule) and the 60 republishes can run: Artifact publish with url from outputs/deck_urls_all.json, file_path split/<id>/project/deck.json, root split/<id>, files = every project/slides/*.html (paths relative to root). Live decks still carry old text and, per the earlier Mi republish, still have Mi on L1-3, so a full-deck republish is needed (not only Mi slides).

## Verified on current local sources (60 decks: l1-10, p2l1-10 ... p6l1-10)
- Mi: exactly one img[data-mi] on the title, brain-break and last slide (lesson 10: also the "end" trophy slide when not last), none elsewhere. All 60 pass.
- Time pills: duplicates found only in split/l1 (l1-title x4, rules x4, routine x4); fixed in source (levels/restyle.py dedupe_pills). Now one per slide everywhere.
- Camera wording: no affirmative "hold ... to the camera" anywhere. Remaining hits are the new negative rule ("nothing is held up to the camera", "Never ask a child to hold a page to the camera"), mostly in P4 and teacher notes.
- Mi overlap with text: none on any title, break or last slide after the fixes below (Playwright text-rect test, Chromium, 1920x1080, Nunito Sans/Fredoka loaded).

## Found and fixed in SOURCE (levels/mi_deco.py, levels/restyle.py)
1. L1-3 decks had lost Mi (holiday-fix rebuild). Restored with mi_deco (idempotent, via restyle.py).
2. L1-3 title slides: "Today we will" card ran under Mi. Card now gets margin-right 250px (L4-6: 150px).
3. L1-2 look-back: Mi covered "asking a question". Mi on every look-back slide is now 120 px.
4. L5 look-back: yellow "tutor may read this" notice touched Mi. Notice narrowed to 1520px in the pass.

## Not fixed (pre-existing, not caused by Mi)
- Many slides are taller than 1080 px in a 1920x1080 render (about 160 slides, e.g. L1-3 look-back last rows, P3 look-back cards, P4/P5 talk, P5 ws2). Unchanged vs earlier commits; live decks have the same. Needs a layout pass by the slide owner.
- Footer line "Math Inquirers ... Notice it." overlaps content on dense slides (normfoot).
