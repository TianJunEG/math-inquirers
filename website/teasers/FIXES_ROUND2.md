# Fix round 2 (24 Oct 2026): answers to AUDIT_ROUND2.md

Scope: `website/teasers/` and the owner preview only. `website/dist` untouched, nothing deployed, `site_enabled` still `false`. January to October are not written.
Owner policy applied: a new story AND a new frame. Honest wording only ("a new puzzle every day", never "a new kind"). Decisions taken: sub-structure cap 1 per quarter and family cap 3 per quarter at Levels 3 to 6 (as built); Levels 1 and 2 on a 60-day circular gap with no per-quarter sub cap; the same date may return next year, with fresh numbers and stories where possible (README).

## Closed and not closed

| ID | Item | Status | What was done |
|---|---|---|---|
| H-1 | Near-copies of our own items (5 High, about 8 Medium) | Closed for the listed items; heuristic only | `L2-trirow`, `L2-snailwall`, `L6-clockhours`, `L4-yearlater`, `L5-jacket`, cartons (L2/L3/L4), frog in a well, fewest coins (L1-L3), digit cards, rope and string, and the rest of the top-20 table were replaced by new stories on new structures. New content-word story check in `verify_bank.py` (rules F1, F2, F4, F5 and wording rule W, against about 115,000 sentence windows of the 21,000 source chunks): a shared story skeleton is a hard FAIL. About 170 REVIEW lines remain, read by the author only. |
| H-2 | Capacity table overstated | Closed (numbers corrected) | `capacity_lines` now uses sum of min(cap, n_f); true table below. |
| H-3 | Full-year answer rule impossible at L1 | Closed | L1 and L2: answer rule windowed to 60 days (single digit at most 2 per window). L3 to L6 keep the full-year rule, checked as feasible. |
| M-1 | Family cap 3 vs "repeat at most once" | Not closed | Kept at 3 per quarter as built; owner to confirm. Under the stricter reading (2) the L3 to L6 numbers are short. |
| M-2 | Quarter-boundary loophole | Closed | 30-day gap across quarters for L3 to L6, circular; selftest probe at 29 and 30 days. |
| M-3 | Level fit (L1 perimeter, line-up, 90 minutes, squares in a grid; L2 fraction of a set, area cut-out; L3 rounding) | Closed in taxonomy and bank | perimeter basic from L2; line-up folded into orderings at L3 to L6; durations over one hour from L2 (new `durations` family); squares in a grid from L3; fraction of a set L4 and L5; area with a cut-out removed from L2; rounding L4 to L6. |
| M-4 | Sibling sub-structures counted as distinct | Closed | 100 old ids merged into 39 (5 same pairs and 11 borderline pairs among them); `merged_from` recorded. |
| M-5 | L1 zero slack, 10 or more new subs, gap must bind families and answers | Partly closed | 23 new usable L1 subs and 36 new L2 subs (50 new in all, each with citation, level range, independent checker and sample). Gap binds sub, family (3 in 60 days, never consecutive) and answers. L1 still has slack 1 (see below). |
| M-6 | `L1-think8`, `L3-fatherage`, `L3-ropestring` near sources | Closed | Replaced. |
| M-7 | Verifier blind to story; capacity text | Closed | Story check added; capacity text rewritten. |
| M-8 | Same puzzle on the same date every year | Closed as documentation | README states it, and the plan (fresh batch before a date returns). |
| M-9 | Home page has no level picker | Not closed | Unchanged; out of scope. |
| L-1 | Answer formats not accepted | Not closed | Not touched. |
| L-2 | `data-teaser-state` stays `loading` | Not closed | Not touched. |
| L-3 | Late reply documented | Closed | In README. |
| L-4 | "Scratch" and "Python" in `L6-codingclub` | Not closed | Not touched (the level page's own subject). |
| L-5 | `L3-lanes5` 120 orderings, podium repeats | Not closed | Not touched. |
| L-6 | Same idea at many levels in the same weeks | Partly closed | Merges removed several; adjacency rules otherwise unchanged. |
| L-7 | `L3-round350` | Closed | Replaced with a new rounding puzzle. |
| L-8 | `L1-chairs`, `L2-stickerbook` above level | Closed | Both replaced. |
| L-9 | No early hint button | Not closed | By design. |
| L-10 | Device clock decides the day | Not closed | By design. |

## Verifier changes (audit 6c, eight steps)

`min_gap_days` per level; family cap 3 in any 60 days and never on consecutive days (L1/L2); windowed answer rule; correct `capacity_lines`; 30-day cross-quarter gap for L3 to L6; content-word story check as hard FAIL; selftest probes (59/60-day gaps, circular wrap, 1 Jan to 1 Mar leap effect, family consecutive and window, answer window, 29/30-day cross-quarter gap, 7-word run, shared numbers, story probes, a sample for each of the 50 new kinds). `--strict-capacity` fails the run on a capacity shortfall.

## True capacity after merging

| Level | Subs | Families | Needed | Slack | Capacity | Verdict |
|---|---|---|---|---|---|---|
| 1 | 62 | 39 | 61 | 1 | 372 a year | Shortfall: slack 1, 71 subs wanted (9 short) |
| 2 | 87 | 51 | 61 | 26 | 522 a year | ok |
| 3 | 108 | 56 | 92 | 11 | 103 a quarter | ok |
| 4 | 108 | 58 | 92 | 9 | 101 a quarter | ok |
| 5 | 103 | 57 | 92 | 3 | 95 a quarter | ok, thin |
| 6 | 98 | 56 | 92 | 0 | 92 a quarter | zero slack |

Level 1 can fill a year with a rigid 61-day rotation (`batches/YEAR_PLAN.md`, 0 violations) but one lost sub breaks it. Honest finding: Level 1 has about 62 genuinely different MOE P1 to P3 ideas and I could not find 9 more that a parent would call different.

## Retired, merged, new

- Retired (our own books already use the frame): `moves.climb_and_slip`, `growing_pattern.stick_row`, `digit_puzzles.sum_of_all_digits`.
- Restricted: `digit_cards.make_number` to L1 and L2; `rate.work_and_time` to L5 and L6.
- 39 merged subs absorb 100 old ids.
- 50 new subs: 23 usable at L1, 36 at L2, 42 at L3, 37 at L4, 28 at L5, 13 at L6.

## Results

`build_bank.py`: 30 puzzles per level for November, 31 for December. `verify_bank.py`: November 0 FAIL (100 REVIEW), December 0 FAIL (84 REVIEW), structure rules 0 FAIL, one intentional L1 CAPACITY FAIL line. `--selftest`: 0 problems over 50 kinds. Exactly one valid answer per puzzle by the independent checkers. `test_site.py` on a rebuilt scratch site: 431 checks, 0 failed.

## What remains open

L1 slack (9 short); L6 zero slack and L5 slack 3; M-1 owner confirmation; Low items above; the story check is a heuristic and the round-2 content is self-checked only, so an independent audit is needed; the worst-case frame also appears in sasmo drafts (stories changed, idea overlaps; judgement call); January to October not written.
