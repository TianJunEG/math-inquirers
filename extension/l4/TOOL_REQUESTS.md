# Tool requests (Level 4)

No shared tool was edited. Work-arounds are noted.

1. `tools/render.py` prints the `beyond` label as "Beyond Level 1: <name>" (the level is hard-coded). Level 4 therefore does NOT use the item key `beyond`; a beyond-syllabus item starts its stem with the first line "Beyond Level 4: <name>" instead. If render.py is changed to print the book's level, the Level 4 items can be switched to the `beyond` key (search the data for "Beyond Level 4").

## Requested after the audit (23 Oct): NOT made, needs the shared tools

The coordinator authorised one minimal edit of `extension/tools/build.py` and `render.py`. The edit was blocked by the session's permission system ("Modify Shared Resources"), so no shared tool was changed. Exact edit, ready to apply by someone with permission (Level 1 output stays identical when the keys are absent):

1. `extension/config/levels.json`, per level, optional keys: `welcome_equipment` (html; printed as "You will need: ..." in "For the grown-up"), `welcome_notes` (list of html list items, for example the line explaining "Beyond Level N"), `welcome_print_note` ({"colour": ..., "bw": ...}, replaces the last line, which is now the Level 1 sentence about rulers), `session_minutes` (default "20 to 25"). Suggested Level 4 values: equipment "a pencil, a rubber, a ruler and a 180 degree protractor (Unit 6)"; notes "Beyond Level 4 means ahead of the school year. It is fine to skip these."; print note colour "Printing this soft copy? Print at 100 percent so the angles in Unit 6 are the right size.", bw "The angles in Unit 6 are printed at real size."; session_minutes "25 to 30".
2. `build.py`: `welcome()` and `pace()` read those keys (defaults reproduce today's text exactly).
3. `render.py`: `item_html` prints "Beyond Level 1" (hard-coded): use the level of the unit being rendered (set a module variable in `unit_pages`). Level 4 can then switch to the `beyond` key.
4. Answer boxes: `.abox` is 16 x 10 mm from `levels.json` (`box_mm`); 5-digit answers need about 24 mm. A new markup (for example `{bw}` for a wide box) or a per-item option is needed; Level 4 cannot do it from its own files.
5. Contents page prints each unit title twice (title and lower-case topic).


## Status (23 Oct)

All requests above were landed by the coordinator (levels.json keys, `beyond` label by level, `{bw}` wide box). Level 4 now uses them. Remaining: the Welcome soft page 3 overflows by 3 mm with the new shared text (equipment line); a shorter equipment or notes string in levels.json would fix it.
