# Mi the dolphin in the holiday decks, Levels 1 to 3 (2026-10-23)

Owner decision: docs/terms/owner_decisions.md, "Mi joins the HOLIDAY program decks". Scope here: the 30 decks of Level 1 (split/l1 to l10), Level 2 (split/p2l1 to p2l10) and Level 3 (split/p3l1 to p3l10). Levels 4 to 6 not touched (the module has smaller sizes ready; switch on with LEVELS_ON).

## Where Mi appears (one small pose, bottom-right corner, same place every time)
| Slide | Pose |
|---|---|
| title | hello_wave (lesson 10, Puzzle Day opening: map) |
| brain break | stretch |
| lesson 10 "end" certificates slide (when not the last slide) | trophy |
| last slide (look-back, or "end" when it is last) | goodbye_wave |
Never on exit ticket or any question slide; no speech bubbles, no numbers, no calculator. Height 230 px (Level 3 look-back slide 120 px so it clears the text cards). Level 4-6 sizes in the module: 170, 160, 150 px with slight opacity.

## How it survives a rebuild
- levels/mi_deco.py: idempotent post-pass. levels/restyle.py calls it for each deck folder, so the chain gen_* then restyle.py puts Mi back.
- Images are Claude Slides assets (src /_blob/<id>, never data URIs). Ids differ per deck and live in mascot/blob_ids.json. A deck/pose with no id gets no Mi (never a broken image). Small poses: mascot/poses_small (360 px tall).
- Caveat found: re-running a rebuild/gen_* script on an already-patched split/ folder is not idempotent (duplicate time pills, "text not found" in p1fix). The gen scripts were therefore NOT re-run; only the Mi pass was applied to the existing generated slides (verified: diff shows only the Mi img lines).

## Checks
- Rendered title, break, exit and last slide (plus lesson 10 end) of all 30 decks, contact sheets viewed. Programmatic overlap test of the Mi box against all text and pills: one overlap found (Level 3 look-back cards, bottom-right), fixed by the smaller pose; re-test clean.
- Not mine, noticed: Level 1 title slides carry the time pill three times (stacked on the same spot, invisible but untidy); the pill sits on the decorative "?" cloud on dark slides.

## Republish
All 30 decks republished in place at their existing URLs (outputs/deck_urls_all.json, unchanged), private, one at a time, only the Mi slides sent (title, break, last or end slide; assets uploaded per deck first). Method as in docs/audit/final_fixes_decks.md (Artifact publish with url, root = split/<id>, files by project/ path). Level 1 to 3 slide files sent contain whatever other agents had in split/ at that moment for those 3 to 4 slides.
