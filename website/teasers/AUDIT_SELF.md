# Self-audit of the daily teasers (author's checklist)

**Updated after fix round 1: section 6 is the current result and supersedes the numbers and the fallback-pool wording in sections 1 to 5, which describe the first version (the pool was removed; the page's fixed puzzle is now the fallback).**

Scope: batches **November 2026 (30 days) and December 2026 (31 days)** for all six levels = 366 puzzles, the browser code, the page wiring, the
preview. Nothing in `website/dist` was changed or built; the live site is untouched (`site_enabled` is `false`).
Run on 24 Oct 2026. "Pass" means the command below printed 0 FAIL.

## 1. Puzzle correctness (`python3 website/teasers/verify_bank.py`)

| Check | Result |
|---|---|
| Every puzzle re-solved by `brute.py`, which does not import the author solver `kinds.py` and walks the whole search space (all numbers in range, all permutations, every simulation step, all dice/coin outcomes) | 366 of 366 have **exactly one** valid answer, equal to the bank answer |
| Two real bugs this independent pass caught and that were fixed: a kite drawn as a rhombus in the symmetry checker (answer 9 vs 10), and an arithmetic slip in a worked explanation (a routes puzzle, 20 - 4 written where 20 - 12 was meant) | fixed; re-run clean |
| Arithmetic written in the questions, hints and explanations (every `a op b = c` chain is evaluated) | 0 wrong |
| Repeating-pattern wording lists the same pattern that was solved | pass |
| Listed wrong answers never equal the answer; in the browser test every integer from 0 to 3 x answer + 5 (at least 300) is also tried and rejected | pass |
| Frames unique within each level across both released months (`P('frame', ...)` ids) | pass (0 repeats in 6 levels x 61 days) |
| Dates: each level has exactly one puzzle for every calendar day of Nov (01-30) and Dec (01-31) | pass |
| Question numbers not coming from the parameters (examples written in the wording) | listed as REVIEW in each `VERIFY_REPORT.md`; each one read by hand (terms of the sequence shown, example numbers, "half past"), all consistent with the parameters |

## 2. Originality and wording

| Check | Result |
|---|---|
| Similarity to holiday banks, term lessons (`term/l*/lessons`), every extension workbook item, and the private external source files (present in this checkout): shared run of 9 or more words | 0 FAIL. Shared 7-8 word runs are only ordinary maths question stems ("how many children are in the", "give your answer as a fraction in its simplest form", "I think of a number"); they are listed per batch in the report as `stem` lines and were left as they are. |
| Same idea against the seven fixed website puzzles (home and six level pages) | only 5-word generic stems in common ("by 4 the remainder is", "I am a number between") |
| Singapore spelling and words: no "color / meter / liter / math" (British "maths", "metres", "litres", "colour"); Singapore settings (HDB, hawker centre, kopitiam, MRT, GST 9%, Primary, $ and cents) | pass (scripted) |
| No coin or note images, no pictures at all: money appears only as words and numbers; coin puzzles say "10-cent coin" in text | pass |
| Reading load: words per question and words per sentence limited per level (L1 48 / 20, L2 55 / 22, L3 65 / 26, L4 75 / 30, L5 85 / 34, L6 95 / 38) | 0 over the limit after shortening 6 questions |
| Curriculum fit: L1 numbers to about 100 and 1-digit groups; L2 3-digit numbers, tables 2/3/4/5/10, simple fractions, money with cents, time; L3 4-digit numbers, tables up to 9, bar models, perimeter/area, fractions of a quantity; L4 factors/multiples, mixed numbers, decimals, angles, symmetry, data, 24-hour time; L5 ratio, percentage, rate, volume, triangle area, averages; L6 sequences, primes, negative numbers, algebra, probability, binary, simple programs | read by hand against `docs/levels_and_placement.md` and the level pages' lesson lists |
| Each puzzle has a kind hint (shown after a wrong try, never the answer; a scripted check flags hints that contain the answer when it is 20 or more) and a short worked explanation | 366 of 366 |

## 3. Browser behaviour (`python3 website/teasers/test_site.py <scratch site>`; Chromium via Playwright, built with `MI_TEASERS=1 ... build_site.py --out <scratch>`)

**Result: 392 checks, 0 failed** (final run on the rebuilt scratch site, after the last wording edit).

What the time-zone tests cover (with the browser clock fixed, browser time zone set to each of Asia/Singapore, America/Los_Angeles, Pacific/Kiritimati (UTC+14), Pacific/Pago_Pago (UTC-11), Europe/London, UTC):

- 24 Nov 10:00; **30 Nov 23:59:30 SGT** (still 30 Nov); **1 Dec 00:00:00 and 00:00:30 SGT** (1 Dec, even where the browser's own date is still 30 Nov); 31 Dec 23:59:59 SGT; **1 Jan 2027 00:00:01 SGT** (year end, no January batch yet, so the fixed puzzle stays); 28 Feb 23:59:59 and 1 Mar 2027; leap day 29 Feb 2028; 24 Oct 2026 (before the first batch). Each on all six pages. The puzzle shown equals the expected bank entry (or the page's fixed puzzle).
- The same instant gives the same puzzle in all six browser time zones.
- Fetch of the month file blocked: the page keeps its fixed puzzle. JavaScript off: the old fixed puzzle is on the page (home: frog hops with its Check button; level pages: the sample puzzle with "Show the answer").
- Accepted formats for every released puzzle (as displayed, with the number alone, with spaces, thousands commas or spaces, `$`, units that are listed) and rejected wrong answers (wrong numbers, a wrong unit, the answer with an extra digit, the answer with a made-up unit). Edge cases: `12 m` for a `12 cm` answer is wrong, `2/4` for `1/2` asks for the simplest form, `-6` and `−6`, text answers with capitals and a full stop.
- UI flow: Enter key; wrong answer shows "Not yet. Hint: ..." plus a "Show me how" button; right answer shows "Correct!" and the worked explanation.
- Privacy: 0 cookies, 0 localStorage or sessionStorage entries, 0 requests to any host other than the site itself, no timers used for the puzzle (a single 2.5 second timeout guards the fetch only).
- Layout: at 390 px (phone) and 1280 px (desktop), on all six pages, on two dates: no sideways scroll and the puzzle box inside the viewport; screenshots read by eye (`outputs/owner_review/teasers_preview/shots/` for the preview; the page screenshots are in the scratch folder).

## 4. Site wiring and safety

| Check | Result |
|---|---|
| With the switch off (`site_enabled` false, no `MI_TEASERS`), `lp_build.py` and `level_pages.py` reproduce the committed `mi_signup.html` and `level_pages/*.html` byte for byte | pass (`git status` clean after running them) |
| `build_site.py --out DIR` builds anywhere else; default is still `dist/`; the preview build used a scratch folder | pass |
| `git diff --stat` vs origin shows nothing under `website/dist` | pass |
| `_headers` for `/teasers/*` (1 hour cache) only when the teaser is enabled; the existing CSP (`connect-src 'self'`) already allows the same-site fetch | pass |
| After preview builds the two generators' tracked outputs were restored (`git checkout website/mi_signup.html website/level_pages`) | done |

## 5. Known limits and open points for the independent audit

- Only November and December exist. January to October (305 puzzles per level) are not written; until then those dates show the page's fixed puzzle.
- Home page: no level picker exists, so it always shows Ages 6-8; `?level=` links only pre-fill the sign-up form.
- "Frame" is interpreted as the story/setting plus what is asked. The same maths structure returns in other stories (for example "work backwards", "arrays", "pairs") on other days; kind counts per level are in each report. An auditor who reads "frame" as the maths structure would find repeats within a month (at most 5 of one kind in a 31-day month).
- The fetch adds one small request to the page; if it fails the visitor keeps the fixed puzzle, not a blank.
- Answers are normalised leniently (a wrong unit is rejected, a missing unit is accepted). Text answers (names, days, colours, shapes) accept the full word or the listed short forms.
- The hint is shown after a wrong try and the worked explanation after a right one or after "Show me how"; there is no way to see the answer before trying once. (Easy to change if the owner wants the button from the start.)
- Some L5/L6 puzzles use a definition inside the question (prime, mode, range, palindrome) because the level range assumes the idea but not every child has met the word; the wording defines it where it matters.
- The preview page (`outputs/owner_review/teasers_preview/index.html`) carries an answer key for the owner. Do not publish that page.

## 6. Fix round 1 (24 Oct 2026): re-run results

Fixes are listed in `FIXES_ROUND1.md`. Final state of every check:

| Check | Result |
|---|---|
| `build_bank.py` | 30 puzzles per level for November, 31 for December (366 in all) |
| `verify_bank.py` | November 0 FAIL (38 REVIEW), December 0 FAIL (28 REVIEW), structure rules 0 FAIL; REVIEW lines read by hand: example numbers in the wording, and two skeleton matches (`L3-petshop`, `L4-yearlater`) with 0 shared numbers |
| `verify_bank.py --selftest` | 9 of 9 rule probes fire as intended (sub-structure twice in a quarter, 4 of a family, repeated answer, 7-word run, repeated numbers; same sub in another quarter allowed; taxonomy matcher) |
| `brute.py` / `brute_more.py` | every one of the 366 puzzles has exactly one valid answer, equal to the bank answer, by an independent search |
| `test_site.py` on a rebuilt scratch site | 431 checks, 0 failed (date matrix over 6 time zones, no-puzzle date, blocked / slow / failed / late fetch, no-JS, answer matcher, light and dark UI, contrast at least 4.5:1, focus, privacy, layout on three dates) |
| Flag off | `site_enabled` false; generators unchanged; `website/dist` untouched |

Changes to the earlier limits: the fallback is the page's fixed puzzle, not a pool; "frame" now means the maths structure (taxonomy).

## 7. Fix round 2 (24 Oct 2026): re-run results

Fixes are listed in `FIXES_ROUND2.md`. Round 2 is the author's own check, not an independent audit.

| Check | Result |
|---|---|
| `build_bank.py` | 30 per level for November, 31 for December (366 in all), rebuilt with new stories on new structures |
| `build_bank.py --plan` | `batches/YEAR_PLAN.md`, 0 violations of the 60-day rule at Levels 1 and 2 |
| `verify_bank.py` | November 0 FAIL (100 REVIEW), December 0 FAIL (84 REVIEW), structure rules 0 FAIL; one intentional capacity line: Level 1 slack 1 (needs 71 subs) |
| `verify_bank.py --selftest` | 0 problems; 50 kinds sampled, gap, family, answer window, cross-quarter and story probes fire |
| `brute*.py` | every puzzle has exactly one valid answer, equal to the bank answer |
| `test_site.py` on a rebuilt scratch site | 431 checks, 0 failed |
| Flag off | `site_enabled` false; `website/dist` untouched |

Retired: climb_and_slip, stick_row, sum_of_all_digits. Merged: 100 old sub ids into 39. New: 50 sub-structures with independent checkers.
Known limits: the story check is a heuristic with about 170 REVIEW lines read only by me; Level 1 true ideas 62; Level 6 quarter capacity exactly 92.
