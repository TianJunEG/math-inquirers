# Fix pass, Term 3 Lesson 5 (lesson 25, Price Tags: Compare and Choose)

Changed: `lessons/l25.json`, `verify/l25_checks.py` (294 checks), `AUDIT_L25.md`, `out/l25/`. Validator 0 FAIL / 0 WARN (built files included), leak check clean; workbook 6 pages (5 + kit), fill 96/90/100/95/99% (kit 85%); home sheet 96%; parent page 99%; timing 90, slow class 77:23. Not touched: shared tools, other lessons.

Source audits: W (workbook), G (guide and deck), H (home, parent, online).

| Finding | Action |
|---|---|
| W1 / G8 / G11 T4b repeats allowed | Stem: "uses each tag once"; key and guide worked solution now list systematically from $2; check added |
| W2 / G2 kit does not match tags shown | Explore, S1, S3, S4, T4 and Mini m5 use kit tags at kit prices (m5 tags: $3, $5, $7, $8, $12; pairs 3+12, 7+8). Every other picture uses items that are not on the kit (car, sock, bike, spoon, shoe, button, fish), so no kit item shows a different price (check added). Investigation: "Write $11 on a blank tag"; contract: blank tags used by I1 |
| W3 "ball" is a globe | The kit tag and all uses are now a jar (icon is a shared tool; L24 and L26 still show the old ball: listed) |
| W4 / G4 old Mi | Rebuilt: no-calculator Mi (viewed) |
| W5 T3 Kumar $50 and $40 | (c) now "Ali has $40" |
| W6 S5 notes small | Notes drawn larger (size 80), viewed |
| W7 / H work-back | S-level untouched; H4 (home) is now the work-back item, plus online t4; "work backwards" in contest_moves. Page 3 is full, so no new workbook item |
| W8 kit page spacing, not centred | Shared tool (`figs3.price_tags`): listed. "No printer" line added to the kit intro |
| W9 pages 3 and 4 for home | One line on each page hint |
| W10 / G10 class numbers repeated | S2 now hat $6 and toy car $15, S5 shoe $12, S6 toy fish $17, E1 $17 and $9, E2 $9 and $6, E3 $13; sneak-peek bag $15 and hat $9; G2 uses a scooter, puzzle and doll |
| W11 Investigation lines, look-back wrap | Not changed (shared layout) |
| W12 S3(b) repeats 15 | S3 is one part: number sentence only |
| G1 / G7 notice after recording | Opening in the final Term 1 order and words; REC cue says price tags; tutor_prep and s-title note match |
| G3 jumps shown while asking | s-rem2 has no jumps; new s-rem2-ans shows them |
| G5 "papers to the camera 30 s" | Printed by `tools/b_guide.py`: listed |
| G6 small notes on slides | s-m4 notes enlarged; the `qs` slide thumbnails are shared: listed |
| G9 Mini timing | Not changed: slow class 10:55 of 11:00, skip order already names the cut |
| G12 / H2 dearer, dearest, cheapest | Replaced with costs more / costs the most / costs the least in parent words, online t1, guide notes |
| H1 online steps omit numbers | t2, t3, g1, g2 templates now derive and show the middle value; oracles pass |
| H3 home sheet text only | Shared print tool has no home figures: listed |
| H4 beyond sentence | Parent beyond line now names all the beyond items |
| H5 recording statement | Parent `next` carries the final Term 1 sentence incl. private link |
| H6 no exact-amount online item | Not added (runner `set` item needs a design); online t4 added instead |
| H7 runner header, H8 "Term 1 Lesson 5" on child sheet | Runner / `b_print.py`: listed |
| Own: S6 "does she need" matched a school-paper phrase | Names used (Mei, Siti, Aisha) |

Money: no "50c". Numbering "Term 3 • Lesson 5" viewed. Hand-off to L26 true (tags and money, nothing new to cut).

Shared-tool needs: redraw `ball` icon (figs2); `price_tags` kit 6 mm gaps and centring; `b_guide.py` camera clause; `b_print.py` rewind label; qs-slide thumbnail size; look-back wrap; runner Term in header.
