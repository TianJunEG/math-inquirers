# Level 5: requests for shared tool changes (not made by the Level 5 author)

Resolved (23 Oct): the shared build now supports the `beyond` item key ("Beyond Level 5"), `{bw}` wide answer boxes, and per-level Welcome text from `extension/config/levels.json`. Level 5 uses all three.

Still open, optional:

1. `extension/verify/wording_lint.py` NUMWORD rule flags place-value phrases ("ten thousands", "two hundred and five thousand"). Workaround used in Level 5: the hyphenated forms "ten-thousands" and "hundred-thousands", and numerals in "write the number" items.
2. Quiz items without a figure always get a "Working:" row (render.py). Optional: a unit key to switch it off for one item. Workaround: none needed (a few Check yourself items were reworded to fit).
3. `wording_lint.py` has a fixed cast list of names; Level 5 uses Lin, Mo, Kai and Dev, which give only WARN lines.
