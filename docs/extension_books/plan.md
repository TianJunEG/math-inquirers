# Extension workbooks: plan, spec, tooling, QA

Written 23 Oct 2026. Status: Task 1 done for Level 1 (tooling built, Level 1 units 1 and 2 written and built as a proof). Units 3 to 10 of Level 1 and all of Levels 2 to 6 are NOT written.
Owner decisions that bind this plan: `docs/terms/owner_decisions.md`, entries of 22 and 23 Oct (extension workbooks, addenda 1 to 4, black-and-white printing, "workbooks posted", prices on hold, beyond-syllabus rule). Anything marked **(default)** is the assistant's choice, not an owner decision.

## 0. What the product is

- One extension workbook per level (Levels 1 to 6), WITH answers, sold in the website shop as a physical copy (printed, posted) and a soft copy (download). **No price is printed anywhere** (prices are on hold; the SGD figures in `docs/school_books/pricing_research.md` are placeholders).
- Primary reader: a child who attended the HOLIDAY program, does not want term classes and wants to self-learn. Secondary: an enrolled child wanting extra practice (so nothing assumes the class, and nothing gives away class answers or relies on a tutor, class chat or class numbers).
- Questions are SIMILAR question types to the holiday program of the same level: new numbers, new contexts, new variants. Never a repeat of a holiday question; original problems only; never a copy or light rewording of a contest, book or school-paper problem.
- Not the school early-finisher product (separate edition, separate questions; addendum 6). Home voice, parent/child, Mi on the home edition only.
- Printed copy is BLACK AND WHITE; the soft copy has the same content in a colour theme. Nothing may depend on colour.
- Labels: neutral tiers **Start here / Think harder / Go further** (as in the term books). Private paper. No MOE, GEP or SASMO claim anywhere.

## 1. Product spec

### 1.1 Structure of each level book (A4, portrait)

| Part | Pages | Notes |
|---|---|---|
| Cover | 1 | title, level, "Self-study", ages, Mi (waving), name line. No price. |
| Welcome | 1 | for the child and for the grown-up; the four labels; tips |
| Contents | 1 | unit pages and answer pages |
| Pace plan | 1 | 10 weeks, 3 short sessions a week (20-25 min), week 11 catch-up, tick boxes |
| 10 units | 70 | 7 pages each, see 1.2 |
| My progress | 1 | tick table, Check yourself score, date, look-back lines |
| Certificate | 1 | name line, date, "signed by a grown-up", Mi with trophies |
| Answers divider | 1 | starts on a right-hand page; no tear line (1.5) |
| Answers | about 17 | short worked explanation for every item ("Why:") |
| Blank back | 0 or 1 | only to make the page count even |

Total about 94 pages (target 80 to 100). Measured on the proof: 2 units gave 3.3 answer pages, so 10 units give about 17. If a level's answers run long (Levels 4 to 6 have longer explanations) the fallback is 6 pages per unit for that level (see open decision D1).

### 1.2 One unit = 7 pages (D1: the brief said about 6; the proof showed 6 does not fit at the type size for ages 6-8)

| Page | Content |
|---|---|
| 1 Learn it | "My goal" line; 2-sentence intro; WORKED EXAMPLE (problem, figure, numbered steps, answer); "How to" box (3-4 steps); "Your turn": one try-it item (answer at the back) |
| 2-4 Start here | 3 pages, 4 to 5 items each (13 to 14 items). The main path: school-range plus scaffolding. |
| 5 Think harder | 3 items, each with an upside-down hint |
| 6 Go further | 3 to 4 items (beyond-syllabus items live here and in Think harder only), upside-down hints |
| 7 Check yourself | 4 quick items with a working line, score box (out of 4), "What next?" advice, look-back lines |

Weekly pace (printed in the book): session 1 = pages 1-2, session 2 = pages 3-4, session 3 = Think harder and Check yourself (pages 5 and 7). Go further (page 6) is a weekend page (audit M5, fixed 23 Oct).
Self-study devices: a worked example at the start of every unit; hints printed upside down (no tutor needed, a peek is a choice); a Check yourself score with a rule for what to do next; answers with a short "Why" a parent or child can follow.
Items per unit: about 24 (13-14 Start here, 3 Think harder, 3-4 Go further, 4 Check yourself) plus the try-it. Per level about 245 items; for six levels about 1,470 items.
Unit titles are the 10 holiday lesson topics of the level. Level 1: Number patterns, Number bonds, Picture graphs, Repeating and growing patterns, Working backwards, Money, 2D shapes, Logic and sorting, Length, Puzzle day. Levels 2 to 6: `extension/config/levels.json` (taken from `p2..p6/content/lN.js` headers).

### 1.3 Page grid, type and writing space

- A4 210 x 297 mm. Content width 172 mm in both editions, so pagination is identical.
- Print edition: double-sided, bound on the left edge. Mirrored 12 mm gutter on top of the 13 mm margin: right-hand pages 25 mm left / 13 mm right, left-hand pages 13 mm left / 25 mm right (same idea as `print/make_term_books.py`, which shrinks the page instead). Top 12 mm, bottom 15 mm, page number and running line in the bottom margin (number at the outer corner).
- Soft edition: 19 mm each side, PDF bookmarks, same page numbers.
- Fonts: Fredoka (headings, numbers, body) and Nunito Sans (hints, answers, small print), both from `fonts/node_modules/@fontsource`; embedded in the PDF.
- Writing space by age (`config/levels.json`; defaults, assistant-chosen from common handwriting practice, to be tested with children, D8):

| Level | Ages | Body type | Ruled line | Answer box | Max sentence | Mean sentence |
|---|---|---|---|---|---|---|
| 1 | 6-8 | 17.5 px (13 pt) | 9.5 mm | 16 x 12 mm | 14 words | 9 |
| 2 | 7-9 | 18 px | 9 mm | 16 x 11 | 16 | 10 |
| 3 | 8-10 | 17 px | 8.5 mm | 16 x 10 | 18 | 11 |
| 4 | 9-11 | 16 px | 8 mm | 16 x 10 | 20 | 12 |
| 5 | 10-12 | 16 px | 7.5 mm | 16 x 10 | 22 | 13 |
| 6 | 11-13 | 16 px | 7.5 mm | 16 x 10 | 22 | 13 |

(Level 1 was set to 17.5 px in the proof so that the pages fit; the other rows are untested guesses.)
- Every item sits in a ruled box with a tier badge (circle = Start here, diamond = Think harder, star = Go further, tick-square = Check yourself); the leftover space on a page is shared out as extra working space inside the boxes.

### 1.4 Black-and-white rules (print edition is built in black and white, not converted)

- The print PDF uses a `bw` theme: only black and white; no tints. Tier banners are black bars with a shape and the tier name; Think harder uses a double border. Hatching (45 degree lines) replaces yellow fills; small dots and counters are solid black.
- Lines at least 0.5 pt (answer boxes and item borders 0.55 mm, writing lines 0.35 mm = 1 pt, dashed figure strokes about 0.5 mm).
- Mi is converted to a 1-bit line-art and ordered-dither image (`tools/build.py: mi_uri`), small and few: cover, welcome, certificate only.
- Colour theme for the soft copy: palette from `hp/wb_style.css` (navy, teal, gold), same layout.
- Verification: `verify/bw_check.py` (1.7).
- Why not reuse `print/make_bw_print.py` (colour to 1-bit at 600 dpi): it works on any PDF and remains the fallback, but native B&W keeps the text as vector and avoids 600 dpi raster pages (the proof print PDF is 0.5 MB; a converted 94-page book would be tens of MB).

### 1.5 Answers inside the book, and the perforation note

- Answers are the last section of the same book (one file, one purchase). The divider page sits on a right-hand page; the answer section carries no margin dash and no tear note (audit L17: a double-sided sheet cannot be torn out); the divider says to print the answer pages on their own and keep them in an envelope.
- **(default)** No real perforation: a dashed line and a note only. Real perforation needs the printer (D4).
- The Welcome page tells the grown-up which page the answers start on.

### 1.6 Cut-outs

None needed for the units so far. The builder is written for none; if a unit needs a cut-out (for example a number strip) it must be added as a page that starts on a right-hand page with a BLANK back (as in `print/make_term_books.py`, kit pages) and only when essential (D6 default: avoid cut-outs).

## 2. Data model and pipeline

### 2.1 Files

`extension/data/lN_uXX.json`, one per unit (schema_version 1):

```
id "L1U01", level, unit, title, topic, holiday_lesson, goal
learn: { intro, example: {problem, figure?, steps[], answer},
         howto: {title, steps[]},
         try: {id "L1U01-L01", text, figure?, answer{value[],text}, explanation} }
items[]: { id "L1U01-S01" (S start, T think, G go, C check), tier start|think|go|quiz, page 1-3 (start pages) 4 5,
           text, figure?, parts?[{label, text, answer}], answer{value[], text, list?}, space?{rows[] | table}, hint?, explanation }
```

- `answer.value` is the machine value (list of strings, one per blank or per listed item); `answer.text` is what is printed; `explanation` is the printed "Why". Think harder and Go further items must carry a `hint`.
- Text markup: `{b}` answer box, `{l}` answer line, `{circ:a|b}` choices to circle; newline is a line break.
- Figure specs (`tools/figs.py`): `tiles` (number tiles with arcs; blank tiles for the child), `numstrip`, `dot_boxes`, `tri_dots`, `bonds` (part-whole), `ten_frame`, `number_line`. Tiles, number line and ten frame reuse `term/l1/tools/svg.py`; the black-and-white theme is produced from the same drawing by `recolour()` (dark inks to black, light tints to white, mid fills to hatching).
- Needed for later levels (to be added to `figs.py`, reusing `term/l1/tools/figs2.py`, `figs3.py` and the `p2..p6/content/*.js` SVG helpers where they exist): picture and bar graphs, bar models, fraction walls, clocks, 2D/3D shapes and nets, angles, area grids, ruler, coin and note pictures, code blocks (Level 6; the holiday P6 content draws its own blocks, not Scratch art).

### 2.2 Build pipeline (`extension/tools/build.py`)

1. Load unit JSON; render each page as HTML (`render.py`) per theme (`colour`, `bw`).
2. Paginate the answers: measure every answer block in Chromium, pack them greedily into pages (the unit heading stays with its first entry).
3. Fix numbering: front matter 4 pages; unit n starts at page 5 + 7(n-1); progress, certificate, divider (forced onto a right-hand page, a blank page is added before it if needed), answers; blank last page if the print count is odd.
4. Write two HTML files and print both to PDF with Chromium (Playwright), A4, zero page margin (the page grid is in the HTML), PDF title/author set, bookmarks in the soft copy.
5. Measure in the browser: natural fill of every page body and overflow, before leftover space is shared out; write `outputs/extension/L<N>/build_report.json`; exit 1 on overflow or fill under 85 percent.

Outputs for Level N, in `outputs/extension/L<N>/`: `Math_Inquirers_L<N>_Extension_Workbook_Soft_Copy_Colour.pdf` and `..._Print_BW.pdf` (double-sided, left binding, mirrored gutter, even page count, answers last). Build time is about 15 seconds for the proof.
Printer quote data: page count and sheets per level (print pages divided by 2); extend `print/make_term_books.py`'s `term_books_spec.json` style when quoting. Binding method for a 94-page book (D3).

## 3. Verification tooling (all built; `extension/verify_all.sh <level>`)

| Gate | File | What it does | Failing means |
|---|---|---|---|
| Answers | `verify/run_checks.py` + `verify/lN_uXX_checks.py` | Schema check, then for EVERY item and every part a check function recomputes the answer (simulation or brute force, written without looking at the book answer) and the runner compares it with `answer.value`. A missing check is a failure. Also checks that the number of blanks matches the number of answer values. | wrong answer, missing check |
| Overlap | `verify/dup_check.py` | 7-word runs of every question text against (1) the holiday program of the level (`hp/` for Level 1, `pN/` for Levels 2 to 6), (2) external source texts (`docs/books/private_*`, `docs/sasmo/private_*`): both FAIL; (3) the term lesson files: warning only. Also lists "same sentence skeleton with other numbers" as a REVIEW list for a person. Our own catalogues (`docs/books/pN_non_routine_catalogue.md`) are not a source. Stock command phrases are in `verify/stock_phrases.txt`. | shared 7-word run |
| Wording | `verify/wording_lint.py` | Reading load (max and mean sentence length per level, sentences per stem, long words) and the wording-guide rules: banned words, `50c`, decimal money at Level 1, quantities written as words, claim words (MOE, GEP, SASMO, PSLE, gifted, syllabus), price words, command word present, names outside the cast. | any ERROR |
| Black and white | `verify/bw_check.py` | Renders the print PDF at 200 dpi; fails on any colour pixel (chroma over 0.05 percent) or any flat mid-grey area (a fill that would not survive a photocopier) and on an odd page count. | colour or grey fill |
| Fill and overflow | `verify/fill_check.py` + `build.py` report | Every unit page at least 85 percent full (measured before leftover space is spread), no page overflows. Front and back matter is exempt from the 85 percent rule, never from the overflow rule. | thin or overfull page |

Results on the proof: 80 answers independently checked, 0 mismatches (a mutation test with two planted wrong answers was caught by the runner); 52 question texts, 0 shared 7-word runs with the holiday bank (23,695 grams) or the private sources (360,000 grams); 189 texts linted, 0 errors; print PDF 26 pages, 0 colour pixels; every unit page 86 percent to 100 percent full.

Limits (these need people, see section 4): the checks do not read the explanation sentences; a figure is drawn from its own spec, so a figure that disagrees with the question text is only caught by a person looking; word-overlap does not catch a reworded copy of a problem (the checker finds runs, not ideas); the private source texts are gitignored, so a fresh checkout cannot run the external check (the script prints a warning); duplicates inside one level between units are not checked yet (to add), and the school puzzle books (`docs/school_books`) must be added as a comparison corpus once they have text, to keep addendum 6 (home and school items different).

## 4. QA process and roles

Per unit, in order (the author and the checker are different agents so that a wrong idea is not repeated in both):

1. **Author** (agent): writes `lN_uXX.json` from the holiday program of the level (`hp/lessons.js`, `hp/qbank.json`, `pN/content`), `docs/syllabus_map`, `docs/terms/level_N_year_plan.md` and the non-routine catalogue `docs/books/pN_non_routine_catalogue.md` (original examples may be reused). Writes to `docs/extension_books/lN_source_notes.md` which holiday item type each Start here item mirrors (type map).
2. **Checker** (second agent): writes `verify/lN_uXX_checks.py` from the question text only, without reading the book answers; runs `run_checks.py`; resolves every mismatch by recomputation, not by copying.
3. **Gates**: `verify_all.sh` (dup, wording, bw, fill). Author fixes; REVIEW lines (same skeleton) are read by the reviewer and either accepted ("similar type, new numbers") or changed.
4. **Page review** (agent, with the page images): every page of both PDFs is VIEWED, one by one; checks figure against text, hint upside down, no clipped numbers, space to write, B&W legibility of hatching.
5. **Independent audit** (third agent, as for the term lessons: `term/l1/AUDIT_L*.md`): a cold read of the whole unit as a parent would, solving every item from the printed page and the answer section, listing any ambiguity (more than one right answer), wording trouble ("strange wording"), difficulty out of band for the tier, answers with unclear explanation.
6. **Owner review** (human): units in batches of 5; owner decides tier difficulty, wording and the open decisions.
7. **Child trial** (human, per level): 3 children of the right age do one unit each in a real print (pace, writing space, hints, reading load); fix the config numbers.
8. **Printer proof** (human): one sample print of a full level (binding, gutter, B&W legibility, hatching, Mi, page-count parity) before any physical order. Soft copy: open in two PDF viewers and on a phone.
9. **Release check**: all gates green for the level; no price, MOE, GEP or SASMO text anywhere (`grep`); decisions D1 to D10 settled.

Roles: author agent, checker agent, page-review agent, audit agent (each a separate session), owner, trial families, printer. A change after sign-off (answer, wording) re-runs steps 2 to 5 for that unit.

### 4.1 Effort estimate (assistant's rough numbers; the proof is the only measurement)

Measured on the proof: building the whole pipeline and the first 2 units was one long working session; units 1 and 2 themselves took roughly 1 to 1.5 hours each to write, check, lint and view (the first layout passes took longer than the content).

| Work | Per unit | 60 units (6 levels) | Notes |
|---|---|---|---|
| Author (about 24 items, learn page, explanations) | 1.0 to 1.5 agent-hours | 60 to 90 | Levels 4 to 6 slower (longer problems, more checking) |
| Independent checks file | 0.4 to 0.7 | 25 to 40 | |
| Gate fixes and page layout | 0.3 to 0.5 | 18 to 30 | falls as the layout stabilises |
| Page-by-page viewing | 0.3 | 18 | 7 pages x 2 editions at the end of each level |
| Independent audit | 0.5 | 30 | |
| Owner review | 20 to 30 minutes | 20 to 30 hours | human |
| Child trial | 1 unit x 3 children per level | 18 child sessions | human |

Level-level extras: new figure types for each of Levels 2 to 6 (1 to 2 agent-days each, see 2.1); Level 6 coding pages (extra); printer proof and quotes. Total about 150 to 220 agent-hours of authoring and QA for six levels. With several agents in parallel and the owner reviewing in batches, a realistic calendar is 2 to 4 weeks after the open decisions are settled; Level 1 alone about 1 week (8 units left).

## 5. Risks

1. **Copying risk**: similar-type questions drift towards school and contest wording. Mitigation: the 7-word gate against private sources, original contexts, reuse only our own catalogues, audit step.
2. **Wrong answers**: a wrong key in a sold book. Mitigation: independent per-item checks (the author does not write them), audit solving every item.
3. **Overlap with the holiday book is a judgement**: "similar types" means the skeleton may repeat; the REVIEW list makes the call visible. An item whose numbers differ only trivially from a holiday item is rejected by the reviewer.
4. **Reading load and "strange wording"**: owner already reported odd wording in term books. The lint helps, a human read is still needed (read-aloud test, wording guide rule 7).
5. **Black-and-white legibility**: hatching on small shapes and the dithered Mi image can look muddy on a cheap printer or copier. Mitigation: solid black for small marks, printer proof, a 300 dpi check.
6. **Page count and binding cost**: about 94 pages (47 sheets) A4 is too thick for saddle stitch; needs perfect binding, wire-o or a stapled spine (D3). Cost per copy depends on this.
7. **Soft copy sharing**: a PDF can be forwarded. Options: per-buyer watermark in the footer (needs the order system), or accept it (D7).
8. **Level 6 is a coding course** (holiday P6 uses code blocks): the extension needs printed code blocks that read in black and white and a tracing-style answer; most expensive level.
9. **Dependencies**: the build needs Playwright/Chromium, the fonts in `fonts/node_modules` (gitignored), and the private source files for the external gate; a fresh checkout needs setup (`extension/README.md`).
10. **Parity**: 7 pages per unit makes units start on alternating sides; fine for reading, but a unit never starts on a spread of its own. Acceptable (default).
11. **Teacher/school re-use**: addendum 5 floated selling these to schools; addendum 6 says the school edition is a different product. Keep the two item sets disjoint (add the school books to the overlap gate).
12. **Mi poses and the rule "small and few"**: only 3 images per book; if the owner wants Mi on unit pages the page budgets change.

## 6. Open decisions (defaults marked)

| # | Decision | Default |
|---|---|---|
| D1 | Pages per unit: 7 (default, fits the large type) or 6 (cut Check yourself into Go further) | **7** |
| D2 | Title on the cover and in the shop: "Extension Workbook" or another name | **"Extension Workbook, Level N"** |
| D3 | Binding for physical copies (perfect binding, wire-o, stapled) | **perfect binding or wire-o; get printer quotes** |
| D4 | Perforation of the answer section | **dashed line and note only, no perforation** |
| D5 | Soft copy delivery route (download link after payment) and file name | **soft copy = the colour PDF in this folder; route to be built with the shop** |
| D6 | Cut-outs (number strip, coins) | **none; the printed ruler-free design avoids them** |
| D7 | Watermark or order number in the soft copy footer | **off** |
| D8 | Type size and writing space per level (table 1.3) | **as in the table; confirm with the child trial** |
| D9 | Mi: cover, welcome and certificate only | **yes (small and few)** |
| D10 | Hints printed upside down on Think harder and Go further | **yes** |
| D11 | Answers in the same book (yes, per owner addendum 4: "with answers") and a separate loose answer booklet option for parents who want it | **same book only** |
| D12 | Page-count limit per level if a level runs over 100 pages | **drop to 6 pages per unit for that level** |
| D13 | Whether enrolled children also get a discount or bundle (price decision, on hold) | **not decided; no price anywhere** |
| D14 | Unit names (child-facing titles such as "Hops and rules") vs plain topic names | **both: title in the header, topic on the Learn it page** |

## 7. Level 1 proof: what exists

- Units written: 1 (Number patterns, "Hops and rules": 14 Start here, 3 Think harder, 3 Go further, 4 Check yourself) and 2 (Number bonds, "Make 10 and 20": 13, 3, 4, 4); 48 items, 80 checked answers.
- Item types mirror the holiday lessons 1 and 2: skip counting in 2, 5, 10; add and take-away rules; growing patterns; odd one out; two counters meeting on common numbers; first and later terms; bonds to 10 and 20; equal sums; pairs and lists; shape equations; sharing with a difference; magic-number riddles.
- Outputs: `outputs/extension/L1/Math_Inquirers_L1_Extension_Workbook_Soft_Copy_Colour.pdf` (25 pages) and `..._Print_BW.pdf` (26 pages, even; the last page is blank).
- Both PDFs were viewed page by page.
- Not done: units 3 to 10; the type map notes; the cross-unit duplicate check; a full cold-read audit of units 1 and 2; any trial with children.


## 8. Level 1 audit fixes (23 Oct 2026)
See `extension/l1/FIXES.md`. Print edition: the native vector PDF is now converted by `print/make_bw_print.py` (1-bit, 600 dpi) inside `extension/tools/build.py` and checked by `print/check_bw.py`; the vector file stays as `..._Print_BW_vector.pdf`.
