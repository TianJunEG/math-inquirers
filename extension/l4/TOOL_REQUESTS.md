# Tool requests (Level 4)

No shared tool was edited. Work-arounds are noted.

1. `tools/render.py` prints the `beyond` label as "Beyond Level 1: <name>" (the level is hard-coded). Level 4 therefore does NOT use the item key `beyond`; a beyond-syllabus item starts its stem with the first line "Beyond Level 4: <name>" instead. If render.py is changed to print the book's level, the Level 4 items can be switched to the `beyond` key (search the data for "Beyond Level 4").
