# P3 re-audit fixes, round 2

Source: docs/audit/reaudit/reaudit_p3.md. Only P3 files edited. Nothing committed or published.

## Fixes
| # | Finding | Fix | Files |
|---|---|---|---|
| 1 | "Send a photo via approved channel" | Line deleted; now "hold up the answer page to the camera in the open group call. Never ask a child to send a photo or message." Paper-to-camera practice kept. | p3/guide.js |
| 2 | "Only to the tutor on camera" claims (not private in a group call) | Reworded everywhere to "show your tutor on camera, in the open call, or keep it to share if you want; no photos, no private messages" (guide routine table, sneak-peek, exit, setup; sneak-peek and exit slide notes). | p3/guide.js, rebuild/p3_gifted.py |
| 3 | "(hold up together)" whiteboard wording | Replaced with "show your tutor on camera or keep it to share if you want" in L1, L2 (incl. visible warm-up text), L3, L5, L6, L9 slide notes. | rebuild/gen_p3l1,2,3,5,6,9.py |
| 4 | Look-back "still stuck" has no tutor view | Tick now reads "I am still stuck (I can ask for a check-in in the open class, with my parent nearby)". Workbook note and slide/guide tell the tutor to say to the whole group "say check-in please in the open class or ask your grown-up to tell me"; no hand signals, no private messages; next lesson opens with a whole-group "what is still tricky?". | p3/workbook_html.js, rebuild/p3_gifted.py, p3/guide.js |
| 5 | Investigation (min 67-70) has no slot or debrief | New "Investigation" slide in all 10 decks (67-72 min, own slot, model answer in notes). Talk time now 72-80 with the first 3 minutes as the Investigation debrief; unfinished work goes home and is shared (volunteers) at the start of next lesson. Plan, guide routine, segments, title time plan updated. | p3/gifted.json (plan), rebuild/p3_gifted.py, p3/guide.js |
| 6 | Unsupervised pairs until min 52 | Tutor visits every breakout room by minute 47 (guide, ws1 slide notes, title time plan). | p3_gifted.py, guide.js |
| 7 | "After question 3 choose" lets a child skip page-2 practice | Now "page 1, then Q4 and Q5 of page 2, then choose" (workbook Start-here box, guide, slide notes). | workbook_html.js, guide.js, p3_gifted.py |
| 8 | L8 Q5(c) hint gave the answer | Hint now "put your checker on EF first, then slide it to G". | p3/content/l8.js |
| 9 | L9 spill and typo, 17 parts | Cut to 12 parts: Q1 a/b merged to pairs (4 parts), Q2 2, Q3 1, Q4 2, Q5 3; Q3(b), Q6 bus table removed (budget-best item added to unprinted stretch; bus idea already in stretch s3). No "if time" marks left. Keys, deck lines, ws1/ws1ans/ws2/ws2ans/teach24/teachlist notes updated. "5:15 p.m.." double full stop fixed in the guide and slide notes. Page 43 and 44 rendered: no spill. | p3/content/l9.js, rebuild/gen_p3l9.py, guide.js, p3_gifted.py |
| 10 | L2 Q1(a) hard first item | Swapped: (a) 532 - 216 = 316 is now the first, supported item; the two-carry sum is (b). Hint and key updated. Rendered p8 OK. | p3/content/l2.js, rebuild/gen_p3l2.py |
| 11 | L3 page 2 only Q5 non-star | Q4 "(if time)" removed; only Q6 starred. | p3/content/l3.js, rebuild/gen_p3l3.py |
| 12 | L7 sneak vocabulary | Sneak puzzles and explore Go further now say "how many squares does it cover" and "how far all the way round the edge" instead of area/perimeter. | p3/gifted.json |
| 13 | L4 Go further Q1 (c0) and sneak puzzle 2 at P4/P5 level | c0 now: 120 stickers, 3 times as many, (a) each (30, 90), (b) Ali gives 20 (70, 50). Slide, see-it diagram, walk-through updated. Sneak puzzle 2 now: Ali $12, Ben $5 less, Mei twice Ben = $14. | l4.js, gen_p3l4.py, gifted.json |
| 14 | L1 ws1ans garbled note | Reworded (9 numbers, two 5s are one card). | gen_p3l1.py |
| 15 | L10 exit notes favourite-lesson line | Removed. | gen_p3l10.py |

## Verified with Python
532-216=316 and the digit solution 3447+2578=6025 (unique: 4, 7); 5?2-216=316 gives 3; 4x65=260, 300-260=40; 4080 ml = 4 l 80 ml; 3 m 6 cm = 306 cm; 3:45 to 5:10 = 1 h 25; 4:35 + 50 min = 5:25; 9:15 back 1 h 50 = 7:25; all 3-item budgets of the L9 list (best $19.35, change 65 cents; book+puzzle+water = $20.25); L4 120/4 = 30, 90, 70, 50 (total 120); L4 12-5=7, 14; L1 count 9 of 12 arrangements.

## Build
Decks regenerated (gen_p3lN.py then levels/restyle.py split/p3lN, all 10); slide counts 30, 29, 29, 29, 29, 29, 28, 28, 27, 30; previews: no overflow; new/changed slides viewed. `bash levels/build_level.sh 3` ran: workbook 58 pp, tutor guide 83 pp, weekly dose 25 pp. Workbook pages 8, 14, 39, 43, 44, 47 viewed.

## Left and why
- L5 and L8 reading load (about 372 and 254 words): needs rewritten stems; not changed in this pass.
- L10 no "List card" slide for the breakout stations: layout work, left.
- L7 and L4 mini-lesson second-solution-path, "what will I try next" Look-back line: design additions, not defects.
- Gifted rubric criterion items not wording defects.
- Shared files (not touched): Weekly Dose PDF (levels/mkextras.py / hp parent pack) still uses the heading "Challenge"; the weekly tutor PDFs are sliced from the guide so they carry the fixes. levels/scheme.py and hp/* may carry the older "tutor only on camera" or "approved channel" phrasing for other levels; not checked here.
- The workbook Look-back page and guide now promise only what the tutor can do. If the decision is to drop the "still stuck" tick altogether, edit workbook_html.js lookBack and p3_gifted.py c3.
