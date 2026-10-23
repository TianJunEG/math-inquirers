# Level 6: requests for shared tool changes (not made by the Level 6 author)

None of these blocks the Level 6 build; each has a workaround in the Level 6 files.

1. `render.py` item_html prints the beyond label as "Beyond Level 1: <name>" for every level (hard-coded "Level 1").
   Workaround: Level 6 items do not use the `beyond` key. `extension/l6/src/lib.py` puts the words "Beyond Level 6: <name>." as the first line of the item text.
   Fix: print `Beyond Level {unit["level"]}` in render.py (pass the level to item_html), then Level 6 can use the key again.
2. `build.py` welcome(): the last bullet says "The rulers in Unit 9 are printed at real size." for the print edition and "Printing this soft copy? Print at 100 percent so the rulers are true size." for the soft copy. Level 6 has no rulers.
   Not worked around (a build.py text). Suggest making the bullet conditional on the level (only Level 1 has rulers) or on a config key.
3. `build.py` welcome(): "Every unit has 7 pages" and the pace plan assume the Level 1 session split; they are correct for Level 6. The sentence "practice for the same ideas as the Holiday Program" is correct for Level 6 too.
4. `build.py` cover(): "Self-study" tag and "Level 6" fine. No change needed.

5. Coordinator note (23 Oct): build.py and render.py will read the Welcome/equipment text and the Beyond label from levels.json. Not landed when Level 6 finished. Level 6 needs: no ruler sentence on the Welcome page. After the change, rebuild Level 6 and check page 3.
