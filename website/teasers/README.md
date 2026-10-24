# Daily teasers (website/teasers/)

A new puzzle every day for each of the six levels, picked in the visitor's browser from the **Singapore calendar date**
(Asia/Singapore, UTC+8 with no daylight saving), so every visitor sees the same puzzle that day and it changes at 00:00
Singapore time whatever time zone the browser is in. Static only: no server, no cookies, no tracking, no timers, no scores,
no streaks, nothing saved. The existing fixed puzzle stays on the page as the no-JavaScript / failed-JavaScript fallback.

Owner decisions: **TEASER-DAILY-GO** (docs/terms/owner_decisions.md) and the follow-up: 365 puzzles per level (one per calendar
date, MM-DD, with a spare for 29 Feb), released in monthly batches, November 2026 first, then December 2026, January 2027 ...

## Status

| | |
|---|---|
| Released batches (in `manifest.json`) | 11 (Nov, 30 days) and 12 (Dec, 31 days), for all six levels: 366 puzzles |
| Not yet written | Jan to Oct (305 puzzles per level to go, in monthly batches of about 30) |
| On the live site? | **No.** `site_enabled` is `false` in `manifest.json`, so `lp_build.py`, `level_pages.py` and `build_site.py` produce exactly the old pages. `website/dist` has not been touched. |

## How a visitor's page decides what to show

1. Work out the Singapore date from `Date.now() + 8 hours` (no `Intl`, no dependence on the browser's own time zone).
2. Fetch `/teasers/L<level>-<MM>.json` (that level's puzzles for that month, keyed `MM-DD`). If `MM-DD` is there, show it.
3. If the month is not released, the file is missing, the fetch fails or takes more than 2.5 seconds: show a puzzle from the
   **fallback pool** (the first released month for that level, built into the page), chosen by `day number mod pool size`.
4. If JavaScript is off or fails, the old fixed puzzle (home: frog hops, ages 6-8; level pages: that level's sample) is what is on the page.

The home page uses the Ages 6-8 set (there is no level picker on the home page; the `?level=` links only pre-fill the sign-up form).
If a page is left open past midnight, the new day's puzzle appears when the visitor returns to the tab (focus / visibility events,
no timers).

## Files

| File | What it is |
|---|---|
| `manifest.json` | Which months are released, and `site_enabled` (the switch for going live). |
| `defs/m<MM>/l<N>.py` | Puzzle sources, one file per month and level. Each puzzle is a template (`P(...)`) with parameters, wording, hint and worked explanation. |
| `defs_common.py` | The `P()` helper and text formatting (money, ordinals, mixed numbers). |
| `kinds.py` | **Author-side solvers** (`SOLVE[kind]`), one per puzzle family. |
| `brute.py` | **Independent checker** (`BRUTE[kind]`): never imports `kinds.py`; walks the whole search space and returns every valid answer. |
| `build_bank.py` | `python3 website/teasers/build_bank.py [MM ...]` builds `batches/m<MM>/bank.json` (interleaves topics so neighbouring days differ, assigns the dates). |
| `verify_bank.py` | `python3 website/teasers/verify_bank.py [MM ...]` re-solves every puzzle with `brute.py`, checks unique answer, arithmetic in the wording, frames, wording rules, similarity to holiday/term/extension/external sources, and writes `batches/m<MM>/VERIFY_REPORT.md`. |
| `batches/m<MM>/` | `bank.json` (built) and `VERIFY_REPORT.md` for each month. |
| `teasers.js` | The browser code (date, picking, answer checking, rendering). |
| `teaser_html.py` | Glue used by `lp_build.py`, `level_pages.py` and `build_site.py`; exports the per-month files. |
| `build_preview.py` | Writes `outputs/owner_review/teasers_preview/index.html` (date and time selector, midnight buttons, answer key). |
| `test_site.py` | Chromium (Playwright) tests on a built site directory. |
| `AUDIT_SELF.md` | The author's own checklist of what was checked and the results. |

## Commands

```
python3 website/teasers/build_bank.py           # rebuild released months
python3 website/teasers/verify_bank.py          # independent verification (exit 1 on any FAIL)
python3 website/teasers/build_preview.py        # owner preview page

# a full site build to a scratch folder (never to dist) with the teaser switched on:
MI_TEASERS=1 python3 website/lp_build.py && MI_TEASERS=1 python3 website/level_pages.py
MI_TEASERS=1 python3 website/build_site.py --out /tmp/site_preview
python3 website/teasers/test_site.py /tmp/site_preview --shots /tmp/shots
git checkout website/mi_signup.html website/level_pages     # the two generators rewrite tracked files; put them back after a preview build
```

## Adding the next month (for example January)

1. Write `defs/m01/l1.py` ... `l6.py` (31 puzzles each). Every puzzle needs a **new frame** (the `P('frame', ...)` id: a story or setting not used before in that level, in any month). Vary the families across the year: number, shape, pattern, measurement, logic, money (no coin or note images), time, data. Match each level's range (see `docs/levels_and_placement.md`).
2. `python3 website/teasers/build_bank.py 01`, then `verify_bank.py 01` until 0 FAIL and the REVIEW lines are explained.
3. An independent audit of the batch, then add `"01"` to `released` in `manifest.json`, rebuild and re-test.
4. Releasing to the live site is a separate step: set `"site_enabled": true`, run the generators and `build_site.py`, commit the rebuilt `website/dist`.

## Rules every puzzle follows

- Original wording and frames; not copied from the holiday program, term lessons, extension workbooks, school booklets or external sources (`verify_bank.py` fails on any shared run of 9 words and lists shorter shared question stems for review).
- One answer, proved by brute force over the whole search space; the author solver and the independent checker must agree.
- Singapore wording and spelling (metres, litres, colour, Primary, HDB, hawker centre, MRT, $ and cents; GST at 9%). No coin or note images (money is written in words and numbers only).
- Reading load and sentence length limited per level (checked); numbers within the level's range.
- A kind hint (shown after a wrong try) and a short worked explanation (shown after a right answer, or on "Show me how").
- Accepted answer formats: `12`, ` 12 `, `12 cm` (only when the unit is listed for that puzzle), `$10.40`, `10.4`, `3,500,000`, `3 500 000`, `4 3/8`, `35/8`, `4.375`; equal fractions that are not in lowest terms get "write it in its simplest form". A wrong unit is not accepted.
- "Same frame": a frame is the story/setting plus what is asked. Frames are unique within a level across all released months (checked). The same maths idea (for example "work backwards", "pairs") returns in other stories on other days.
