# Level 5: requests for shared tool changes (not made by the Level 5 author)

1. `extension/tools/render.py`, line with `Beyond Level 1:` prints "Beyond Level 1" for every level. Please use `unit["level"]` ("Beyond Level {level}"). Workaround used in Level 5: the item key `beyond` is NOT used; the first line of the item text reads "Beyond Level 5: <name>".
2. `extension/verify/wording_lint.py` NUMWORD rule flags place-value phrases ("ten thousands", "two hundred and five thousand"). Workaround used in Level 5: the hyphenated forms "ten-thousands" and "hundred-thousands", and numerals in "write the number" items.
3. Quiz items without a figure always get a "Working:" row (render.py). Optional: a unit key to switch it off for one item. Workaround: none needed.
