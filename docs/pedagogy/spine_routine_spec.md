# Spine routine spec: strategy card and common look-back (holiday program, 60 lessons)

Design spec only, 23 Oct 2026. Nothing in lessons, decks, workbooks or generators has been changed. Source decision: `docs/terms/owner_decisions.md`, last entry (spine = toolbox of named strategies, giving a reason, checking and persistence; two ROUTINE changes before about 9 Nov: a STRATEGY CARD in every lesson and ONE COMMON LOOK-BACK at the end of every lesson, in workbooks, decks and tutor guides; no lesson rewritten). Findings used from `docs/pedagogy/holiday_review.md` (sections 1, 3, 4, 8.2, 12): toolbox is the weakest pillar; strategies are used but named only on Puzzle Day; "try a simpler case" is almost absent below Level 5; every lesson has a look-back slot but no common routine; only Levels 2 and 5 schedule a check-together slot. Constraints kept: no MOE, GEP or SASMO claims, no result promises, original art only, printed books pure black and white, no Mi on new elements (Mi stays only where `levels/mi_deco.py` already puts it), no calculator.

Owner updates applied (coordinator, 23 Oct): the six holiday workbooks have NOT gone to printers, so they may change now; the Artifact tool is allowed to republish the 60 decks once the changes have landed and been verified.

## 1. The toolbox: eight strategies

Level bands for wording: **A = ages 6-8 (Levels 1, 2)**, **B = ages 8-10 (Levels 3, 4)**, **C = ages 10-13 (Levels 5, 6)**. Names are the same at every level; only the one-line definition changes. (Review question (a): "Try something simpler" is kept at Levels 1-2 with the child words "smaller numbers".)

| # | Name | A (6-8) | B (8-10) | C (10-13) | Icon concept (black line, no fill) |
|---|---|---|---|---|---|
| 1 | Spot the pattern | Look for what repeats or grows. | Look for what repeats or changes by the same amount, then say the rule. | Find the rule, test it on a new case, then use it to jump far. | A row of four shapes (circle, triangle, circle, triangle) and a fifth place drawn as a dotted outline circle. |
| 2 | List every way | Write each way down, in order, so none is missed. | List all the possibilities in an organised order and say how you know you have them all. | Count every case once with a systematic order; rule out repeats. | Three ruled lines, each starting with a small tick box, each with a different pair of dots (filled/empty swapped). |
| 3 | Draw it | Draw a picture or a bar of what the story says. | Draw a picture, bar model or number line that shows what is known and what is asked. | Sketch and label a model; let the picture show what stays the same. | A pencil drawn diagonally, finishing a long bar that is split into three parts. |
| 4 | Make a table | Put what you know in rows and columns. | Make a table, fill it row by row and look down the columns. | Tabulate cases, find the change in each column, extend or generalise. | A 3 by 3 grid with a thick top row and one dot in the centre cell. |
| 5 | Work backwards | Start at the end and undo each step. | Start from the answer and undo each step in reverse order, then check forwards. | Reverse the operations from the result, then confirm by running forwards. | Two boxes with a long arrow curving from the right box back to the left box. |
| 6 | Guess and check | Pick a number, test it, then try a better one. | Make a sensible guess, check it against every clue, improve it. | Guess, check, adjust using how far off you were; stop when every condition holds. | Two stacked small boxes, top box with a cross, bottom box with a tick, joined by a curved arrow. |
| 7 | Try something simpler | Try it with smaller numbers first. | Solve a smaller version first, then see what changes as it grows. | Solve 1, 2, 3 cases first, find how the answer grows, then handle the real size. | A large square on the left, an arrow, a small square with a 2 by 2 grid on the right. |
| 8 | Act it out | Use counters, paper or people to show it. | Use objects, folding or a role-play to see what happens, then record it. | Model or simulate the situation (objects, fold, cut, dice) and record the outcomes. | Two round-headed simple figures facing each other with one round counter between them. |

Icon rules (icons are built later as SVG): 64 by 64 viewBox, one stroke weight (3 units, round caps), stroke only, one stroke colour set by CSS (`#1B2A49` in workbooks, `#FFF9EC` on navy slides), no grey, no tints, no text or numerals inside, no question mark (a dotted outline is used instead), no Mi, no calculator. Each icon must be recognisable at 10 mm in a 1-bit 600 dpi print and at 200 px on a slide. Files: `levels/spine_icons/<id>.svg` (ids: pattern, list, draw, table, backwards, guess, simpler, actout). Review at 10 mm after `print/make_bw_print.py` before approving.

## 2. The STRATEGY CARD

**Content (same structure at every level):** icon + small label "TOOL OF THE DAY" + strategy name + the band definition (table above) + a tick box "I used it". If the lesson has an "also" strategy: a second line "Also useful: <name>" (text only, no icon). Lesson 10 (Puzzle Day, Challenge Day, Showcase Challenge) shows "TOOL OF THE DAY: Choose one" with all eight small icons in a row and a tick box under each ("I chose"). Data for all cards lives in one file, `levels/spine.json` (toolbox, band definitions, the 60 lesson rows below), read by the workbook, deck and guide code, so wording cannot drift between the three.

**Workbook.** First page of every lesson (the page that begins with `hdr(n, topic, 'Start here')`; in Level 6 the first `hdr` call). A fixed box 62 mm wide by 17 mm high (Lesson 10: full width 182 mm by 17 mm), right-aligned in the same flex row as `.ltitle`, so it costs almost no vertical space (title row is about 12 mm tall; net growth 3-5 mm). Icon 12 mm square at left, name bold 13 pt, definition 9 pt (max two lines), tick box 4 mm. Border 0.5 mm solid black, white background (no tint, so the B&W converter leaves it alone). Fallback if the title is long or the first page is full: a full-width strip 182 by 11 mm under the `.namer` line, with the definition dropped (icon, name, tick box only). Hard gate: no lesson may gain a page.

**Deck.** Title slide, all levels: a "TODAY'S TOOL" chip (icon in `#FFF9EC` plus name), 90 px high, inside the "Today we will" card at bottom-left; it must stay left of the card's right margin, which `mi_deco` sets (150 or 250 px) to clear Mi. Levels 1-3 (youngest; Opening is only 1.5 to 4 min): in addition ONE full slide `<deck>-tool` straight after the title, "Strategy of the day": icon 360 px, name 110 px (Fredoka), band definition 44 px, "Say it with me" line, pill matching the Opening window (so `tutor/build_data.py`, which reads the pill, maps it to the Opening part with no budget change). Levels 4-6: badge only: the title chip plus a small chip (70 px high, `left:128px; bottom:100px`) on the `talk` slide: "Tool today: <name>. Did it help?". Lesson 1 of each level adds one line on the tool slide or title: "Eight tools: see your Inquirer Kit card" (the A5 toolbox card is a separate kit item; if print timing fails, send it as a PDF in the welcome message, per review step 3).

**Tutor guide.** Opening part, after the title cue (20 seconds, inside the existing Opening time): SAY "Today's tool is <name>. <band definition> Look for where you use it." DO "Point at the card on page 1 of the workbook." Talk time (20 seconds, inside the existing Talk time): ASK "Where did you use <name> today? What did it help you see?" and listen for the tool named, not the answer. Lesson 10: SAY "Today you choose the tool." ASK "Which tool did you choose, and why?". No minute changes; Level 2 Opening (1.5 min) is the tightest, so the line must be one breath.

### Mapping of all 60 lessons

Main = the lesson's tool of the day (review section 8.2; where 8.2 listed a tool the lesson only touches, I used the lesson's real main move from the section 4 table and show the other as "also"). Hint column: "Y" = "Try something simpler" can be added cheaply as one extra line in the existing hint ladder (17 lessons flagged); "in content" = the lesson already teaches it.

| Lesson | Title | Main strategy | Also | Try something simpler: cheap extra hint? |
|---|---|---|---|---|
| 1.1 | Count with the Frog | Spot the pattern | Act it out | Y: find the 5th jump first, then the 50th |
| 1.2 | Number Bond Inquiry | List every way | Guess and check | - |
| 1.3 | Let's Plan the Fruit Party | Draw it | - | - |
| 1.4 | Pattern Inquiry | Try something simpler | Spot the pattern | in content (build 1, 2, 3) |
| 1.5 | Mystery Number | Work backwards | Act it out | - |
| 1.6 | Coin Combos | List every way | Make a table | - |
| 1.7 | Shape Safari | Act it out | List every way | - |
| 1.8 | Logic Lab | Make a table | - | - |
| 1.9 | Measure It! | Act it out | - | - |
| 1.10 | Puzzle Day | Choose (all eight) | - | - |
| 2.1 | Digit Detectives | List every way | - | Y: 2-digit numbers from 2 cards first |
| 2.2 | Missing Digit Mysteries | Work backwards | Guess and check | - |
| 2.3 | Legs, Wheels and Arrays | Make a table | Draw it, Guess and check | - |
| 2.4 | Pattern Machines | Spot the pattern | Make a table | Y: first 6 cubes, then the 20th |
| 2.5 | Mystery Number Machines | Work backwards | - | - |
| 2.6 | Market Day | List every way | Work backwards | - |
| 2.7 | Fair Shares | Draw it | Act it out | - |
| 2.8 | Shape Builders | List every way | Try something simpler | Y: squares in 2x2, then 3x3, then 5x5 |
| 2.9 | Measure Masters | Make a table | Act it out | - |
| 2.10 | Puzzle Day | Choose (all eight) | - | - |
| 3.1 | Number Sleuths | List every way | - | Y: 3 digit cards, then 4 |
| 3.2 | Cryptarithm Crackers | Guess and check | Work backwards | - |
| 3.3 | Times Table Treasure | Spot the pattern | - | Y: 6x1, 6x2, 6x3 last digits |
| 3.4 | Model Makers | Draw it | - | - |
| 3.5 | Remainder Riddles | Work backwards | List every way | - |
| 3.6 | Fraction Walls | Draw it | Act it out | - |
| 3.7 | Area Architects | List every way | Try something simpler | Y: 4 squares, then 12 |
| 3.8 | Angle and Line Detectives | List every way | Spot the pattern | Y: 1 stair, 2 stairs, 3 stairs |
| 3.9 | Measure and Money Masters | Draw it | - | - |
| 3.10 | Puzzle Day | Choose (all eight) | - | - |
| 4.1 | Factor Hunters | List every way | - | Y: factors of 12 before 24 |
| 4.2 | Big Number Puzzles | Work backwards | List every way | Y: round to tens before thousands |
| 4.3 | Operation Detectives | Guess and check | - | - |
| 4.4 | Fraction Frontier | Draw it | - | - |
| 4.5 | Decimal Detectives | List every way | - | - |
| 4.6 | Angle Turns | Draw it | Work backwards | - |
| 4.7 | Area Architects II | Spot the pattern | List every way | Y: cut 4 tiles, then 12 |
| 4.8 | Symmetry and Nets | Act it out | List every way | - |
| 4.9 | Data Detectives | Make a table | Draw it | - |
| 4.10 | Puzzle Day | Choose (all eight) | - | - |
| 5.1 | Million Puzzles | List every way | - | Y: closest number below 100 000 first |
| 5.2 | Fraction Feats | Draw it | - | - |
| 5.3 | Before and After | Work backwards | Draw it | - |
| 5.4 | Triangle Areas | Act it out | - | - |
| 5.5 | Volume Vault | List every way | Try something simpler | Y: 2x2x2 cube first |
| 5.6 | Rate Racers | Make a table | - | - |
| 5.7 | Percentage Puzzles | Draw it | Make a table | - |
| 5.8 | Angle Chasers | Draw it | - | - |
| 5.9 | Pattern Generalisers | Try something simpler | Spot the pattern, Make a table | in content (start small) |
| 5.10 | Challenge Day | Choose (all eight) | - | - |
| 6.1 | Code the Pattern | Spot the pattern | - | in content (nth term, small n) |
| 6.2 | Prime Hunters | List every way | Try something simpler | Y: primes below 20 first |
| 6.3 | Below Zero | Draw it | - | - |
| 6.4 | Algebra Machines | Work backwards | Spot the pattern | Y: small n first |
| 6.5 | Every Possible Way | Try something simpler | List every way | in content (2, 3, 4 friends) |
| 6.6 | Fair or Unfair? | Act it out | List every way | - |
| 6.7 | Turtle Geometry | Spot the pattern | - | Y: triangle and square before hexagon |
| 6.8 | Secret Codes | Spot the pattern | - | Y: 4-hour clock before 12 |
| 6.9 | Data Detectives | Draw it | Work backwards | - |
| 6.10 | Showcase Challenge | Choose (all eight) | - | - |

Coverage as main: Spot the pattern 7; List every way 13; Draw it 12; Make a table 5; Work backwards 7; Guess and check 2; Try something simpler 3; Act it out 5; Choose (all eight) 6. As also: Spot the pattern 4; List every way 7; Draw it 3; Make a table 4; Work backwards 4; Guess and check 3; Try something simpler 4; Act it out 5. Gaps: Guess and check is main in only two lessons and Make a table in five; Level 5 has no guess-and-check lesson and Level 6 none by hand (review 8.2). That is a content note, not something to patch.

## 3. The COMMON LOOK-BACK

**Three prompts, same meaning at every level, wording by band.** They are about ONE problem the child picks from today (the last or the hardest).

| # | A (6-8) | B (8-10) | C (10-13) |
|---|---|---|---|
| 1 | Did I answer the question? | Did I answer what was asked? | Did I answer the question that was asked (with units or a reason)? |
| 2 | Does my answer make sense? | Does my answer make sense? (Is it about the right size?) | Is my answer reasonable? (Estimate or compare.) |
| 3 | Can I check it another way? | Can I check it another way? | How can I check it another way? (Go backwards, estimate or try a smaller case.) |

Response format: tick "yes" or "not yet" for 1 and 2; for 3, A draws or writes one word, B and C write one short line "I checked by ...". Below the prompts a thin footer that is NOT a prompt: eight small icons with tick boxes "Tool I used" (ties the card to the look-back and replaces the ad hoc "What helped me" lists), plus "I am still stuck (my tutor will come)" and "pass". Pass is always allowed; nothing is collected, read aloud or marked (existing promise kept). Retired rows: "Something I did well", "The hardest part was", "Next time I will try". Loss: tutors lose that feelings signal (decision D3).

**Workbook.** A fixed box at the bottom of the lesson's last page (the page "Before you go: Investigation and Looking back"; Level 1 `coreEnd`), where the current box sits, same width, no taller than the old box (about 42 mm). Heading "Look back" at all levels. Black 0.5 mm border, white fill, dotted answer lines as now.

**Deck.** ONE fixed `reflect` slide per deck (existing id, same position after `exit`, so deck order, `mi_deco` last-slide logic and `tutor/build_data.py` do not change). Identical layout in all 60 decks: title "Look back", three large prompts (band wording), footer ticks, and a label "Timer: 120 / 90 / 75 seconds" (A / B / C; allowed 60-120). Content width at most 1664 px (Levels 1-3) or 1520 px (Levels 4-6) so the small Mi (bottom-right, 120 px) stays clear.

**Tutor guide.** Script, same words every lesson (about 25 s): SAY "Pick one problem from today. Question 1: did I answer the question? Question 2: does my answer make sense? Question 3: can I check it another way? Tick, write one line, or pass. If you are still stuck, tick the box and I will come." DO "Start the timer. Nobody reads theirs out. Praise a check you saw, not speed. Then stamp journals." Existing privacy safeguards stay.

**Timing: each lesson still totals its planned minutes.** The timer is 60-120 seconds; the slot also holds the journal stamp. Only Level 4 changes a budget.

| Level | Existing slot | New plan | Change |
|---|---|---|---|
| 1 | Look-back 3 min (85-88) | timer 120 s + stamp 60 s | none |
| 2 | Looking back 2 min | timer 90 s + 30 s | none |
| 3 | inside "Exit ticket, look back and close" (10.5-13 min) | timer 90 s inside the block; guide `pr('reflect')` text updated | none |
| 4 | Looking back 3.5 min | slot 2.5 min (timer 90 s + 60 s) | 1 min moves to Talk time (3.5 to 4.5; the review's thinnest talk time). Edit `DUR` in `rebuild/p4_budget.py`, regenerate `p4/budget.json`; sums stay 90 |
| 5 | reflection about 2.5 inside the exit block (7-10.5 min) | timer 90 s inside the block | none |
| 6 | Looking back 2 min | timer 75 s + 45 s | none |

Fallback with zero budget edits: leave Level 4 at 3.5 min; the extra minute is stamping time.

**Level 2 and 5 check-together slot.** Levels 2 (2.5 + 2.5 min) and 5 (3 to 4 min per page) already schedule check-together after worksheet pages; they stay unchanged, and the guide line for prompt 3 at those levels adds "That is what we did in check together." Levels 1, 3, 4 and 6 have no such slot; this spec does NOT add one (it would take worksheet time). Decision D4.

## 4. Implementation plan (follows the existing pattern)

Principle from the repo: the workbook and guide generators rebuild from source, so edits inside them are idempotent by construction. Decks are patched files that gen_* scripts overwrite, so deck changes go into a post-pass run LAST that strips its own earlier output before re-adding it (as `mi_deco.py` does with `IMG=re.compile('<img data-mi=...')` and `restyle.py` does with `dedupe_pills`).

**New shared files (create once):**
1. `levels/spine.json`: toolbox, band definitions, look-back prompts and timers, the 60 lesson rows (section 2).
2. `levels/spine_icons/*.svg` (8) and `levels/spine_icons.py` exposing inline-SVG strings (dark and light stroke).
3. `levels/spine_deco.py` (deck post-pass).
4. `levels/spine_wb.js` (`card(lv,n)`, `lookback(lv)` returning HTML) and `levels/spine_guide.js` (`openLines`, `talkLines`, `lookbackLines`).

**Decks (60, `split/*`).** `levels/spine_deco.py <deck dirs>`, called from `levels/restyle.py` in the per-deck loop just before `mi_deco.apply(d)`; also add a restyle call to `levels/build_level.sh` (it does not call restyle today). Idempotence rules:
- (a) every inserted fragment is one top-level element with `data-spine="chip"` or `"badge"` and ends with `<!--/spine-->`; each run first removes `<div data-spine=.*?<!--/spine-->` (re.S), then inserts.
- (b) `<deck>-tool.html` is written whole each run; its id is added to `deck.json` `order` right after the title only if absent. gen_* scripts and `p5_gaps.py` / `p6_gaps.py` rewrite `order` but keep unknown ids; the pass re-checks anyway.
- (c) the `reflect` slide is rebuilt whole from a template that keeps the existing section wrapper, bar, time pill (copied from the old file by regex) and footer, replacing the body and the `<aside>` (new tutor script).
- (d) aside text added to title and tool slides starts with the sentinel `SPINE:`; each run first removes from `SPINE:` to `</aside>`.
- (e) order: `levels/normfoot.py N`, restyle fix, `spine_deco`, `mi_deco`. Test: run twice; the second run must change 0 files.

**Budgets.** Only `rebuild/p4_budget.py` (look 3.5 to 2.5, talk +1), re-run, then `rebuild/p4_fix.py` / the Level 4 deck chain if pills change; run `tutor/build_data.py all` to refresh the console. No other budget is touched.

**Workbooks (6 generators).** Edit: `hp/workbook_html.js` (`hdr` line 6 adds the card; `refl` line 18 becomes `lookback`), `p2/workbook_html.js` (`hdr` line 8; `reflect` line 21), `p3/workbook_html.js` (`hdr` line 9; `lookBack` line 49), `p4/workbook_html.js` (`hdr` line 8; `reflectBox` line 20), `p5/workbook_html.js` (`hdr` line 8; `reflect` line 15), `p6/workbook_html.js` (`hdr` line 12; box at line 27). The card is added only on the lesson's first page (`tag` 'Start here'; Think harder, Go further and Investigation pages get none). Check that `hp/workbook.js` (docx builder) is not in the shipped pipeline before ignoring it. Rebuild per `levels/build_level.sh`: `cd pN && node workbook_html.js && python3 wb_pdf.py` (Level 1 in `hp/`).

**Tutor guides (6 generators).** Edit `hp/guide.js` (Opening segment, Talk time segment, look-back lines 186-188), `p2/guide.js`, `p3/guide.js` (lines 191-195), `p4/guide.js`, `p5/guide.js`, `p6/guide.js`. Add the card text from `spine_guide.js`, replace the look-back SAY/DO block, and add a short "Toolbox and look-back" section to the front matter (eight tools, three prompts). The review's optional Check card and sentence ladder are NOT part of this change. Rebuild: `node guide.js`, then the `docx2pdf_designed.py` line of `build_level.sh`.

**Downstream:** `hp/weekly_level.py` and `hp/parent_pack_level.py` (read the rebuilt PDFs; in `build_level.sh`), and `levels/scheme.py pN` (one sentence about the Look-back). Parent line from `holiday_parent_outcomes_draft.md` ("Your child will also learn eight simple tools for starting a problem, such as draw it, make a list and try a smaller case") goes on the level pages once the owner approves wording.

**Order of work and estimate (today 23 Oct; target done 7 Nov; deadline about 9 Nov).**

| Step | Work | Estimate |
|---|---|---|
| 0 | Owner answers D1-D7 | 30 min owner time |
| 1 | `spine.json`, 8 icons, `spine_wb.js`, `spine_guide.js`, `spine_deco.py` | 4-5 h |
| 2 | Level 1 end to end as pilot (workbook, guide, 10 decks, B&W print, verify) | 3 h |
| 3 | Levels 2 and 3 | 2 h each |
| 4 | Levels 4 (budget edit), 5, 6 | 2.5 h each |
| 5 | Rebuild print (below) | 1.5 h wall time |
| 6 | Verify all 60 decks, 6 workbooks, 6 guides (section 5) | 3 h |
| 7 | Republish 60 decks one at a time (below) | 2-3 h, publish limit applies |

Total about 24-28 hours. Calendar: Levels 1-3 by 28 Oct, Levels 4-6 by 2 Nov, print rebuild 3 Nov, verification 4-5 Nov, republish 5-7 Nov, two days spare.

**Print rebuild order (workbooks may change; not yet at printers):** (1) workbook generators produce the six designed PDFs; (2) `python3 print/make_print_pdfs.py` (colour print PDFs and `print_spec.json`); (3) `python3 print/make_bw_print.py --rebuild --check` (B&W printer files and `bw_spec.json`); (4) `python3 print/check_bw.py`; (5) look at the card and look-back pages of each level in the B&W PDF at 100 percent.

**Republish step (after the changes land and verification passes, never before).** Use the Artifact tool per deck, one at a time, `url` = the deck's existing private link, `file_path` = the deck page. Links: `outputs/deck_urls_all.json` (62 keys; `l6s`, the 60-minute trial deck, is NOT republished; check the extra key) and, for Levels 4-6, `outputs/deck_urls_p4_p6.md`; the two lists must agree before publishing (the md status line says all 60 were republished 2026-10-23). Order: Level 1 lesson 1 to Level 6 lesson 10. After each publish open it once and check the title chip and Look back slide. Decks stay private. On the publish limit, stop and resume the next day; never in parallel. Record the date in the status line of `outputs/deck_urls_p4_p6.md`.

## 5. Verification checklist

**Every deck (60):** `spine_deco.py` twice gives 0 changed files the second time; `deck.json` order has `tool` right after title (Levels 1-3), `reflect` after `exit`, no duplicate ids; one time pill per slide; title chip shows the strategy from the table and clears the card edge and Mi; `reflect` has exactly three prompts in the right band wording and the timer label; Mi on the last slide not overlapping; slide count = old +1 (Levels 1-3) or unchanged (Levels 4-6); speaker notes present; `tutor/build_data.py all` maps `tool` and `reflect` to the right parts and part minutes still sum to 90; render title, tool or talk, and reflect for each level and look.

**Every workbook (6):** page count unchanged (58, 66, 58, 66, 57, 55 source pages per `print_spec.json`); card on the first page of all 10 lessons; Lesson 10 card shows all eight icons; look-back box on the last page of each lesson without spill; nothing outside margins; text 9 pt or larger; `check_bw.py` passes (0 non-grey, no new light-tint cells); icons readable at 10 mm in the B&W PDF; cut-out start and certificate pages unchanged (the print builder finds them by first-line text).

**Every guide (6):** each lesson has the Opening SAY, Talk ASK and look-back script; the tool named matches `spine.json`; segment minutes still total 90; recording chapters (`levels/reccues.js`) still produced; page count about +2 per guide.

**Cross-checks:** the tool named in the deck chip, workbook card and guide is identical for each of the 60 lessons (a 30-minute script over the three outputs); band wording matches level; grep for "Something I did well" returns nothing in decks or workbooks; no calculator, Mi or colour dependency in the new icons.

## 6. Files touched

New: `levels/spine.json`, `levels/spine_icons/*.svg` (8), `levels/spine_icons.py`, `levels/spine_deco.py`, `levels/spine_wb.js`, `levels/spine_guide.js`.
Edited code: `levels/restyle.py`, `levels/build_level.sh`, `rebuild/p4_budget.py`, `hp/workbook_html.js`, `p2..p6/workbook_html.js`, `hp/guide.js`, `p2..p6/guide.js`, `levels/scheme.py` (one sentence).
Regenerated, decks: `split/l1..l10` and `split/p2l1..p6l10` (`*-title`, new `*-tool` at Levels 1-3, `*-talk` at Levels 4-6, `*-reflect`, `deck.json`), then republished.
Regenerated, workbooks and the print files that change: `hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf`, `p2..p6/Math_Inquirers_PN_Student_Workbook_Designed.pdf`, `hp|pN/workbook_body.html`, `workbook_full.html`; `outputs/print/Math_Inquirers_P1..P6_Workbook_PRINT.pdf` (colour, soft copy); `outputs/print/bw/Math_Inquirers_P1..P6_Workbook_PRINT.pdf` (the printer files); `outputs/print/print_spec.json` and `outputs/print/bw/bw_spec.json` (page counts should not change; update `docs/printing/quote_request.md` only if they do).
Regenerated, guides and packs: `hp|pN/Math_Inquirers_PN_Tutor_Guide.html` and `.pdf`, `PN_Holiday_Program_Guide.docx`, `Math_Inquirers_PN_Weekly_PDFs.zip`, parent packs, `tutor/data/*`.
Not touched: lesson content (`content/*.js`, `lessons.js`), question banks, term books, extension workbooks (a later pass can add the card).

## 7. Risks

- **Page overflow:** Start-here pages are dense (Level 5 about 300 words). The card sits in the title row; the gate is unchanged page count, with the 11 mm strip fallback.
- **Timing:** Opening is 1.5 min at Levels 2-4; the tool line adds about 20 s. The Level 4 edit moves 1 min between parts; re-run its sum check. No lesson has been stopwatch-timed (review), so all seconds are estimates; pilot one lesson.
- **Black and white:** stroke-only icons, white-filled card; verify at 10 mm. No colour is the only cue.
- **Duplicates:** gen_* scripts overwrite decks and drop post-pass output; the pass runs last, strips by `data-spine` markers and the `SPINE:` sentinel, and is tested by running twice. Keep `dedupe_pills`.
- **Mi collisions:** new chips are bottom-left or inside the title card; keep `reflect` content narrow at Levels 4-6; add nothing bottom-right.
- **Drift between deck, workbook and guide:** one `spine.json` and the cross-check script.
- **Printers:** the owner says nothing has been sent; if that changes, the 12 print PDFs (6 colour, 6 B&W) are superseded and the printer must be told.
- **Republish:** publish limit; one at a time after verification; a bad republish overwrites the earlier version. `l6s` stays out.
- **Parent claims:** keep "your child will practise"; nothing about results.

## 8. Decisions the owner must make

- **D1** Approve the eight names and the three band definitions.
- **D2** Approve the main/also mapping, notably L1.4, L5.9 and L6.5 as the three "Try something simpler" lessons, and the 17 hint additions.
- **D3** Look-back: accept retiring "Something I did well / hardest part / next time", keeping the "Tool I used" and "still stuck / pass" footer; or keep one old row.
- **D4** Add a check-together slot to Levels 1, 3, 4, 6? Recommended no for now.
- **D5** Level 4: move 1 minute from Looking back to Talk time (recommended) or keep 3.5 min.
- **D6** Full "Strategy of the day" slide at Levels 1-3 and badge only at Levels 4-6 (recommended), or a full slide everywhere.
- **D7** Print the A5 toolbox card in the Inquirer Kit, or send it as a PDF in the welcome message.
