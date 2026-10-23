# Fix pass, Term 3 Lesson 6 (lesson 26, The School Shop)

Changed: `lessons/l26.json`, `verify/l26_checks.py`, `AUDIT_L26.md`, `out/l26/`. Validator 0 FAIL / 0 WARN (built files included), leak check clean; workbook 5 pages, fill 95/96/98/90/93%; home sheet 94%; parent page 99%; timing 90, slow class about 78:00. Not touched: shared tools, other lessons. Source audits: W, G, H.

| Finding | Action |
|---|---|
| W1 / G5 S1 allows $5 twice | Stem "two different things"; Explore and S1 reading say "two different"; page hint "Each tag only once"; key explains why 5+5 is out; check added |
| W3 kit mismatch ($9 globe, ruler $6 vs $7) | S1 uses kit tags $3, $5, $7, $8 (only 3+7 works); ruler is $7 everywhere; S2 ruler $7 and cup $8; S3 jar $14; S4 ruler and glue stick; Mini car and shoe, cup and pencil. A new check: no picture shows a kit item at a price different from the Lesson 25 kit |
| W2 / G2 old Mi | Rebuilt with the no-calculator Mi |
| W4 T1 "only pens", no stopping point | "He may buy 0 books."; table has a row for 3 books (X, too much) |
| W5 G1 gives away the count | Seven rows; "Write how many of each note" |
| W6 no note pictures | Not done: pages are full; listed |
| W7 class numbers reused | T3 now $9, $4, $2 (change $35); E2 $6 and $8; S2 and S1 new |
| W8 / G6 timing, page 2 | Page times 8:30 and 10:30, choice time cut to about 2 minutes (guide says pages 3 to 5 are for home) |
| W9 / G10 / H5 "page 6 of your book" | "the last page of your Lesson 27 workbook" (parent page; viewed) |
| W10 E2 "Circle one." twice | Stem ends with the question; part says "Circle Yes or No." Look-back wrap is a shared layout: listed |
| W11 S6 hint | Kept: page hint plus the table |
| G1 notice order | Opening in the final Term 1 order and words; REC cue names tags and money; tutor_prep and title note match |
| G3 / G8 break calls $3 and $1; optional slide title | Break calls $6, $7, $9, $10, $11, $12, $14 only; slide retitled "Go further: pens and rubbers" |
| G4 camera clause in guide timing | `tools/b_guide.py`: listed |
| G7 spare menu "most expensive first" | "Start at the smallest number and go up" in guide and slide |
| G9 table slide unreadable | `qs` slide layout is shared: listed |
| G11 Mini timing | Not changed: slow Mini 10:47 of 11:00; skip order names the cut |
| H1 online t3 plural, pointless variants, no step values | five-dollar notes 2 to 4 only, steps show the value of the notes |
| H2 online t2 hint stops early | Hint and steps run "until the notes are too much" |
| H3 no list item online | Not added (runner `set` item needs design): listed |
| H4 recording statement | Parent `next` has the final sentence |
| H6 online c1 draws one tag; H home text only | Shared figure and print tool: listed |
| H7 answer page either order | H4 answer says either can come first |
| H8 c5 slip "he", c4 "$" | Fixed; runner header "Term 3": listed |
| Own: school-paper phrase overlaps | Online c5 uses Aisha; change questions reworded |

"cheapest" is now "the tag that costs the least" everywhere. No "50c". "Term 3 • Lesson 6" viewed.

Shared-tool needs: as in FIXES_T3_L25 plus `qs` table slide size, note pictures on text-only money pages, runner `set` list item.
