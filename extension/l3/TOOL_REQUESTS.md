# Level 3: shared tool changes wanted (nothing here has been edited by the Level 3 agent)

1. `extension/tools/render.py` line 80 prints the beyond label as "Beyond Level 1: <name>" for every level. Wanted: `Beyond Level {unit.level}: ...`
   (the `unit` dict is not passed to `item_html`, so it needs one more argument). Work-around used in Level 3: the item field `beyond`
   is NOT used; the first line of the item text reads "Beyond Level 3: <name>." (plain text, same wording).
2. `extension/tools/build.py` line 110, welcome page: the print edition says "The rulers in Unit 9 are printed at real size." This is only
   true for Level 1. Level 3 Unit 9 does have a real-size ruler (1 cm = 10 mm), so the sentence happens to be correct for Level 3 too.
3. Figure types: every Level 3 type is prefixed `l3_` so that plug-in names cannot clash with other levels (see `extension/tools/figs_l3_*.py`).

4. Coordinator note (23 Oct): build.py/render.py are being changed (by the Level 4 agent) to read the Welcome/equipment text and the "Beyond Level N" label from `extension/config/levels.json`. At the time of the final Level 3 build that change was not yet in the tree. When it is: set the Level 3 keys (Unit 9 real-size ruler line applies; Level 3 needs ruler, nothing else), optionally move "Beyond Level 3: ..." from the item text to the `beyond` field, rebuild and re-run the gates.
