# Level 6 re-budget pass: every lesson fits 90 minutes live online

Applies `docs/audit/timing_p6.md` (sections 5 and 6). Nothing was committed. Sources edited: `p6/content/l1..l10.js`, `p6/content/gaps.json`, `p6/guide.js`, `rebuild/gen_p6l1..l10.py`, `rebuild/p6_gaps.py` (the P6 helper every gen calls), new `rebuild/p6_budget.py`, new `p6/budget.json`. Rebuilt: all ten decks (gen scripts, then `levels/restyle.py`), `bash levels/build_level.sh 6`, `python3 levels/mkextras.py 6`. `rebuild/preview.py` reports no overflow on any slide of any deck.

## 1. Single source of the clock

`rebuild/p6_budget.py` holds the part budgets and the clock time of every slide of the ten lessons (each lesson sums to 90, checked by `check()`). `python3 rebuild/p6_budget.py` writes `p6/budget.json` in the requested shape (`parts` with title/start/end, `optional_slides`). `rebuild/p6_gaps.py` (called at the end of every gen) rewrites every slide's time pill and the leading `Minutes a to b` of its notes from that table, the title-slide time plan (L1 to L9), and the break minutes. `p6/guide.js` reads `p6/budget.json`: seg headings, REC cue minutes (rounded to whole minutes because `levels/reccues.js` reads integers only), the "at about minute" lines, the routine table, the new cut-first ladder. Half minutes are kept (for example 12.5) so the numbers equal the audit's.

## 2. Part budgets, old -> new (minutes)

| Lesson | Opening | Sneak | Warm-up | Explore | Mini | Break | Worksheet | Flex | Talk | Exit + looking back + stamp | Sum |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 -> 4 | 5 -> 6.5 | 15 -> 12.5 | 10 -> 11 | 5 -> 4.5 | 35 -> 33.5 | 0 -> 2.5 | 7 -> 5 | 8 -> 8.5 | 90 |
| 2 | 2 | 3 -> 4.5 | 5 -> 6 | 15 -> 14 | 10 -> 8.5 | 5 -> 5 | 35 -> 35.5 | 0 -> 1.5 | 7 -> 5 | 8 -> 8 | 90 |
| 3 | 2 | 3 -> 3.5 | 5 -> 6 | 15 -> 15 | 10 -> 10 | 5 -> 5 | 35 -> 33 | 0 -> 3 | 7 -> 6 | 8 -> 6.5 | 90 |
| 4 | 2 | 3 -> 4 | 5 -> 6.5 | 15 -> 14 | 10 -> 8 | 5 -> 5.5 | 35 -> 34.5 | 0 -> 3.5 | 7 -> 5 | 8 -> 7 | 90 |
| 5 | 2 | 3 -> 4.5 | 5 -> 6.5 | 15 -> 13 | 10 -> 9.5 | 5 -> 5 | 35 -> 34.5 | 0 -> 3 | 7 -> 5 | 8 -> 7 | 90 |
| 6 | 2 | 3 -> 4.5 | 5 -> 6 | 15 -> 14.5 | 10 -> 10.5 | 5 -> 5 | 35 -> 31.5 | 0 -> 2.5 | 7 -> 6 | 8 -> 7.5 | 90 |
| 7 | 2 | 3 -> 4.5 | 5 -> 6.5 | 15 -> 14.5 | 10 -> 12.5 | 5 -> 5.5 | 35 -> 30 | 0 -> 2.5 | 7 -> 5 | 8 -> 7 | 90 |
| 8 | 2 | 3 -> 4 | 5 -> 5.5 | 15 -> 14.5 | 10 -> 11 | 5 -> 5 | 35 -> 31 | 0 -> 4 | 7 -> 6 | 8 -> 7 | 90 |
| 9 | 2 | 3 -> 4.5 | 5 -> 5.5 | 15 -> 14 | 10 -> 11.5 | 5 -> 5.5 | 35 -> 32.5 | 0 -> 1.5 | 7 -> 5 | 8 -> 8 | 90 |

Lesson 10 (own plan): opening 2; sneak 4; warm-up relay dropped (3 -> 0); challenge round 15 -> 13.5; starter projects 7 -> 7; break 2 -> 3.5; plan and build 30 -> 28; flex 2.5; showcase 23 -> 22; talk 1 -> 0 (folded into the exit slip); exit slip 2 -> 3.5; looking back 2 (kept); certificates and close 2 (kept). Sum 90. The L10 section of the tutor guide now prints this plan: 11 segment headings, REC cue minutes and recording chapter table match it (they printed the default Explore/Mini-lesson/Worksheet headings before).

Exit slip + looking back + close = exit slip (minutes to 86) + looking back 86 to 88 + close and stamp 88 to 90 in every lesson, so the 4 never-cut minutes are always the last 4. The flex sits right after the worksheet check (L10: after plan and build) and is labelled "Flex (catch-up or Think harder; lose first)" in the guide, the slides' title notes and `budget.json`.

## 3. What was cut or moved, by lesson

Every lesson: sneak-peek has one show moment after both puzzles, answers clicked through with no reaction round (15 words each); the `go` (Go further) slide is out of the deck (its what-if is in the notes of the explore slide and in the guide, for pasting in the chat); worksheet preview slides are shown, not read; check-together slides show all answers at once (no click builds) and the notes ask one volunteer to explain only the idea question; exit slips are held up together; shorter looking-back line in the guide; the four early-finisher slides (stretch, challenge, chdiag, chwalk) carry the pill "Optional, if you finish early" and no clock time (they stay at the end of the deck order and are listed in `optional_slides`). Take-home questions carry a star and the words "take-home" in the workbook and on the preview and check slides; answers stay on the check slides and in the keys.

| Lesson | Warm-up | Explore | Mini-lesson | Worksheet | Talk / exit |
|---|---|---|---|---|---|
| 1 | cards 1, 2, 3, 5 (doubling and decimal cards out); quick Q2, Q3, Q4 | Scratch step and "finished early" Scratch hint removed; Scratch first appears in `we2` (240 s, opens scratch.mit.edu); discussion Q2, Q3 | `try1` kept (slides unchanged) | Q5 take-home; `teachplan` out; `teachbug` folded into `teachtrace` as a second panel | first talk question only (second kept as `talkNext`) |
| 2 | 4 factor cards (12, 16, 24, 29); quick questions 17 / 5, 100 / 7, remainder 0 | discussion Q1 and Q3 (why stop at 7 moved into `we1`); 1-100 grid: see section 6 | `try1` out; prime checker pre-built (150 s) | Q5 take-home; `teachsq` out, `teachplan` folded into `teachtrace` | first talk question only |
| 3 | city line-up shortened (5 cities + Tokyo/Seoul); 3 quick questions | `go` out; all 3 questions kept | unchanged | `teachbug` folded into `teachtrace`; no take-home | both talk questions kept |
| 4 | 3 guess-my-rule rounds (n + 5 out); 3 quick questions | tutor builds live 2 min; one direction per pair, swap = the Go further what-if (gaps.json updated); discussion Q2, Q3 | `try1` out | Q7 take-home; `teachtrick` out, `teachsearch` folded into `teachcode` | first talk question only |
| 5 | 4 counting puzzles (the "pages 15 to 40" and even-numbers cards out); 3 quick questions | paper only; the nested loop is built once, in `teachcode`; discussion Q1, Q2 | `try2` out | Q5 take-home; `teachroute` out, `teachhandcode` folded into `teachhand` | first talk question only |
| 6 | 4 events on the line; 3 quick questions | discussion Q1, Q2 | `teachwhy` folded into `teachcode` (7 slides) | `teachplan` folded into `teachfair`; no take-home | both talk questions kept |
| 7 | turtle game kept (150 s); 3 quick questions | `setup` merged into `explore1`; the start file is the default; triangle and hexagon only (pentagon = Go further what-if); discussion Q1, Q3 | unchanged (7 slides + keep `try1` as first drop) | Q5 take-home; `teachsum` out | first talk question only |
| 8 | 4 clock calls; 3 quick questions | shifted-alphabet strip shown, not copied; discussion Q1, Q2 | `try1` out; `teachloop` folded into `we3` (6 slides); demo 120 s | Q5 take-home; `teachcomb` out | both talk questions kept |
| 9 | 2 quick-eye rounds; 3 quick questions | typing into the Scratch list and the run removed (the program is built once in `code1`, pre-built list, 150 s); discussion Q1, Q2 | `change` folded into `key` | Q6 take-home; `teachif` out | first talk question only |
| 10 | relay dropped | rules slide, teams do Q1 and Q3; `explore2` out (first line of the check) | `try1` out; only Starter A run live | Q2 take-home; Q4 only the chosen starter; Q5 three cells; Q6 three test rows; showcase 2:15 each, stars typed | talk question is the last line of the exit slip; certificates sent as PDFs with praise written; deck order 28 -> 23 slides |

Slides now (including optional): L1 26, L2 25, L3 26, L4 25, L5 25, L6 27, L7 27, L8 26, L9 26, L10 23 (was 29, 29, 28, 29, 29, 30, 30, 30, 29, 28).

## 4. New totals (timing model re-run on the rebuilt decks)

`python3 docs/audit/rebudget_p6_model.py` (new; wraps `timing_p6.py`, applies the audit's FX but not the fixes that only counted a removed slide, because those slides are now physically gone; `timing_p6.py` regex fixed to strip decimal pills). Central estimates:

| Lesson | Audit prediction | Now | Fast to slow | Now minus prediction |
|---|---|---|---|---|
| 1 | 87.3 | 85.7 | 76.5 to 94.8 | -1.6 |
| 2 | 88.5 | 86.7 | 76.9 to 96.4 | -1.8 |
| 3 | 86.8 | 86.1 | 77.1 to 95.0 | -0.7 |
| 4 | 86.5 | 85.0 | 75.8 to 94.3 | -1.5 |
| 5 | 86.9 | 84.9 | 75.6 to 94.3 | -2.0 |
| 6 | 87.1 | 86.2 | 77.0 to 95.4 | -0.9 |
| 7 | 87.7 | 86.8 | 77.5 to 96.1 | -0.9 |
| 8 | 86.0 | 84.9 | 75.7 to 94.0 | -1.1 |
| 9 | 88.3 | 86.6 | 77.3 to 96.0 | -1.7 |
| 10 | 87.3 | 87.4 | 76.7 to 98.1 | 0.1 |

All ten central totals are 84.9 to 87.4, below 90, so the plan keeps 2.6 to 5.1 minutes of real slack on top of the 1.5 to 4 minutes of scripted flex. The slow run is 94.0 to 98.1: the ladder in the guide (and the ladder text in the routine section) covers it. Totals are a little under the prediction because the audit modelled the cuts on the old decks and the rebuilt decks also lose a few slide-change seconds and words.

## 5. Page counts

Workbook 55 pages (unchanged; L1 and L10 spilled to 3 worksheet pages after the star edits and were trimmed back: shorter Q4 text in L10, shorter Q5 text and a 132 px program box in L1, one table row removed in L10 Q5). Tutor guide 102 -> 104 pages (cut-first ladder, flex lines, L10 plan). Weekly Dose 25. Free taster 5, What Learners Get 1.

## 6. Not applied, and shared-file notes for the lead

- 1-100 grid for L2: not added. The kit has no grid page and a new page would grow the workbook; the materials list and `explore1` already say "printed 1 to 100 grid (or squared paper)". Needs a kit page or the weekly pack (shared `hp/*` / `p6/kit.js` decision).
- "pages 15 to 40" in L5 was not stray wording but a real counting card (answer 26); the audit's fix (drop that card) is applied and the phrase is gone from the content and slides.
- Tutor-built Scratch files (L4, L7, L10) not built, as instructed; the notes still say the tutor builds them.
- Take-home questions are marked in the question text, preview and check slides, key and guide; the Finish page was not given a take-home list (it is full).
- Optional early-finisher slides stay at the end of the deck order (labelled, no clock time) rather than moving before `ws1`.
- Shared files not edited: `rebuild/slidekit.py` `check_slide` builds each answer with a click build, so L9 and L10 define a local all-at-once `check_slide` (L1 to L8 had local helpers edited). `levels/reccues.js` `mins()` only reads whole minutes; `guide.js` therefore passes the rounded length (a 12.5-minute explore says "about 13 minutes"). `rebuild/p6_gaps.py` is shared by all ten P6 gens (it now owns the clock text); other levels' helpers are untouched.
- `docs/audit/timing_p6.py` was lightly edited (decimal pill regex); its FX table is unchanged.
- Notes of every slide stay under 4,000 characters (checked).
