# Daily teasers (website/teasers/)

A new puzzle every day for each of the six levels, picked in the visitor's browser from the **Singapore calendar date**
(Asia/Singapore, UTC+8 with no daylight saving), so every visitor sees the same puzzle that day and it changes at 00:00
Singapore time whatever time zone the browser is in. Static only: no server, no cookies, no tracking, no timers, no scores,
no streaks, nothing saved. The existing fixed puzzle stays on the page as the no-JavaScript / failed-JavaScript fallback.

Owner decisions: **TEASER-DAILY-GO** (docs/terms/owner_decisions.md) and the follow-ups: 365 puzzles per level (one per calendar
date, MM-DD, with a spare for 29 Feb), released in monthly batches, November 2026 first, then December 2026, January 2027 ...;
**TEASER-STRICT** (Levels 3 to 6: a sub-structure at most once a quarter, only with a new story and a new frame) and **L1L2-GAP60**
(Levels 1 and 2: a sub-structure may return after at least 60 days with a new story and new numbers).

**What may be promised on the site (the honest wording rule):** "a new puzzle every day", never "a new kind of puzzle every day" and never "a new idea every day".
At Level 1 a maths idea comes back six times a year (every 61 days) with a new story and new numbers; at Level 2 the same; at Levels 3 to 6 an idea returns once
per quarter at most. Across levels the same idea may appear at several levels: in the round-2 bank **50 of the 172 sub-structures used appeared at three or more
levels** (202 of 366 puzzles; one pattern idea at all six). That is allowed (the rules are per level), but it is one more reason not to promise "a new idea".
In the round-3 bank (Nov and Dec, rebuilt) 41 of the 196 sub-structures used appear at three or more levels (161 of 366 puzzles), and 105 appear at one level only.

**Owner decisions that bind the bank.** TEASER-STRICT, L1L2-GAP60 and the family cap are in force: a **family is used at most 3 times per quarter at Levels 3 to 6
(and at most 3 times in any 60 days at Levels 1 and 2)**; this cap is CONFIRMED by default (the owner's "proceed with the recommendations" instruction), no longer an open question.

**The same date next year.** The bank is keyed by month and day, so a child who visits on 14 Nov 2027 meets the 14 Nov 2026 puzzle again. The
plan is to write a fresh batch (new numbers and new stories, same sub-structure rotation) before a date comes round a second time, and to
publish it under the same MM-DD key only when the previous year's puzzle for that date is retired. Until then the same date shows the same puzzle.
Within one year every answer, number set and story is different (checked by `verify_bank.py`).

## Status

| | |
|---|---|
| Released batches (in `manifest.json`) | 11 (Nov, 30 days) and 12 (Dec, 31 days), for all six levels: 366 puzzles. Rebuilt in fix round 3 (24 Oct 2026): 4 High and 20 or so Medium near-copies replaced by new stories on new structures. |
| Not yet written | Jan to Oct (305 puzzles per level to go, in monthly batches of about 30). Not started: round 2 fixed the structure first. |
| On the live site? | **No.** `site_enabled` is explicitly `false` in `manifest.json`, so `lp_build.py`, `level_pages.py` and `build_site.py` produce exactly the old pages. `website/dist` has not been touched. |
| Taxonomy | 222 sub-structures in 81 families (`taxonomy.json`); 200 are usable at one or more levels. Round 2 merged look-alikes (100 old ids into 39) and added 50; round 3 added **38 new sub-structures** (each with a syllabus citation, a level range, a solver, an independent checker and a sample; all 35 usable ones are used by a released puzzle) and **retired 13 more** whose frame our own books already use (16 retired in all, listed with the reason in `batches/STRUCTURE_REPORT.md`). Usable sub-structures per level: L1 73, L2 97, L3 126, L4 129, L5 121, L6 109; family-capped capacity per quarter at Levels 3 to 6: 114, 117, 113, 104 against 92 needed. Year plan for Levels 1 and 2: `batches/YEAR_PLAN.md`; independent year check: `year_model.py`. |
| Audits | `AUDIT_ROUND1.md` / `FIXES_ROUND1.md`, `AUDIT_ROUND2.md` / `FIXES_ROUND2.md`, `AUDIT_ROUND3.md` / `FIXES_ROUND3.md` (what is closed and what is not), `AUDIT_SELF.md`. |

## How a visitor's page decides what to show

1. Work out the Singapore date from `Date.now() + 8 hours` (no `Intl`, no dependence on the browser's own time zone).
2. The page ships its own fixed puzzle (home: frog hops, ages 6-8; level pages: that level's sample). This is the fallback (owner decision TEASER-DAILY-GO).
3. The two most recent released months are built into every page, so a visitor on those dates sees the daily puzzle at once. Any other released month is fetched from `/teasers/L<level>-<MM>.json`, waiting up to 8 seconds; a late reply is swapped in only if the visitor has not touched the fixed puzzle.
4. If the date has no released puzzle (month not released, file missing, fetch failed or too slow), the fixed puzzle stays, with no date label. Nothing is fetched for an unreleased month.
5. If JavaScript is off, the fixed puzzle is what is on the page. Every visitor therefore sees the same puzzle for the same date, or the fixed one; there is no random or per-visitor pool.

The home page uses the Ages 6-8 set (there is no level picker on the home page). If a page is left open past midnight, the new day's puzzle appears when the visitor returns to the tab (focus / visibility events, no timers).

## Files

| File | What it is |
|---|---|
| `manifest.json` | Which months are released, and `site_enabled` (the switch for going live). |
| `defs/m<MM>/l<N>.py` | Puzzle sources, one file per month and level. Each puzzle is a template (`P(...)`) with parameters, wording, hint and worked explanation. |
| `defs_common.py` | The `P()` helper and text formatting (money, ordinals, mixed numbers). |
| `kinds.py`, `kinds_more.py`, `kinds_r2.py`, `kinds_r3.py` | **Author-side solvers** (`SOLVE[kind]`), one per puzzle kind. `kinds_r2.py` and `kinds_r3.py` hold the kinds of the round-2 and round-3 sub-structures. |
| `brute.py`, `brute_more.py`, `brute_r2.py`, `brute_r3.py` | **Independent checkers** (`BRUTE[kind]`): never import the solver files; walk the whole search space (enumeration, simulation, breadth-first search, exact geometry, dynamic programming over edge sets) and return every valid answer (an impossible extra value when the puzzle is not well posed). |
| `samples_r2.py`, `samples_r3.py` | Worked instances of every round-2 and round-3 kind; `verify_bank.py --selftest` proves solver and checker agree on each (88 kinds), even for sub-structures that no released month uses yet. |
| `taxonomy.json`, `taxonomy.py` | The list of maths kinds (families) and sub-structures per level, with the syllabus citation, the level range, `merged_from` (which round-1 ids were merged), `retired` and the structure rules (gap rule, quarter rule). Every puzzle names its `sub=`. |
| `stock_phrases.txt` | Generic answer-format phrases that may repeat. |
| `build_bank.py` | `python3 website/teasers/build_bank.py [MM ...]` builds `batches/m<MM>/bank.json` (no neighbouring puzzles share a family or a kind, also across a month boundary; 31 Dec is followed by what was 1 Nov at Levels 1 and 2). `--plan` writes `batches/YEAR_PLAN.md`: the 61-day rotation that keeps Levels 1 and 2 inside the 60-day gap rule all year. |
| `verify_bank.py` | `python3 website/teasers/verify_bank.py [MM ...]` re-solves every puzzle with the checkers, checks unique answer, arithmetic in the wording, wording rules, 7-word shared runs, masked-skeleton similarity and the **story check**, the structure rules below, and writes `batches/m<MM>/VERIFY_REPORT.md` and `batches/STRUCTURE_REPORT.md` (true capacity table, retired list). Since round 3 the story check reads **every sentence of the whole working tree** (about 3,800 files, 478,000 sentences, tracked or not, git-ignored private sources included: `outputs/`, `docs/**`, `practice/**` including every `lesson.py` and its data, school booklets, the holiday weeks, `split/`, `rebuild/`, `website/` without `teasers/`, `dist/` and the preview) in windows of one to three sentences, and applies the independent auditor's rules (content words A and A2, numbers B, four-word runs with numbers masked C) on top of the round-2 rules. `--selftest` proves the rules fire (it replays the round-2 wording of the four High near-copies and the Mediums), `--update-lock` rewrites `source_lock.json`, `--strict-capacity` also fails on a taxonomy that cannot supply a full year. |
| `source_lock.json` | Minimum files per source root and the private sources that must exist. `verify_bank.py` refuses to give a verdict (exit 2, "INVALID VERIFICATION") on a checkout that lacks them, so a tracked-only export can no longer print "0 FAIL". Every report starts with the source digest (sha256 over the paths and contents of all source files): the verdict is a function of the bank, the rules and that digest, never of file times, file order or the machine. |
| `selftest_probes.json` | The round-2 wording of the near-copies of AUDIT_ROUND3 and the retired sub-structures that `--selftest` replays. |
| `year_model.py` | **Independent circular year check** (does not import the verifier, the builder or `taxonomy.py`): Levels 1 and 2 rotation (366-day and 365-day year, family window, spares) and an integer program for Levels 3 to 6 (one sub-structure a day, quarter caps, 30-day gap round the year, released Nov and Dec fixed, cap 3 and cap 2, seeded random loss of unreleased sub-structures). Writes `batches/YEAR_MODEL_RESULT.json`. |
| `test_flag_off.py` | Fails when a committed `website/mi_signup.html` or `website/level_pages/*.html` differs from the **flag-off generator output** (generated in a scratch copy, nothing in the working tree is written) or carries the teaser while `site_enabled` is false; also checks `website/dist` is untouched. `test_site.py` runs it first. |
| `batches/m<MM>/` | `bank.json` (built) and `VERIFY_REPORT.md` for each month. |
| `teasers.js` | The browser code (date, picking, answer checking, rendering). |
| `teaser_html.py` | Glue used by `lp_build.py`, `level_pages.py` and `build_site.py`; exports the per-month files. |
| `build_preview.py` | Writes `outputs/owner_review/teasers_preview/index.html` (date and time selector, midnight buttons, answer key). |
| `test_site.py` | Chromium (Playwright) tests on a built site directory (446 checks, flag-off check first). |
| `AUDIT_SELF.md` | The author's own checklist of what was checked and the results. |

## Commands

```
python3 website/teasers/build_bank.py           # rebuild released months
python3 website/teasers/build_bank.py --plan    # Levels 1 and 2: the year rotation (batches/YEAR_PLAN.md)
python3 website/teasers/verify_bank.py          # independent verification (exit 1 on any FAIL)
python3 website/teasers/verify_bank.py --selftest
python3 website/teasers/build_preview.py        # owner preview page

python3 website/teasers/year_model.py          # independent circular year check (--full for more trials)
python3 website/teasers/test_flag_off.py       # committed pages equal the flag-off generator output

# a preview build with the teaser switched on: ALWAYS in a scratch COPY of website/, never in place (the generators rewrite tracked files):
mkdir -p /dev/shm/wsite && python3 -c "import shutil; shutil.copytree('website', '/dev/shm/wsite/website', ignore=shutil.ignore_patterns('dist', '__pycache__'))"
ln -s $PWD/fonts /dev/shm/wsite/fonts
(cd /dev/shm/wsite/website && MI_TEASERS=1 python3 lp_build.py && MI_TEASERS=1 python3 level_pages.py && MI_TEASERS=1 python3 build_site.py --out /dev/shm/site_preview)
python3 website/teasers/test_site.py /dev/shm/site_preview --shots /dev/shm/shots
# if you ever did build in place: git checkout -- website/mi_signup.html website/level_pages
```

## Adding the next month (for example January)

1. Levels 1 and 2: the sub-structure of each day is fixed by `batches/YEAR_PLAN.md` (the released day 61 days earlier); write a new story and new numbers for it, with an answer that differs from every answer within 60 days. Levels 3 to 6: choose sub-structures that are unused in the quarter and at least 30 days from their last use (`taxonomy.json` lists them per level); a family at most 3 times a quarter. A story must not repeat a sentence, a frame or the numbers of anything in our books: write it, run the verifier, and rewrite on any FAIL (a REVIEW is read by the author).
2. Write `defs/m01/l1.py` ... `l6.py` (31 puzzles each). Every puzzle needs a `sub=` that exists in `taxonomy.json` for that level; a new sub-structure needs a syllabus citation, a level range, a solver in `kinds_r2.py`, an independent checker in `brute_r2.py` and a sample in `samples_r2.py` first.
3. `python3 website/teasers/build_bank.py 01`, then `verify_bank.py 01` **on the full working tree** (it refuses an incomplete tree) until 0 FAIL and the REVIEW lines are explained; then `verify_bank.py --selftest`, `year_model.py` and `test_flag_off.py`. Re-run the verifier on the full tree again just before the release: the holiday, term and extension books keep growing.
4. An independent audit of the batch, then add `"01"` to `released` in `manifest.json`, rebuild and re-test.
5. Releasing to the live site is a separate step: set `"site_enabled": true`, run the generators and `build_site.py`, commit the rebuilt `website/dist`.

## Rules every puzzle follows

- Original wording and story; not copied from the holiday program, term lessons, extension workbooks, school booklets or external sources. `verify_bank.py` fails on any 7-word shared run, on a masked-skeleton match with shared numbers, and (round 2) on a **shared story**: the content words of the question (names, number words and very common words removed) found in one source sentence or two neighbouring sentences with the same objects and the same numbers, or the same specific objects (snail and wall, frog and well), or the same wording with other numbers.
- Flag off until launch: `website/mi_signup.html` and `website/level_pages/*.html` stay in their committed no-teaser state while `site_enabled` is false (`test_flag_off.py`). A preview is built in a scratch copy of `website/`, never in place.
- Structure policy (owner). **Levels 3 to 6 (TEASER-STRICT):** a sub-structure at most once per calendar quarter and never within 30 days of itself across a quarter boundary (checked circularly over the year); a family at most 3 times a quarter; an answer of 10 or more once per level and a single digit at most 4 times in the level. **Levels 1 and 2 (L1L2-GAP60):** a sub-structure at least 60 days after its last use, counted round the year in both a 365-day and a 366-day year (so 31 Oct and 1 Nov of the next year are neighbours, and 28 Feb to 1 Mar is counted); a family at most 3 times in any 60 consecutive days and never on two consecutive days; an answer not repeated within 60 days and a single-digit answer at most twice in any 60 days. No sub-structure that the level's fixed page puzzle uses; no repeated frame; no two puzzles of a level with most of their numbers or the same story in common.
- A sub-structure is a maths idea a parent would see as different. Sub-structures that a parent would call the same puzzle (three division stories, two ways to calculate a bracket expression, add or take off a percentage ...) were merged in round 2, so the taxonomy counts only ideas that look different.
- One answer, proved by brute force over the whole search space; the author solver and the independent checker must agree.
- Singapore wording and spelling (metres, litres, colour, Primary, HDB, hawker centre, MRT, $ and cents; GST at 9%); coins 5, 10, 20, 50 cents only; no brand names. No coin or note images.
- Reading load and sentence length limited per level (checked); topics only from that level's syllabus (cited in `taxonomy.json`); level-fit corrections of round 2: perimeter, line-ups, squares in a grid and durations of more than one hour start at Levels 2 or 3; fractions of a set and area with a corner cut out start at Level 3 or 4; rounding starts at Level 4.
- A kind hint that does not give the answer (shown after a wrong try) and a short worked explanation (after a right answer, or on "Show me how").
- Accepted answer formats: `12`, `12 cm` (only when the unit is listed), `$10.40`, `10.4`, `3,500,000`, `4 3/8`, `35/8`, `4.375`, `21st`, `on Sunday`, `0.96` for 96%, and since round 3 a sentence round the answer: `It is 12`, `It's 12`, `The answer is 12 cm`, `The answer is Sunday`; equal fractions not in lowest terms get "write it in its simplest form". A wrong unit is not accepted.
