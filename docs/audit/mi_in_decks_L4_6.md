# Mi the dolphin in the holiday decks, Levels 4 to 6 (2026-10-23)

Owner decision: docs/terms/owner_decisions.md, "Mi joins the HOLIDAY program decks". Scope: the 30 decks split/p4l1..p4l10, p5l1..p5l10, p6l1..p6l10. Levels 1 to 3 are in docs/audit/mi_in_decks_L1_3.md (same module).

## Where Mi appears (one small pose, bottom-right corner, same place on every deck)
| Slide | Pose |
|---|---|
| title | hello_wave (lesson 10 Challenge / Showcase opening: map) |
| brain break | stretch |
| last slide (Looking back; lesson 10: the "end" slide) | goodbye_wave |
Never on the exit ticket or any question slide; no speech bubbles, no numbers, no calculator. Older-level sizes (smaller, slightly translucent): Level 4 170 px / 92%, Level 5 160 px / 88%, Level 6 150 px / 85%. Looking-back slide 120 px so Mi stays below the cards.
Level 4 to 6 lesson 10 has no separate trophy slide (the "end" slide is the last one), so it gets goodbye_wave.

## How it survives a rebuild
- levels/mi_deco.py: LEVELS_ON now holds 1 to 6. Idempotent post-pass called by levels/restyle.py for each deck folder (gen_* then restyle.py puts Mi back).
- Level 4 to 6 title slides also get margin-right:150px on the "Today we will" card (done in the same pass, idempotent) so the card does not run under Mi.
- Images are Claude Slides assets (/_blob/<id>), uploaded per deck from mascot/poses_small (360 px tall). Ids per deck: mascot/blob_ids.json (now 60 decks). A deck/pose without an id gets no Mi (never a broken image).
- The gen_p4*/p5*/p6* scripts were not re-run (re-running on patched split/ is not idempotent, see the L1-3 note); the pass was applied to the existing generated slides. Diff is only the Mi img lines plus the title card margin (a few title/reflect files also carry other agents' uncommitted edits).

## Checks
- Rendered title, break, exit and last slide of all 30 decks (120 slides) at 1920x1080, contact sheets viewed for each level. Programmatic bounding-box test of the Mi image against all text and the time pills: clean after the two fixes (title card margin, smaller Mi on look-back), apart from the full-width subtitle box on the lesson 10 "end" slides whose text stops about 640 px short of Mi.
- Exit slides carry no Mi (checked in the sheets).
- Renderer caveat: my page wrapper lets the title footer text sit over the "Today we will" card; that is a wrapper artefact, not new.

## Republish
All 30 decks republished in place at the existing URLs (outputs/deck_urls_all.json unchanged), private, one at a time. Only the 3 Mi slides of each deck were sent (title, break, last/end slide); assets uploaded per deck first. Method as in docs/audit/final_fixes_decks.md plus: read the artifact and list its files before each publish (the tool refuses otherwise). The slide files sent are the current split/ copies, so the few lines other agents had changed in those slides were published with them.
