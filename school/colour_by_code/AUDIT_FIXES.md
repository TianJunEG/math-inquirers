# Colour by Code: fixes after the independent audit (`AUDIT.md`, 23 Oct 2026)

Scope: `school/colour_by_code` only. Result: Primary 1 has 14 sheets (was 10), Primary 2 has 15 (was 12). `verify.py` passes on both levels (Primary 1: 706 checks, Primary 2: 741 checks, 0 failures). Every pupil page was rendered and looked at; the contact sheets and galleries are rebuilt (`out/p1`, `out/p2`).

## What changed, by audit finding

| finding | status | what was done |
|---|---|---|
| F1 CBC-06 two wrong answers, wrong key | fixed | `banks_p1.py`: "10 less than a, then 1 more" now uses `a + 9` (71 gives 62, 76 gives 67 is no longer printed; the sheet reads "10 less than 64, then 1 more" = 55, "10 less than 84" = 75). The same sheet's "10 more than 54, then 1 more" = 65 is unchanged. |
| F1 cause: verifier trusted the bank | fixed | New `textcheck.py`: an independent evaluator that re-solves every printed question from its text (and, for picture questions, from the decoded picture: clock hand angles, ruler ends, coin values, dots, graph rows, tally, solids, fraction parts). `verify.py` runs it on every bank sample (hundreds per bank and tier) and on every printed question of every worksheet; the result must equal the coloured answer and be a key value; a form with no rule fails. Self-tests: "10 less than 71, then 1 more" must give 62 and reject 60; an unknown question is refused. Regression check done by hand: putting `a + 11` back makes 125 samples fail ("10 less than 86, then 1 more" is 77, not 75). |
| F2 P2-06 shaded bars solid black | fixed | Shaded parts are hatched, the equal parts are separated by white lines, the bar outline shows every part. Teacher page unchanged in layout. |
| F7 slash fractions | fixed | Fractions are stacked (numerator, bar, denominator) in questions, answers, key boxes and teacher answers. Fraction domain is compared as written (2/4 is not 1/2). |
| F3 P2-10 graph key and labels 2.5 mm, one-row graphs | fixed | Key and row labels are 3.8 mm (P1 graph 3.5 mm, never scaled down); the icon is a small face, not a black dot; rows are labelled with what is counted (Cats, Dogs, Pies, Cars ...); real two-, three- and four-row graphs ("How many more", "How many dogs and cats", total) are preferred wherever one fits (`pref`), the smallest regions keep tally and one-row items. Rebuilt on the butterfly (large regions); tag reads "Picture graphs and tally marks". Key values 6, 8, 10, 12, 15. |
| F10 P2-09 not Primary 2, tag over-claims | fixed | Sheet is two stars with real units: ruler/cm cut-off, 1 m minus cm, 1 kg minus g, g sums, litres shared and left, balance. The real-unit forms are preferred over bare sums with a unit label. The footer now names only the units the page contains (`Bank.parts`): "Length, mass and volume: cm, g, kg, l". Not changed: three-addend items on P2-02 and tally on P2-10 (not in the syllabus text, in the papers; low). |
| F4 phrases naming parts a pupil cannot find | fixed | The counted-subset sentences ("the two windows", "6 wall and window parts", "6 scales", "body has 4 parts") are gone. Non-symmetric pictures carry small black marks (triangle, square, diamond, star, cross, hexagon) on matching parts; the check box says "Parts with the same small mark have the same colour" and shows the marks. A grep of all pupil pages finds no window, scale or wall wording. |
| F6 swaps escape the tally | fixed | Two checks besides the tally on every sheet: left-right match (symmetric pictures) or small marks (others). `verify.py` enumerates every double slip (every pair of regions, every pair of wrong colours, 1000 to 2200 cases a sheet): at least 95 percent must be caught, and the swap subset separately. Result on all 29 sheets: double slips caught at least 99.86 percent, swaps at least 97.4 percent (audit baseline: 24 to 48 percent of swaps missed on non-symmetric pictures). Single slips: 100 percent. |
| F5 duplicates | fixed | Questions are compared by what they are, not by their text: operands in any order, wording ignored for picture questions (the same clock, coins, ruler, dots or shapes), a bare digital time in any wording, fractions; `verify.py` fails on any repeat and separately on a clock face drawn twice or a digital time printed twice. Seeds were re-chosen so no sheet repeats. The assignment of answers to regions now spreads colours evenly (three a colour where the matching sets allow it, otherwise four), and where bonds, shapes or ordinals had too few distinct forms for four regions of one answer, forms were added (bonds: "Make 10 with 9", "9 needs [] more to make 10"; shapes: up to three shapes; ordinals: 11 forms). Known limit: on the bonds sheet an answer with four regions shows the same fact four ways (9 and 1); the questions are distinct but the numbers repeat. |
| F18 coverage | fixed (pilot size) | P1 new: CBC-11 multiplication within 40 (two stars), CBC-12 sharing and grouping within 20 (no division sign), CBC-13 picture graphs (one face is one), CBC-14 ordinal numbers (first to tenth, from the left or right). P2 new: CBC-P2-13 number patterns, CBC-P2-14 multiplication (two stars), CBC-P2-15 fractions (two stars, up to twelfths). New banks `mult`, `share`, `pgraph`, `ordinal` (P1) all pass the bank checks and have evaluator rules. |
| F11 tags overclaim | fixed | Footer tags are now derived per sheet (`Bank.parts`) or set per tier: P1 money "coins and cents" / "notes and dollars", P1 shapes "corners" (one star), P2 time "hours and minutes", P2 fractions and measures list only what is on the page. |
| F12 "mirror" wording | fixed | "Parts in the same place on the left and on the right have the same colour." |
| F17 elephant looks like a balloon | partly | P2-03 now uses the owl; the elephant stays in the library. |
| F8 P2-08 clocks and wording | open | Clock faces are still about 12 mm with hands of similar length; "25 minutes to 9" and "15 minutes to 7" are unchanged. The sheet has no repeated time and its tag is "Time: hours and minutes". |
| F9 P2-07 decimal-notation add and subtract | open for the owner | `docs/moe/syllabus_by_level.md` says compare and convert only; `docs/books/p2_school_paper_patterns.md` shows sums and change in the papers. Not changed. |
| F13 instruction lines ("Add.", "Take away.", "Share or group.") | open (low) | Not changed. |
| F14 rulers starting at 1 (P1) | open (low) | Not changed. |
| F15 subjectless wording ("Sold 170. Left 554. At first:") | open (low) | Not changed; limited by label size. |
| F16 tier honesty (CBC-05, P2-12 two stars; visible +101 key on P2-12) | open (note) | Not changed. |
| F19 teacher page gaps (outcome code, "say the time" shows only a colour, marking line) | open (low) | Not changed. |

## Other changes

* `sheet.py`: balanced answer assignment, content-based duplicate signature, a form can be preferred (`f.pref`), a too-big random variant of a form no longer ends the search (the form is retried), footer school-name field no longer wraps.
* `art.py`: picture graph takes pitch and font size; `queue` (a row of children with one marked) for ordinals.
* `build.py`: contact sheet grid has 8 columns when a gallery has more than 12 sheets.
* `verify.py`: evaluator checks (banks and worksheets), evaluator self-tests, double-slip and swap enumeration, twin-set check, content-based duplicates and clock repeats, per-level gallery size (P1 12 to 14, P2 14 to 16), double-slip and swap columns in `inventory.md`.
* `README.md` and `out/pN/compat.md` regenerated (Primary 1: 277 of 308 picture, topic and tier combinations build; Primary 2: 256 of 286).
* Pictures: no new picture. Gallery pictures re-chosen: P2-03 owl, P2-09 sailboat (two stars), P2-10 butterfly.
* Black and white print rule unchanged: only black and white in the HTML and PDF, 0.9 mm outlines, hatching and small marks are black lines on white.

## How to re-run

```
python3 build.py && python3 verify.py          # both levels; exit code 1 on any failure
python3 compat.py --level 1 > /dev/null        # which picture, topic and tier combinations build
```
