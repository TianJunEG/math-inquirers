# Level 1 diagram fixes: running log (branch claude/great-fermi-1hv4vc)

Source: audit/DIAGRAM_AUDIT.md. Owner approved ("DIAGRAMS: go"). Only term/l1 files touched.

## Batch 1: shared helpers and picture graphs (L37, L38)
Done:
- tools/figs4.py (new): picture-symbol icons batch 3 (cat, dog, pear, plum, fig, orange, pawn, die, card, hat, stone, feather, mint, toffee, gum, rose, daisy, tulip, bowl, stamp, duck, goose, hen, kite, kite_blue, egg, fish_red/blue/gold (stripe, spot, plain so they differ in B&W), book_m/s/a/sc, crab, snail, crayon, shirt, shorts, seat, pocket, page). figs3.icon_body falls back to figs4.
- tools/figs3.py: picture_graph accepts an `icon` per row (mixed picture symbols), larger row labels and key text; shell icon redrawn as a scallop.
- L37 and L38: all 12 audit graphs (and the deck, exit-ticket and online-practice graphs) now use real picture symbols per row instead of red dots (deck sort slide: ball, car, bike icons carry through to the graph slide). Graph sizes raised where the page allows. Answers unchanged.
