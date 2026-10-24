# Daily teasers (website/teasers/)

A new puzzle every day for each of the six levels, picked in the visitor's browser from the **Singapore calendar date**
(Asia/Singapore, UTC+8 with no daylight saving), so every visitor sees the same puzzle that day and it changes at 00:00
Singapore time whatever time zone the browser is in. Static only: no server, no cookies, no tracking, no timers, no scores,
no streaks, nothing saved. The existing fixed puzzle stays on the page as the no-JavaScript / failed-JavaScript fallback.

Owner decisions: **TEASER-DAILY-GO** (docs/terms/owner_decisions.md) and the follow-ups: 365 puzzles per level (one per calendar
date, MM-DD, with a spare for 29 Feb), released in monthly batches, November 2026 first, then December 2026, January 2027 ...;
**TEASER-STRICT** (Levels 3 to 6: a sub-structure at most once a quarter, only with a new story and a new frame) and **L1L2-GAP60**
(Levels 1 and 2: a sub-structure may return after at least 60 days with a new story and new numbers).

**What may be promised on the site:** "a new puzzle every day", never "a new kind of puzzle every day". At Level 1 a maths idea comes back six
times a year (every 61 days) with a new story and new numbers; at Level 2 the same; at Levels 3 to 6 an idea returns once per quarter at most.

**The same date next year.** The bank is keyed by month and day, so a child who visits on 14 Nov 2027 meets the 14 Nov 2026 puzzle again. The
plan is to write a fresh batch (new numbers and new stories, same sub-structure rotation) before a date comes round a second time, and to
publish it under the same MM-DD key only when the previous year's puzzle for that date is retired. Until then the same date shows the same puzzle.
Within one year every answer, number set and story is different (checked by `verify_bank.py`).

## Status

| | |
|---|---|
| Released batches (in `manifest.json`) | 11 (Nov, 30 days) and 12 (Dec, 31 days), for all six levels: 366 puzzles. Rebuilt in fix round 2 (24 Oct 2026). |
| Not yet written | Jan to Oct (305 puzzles per level to go, in monthly batches of about 30). Not started: round 2 fixed the structure first. |
| On the live site? | **No.** `site_enabled` is explicitly `false` in `manifest.json`, so `lp_build.py`, `level_pages.py` and `build_site.py` produce exactly the old pages. `website/dist` has not been touched. |
| Taxonomy | 78 families and 184 sub-structures (175 in use). Look-alike sub-structures were merged (100 old ids into 39), 50 new ones were added (23 usable at Level 1, 36 at Level 2) and 3 were retired because our own books already use the same frame. Capacity table: `batches/STRUCTURE_REPORT.md`; year plan for Levels 1 and 2: `batches/YEAR_PLAN.md`. |
| Audits | `AUDIT_ROUND1.md` / `FIXES_ROUND1.md`, `AUDIT_ROUND2.md` / `FIXES_ROUND2.md` (what is closed and what is not), `AUDIT_SELF.md`. |

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
| `kinds.py`, `kinds_more.py`, `kinds_r2.py` | **Author-side solvers** (`SOLVE[kind]`), one per puzzle kind. `kinds_r2.py` holds the kinds of the new round-2 sub-structures. |
| `brute.py`, `brute_more.py`, `brute_r2.py` | **Independent checkers** (`BRUTE[kind]`): never import the solver files; walk the whole search space and return every valid answer (an impossible extra value when the puzzle is not well posed). |
| `samples_r2.py` | One worked instance per round-2 kind; `verify_bank.py --selftest` proves solver and checker agree on each, even for sub-structures that no released month uses yet. |
| `taxonomy.json`, `taxonomy.py` | The list of maths kinds (families) and sub-structures per level, with the syllabus citation, the level range, `merged_from` (which round-1 ids were merged), `retired` and the structure rules (gap rule, quarter rule). Every puzzle names its `sub=`. |
| `stock_phrases.txt` | Generic answer-format phrases that may repeat. |
| `build_bank.py` | `python3 website/teasers/build_bank.py [MM ...]` builds `batches/m<MM>/bank.json` (no neighbouring puzzles share a family or a kind, also across a month boundary; 31 Dec is followed by what was 1 Nov at Levels 1 and 2). `--plan` writes `batches/YEAR_PLAN.md`: the 61-day rotation that keeps Levels 1 and 2 inside the 60-day gap rule all year. |
| `verify_bank.py` | `python3 website/teasers/verify_bank.py [MM ...]` re-solves every puzzle with the checkers, checks unique answer, arithmetic in the wording, wording rules, 7-word shared runs, masked-skeleton similarity and the **story check** (content words against ~115,000 sentence windows of the ~21,000 source chunks), the structure rules below, and writes `batches/m<MM>/VERIFY_REPORT.md` and `batches/STRUCTURE_REPORT.md` (with the true capacity table). `--selftest` proves the rules fire; `--strict-capacity` also fails on a taxonomy that cannot supply a full year. |
| `batches/m<MM>/` | `bank.json` (built) and `VERIFY_REPORT.md` for each month. |
| `teasers.js` | The browser code (date, picking, answer checking, rendering). |
| `teaser_html.py` | Glue used by `lp_build.py`, `level_pages.py` and `build_site.py`; exports the per-month files. |
| `build_preview.py` | Writes `outputs/owner_review/teasers_preview/index.html` (date and time selector, midnight buttons, answer key). |
| `test_site.py` | Chromium (Playwright) tests on a built site directory. |
| `AUDIT_SELF.md` | The author's own checklist of what was checked and the results. |

## Commands

```
python3 website/teasers/build_bank.py           # rebuild released months
python3 website/teasers/build_bank.py --plan    # Levels 1 and 2: the year rotation (batches/YEAR_PLAN.md)
python3 website/teasers/verify_bank.py          # independent verification (exit 1 on any FAIL)
python3 website/teasers/verify_bank.py --selftest
python3 website/teasers/build_preview.py        # owner preview page

# a full site build to a scratch folder (never to dist) with the teaser switched on (run in website/):
MI_TEASERS=1 python3 lp_build.py && MI_TEASERS=1 python3 level_pages.py
MI_TEASERS=1 python3 build_site.py --out /tmp/site_preview
python3 teasers/test_site.py /tmp/site_preview --shots /tmp/shots
git checkout mi_signup.html level_pages     # the two generators rewrite tracked files; put them back after a preview build
```

## Adding the next month (for example January)

1. Levels 1 and 2: the sub-structure of each day is fixed by `batches/YEAR_PLAN.md` (the released day 61 days earlier); write a new story and new numbers for it, with an answer that differs from every answer within 60 days. Levels 3 to 6: choose sub-structures that are unused in the quarter and at least 30 days from their last use (`taxonomy.json` lists them per level); a family at most 3 times a quarter.
2. Write `defs/m01/l1.py` ... `l6.py` (31 puzzles each). Every puzzle needs a `sub=` that exists in `taxonomy.json` for that level; a new sub-structure needs a syllabus citation, a level range, a solver in `kinds_r2.py`, an independent checker in `brute_r2.py` and a sample in `samples_r2.py` first.
3. `python3 website/teasers/build_bank.py 01`, then `verify_bank.py 01` until 0 FAIL and the REVIEW lines are explained.
4. An independent audit of the batch, then add `"01"` to `released` in `manifest.json`, rebuild and re-test.
5. Releasing to the live site is a separate step: set `"site_enabled": true`, run the generators and `build_site.py`, commit the rebuilt `website/dist`.

## Rules every puzzle follows

- Original wording and story; not copied from the holiday program, term lessons, extension workbooks, school booklets or external sources. `verify_bank.py` fails on any 7-word shared run, on a masked-skeleton match with shared numbers, and (round 2) on a **shared story**: the content words of the question (names, number words and very common words removed) found in one source sentence or two neighbouring sentences with the same objects and the same numbers, or the same specific objects (snail and wall, frog and well), or the same wording with other numbers.
- Structure policy (owner). **Levels 3 to 6 (TEASER-STRICT):** a sub-structure at most once per calendar quarter and never within 30 days of itself across a quarter boundary (checked circularly over the year); a family at most 3 times a quarter; an answer of 10 or more once per level and a single digit at most 4 times in the level. **Levels 1 and 2 (L1L2-GAP60):** a sub-structure at least 60 days after its last use, counted round the year in both a 365-day and a 366-day year (so 31 Oct and 1 Nov of the next year are neighbours, and 28 Feb to 1 Mar is counted); a family at most 3 times in any 60 consecutive days and never on two consecutive days; an answer not repeated within 60 days and a single-digit answer at most twice in any 60 days. No sub-structure that the level's fixed page puzzle uses; no repeated frame; no two puzzles of a level with most of their numbers or the same story in common.
- A sub-structure is a maths idea a parent would see as different. Sub-structures that a parent would call the same puzzle (three division stories, two ways to calculate a bracket expression, add or take off a percentage ...) were merged in round 2, so the taxonomy counts only ideas that look different.
- One answer, proved by brute force over the whole search space; the author solver and the independent checker must agree.
- Singapore wording and spelling (metres, litres, colour, Primary, HDB, hawker centre, MRT, $ and cents; GST at 9%); coins 5, 10, 20, 50 cents only; no brand names. No coin or note images.
- Reading load and sentence length limited per level (checked); topics only from that level's syllabus (cited in `taxonomy.json`); level-fit corrections of round 2: perimeter, line-ups, squares in a grid and durations of more than one hour start at Levels 2 or 3; fractions of a set and area with a corner cut out start at Level 3 or 4; rounding starts at Level 4.
- A kind hint that does not give the answer (shown after a wrong try) and a short worked explanation (after a right answer, or on "Show me how").
- Accepted answer formats: `12`, `12 cm` (only when the unit is listed), `$10.40`, `10.4`, `3,500,000`, `4 3/8`, `35/8`, `4.375`, `21st`, `on Sunday`, `0.96` for 96%; equal fractions not in lowest terms get "write it in its simplest form". A wrong unit is not accepted.
