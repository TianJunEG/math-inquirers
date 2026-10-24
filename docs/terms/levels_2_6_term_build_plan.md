# Build plan: term-time program for Levels 2 to 6 (200 lessons) in the shape of Level 1

Planning document only, written 23 Oct 2026 on branch `claude/great-fermi-1hv4vc`. No lesson, tool, book or holiday file was edited, nothing was built, nothing was pushed. All hours are agent-hours and are **estimates**; the Level 1 wall-clock figures in section 7 are read from commit timestamps. No private paper or SASMO text appears here; papers are cited by file name only.

Sources read: `docs/terms/owner_decisions.md` (all entries), `level_{1..6}_year_plan.md`, `l2_preflight.md` to `l5_preflight.md` (headline findings, tool and kit sections, effort tables), `l1_term2_preflight.md` and `l1_term3_term4_preflight.md` (headings), `docs/pedagogy/lesson_x10_consolidation_plan.md` (section 10), `docs/pedagogy/term_review.md`, `term/l1/README.md`, `AUTHORING.md`, `WORDING_GUIDE.md`, `SPINE_TERM_DESIGN.md`, `term/l1/tools/*.py` (grep and targeted reads), `term/l1/audit/*.md` (headlines and the `git log` of `term/l1`), `print/make_term_books.py`, `outputs/print/term/term_books_spec.json`, `docs/printing/quote_request.md`, `docs/schedule/term_2027_t1_availability.md`, `docs/schedule/beta_schedule.md`, the headings of `docs/books/p{1..6}_non_routine_catalogue.md`. `docs/sasmo/holiday_skill_coverage.md` does **not exist yet** (the SASMO skill-coverage map ordered on 23 Oct is not written); there is **no Level 6 pre-flight**.

---

## 0. Recommendation in one screen

1. **Generalise, do not copy.** Move the shared tools to one tree (`term/tools/`), read the level from the lesson's folder (`term/lN/`) plus a small `level.json` per level, default every field to the Level 1 value, and prove Level 1 is unchanged with a golden-master rebuild before anything else uses the new tools (section 1).
2. **Pilot first.** Build Level 2 Term 1 (10 lessons) as the pilot, with two independent audit rounds and, if the owner agrees, one real trial class. Then stop and decide (section 5).
3. **Gate the rest on the pilot.** Levels 3 to 6 Term 1 start only after the gate; Terms 2 to 4 of every level are built one term ahead of the calendar, not all at once.
4. **Split Term 1 into two print halves.** Book 1 (lessons 1 to 5) of each level must be print-ready by about Wed 9 Dec 2026 for a 4 Jan 2027 start; Book 2 (lessons 6 to 10 with the Quest) by about mid-January (section 5).
5. **Level 6 needs a pre-flight first** (about 16 agent-hours); it is the only level without one, and Terms 3 and 4 collide with the PSLE.
6. **Keep 8 books per level, 5 lessons per book,** as Level 1 (section 4). That is 48 child workbooks, 48 tutor keys and 48 home packs across Levels 1 to 6.
7. **Total effort for Levels 2 to 6: about 2,600 agent-hours** (range 2,200 to 3,000), about 13 hours per lesson all-in, five times Level 1's lesson budget. At the Level 1 pace this is about 11 working weeks of pure agent time, realistically 4 to 5 months with reviews and trials (section 6).
8. **Nine decisions for the owner** are in section 8. The three that change the schedule most: which levels need Term 1 by January, whether Levels 5 and 6 start with Book 1 only, and whether a trial class comes before Levels 3 to 6.

---

## 1. What to generalise in the Level 1 pipeline

### 1.1 What Level 1 gives us (inventory)

One lesson is one JSON file (about 110 to 120 KB each, 4.3 MB for 40) plus one answer-check script (about 230 lines each, 9,314 lines for 40). Everything else is generated: tutor guide, 1920x1080 deck, workbook, answer key, home sheet and home answers, kit-only pages, parent summary, online practice, and (lesson 10, 20, 30, 40) the Quest Log, Quest tutor notes and Quest grown-up note. Shared code: about 6,200 lines in 17 tool files (`validate.py` 869, `figs3.py` 1,085, `figs2.py` 619, `svg.py` 510, `b_*.py` builders, `common.py`, `spine_term.py`), plus `print/make_term_books.py`, `make_bw_print.py`, `check_bw.py`. Level 1 also has 162 files in `term/l1/audit/` for 40 lessons: that is the real cost of quality, and it is why this plan budgets audits explicitly.

### 1.2 What is Level 1 specific (found by reading the tools)

| Where | Level-1-specific thing | What a level needs instead |
|---|---|---|
| `common.py` | `L1 = term/l1` root for lessons, assets, runner; Mi image path | `LEVEL` root: `term/lN/` |
| `build.py`, `audit.py`, `validate.py` | `AUDIT_LNN.md` and `verify/lNN_checks.py` paths, id pattern `l1-tN-NN`, schema path, leak check keyed on Level 1 titles | level-aware paths, id `lN-tN-NN`, per-level title list |
| `b_guide.py` | "Level 1" in the guide footer and cover | level from the lesson file |
| `b_practice.py`, runner | practice keys `t1l01` collide across levels; runner copied from `term/l1/runner` | prefix `lNt1l01`; one shared runner, per-level data |
| `b_print.py` | the A4 workbook CSS is tuned for ages 6 to 8: 18.5 px question text, 31 px (8 mm) answer lines, 36 px answer boxes, 105 px drawing boxes, figure widths 175 to 540 px, tightening classes `tight`, `tight2`, `tight3` | per-level CSS block from `level.json`; a "Working" box and "Ans:" frame for Levels 4 to 6 |
| `validate.py` | workbook page-fill thresholds (85 percent, warn below 80), reading load (40 words child, 90 parent), tier counts (Start 5 to 8, Think 3 to 5, Go 3), Mi appearances, "tutor reads every question aloud" | per-level values in `level.json` |
| `spine_term.json`, `spine_term.py` | tool-of-the-day table for 40 lessons, spine band A (ages 6 to 8) | one table per level, band by age from `levels/spine.json` |
| `figs2/3/4.py`, `svg.py` | figure families up to Level 1 (no stacked fractions, no vertical column sums, no balance, no solids, no isometric, no graphs with scales) | new families, listed per level in section 3 |
| `b_quest.py` | `TERM_TOOLS` rows (4, 6, 7, 8 tools met), gate counts and page targets (4, 3, 4, 4) | tool rows per level; `scope: "year"` already exists |
| `print/make_term_books.py` | already has `--level`, `--size`, `--per-term`, `--ages`; kit pages and real-size pages handled | nothing structural; page counts re-read per level |
| `docs` inputs | `WORDING_GUIDE.md`, `school_paper_wording_patterns.md`, P1 catalogue and patterns | the matching `p{N}_*` files (all six exist) and a per-level wording delta (pre-flights 1.1) |

The L2 pre-flight already lists this as task M1 (about 6 hours) and M21 (authoring briefs, about 3 hours). Section 2 below turns it into a safe procedure.

### 1.3 Recommendation: a level parameter in shared tools, not a copy per level

Reasons: `validate.py` alone is 869 lines and the figure files about 2,000; a copy per level means five copies that drift (the L2 pre-flight M1 says the same: "a rename, not a copy: two copies of `validate.py` would drift"); Level 1 needed six "template batches" in 30 hours and each batch rebuilt all lessons, so with copies every fix would be made five times. A parameter keeps one fix, one rebuild path.

**Target layout**

```
term/tools/            shared tools (git mv from term/l1/tools)
term/runner/           shared runner v2 (git mv from term/l1/runner)
term/l1/ .. term/l6/   lessons/ verify/ audit/ out/ assets/ spine_term.json level.json AUTHORING_Ln.md WORDING_GUIDE_Ln.md
print/                 unchanged; make_term_books.py already takes --level
```

`level.json` holds config only; every key defaults to the Level 1 value, so a missing key means "behave as today".

| Config key | Level 1 today | Proposed starting value for Levels 2 to 6 (to be fixed by a page-fill calibration on the pilot, not guessed) |
|---|---|---|
| ages, spine band | 6-8, A | L2 7-9, L3 8-10, L4 9-11, L5 10-12, L6 11-13; band by age |
| question text size | 18.5 px | L2 17.5, L3 16.5, L4 15.5, L5 15, L6 14.5 |
| ruled answer line | 31 px (8 mm) | L2 28 (7 mm), L3 25, L4 22, L5 20, L6 19 (plus a squared option for graphs from L3) |
| answer box | 36 px square | L2 32, L3 28, L4 and up an "Ans:" frame with unit, plus a "Working" box (L4 pre-flight N6) |
| drawing box | 105 px | L2 90, L3 80, then per lesson |
| reading load, child string | 40 words (warn) | L2 45, L3 55, L4 65, L5 75, L6 85; tutor reads every question aloud at L1 and L2 only |
| items per tier | S 5-8, T 3-5, G 3 | same shape; L2 plan bank 6 / 8 / 9 per lesson; Start here count may rise with older children, never the tier meaning |
| spine tools met (term 1 to 4) | 4, 6, 7, 8 | same ladder, with the level additions of term_review 2.2 (bar model L2, ratio table L2, suppose and compare L4/L5, invariants L6) |
| kit pieces per year (cut by a grown-up) | 203 in one term was objected to in the Level 1 audit | budgets from pre-flights: L2 48-81 a term, L3 about 270 a year (84 in the worst term), L4 52 a year, L5 146 a year, L6 to be set |
| home instruments assumed | ruler only if the child has one | L4 needs ruler, protractor, set square (L4 pre-flight D5); L5 and L6 the same |
| banned or restricted words on child pages | Level 1 list | L2 adds: remainder, equivalent, decimal point, letters for unknowns; L4 to L6 lists to be written with the wording delta |
| holiday-copy check source | none (Level 1 Term 1 was pre-decision) | `p{N}/content/l1.js` to `l10.js` question banks and workbook text |
| similarity check sources | `docs/sasmo`, `docs/books` incl. `private_*` | same, plus `docs/sasmo/private_solution_notes_g{N}.md` for the level's grade |

### 1.4 How to avoid breaking Level 1

Level 1 is not final: the integration agent is still editing `term/l1`, the diagram fixes, the x10 and spine work, and the RETROFIT-NOW and TERMCHECK items are open (`owner_decisions.md`). So:

1. **Phase 0 does not touch `term/l1/` at all.** Tool generalisation starts only after the integration agent has committed and says the tree is clean. Until then Levels 2 to 6 can be planned, pre-flighted (Level 6) and briefed, which is documents only.
2. **One owner of the tools tree.** Lesson agents never edit tools (Level 1 rule 13/17 in `AUTHORING.md`). Tool changes go to one engineer queue and land in numbered batches, as the Level 1 "template batch N" commits did, at most one batch a day, each stamped with a `TOOLS_VERSION` string written into every build report.
3. **Golden master before and after.** Before the move, build all 40 Level 1 lessons with the old tools and keep: validator output (PASS/WARN/FAIL counts), per-lesson workbook page counts, extracted text of every PDF, `deck.json`, `term_books_spec.json`. After the move, rebuild with the new tools and diff. Required result: identical page counts and identical extracted text for all 40 lessons and all 24 book PDFs, validator results equal. Any difference blocks the move. Cost: about 4 hours of hands-on plus about 2 hours of machine time (the spine design measured 35 minutes for 40 builds at 4 in parallel).
4. **Compatibility shim.** Keep `term/l1/tools/*.py` as one-line wrappers that import from `term/tools/` for one release, so `build.sh`, docs and any agent brief that still says `python3 term/l1/tools/validate.py` keep working. Remove the wrappers only after the Level 1 RELEASE.
5. **Defaults equal Level 1.** A `level.json` is required for Levels 2 to 6 and optional for Level 1 (all defaults).
6. **Never edit `term/l1/lessons/*.json` for a level reason.** If a Level 2 need exposes a Level 1 content problem, record it in `term/l1/audit/` as a finding.
7. **Output isolation.** Outputs are git-ignored (`term/lN/out/`), approved books live in `/releases/` per level and term; a Level 2 build must be physically unable to write into `term/l1/out`.
8. **Two practice-key spaces.** `t1l01` stays for Level 1 (already printed in Quest and parent pages); new levels use `l2t1l01`. Check no printed family page contains a bare `t1l01` for a new level (the L2 pre-flight failure pattern 3).

---

## 2. Lesson anatomy and the gates every lesson must pass

### 2.1 Anatomy (copy Level 1; the 90-minute shape is binding)

Eleven parts summing to exactly 90 minutes (Opening 2 to 4, Remember 6, Sneak-peek 4, Explore about 10 to 14, Mini-lesson about 9 to 10, Break 4, Workbook about 25 to 28, Talk 4 to 6, Exit 6, Look-back 2 to 3, Flex 4 to 5). Lesson 10 of each term (10, 20, 30, 40) is a choose-the-tool consolidation lesson that hosts Mi's Challenge Quest, 20 minutes after the break (owner decisions TERM-ALL-RECOMMENDED, X10-BEFORE; skeleton in `lesson_x10_consolidation_plan.md` section 1: Quest 20, Workbook 25, Talk 4, Look-back 2, Flex 4). Every lesson file carries: identity (`id lN-tN-NN`, term, lesson, lesson_in_term), big idea, strand label (tutor-only), `beyond` (named, Think harder or Go further only; required from Term 3 at Level 1, required from lesson 1 at Levels 2 to 6), `nonroutine: [{type, tier, item_id}]` (tutor-only, tier T or G, never Start here), spine object (tool of the day and common look-back), joining_cold (6-minute Remember, safe-to-miss note), materials with a kit contract, script, slides, tiers (Start here, Think harder, Go further, Investigation with an easy first step), exit ticket, home practice (5), online practice, parent page, safeguarding block, tutor prep, spare-time menu. The product rules in `AUTHORING.md` and `owner_decisions.md` apply unchanged: neutral tier labels, contest-style items at Think harder only, no MOE/GEP/SASMO claims, no prices, original problems only, no paper hold-ups to the camera, WhatsApp route for "I am still stuck", Mi small with no calculator, groups of at most 8, recording notice before recording, black-and-white printed books.

### 2.2 Gates (every lesson, in this order; a lesson is not "done" until all pass)

| Gate | What | Who | Level 1 evidence it is needed |
|---|---|---|---|
| G0 Spec | Lesson row from the pre-flight read; Think harder / Go further items and `nonroutine` entry match the year plan matrix; holiday-overlap register row read | writer | pre-flights L2 to L5 found holiday items repeated at item level (L2 finding 1, L3 finding 2, L4 finding 1, L5 finding 1) |
| G1 Build and validate | `build.sh` stops on any FAIL; `validate.py` 0 FAIL (schema, timing 90 with scripted at most 86 and slow-class at most 90, slide links, tiers, workbook slots, words, spare time, pages, hand-off, slide privacy, mascot, outputs, REC cues, copy, answers, key PDF, quest, beyond, kit contract, plural guard, cover, identity, figures, glyphs, foreign-lesson leak, spine) | writer | validator failing on copy blocked rebuilds of L3, L10, L11, L17 (FINAL_AUDIT_T1, T2) |
| G2 Independent answer check | `verify/lNN_checks.py` recomputes every answer from first principles (enumerate, simulate), one brute-force oracle per templated practice item, every "exactly N ways / exactly one answer" claim brute-forced | writer, re-run by auditor | uniqueness claims named in L2 pre-flight failure pattern 23; practice variants "1 hours / 1 stickers" found twice |
| G3 Page-design checks | workbook has exactly the designed page count, no orphan page, every page about 85 percent full (warn 80, fail 40), home sheet 1 page (2 with answers split), parent page 1 page | writer | L25 kit spilled a page; spine chip overflowed 5 lessons (SPINE_TERM_DESIGN section 7) |
| G4 View the pages | every workbook page, kit page, a deck contact sheet plus title/look-back/Quest slides, guide page 1, parent page, home sheet viewed at readable size and fixed | writer, again by auditor | AUTHORING step 8; DIAGRAM_AUDIT looked at about 240 pages and found 12 graphs with bare dots |
| G5 Hand-solve | an independent auditor solves every question (Start here, Think harder, Go further, Investigation, exit E1-E3, 5 home items, all Quest gates and the cave) by hand from the lesson data, not from the key | independent auditor | FINAL_AUDIT_T1/T2 and AUDIT_BOOKS_5_8 did this and found 0 wrong answers after fixes, and 2 wrong-in-source `parts[].ans` fields (L23 E1, E3) |
| G6 Wording review | child-facing text against `WORDING_GUIDE` plus the level's wording delta (school-paper phrasing: fixed question words, options (1) to (4), "Ans:" lines at L4+) | wording agent | 39 `WORDING_REVIEW_Lnn.md` files (Lesson 4's and Lesson 5's reviews run to about 100 lines each) |
| G7 Copy and similarity | (a) the existing 7-word shingle check against `docs/sasmo` and `docs/books` including every `private_*` folder (already in `validate.py`); (b) a **new idea-level check** (TERMCHECK, owner decided YES for Level 1): for each lesson question compare number multiset, structure and key nouns against the private paper and SASMO notes for that level, flag at three shared numbers in order plus three shared content words; flagged items read by an independent agent; fix = new numbers, new context or new structure; (c) the **holiday-copy check** (5-word overlap with the level's `p{N}/content/l*.js` question banks) | validator + independent reader | pre-flights found near-copies by hand that a 7-word check cannot see: four SASMO-like items in L3, four in L4, replacements in L5 |
| G8 Black and white | `print/check_bw.py` on workbook, key and home sheet; hatch or label for every category; no colour-only meaning; no "real size" claim on a printed length (books print at 94.3 percent) | build + auditor | CUTOUT_AUDIT F4, FINAL_AUDIT_T1 finding 10 |
| G9 V3 word test (where applicable) | wherever a Quest gate, kit or colour-by-code page maps answers to letters, enumerate single slips and swaps and confirm no wrong placement spells a real word; also confirm a wrong answer cannot pass a self-check | writer | P1 booklet rule (owner KEEP of 23 Oct); not needed in an ordinary lesson |
| G10 Safeguarding and privacy | safeguarding block consistent with the script; no private chat; no number on slides; recording sentence before recording; no tally or ranking on any family page; private three-word scale in tutor notes only | validator + auditor | FINAL_AUDIT_T2 finding 4 (six lessons said it after recording) |
| G11 Hand-off | `next_materials` of lesson n matches lesson n+1 kit and keep list; Remember re-teaches what the lesson needs; safe-to-miss stated | validator + term audit | hand-off errors recurred in Terms 1 and 2 (cut-out audit, FIXES_L18 to L20) |
| G12 Claims | no MOE-aligned, syllabus-aligned, GEP, SASMO preparation, exam results, price, name-the-child; beyond-syllabus statement present | validator | owner rules |

### 2.3 Audit rounds (what Level 1 actually did, and what to copy)

- **Term 1 (heaviest, about 9 agent passes per lesson):** write with self-audit, wording review, independent workbook audit, fix pass 1, guide-and-deck audit, home/parent/online-practice audit, fix pass 2, term-wide audit, final independent audit, final fix.
- **Term 2 and Term 3 (about 6 passes):** write with self-audit and wording review, three independent audits (workbook; guide and deck; home, parent and practice), fix pass, final audit.
- **Term 4 (about 3.5 passes):** write with self-audit and wording review, one batched independent audit per five lessons, fix pass. This was cheaper and found real problems, but was done after the template had settled.
- **Recommended for Levels 2 to 6:** full chain (Term 1 pattern) for the **pilot term** and for the first term of each new level; Term 2/3 pattern for the next terms; batched (Term 4 pattern) for a level's Term 4 **only if** the earlier terms of that level finished with no High finding in audit round 2. Always add one **40-lesson consistency sweep** per level (hand-offs, beyond table, holiday-overlap register, spiral/rewind items, books) as in the L2 pre-flight 11.2, and one **cross-level ladder check** (term_review section 7 lists 12 repeated topics across levels; each pair must differ in demand).
- **Severity scale and instruments** stay the project's: High (wrong maths, unsafe, unusable, release gate broken), Medium, Low; Instrument A (12 criteria, at least 18 of 24) and 100 percent strict tier compliance.

---

## 3. Differences by level

Evidence base for each level (all analysed 22 to 23 Oct): P1 78 tests and 268 non-routine items; P2 about 138 tests, 556 items; P3 about 197 tests, 1,098 items; P4 111 paper labels, 807 items; P5 166 papers, 2,279 items; P6 138 papers, 3,078 items. Pictures were lost in the OCR for P3 to P6 (L3 finding 10, L4 finding 10, L5 finding 5, P6 note), so every figure-dependent item is "wording unverified" until the owner supplies pictures (decision D21 in the pre-flights).

| | Level 2 (7-9) | Level 3 (8-10) | Level 4 (9-11) | Level 5 (10-12) | Level 6 (11-13) |
|---|---|---|---|---|---|
| Pre-flight | `l2_preflight.md` (330 h lessons, 109-125 h engineering) | `l3_preflight.md` (340 h, 133-150 h) | `l4_preflight.md` (335 h, 136 h) | `l5_preflight.md` (391 h, 84-93 h net) | **none** (year plan only; plan estimate 109-116 person-days, human baseline) |
| Reading load / who reads | tutor reads aloud; slow readers; fractions and decimal money are core | children read most items; two-step stories; "Hint:" stems at Think harder | children read; Section C style (a) (b) with "Ans:" and units | children read multi-step items; reasons expected | children read; reason lines ("because ..."); code snippets read on paper |
| New figure families | stacked fractions and 0-1 line, place value, vertical column sums, balance, scale dial and jug, solids and nets, spinner and tally cell, ring and magic figures, matchsticks | vertical layouts for four operations, place-value counters, area model, true bar graph, composite grid figures, equal-gap posts, line and angle figures, mirror images, magic circles (18 items; about 85 h figures) | angle and compass, dimensioned shapes with joined/folded pieces, bar model to 16 units with decimals, nets with fold check, line graphs, pie charts, logic grid, spinners and dice (35 items) | geometry with equal-side ticks and angle arcs (GEO is 17 percent of items), isometric dot paper, tank with divider, dice and painted cubes, line/bar/pie graphs, growing patterns (22 items) | coordinate plane (four quadrants), function graphs, tree diagrams, Venn, binary tables, trace tables, block-stack figures, similar triangles, speed/tank rates; **no pre-flight, so unlisted** |
| Cutting load | 48-81 pieces a term | about 270 a year | about 52 a year | about 146 a year | expected near zero |
| Instruments at home | ruler | real ruler for lessons 11, 13, 15 | ruler, protractor, set square | same | same, plus a device only if the family wants the optional starters |
| Hard content risk | school work labelled "preview" (time to the minute, cents) | Level 5 text was pasted into the Level 3 plan (L3 finding 1: rebuilt in its pre-flight section 4) | 4 near-copies replaced; one impossible Go further item replaced | holiday course holds many plan items; Term 4 exams dip | Term 3 bridge block; Term 3-4 around PSLE |
| Weakest lessons (thin or no paper evidence) | 30, 31, 36, 38, 39 | 19, 21, 22, 23, 26, 34, 36 | 1.9, 3.7, 4.4, 4.5, 4.8, 4.9 | 9, 33, 34, 35, 38, 39, 40 | 29, 38 (and 18) |
| Quest Sprint (optional, ages 9-13) | no | no | optional, not in lesson 40 | optional, not in lesson 40 | optional, not in lesson 40 |

### 3.1 Level 2 (pilot level)

Needs the fraction and decimal-money renderer (M2) first, because fractions, cents and time to the minute are Start here content in 9 lessons. Reading load is still low; tutor reads aloud. The holiday overlap register (pre-flight section 13) is the largest content risk: a holiday graduate meets Term 1 next, and the register lists every item that must change. Level 2 also carries the shared engineering for Levels 2 to 5 (88 of its 125 hours are charged here and netted out of the other three).

### 3.2 Level 3

Biggest figure gap after Level 5 (18 items). Real ruler lessons (11, 13, 15) must never rely on a printed length. Colour dependence is high (patterns, graphs, shaded fractions, mirror images): hatch rules from M18 apply from the first figure. Hand-drawn figures for lessons 22 and 23 are a KIV item.

### 3.3 Level 4

Older children change the workbook, not only the numbers: working box, "Ans:" frame with unit, smaller lines, pages that stay 85 percent full without the large type (L4 pre-flight N6). The `validate.py` fill thresholds assume Level 1 geometry, so the per-level config must exist before the first Level 4 lesson is validated. Unit-chain items are 27 percent of the non-routine paper; the `bar_model` has no code cap but was never read-checked at 16 cells and 4 bars.

### 3.4 Level 5

42 percent of school items need a picture and none was seen; stacked fractions are needed in at least 14 lessons (build with Level 2's M2). KIV items: lessons 28 and 29 may merge, lesson 32 may be too full, lesson 35 is the most overloaded. Term 4 attendance dips for year-end exams; lesson 39 is the safest to skip, then 37; lesson 40 holds the Quest and showcase and cannot be replaced by a recording. Level 5 sits in the evening slots (Sat 5:15-6:45pm default; Thu 7:30-9:00pm and Sun 7:15-8:45pm are offered to Levels 5 and 6 only).

### 3.5 Level 6 (maths and coding bridge)

- **No pre-flight.** Write `docs/terms/l6_preflight.md` first, using the L5 pre-flight as the template: lesson specs with S/T/G items, holiday-overlap register against `p6/content/l1.js` to `l10.js`, figure list (coordinates, graphs, trees, binary, trace tables, block figures), kit contract, hand-off chain, Quest definitions, effort table, owner decisions. About 16 agent-hours.
- **Coding items are paper-based.** In the printed workbook and the Quest, every coding item is read, traced, predicted or repaired on paper: a trace table for a loop, "what does this print", fill the missing line, find the bug, and a hand check of the same answer. No child needs a device, an account or an upload (the year plan's "no accounts, nothing uploaded" rule). Scratch and Python starter files (`.sb3`, `.py`) are a separate, optional tutor-side deliverable, not counted in the lesson gates; the year plan notes the existing `.sb3` files were never tested in a real editor. If the owner wants starters, add about 1 to 2 hours for each of the roughly 25 code lessons.
- **PSLE collision.** Per the plan, PSLE written papers usually fall in Sept to Oct, inside Terms 3 and 4. Owner decision 5 (TERM-ALL-RECOMMENDED): Term 3 is a **bridge block**, not acceleration, depth not drills, "Beyond MOE" labels kept, and no PSLE-preparation claim. Consequences for the build: (a) Level 6 Terms 3 and 4 are built **last** and only after the intake question (plan open question 1: P6 children, post-PSLE children, or also Sec 1) is answered; (b) lessons 29 (Term 3) and 38 (Term 4) stay stand-alone and skippable, lesson 39 is not skippable because 40 builds on it; (c) Quest Sprint is optional and absent from lesson 40; (d) every lesson keeps the six-minute warm-up so a P6 child returning after the exams loses nothing. The year plan also notes speed (km/h) is absent from the 2026 papers: lesson 14 should lead with taps and tanks and keep speed as the labelled secondary preview.
- **Likely extra review:** Grade 7 SASMO file does not exist; three or four lessons (16, 34, 38) need careful block and triangle figures drawn by hand.

---

## 4. Book structure and print consequences

**Recommendation: same as Level 1. Eight books per level, five lessons per book, three kinds of file per book (child workbook, tutor answer key, home pack).** Reasons: the payment unit is the term, a paid term issues two books (`quote_request.md`), `make_term_books.py --size 5 --per-term 10` already does this for any `--level`, the Quest Log sits at the end of Books 2, 4, 6, 8, and the printer quote is structured around it. A single 10-lesson book would be 85 to 95 pages, hard to bind and too heavy to carry to a lesson; four-lesson or six-lesson books break the Quest placement.

| Quantity | Level 1 actual | Per level (estimate from Level 1) | Levels 1 to 6 |
|---|---|---|---|
| Books per level | 8 | 8 | 48 |
| PDF files (workbook, key, home pack) | 24 | 24 | 144 |
| Child workbook pages per book | 42 to 48 (21 to 24 sheets), incl. blanks and kit pages | 36 to 48 (Levels 4 to 6 have fewer kit pages, more text) | |
| Tutor key pages per book | 22 to 30 | 22 to 32 | |
| Home pack pages per book | 12 to 14 | 12 to 14 | |
| Total printed pages | Books 5 to 8: 332 across the three kinds | about 650 a level (about 325 sheets) | about 3,900 |
| One child, one term (two workbooks) | about 88 pages (44 sheets) | 76 to 96 pages | |
| One child, one year, one level | about 350 pages (175 sheets) | 300 to 380 | |

Consequences:
- **Page counts are not known until each lesson is built.** `term_books_spec.json` is the truth; re-run `make_term_books.py --level N` and re-read it after any rebuild before a quote is sent (already stated at `quote_request.md` line 64). A lesson that gains or loses a page changes contents, blanks, sheets and quotes: pages per lesson are frozen after the pilot's fix pass.
- **Print cost is volume-driven and unknown here.** Prices are on hold (owner, 23 Oct), so no figure is given. Ask the printer to quote per title for orders of 1 to 9, 10 to 49 and 50 or more copies. Because there are 48 child titles and early cohorts are small (groups of at most 8, one weekly slot per level), print each term's two books **on payment only** and do not stock Terms 3 and 4.
- **Answer keys are tutor copies,** one set per tutor, never per child. With one tutor the key set is 8 books per level, 48 in all, and can stay digital.
- **Binding and scaling rules carry over:** A4, black and white 1-bit 600 dpi, double-sided, flip on the long edge, left binding with a mirrored 12 mm gutter, content scale 0.9429, even page counts, blank pages intentional, kit pages with blank backs. The B&W conversion (`make_bw_print.py`, `check_bw.py`) runs per level and its output per level is checked for equal page counts to the colour version.
- **Quest Log page targets** (4, 3, 4, 4 at Level 1) become targets for each level; a log that needs one more page costs a sheet (two pages) in that book.
- **Toolbox card:** ships printed with Book 1 of the first term a child buys (CARD-BOOK1); one A5 card per child per band.
- **Open print option for the owner:** issue Book 1 at payment and Book 2 at lesson 4 (matches the instalment rhythm in decision 5), instead of both at payment. It halves the January print rush; it is a decision, not assumed.

---

## 5. Sequencing, parallelism, prerequisites and release schedule

### 5.1 Recommended order (8 lines, also the final reply)

1. **Now to about Wed 28 Oct:** no build. Level 1 integration finishes and is committed; owner answers the section 8 decisions that block Phase 0; write the Level 6 pre-flight (documents only).
2. **Phase 0, about 28 Oct to 3 Nov (5 working days):** move tools to `term/tools/`, add `level.json`, golden-master Level 1, build the Level 2 shared engineering (M1, M2, M4, M5, M14, M15, M21, hatch rules M18, kit KA) and a Level 2 stub that builds with a Level 2 footer.
3. **Phase 1, about 4 to 13 Nov: Level 2 Term 1 pilot** (10 lessons, full audit chain: self-audit, wording, 3 independent audits, fix, final audit). Log start and end of every agent so the hours are measured, not estimated.
4. **Gate, about Mon 16 Nov:** owner reviews three lessons (one number, one fraction/money, the Quest lesson) and the audit summary; optional trial class (section 5.4). Decide the go list.
5. **Phase 2, about 17 Nov to 11 Dec: Book 1 (lessons 1 to 5) of Levels 3, 4, 5, 6 in parallel**, with Level 2 Book 1 frozen first. Print-ready files by Wed 9 Dec; order by Fri 11 Dec (lead time 18 days, as the 6 Nov order for a 24 Nov start).
6. **Phase 3, about 14 Dec to 15 Jan:** lessons 6 to 10 and the Quest of Term 1 for Levels 2 to 6 while Term 1 starts; Book 2 print-ready by about mid-January for lesson 6 in early February.
7. **Phase 4, January to March:** Term 2 of Levels 2 to 6 (lessons 11 to 20), print-ready by about 12 Mar for a 22 Mar start; Level 6 Terms 3 and 4 built last, after the PSLE intake decision.
8. **Rolling afterwards:** Term 3 and Term 4 of each level are built one term ahead and only for levels with enrolled groups; dates after Term 2 are unverified.

### 5.2 Prerequisites

1. **Level 1 final first, for tools and decisions, not for content.** Level 2 work needs: the integration agent done; WAIT-DIAGRAMS gates (diagram fixes re-checked) and RETROFIT-NOW / TERMCHECK finished or explicitly deferred, because they change the validator and the `nonroutine` field; spine (Phase B) applied or its fields frozen, because new levels will be authored with the spine from lesson 1. If the Level 1 RELEASE slips, Level 2 can proceed once the tools tree is stable and the golden master is taken.
2. The year plans still carry a stale section 5 (a 25 to 30 minute check) and some tier tables not rewritten after the x10 and spine changes; each pre-flight records the supersession. The Level 3 year plan's non-routine section is Level 5 text (L3 finding 1): use the pre-flight section 4 instead and ask the owner to replace the plan section.
3. Owner-supplied pictures from the school papers (D21) for any lesson whose item depends on a figure. Without them the lesson is built, but marked "wording unverified" and cannot pass G6 for those items.

### 5.3 Parallelism and file collisions

File ownership is the rule that made Level 1's 9-way parallelism work. Map:

| Resource | Owner | Collision risk and rule |
|---|---|---|
| `term/lN/lessons/lNN.json`, `verify/lNN_checks.py`, `AUDIT_LNN.md`, `out/lNN/` | exactly one writer agent per lesson | none if one agent per lesson; auditors write only `audit/*_LNN.md` |
| `term/tools/*` (validate, figs, builders, svg, common) | one engineer agent per file; batches queued | the real collision point. Lesson agents never edit; they file a request. Batch daily; each batch triggers a rebuild of every built lesson (Level 1: "Rebuild L01-L20 with batch N" commits), so with 200 lessons keep batches to weekly after the pilot |
| `term/lN/spine_term.json`, `level.json` | the level lead agent | generated or edited once per level; locked during lesson writing |
| `term/runner/` | engineer | versioned and backward compatible (owner default 7) |
| `print/make_term_books.py`, `make_bw_print.py`, `check_bw.py` | build agent | run after lessons freeze, one level at a time |
| `docs/terms/owner_decisions.md`, year plans, pre-flights | orchestrator only, append-only | lesson agents report, they do not write |
| `levels/spine.json`, `levels/spine_icons` | engineer | shared with the holiday program; changes need a holiday rebuild check |
| git | explicit `git add` of own files; never `git add -A`; never `*.whl` | Level 1 used WIP checkpoint commits; lesson agents commit only their own folder |
| extension workbooks (`extension/`, owner approved Levels 2-6 builds) | separate agents | shares the figure library and the SASMO skill-coverage work; coordinate figure additions through the same engineer queue |

**Agent counts.** Writers: up to 10 per level-term (one per lesson) when the lesson's figures exist; Level 1 ran 9 at once. Auditors: 2 to 3 per term, one per audit type. Engineers: 3 in Phase 0 and the pilot, 2 afterwards (Level 2 pre-flight sprint plan: 1 engineer for Sprint A, 2 for Sprint B). Overall cap suggested: about 12 writers, 3 engineers and 4 auditors at once, across at most **two levels in the same week** after the pilot, so that audit and fix passes of one level do not wait behind the writing of another.

**Within a level**, the L2 pre-flight 11.2 waves apply: Wave A (lessons that need no new figure) can start on day 0; Wave B after place-value, column-sum and fraction figures; Wave C after solids, scale and spinner figures; Wave D the four Quest lessons last, after the term's other nine lessons pass their fix pass. Do not wait for the whole of Term 1 before starting the Term 2 lessons that need no new figure.

### 5.4 Trial classes

No term lesson has been taught to a child yet (stated in the x10 plan and every year plan). Recommended: run **one 90-minute trial of a Level 2 Term 1 lesson** with a small group (at most 8) during the pilot gate, using the December face-to-face pilot slot if the owner chooses that route, or week 1 of the 2027 Term 1. Observe the timing model (independent work was only 19 to 26 of 90 minutes in the Level 1 audit), the tutor script load and the reading load. A trial of the Quest lesson is worth a second slot because the Quest is untried. This also feeds the per-level calibration of text size, answer space and reading load (section 1.3). If no trial is possible before Term 1, run the first Term 1 week of each level as the trial and hold the Book 2 print until its feedback is in.

### 5.5 Release schedule against 2027 term dates

MOE 2027 Term 1 is 4 Jan to 12 Mar with the March holidays 13 to 21 Mar, so Term 2 starts about 22 Mar (**secondary sources only: verify on moe.gov.sg**; dates for Terms 2 to 4 beyond this are not verified here). The holiday course runs from 24 Nov 2026 (first lessons Tue 24 Nov for Levels 1 to 4, Thu 26 and Fri 27 Nov for Levels 6 and 5, two lessons a week for five weeks). Holiday graduates follow the term calendar (decision 4), so every level that has a beta group sends its graduates to Term 1 on 4 Jan.

| Needed by | Item | Basis |
|---|---|---|
| Fri 6 Nov | (existing) holiday workbook print order | owner decision |
| Wed 9 Dec | Book 1 (lessons 1-5) workbook, key, home pack print-ready, **each level that will run Term 1 in January** | 18-day lead as in the holiday order, with margin for the December closures |
| Fri 11 Dec | Book 1 print order(s) placed | same |
| about 15 Jan | Book 2 (lessons 6-10, with the Quest Log) print-ready | lesson 6 about the first week of February |
| lesson - 7 days | each lesson's deck, guide and online practice published; Quest Log loose copy sent a week before lessons 10, 20, 30, 40 | existing Level 1 practice |
| about 12 Mar | Term 2 Books 3 and 4 print-ready for each level that runs it | Term 2 starts about 22 Mar |
| about May and August | Terms 3 and 4 books, rolling; dates unverified | |

**Is Term 1 needed for every level before 4 Jan?** Only for levels where a family has a seat. The weekly slot grid has 8 slots in total (default: one weekly slot per level; Levels 1 and 2 have one early weekday slot between them), groups cap at 8, so at most six groups (48 children) can run in the default plan, plus spare slots. The owner decides the go list from the beta sign-ups; the plan therefore builds Level 2 first, then 3 to 6 in the order of enrolment, and offers a smaller launch for Levels 5 and 6 (section 8, decision 2).

---

## 6. Effort in agent-hours and a calendar

### 6.1 Level 1 actuals (what can be found)

There is **no agent-hour log**; the figures below are wall-clock times read from `git log` timestamps of `term/l1` (331 commits between 22 Oct 10:55 and 23 Oct 14:04), plus the estimates the project made. Treat them as ratios, not measurements.

| Block | First lesson commit to last lesson of the block | Audits | Fix passes | Wall clock to "fix pass done" |
|---|---|---|---|---|
| Term 1 (10 lessons) | pilot 10:55; lessons 2 to 10 committed 15:01 to 15:17 (about 4.4 h after the pilot started, 9 writers in parallel) | wording 15:50-16:13; independent workbook audits 16:18-16:26; round 2 audits 16:53-17:40 | 16:41-16:54; 17:47-18:16 | about 7.4 h; final audit and final fixes ran to 04:40 next day (about 17.8 h) |
| Term 2 (10 lessons) | foundations 19:15; lessons 19:32-21:15 (about 2 h) | independent audits 21:58-22:43 | 23:02-23:52 | about 4.6 h; Quest rework to 00:14; final audit and fixes to 05:40 (about 10.4 h) |
| Terms 3 and 4 (20 lessons) | foundations 01:25; Term 3 lessons 02:18-03:59; Term 4 lessons 06:13-08:28 | Term 3 per-lesson audits 04:13-05:00; Term 4 batched audits 08:37-08:46 | Term 3 05:14-05:49; Term 4 09:29 | about 8 h for both terms |
| All 40 lessons, first complete pass | 22 Oct 10:55 to 23 Oct 09:29 | | | about 22.6 h |
| After the first pass | diagram audit and fixes (10:21 to 13:16+), books 5-8 audit, x10 consolidation and Quest v2 (13:32-13:50), spine design (13:37, not applied) | | | Level 1 was **not final** about 28 hours after the pilot began (WAIT-DIAGRAMS, RETROFIT-NOW, TERMCHECK, spine apply still open) |

Estimates the project made: the L1 Terms 3 and 4 pre-flight budgeted 172 hours for 20 lessons plus 112 to 135 hours of engineering; the L2 pre-flight uses 7.5 hours per lesson (299 hours) with Level 1 at 8.6 per lesson; the x10 plan uses "about 8 hours per lesson all-in". The pre-flights imply a throughput of about 45 to 57 agent-hours per working day (440 to 455 hours in 8 to 10 working days with 8 to 10 writers and 3 engineers). One Level 1 lesson file is about 115 KB, which is one reason one agent writes one lesson.

### 6.2 Effort model for Levels 2 to 6

| | L2 | L3 | L4 | L5 | L6 | Total |
|---|---|---|---|---|---|---|
| Lessons (write, wording, audit, fix, term audits, sweep) per pre-flight | 330 | 340 | 335 | 391 | 380 (my estimate, Level 5 pace; no pre-flight) | 1,776 |
| Add-ons not in the pre-flights: similarity gate G7 (0.5 h/lesson) 20, spine built in from lesson 1 (0.5 h/lesson) 20, x10 consolidation extra 4, diagram/B&W review pass per level 12, books build and audit 10 | 66 | 66 | 66 | 66 | 66 | 330 |
| Shared template engineering (pre-flight, netted for sharing) | 117 (109 to 125) | 91 | 127 (118 to 136) | 88 (84 to 93) | 60 (my estimate: coordinate plane, graphs, tree, trace table) | 483 |
| Golden-master and parametrisation (Phase 0, once) | 12 | | | | | 12 |
| Level 6 pre-flight | | | | | 16 | 16 |
| **Total per level** | **525** | **497** | **528** | **545** | **522** | **about 2,617** |

So **about 2,600 agent-hours, plausible range 2,200 to 3,000**, about 13 hours per lesson all-in (lesson-only: 8 to 9). The pre-flights' own programme total for engineering is about 445 hours for Levels 2 to 5 (388 with deferrals); I add the Level 6 share and the move. The range allows for the first level costing more (Level 1 Terms 1 and 2 took far more than planned because the template was built while the lessons were written) and for batched audits reducing late-term cost. **Instrument the pilot** (start and end of each agent) and replace this table with measured numbers after Level 2 Term 1.

Per lesson (reference): write and build 3.5 to 5, wording 0.5 to 0.7, audit 1.0 to 1.5, fix 1.0 to 1.8, Quest lessons 11 to 12 hours (L2 pre-flight 11.3). Per term at 10 lessons: about 75 hours for Terms 1 to 4 each, plus about 8 hours of term-wide audit.

### 6.3 Realistic calendar

At 45 to 57 agent-hours per working day, 2,600 hours is about 52 working days (about 11 weeks) of pure throughput. Real constraints: owner review latency, tool batches that force rebuilds, tutor trials, one-term-ahead rolling, and the single human who approves. Planning figures:

| Window | What is done | Hours | Confidence |
|---|---|---|---|
| 23 Oct to 3 Nov | Level 6 pre-flight; Phase 0 (move, config, golden master, Level 2 shared engineering) | about 130 | medium |
| 4 to 13 Nov | Level 2 Term 1 (10 lessons) written, audited, fixed | about 100 | medium |
| 16 Nov gate to 11 Dec | Book 1 (lessons 1-5) of Levels 3 to 6 plus shared figures for them | about 280 (25 lessons x 8 = 200, engineering 80 of the 483) | low to medium |
| 14 Dec to 15 Jan | lessons 6-10 and Quests of Levels 2 to 6 (25 lessons) | about 250 | low |
| Jan to 12 Mar | Term 2 of Levels 2 to 6 | about 500 | low |
| Mar to Aug | Terms 3 and 4 of Levels 2 to 5, one term ahead; Level 6 after the intake decision | about 1,000 | low |

All 200 lessons audited by about April to June 2027 if the owner approves at the same pace, with the final sweeps after each level's Term 4. The January deadline is achievable only for **Book 1 of each level that has a seat**, not for all four terms.

---

## 7. Risks

| # | Risk | Evidence | Mitigation |
|---|---|---|---|
| 1 | Breaking Level 1 with a tools move | Level 1 not final; tools edited by several agents | section 1.4: golden master, shim, one tool owner, no move before the integration agent hands over |
| 2 | Holiday repeats at item level | pre-flights L2 to L5 finding 1 or 2 | holiday-copy check in the validator, register per level |
| 3 | Near-copies of contest items that a 7-word check misses | L3 four, L4 four, L5 several | idea-level check G7(b), independent reader, replacement items in the pre-flights |
| 4 | Figure work on the critical path | Level 2 125 h, Level 3 85 h figures, Level 5 150 h if alone | build once in the shared figure library; figure batches ahead of the lessons that need them (waves) |
| 5 | Rebuild storms | every Level 1 template batch rebuilt all lessons; 40 builds took about 35 minutes at 4 parallel | weekly batches after the pilot; `TOOLS_VERSION` in build reports; rebuild only affected lessons |
| 6 | Unverified wording where pictures were lost | L3-L6 papers read from OCR | owner supplies pictures (D21); mark "wording unverified"; do not claim school style for those items |
| 7 | Quest and the spine are untried with children | x10 plan, all year plans | trial class (section 5.4) |
| 8 | Capacity of one tutor | 8 weekly slots, groups of at most 8 | go list by enrolment; no build of a term nobody has enrolled for |
| 9 | Level 6 PSLE intake unknown | plan open question 1 | build Terms 1 and 2 first; decide intake before Terms 3 and 4 |
| 10 | Old plan text still contradicts decisions | stale check text in plan section 5; Level 3 plan section is Level 5 text | pre-flights record supersession; ask the owner to correct the plans (documents, not in this task) |
| 11 | Mascot age fit | Mi follows the Mi usage rules; ages 10 to 13 | keep Mi small; owner may choose a reduced Mi for Levels 5 and 6 (decision 8) |
| 12 | Printing cost and file count | 144 PDFs, about 3,900 pages | print on payment only; per-title quotes; digital keys |

---

## 8. Decisions for the owner

Each gives my recommendation and a one-word reply.

1. **Pilot first.** Build Level 2 Term 1 (10 lessons), audit, optional trial, then decide on Levels 3 to 6. Recommend: YES. Reply `PILOT-L2`.
2. **Which levels need Term 1 by 4 Jan?** Recommend: every level with beta graduates or a registered group, with Book 1 only guaranteed in December and Book 2 by mid-January; Levels 5 and 6 start with Book 1 (5 lessons) printed and Book 2 written during the first weeks, so the evening groups are not delayed if numbers are small. Reply `TERM1-BOOK1` (or `TERM1-FULL` to require all ten lessons printed by 9 Dec, which roughly doubles the December load).
3. **Trial class before Levels 3 to 6.** Recommend: one 90-minute Level 2 trial (and a Quest lesson trial later), in the December face-to-face pilot if that goes ahead. Reply `TRIAL-YES`, or `TRIAL-WEEK1` to use week 1 of Term 1 as the trial.
4. **Move the shared tools to `term/tools/`** after Level 1 hands back, with the golden master and a shim. Recommend: YES. Reply `TOOLS-MOVE`.
5. **Audit depth.** Full chain for the pilot term, Term 2/3 pattern afterwards, batched audits for Term 4 if earlier terms are clean. Reply `AUDIT-TIERED` (recommended) or `AUDIT-FULL` (about 30 percent more cost).
6. **Level 6 pre-flight now (16 h), coding items paper-based, Scratch/Python starters as an optional separate deliverable.** Also decide the intake (P6 children, post-PSLE, or Sec 1) before Terms 3 and 4 are built. Reply `L6-PREFLIGHT`.
7. **Print policy.** Print each paid term on payment only; issue Book 1 at payment and Book 2 at lesson 4 to 6, or both at payment. Also approve asking the printer for per-title quotes for 1 to 9 copies. Reply `PRINT-SPLIT` or `PRINT-BOTH`.
8. **Mi at Levels 5 and 6.** Keep Mi small (current rule) or use a reduced presence for ages 10 to 13. Reply `MI-KEEP` or `MI-REDUCE`.
9. **Pictures from the school papers (D21)** for Levels 3 to 6, so figure-dependent wording can be verified; owner action. Reply `PICTURES-SENT` when supplied.
10. **Resource conflict with the extension workbooks for Levels 2 to 6** (owner approved, same figure library and SASMO skill-coverage work): which comes first for engineering time. Recommend: term Book 1 first, extension books after the Term 1 figures are done. Reply `TERM-FIRST` or `EXT-FIRST`.
11. **Verify the 2027 term dates on moe.gov.sg** (only secondary sources so far) before the print order. Owner or assistant action.

Not decided here: term price and discount mechanics (prices on hold; no figure in this document), whether graduates of Level N+1 holiday courses skip a term, and the open content questions listed in each pre-flight section 10.

---

## 9. What I did not check

- Hours are estimates; no agent-hour log exists for Level 1 and wall-clock times from commit timestamps include overnight runs, waiting and tool batches.
- I did not read all of every pre-flight (Levels 2 to 5 total about 1 MB); I read the headline findings, the tool and kit sections, the effort and sequencing sections of Level 2, and the headings of Levels 3 to 5. Page counts for Books 1 to 4 were not read from the spec (the spec file in the working tree holds Books 5 to 8; the quote request lists Books 1 to 4 as 44 to 48 pages).
- Per-level text sizes and line heights in section 1.3 are starting values for calibration, not tested.
- The 2027 term dates beyond Term 1 and the early Term 2 start are not verified; PSLE timing is as stated in the Level 6 year plan.
- No similarity check was run (this task does not read private papers); the idea-level check is a specification, not a built tool.
- `docs/sasmo/holiday_skill_coverage.md` does not exist; its gaps may add holiday additions but not term lessons.
