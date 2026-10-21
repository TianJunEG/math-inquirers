# P3 audit fixes: applied

Source audit: `docs/audit/audit_p3.md`. All edits are in P3 source files. No shared files were touched (`rebuild/slidekit.py`, `hp/*`, `levels/*` are unchanged). Nothing was published or committed.

## Per issue

| # | Sev | Status | What was done |
|---|---|---|---|
| 1 | High | Applied | L4 Q6 replaced (Ali $45, Ben $18, Grandma gives $10 each; parts a, b, c; key $27 / $27 / difference stays the same). The old "twice as much" problem is now `stretch` s5. `challenge` c0 replaced (120 stickers, 3 times as many, Ali gives 20: Ben 30, Ali 90, then Ali 70, Ben 50). `challenge` c7 replaced (pen $3 more than ruler, 2 + 2 for $18, pen $6). Age problem and rice/flour swapped, so rice/flour is s3 (prints) and age is s4. Slides reworked to match: `teachsame` (now a "$5 to each, same gap $18" model), `ws2`, `ws2ans`, `challenge`, `chdiag` (before and after bars), `chwalk`. The old c7 and the old Mei/Siti c0 are no longer in the bank. c3 was named in the audit but has no replacement text, so it was left as is (it is an unprinted Challenge item). |
| 2 | High | Applied (see note) | L9 worksheet cut. Ribbon Q3 deleted and merged into Q1(d) (4 pieces of 65 cm from 3 m, 40 cm left). Budget is now Q3 with (b) "if time". Page 2 is Q4 24-hour clock, Q5 durations (a, b, c), Q6 bus timetable "if time" with (a) and (b) only. Result: 6 questions, 12 core parts plus 3 "if time" parts (was 7 questions, 17 parts). The audit text says "5 questions" but 7 minus Q3 is 6, so I matched its "about 12 parts" target. Keys, `ws1`/`ws2` deck lines, `ws1`, `ws1ans`, `ws2`, `ws2ans`, `teachbudget`, `teach24` and `teachlist` renumbered. |
| 3 | High | Applied | The "latest bus" question (old Q7c, with the new wording "On another day, Ravi must reach school by 08:30...") moved to `stretch` s3 as a self-contained Think Harder item; answer 07:55 bus. The contradiction with Q7(a) is gone. |
| 4 | High | Applied | L10 explore reduced to two stations (List, then Measure), 7 minutes each, pairs stay in one breakout room. Measure is now the 120 cm ribbon (30, 40, 50 cm). String removed from `materials`; `online`, `explore`, `predict`, `exploreHints`, `expSetup`, `expPic`, `expAsk`, `p3l10-explore1` (slide picture redrawn with two tiles), `p3l10-explore2` and the title notes updated. Graph and Logic stay on worksheet page 1. |
| 5 | High | Applied | L10 Q2 clue 2 is now "Mei and Ravi are not in the choir." (key text already said this). |
| 6 | High | Applied | L8 Q5(c) labelled "Think harder (if you have time)" with the hint "try 1 right and 2 down". Slide `ws2` and deck `ws2` updated. |
| 7 | Med | Applied | L8 c6 and c8 reworded as given. `chwalk` right column no longer uses the turning argument ("Try it: draw 6 square corners on grid paper. What do you always get?"). Slide notes updated. |
| 8 | Med | Applied | L2 Q6(b) now has the scaffold ("Try 0 and 5, then check the tens column"). L2 Q1 got the hint "turn it round and add, 2538 + □46□ = 7□03". Slide previews updated. |
| 9 | Med | Applied | L1 Q5(b) and Q6 marked "★ (if time)". `deck.ws2` set to the audit's exact text; slide `ws2` preview and tutor note updated. |
| 10 | Med | Applied | L3 Q2(a) now tests only the 3, 6 and 9 tables (answer 3 and 9; 6 gives only even digits, checked). Q5(a) has the "Not every number of rows works..." sentence. Key and slides updated. |
| 11 | Med | Applied | L9 explore rule is now "at least 2 ℓ of punch (any number of bottles) and at least one food; more than one of an item is allowed". Brute force confirms exactly 3 exact-$20 plans under this rule. `explore`, `expSetup`, `expAsk`, slide and notes updated. |
| 12 | Med | Applied | L9 c8 clock wording replaced. Answer 14:35 / 2:35 p.m. re-verified. |
| 13 | Med | Applied | Title-slide time plan of all 10 decks gained "If the class is behind, children finish the last question of each page at home; the check slides cover it." "If time" marks added: L1 Q5(b)+Q6, L3 Q6, L5 Q6, L7 Q6, L9 Q3(b) and Q6, L10 Q6 (workbook, deck `ws2` text and slide previews). |
| 14 | Med | Applied | `online` fields of L4, L5, L6, L8 (content and title notes where they exist) carry the print-workbook / breakout-room sentence. L6 now says to send the printed fraction strip page instead of cutting strips; L6 `materials` changed to match. |
| 15 | Med | Applied | L5 s3 wording ("boatloads") and key. |
| 16 | Med | Applied | L6 c2 now "each less than 1". |
| 17 | Low | Applied | L7 Q2: "You may not need all the rows." |
| 18 | Low | Applied | L7 c2 reworded (parallel to one side; 28 cm and 32 cm). |
| 19 | Low | Applied | L8 s6 clock question reworded. |
| 20 | Low | Applied | L8 ANG f changed from 70 to 60 (still smaller than a right angle); s3 now says "2 upright lines and 2 lines across". |
| 21 | Low | Applied | L10 s6 snail key says "highest point each day"; slide `stretch` notes corrected the same way. |
| 22 | Low | Applied | L6 `chwalk` note now says "as in the list-in-order puzzles earlier in the program". |
| 23 | Low | Applied | `p3/data.js` first-line comment fixed to `p3/content`. |
| 24 | Low | Skipped | Audit says leave as is (L7 Q4 stays the last question on page 2). |
| 25 | Low | Skipped | Optional P4-bridge sentences; no content change was requested and they would need new closing-slide text. |

Numeric re-checks (Python): L4 Q6 (27 and 27), c0 (30/90 then 70/50), c7 (pen 6, ruler 3), old Q6 (9), teachsame (35 − 17 = 18); L9 ribbon (40 cm), budget, bus times (06:40 ... 08:45; 07:55 + 35 = 08:30), clock (14:35), three exact-$20 plans; L3 tables (3 and 9 only) and 36-chair ways (7); L6 c2 (two ways); L7 c2 (28, 32); L10 ribbon (30, 40, 50) and snail (day 4); L2 shape puzzle (★ 5, ● 0, ▲ 1 only).

## Files changed

- Content: `p3/content/l1.js`, `l2.js`, `l3.js`, `l4.js`, `l5.js`, `l6.js`, `l7.js`, `l8.js`, `l9.js`, `l10.js`; `p3/data.js` (comment only).
- Generators: `rebuild/gen_p3l1.py` to `gen_p3l10.py` (all ten, for the title-slide time plan line; deeper changes in l1, l2, l3, l4, l5, l6, l7, l8, l9, l10 as listed above).
- Not edited: `p3/workbook_html.js`, `p3/guide.js` (they read the content files).

## Regenerated deck keys

All ten decks were regenerated with `rebuild/gen_p3lN.py` and restyled with `python3 levels/restyle.py split/p3lN` (restyle run once after each regeneration): `p3l1`, `p3l2`, `p3l3`, `p3l4`, `p3l5`, `p3l6`, `p3l7`, `p3l8`, `p3l9`, `p3l10`. Slide counts: 27, 26, 26, 26, 26, 26, 25, 25, 26, 27.

## Printed set

`bash levels/build_level.sh 3` ran cleanly. Student workbook 48 pages (unchanged; every lesson is still 2 core pages + Think Harder + Challenge, and page 2 of each lesson still starts at the expected question), tutor guide 60 pages, weekly dose 25 pages; weekly PDFs: student 14/8/8/8/9 pages, tutor 10 each. L4 page 2 and L9 page 1 were viewed and fit.
