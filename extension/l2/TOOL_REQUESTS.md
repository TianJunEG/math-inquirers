# Shared tool requests from Level 2 (nothing blocks the build; worked around)

1. `render.py` prints the beyond label as "Beyond Level 1: <name>" for every level (a hard-coded `Level 1`). On Level 2 (and 3 to 6) the label should read the level number. Workaround: none needed for the build (the label is still correct in meaning: "beyond Level 1" is true for a Level 2 book), but a Level 2 reader sees "Level 1". Suggested fix: use `unit["level"]` in `item_html`.
2. `render.py` numbers the Start here items by page order but the answers by list order. Level 2 avoids a mismatch by sorting in `extension/l2/author/lib.py`; the shared tool could sort or assert instead.
3. `run_checks.py` only sorts the values of an UNORDERED answer when the item has parts; an item without parts compares in order. Level 2 checks return values in the book's order (see `l2_u06_checks.py` S10).
4. Fractions: only plain text `3/8` is available. A stacked fraction markup (for example `{f:3|8}`) in `render.mk` would read better at ages 7 to 9.
5. `wording_lint.py` bans the word "price" everywhere (book price rule). For a money unit this blocks natural words ("half price", "price tag", "price list"). Suggested: ban only a currency amount next to "price" or a whitelist for shop contexts.
6. `figs.min_text` raises small figure text to 10 pt, but a figure placed at a small width_mm can still have objects under 8 mm. Level 2 plug-ins therefore choose widths so objects are about 8 mm or more.
