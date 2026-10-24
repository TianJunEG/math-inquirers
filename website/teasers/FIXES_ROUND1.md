# Fix round 1: answers to AUDIT_ROUND1.md (24 Oct 2026)

Scope: `website/teasers/` and the owner preview only. `website/dist` untouched; nothing deployed (`site_enabled` false, now explicit in `manifest.json`).
Re-run after the last edit: `build_bank.py` (30 / 31 puzzles per level), `verify_bank.py` (0 FAIL in November, December and the structure rules; `--selftest` all pass),
`brute.py` + `brute_more.py` (366 of 366 puzzles have exactly one answer, equal to the bank), `test_site.py` on a rebuilt scratch site (431 checks, 0 failed).

## Closed / not closed

| ID | Status | What was done |
|---|---|---|
| H-1 | **Closed for Nov + Dec** | "Frame" is now the maths structure. `taxonomy.json` records 63 families (kinds) and 195 sub-structures with level range and a citation. Each level's 61 puzzles (30 + 31) use 61 distinct sub-structures, at most 3 per family. About 50 new kinds were written (`kinds_more.py`, independent checkers in `brute_more.py`). `verify_bank.py` enforces: 1 per sub-structure and 3 per family per level per calendar quarter, no shared numbers and no repeated answers inside a level, sub-structure matches the puzzle's kind and parameters. See the single-digit exception below. |
| H-2 | **Closed** | `L3-riddle21`, `L4-riddle52`, `L1-marbles`, `L3-uncle`, `L6-dice10` and the medium-level close matches were replaced by new stories on new structures. The fixed fallback puzzle of each level page is reserved: its sub-structure (L1 count on, L2 digit-card arrangements, L3 two remainders, L4 common multiple, L5 fraction of the remainder, L6 which term) cannot be used by a bank puzzle, and the verifier fails any bank entry of those kinds. |
| M-1 | Closed | "years years" and similar doubled words fixed; the verifier now fails any doubled word. |
| M-2 | Closed | Brand name removed; a brand-name regex is part of the verifier. |
| M-3 | Closed | Only 5, 10, 20, 50 cent coins; no 2-cent coin or stamp; no coin or note images. Verifier regex enforces it. |
| M-4 | Closed (by my reading of the syllabus; owner to confirm) | Citations are in `taxonomy.json` per family, to `docs/moe/syllabus_by_level.md` and `website/data/level_lessons.json`. Removed from L3: angles on a straight line. From L4: median, mode, mean, hexagon and triangle angles, 360 degrees at a point, 2-digit divisors. From L5: ratio, mean, polygon angles, reverse percentage, percentage change. Mean now sits at L6; ratio and percentage change at L6 only; L5 uses the P5 angle facts. Sub-structure level ranges are my judgment; the owner or an auditor should check `levels` per sub in `taxonomy.json`. |
| M-5 | Closed | Close matches to drafts, catalogue and extension items reworded or replaced; the structure index (about 20,000 own-source questions, masked 4-grams) fails a skeleton match of 0.6 or more with 2 or more shared numbers. Two skeleton REVIEW lines remain (`L3-petshop`, `L4-yearlater`, 0 shared numbers, read by hand: different maths). |
| M-6 | Closed | Shared-run threshold is 7 words (as the extension checker), plus a local list of generic answer-format phrases (`stock_phrases.txt`). |
| M-7 | Closed | Repeated structures and numbers across months removed (see H-1). |
| M-8 | Closed | Light mode: hint text 5.36:1, correct box 5.77:1; `test_site.py` measures at least 4.5:1 in light and dark. |
| M-9 | Closed | The pool is gone. The two newest released months are built into each page; other released months are fetched with an 8 second wait; a late reply is used only if the fixed puzzle is untouched. A date with no puzzle shows the fixed puzzle with no "Puzzle for" label. Same puzzle for the same date for all visitors. |
| L-1, L-2 | Closed | Hints no longer contain the answer (verifier fails otherwise); coin and stamp "sets" wording made unambiguous. |
| L-3, L-4 | Closed | Symmetry definitions and rounding stated in the wording where used. |
| L-5, L-6 | Closed | Logic puzzles use neutral wording ("Who has the ..."), no blame or culprit; winter-city wording removed. |
| L-7 | Closed | Focus moves to the explanation message after "Show me how". |
| L-8 | Closed | The code block has `role="group"` and a visible "Your answer" label. |
| L-10 | Closed | Accepted forms: `21st`, `0.96` for 96%, `on Sunday`, a unicode fraction slash, `+7`, `1 h 30 min`; all tested. |
| L-12 | Closed | Unreleased months are never fetched (no 404). README and manifest agree: `site_enabled` is `false` in both. Fallback is the fixed puzzle, as in TEASER-DAILY-GO. |
| L-9 | **Not closed** | No early "Need a hint?" button (design choice, left for the owner). |
| L-11 | **Not closed** | The device clock still decides the day (the date is Singapore time computed from the clock; a wrong device clock shows the wrong day). Acceptable for a teaser. |

## Things the owner should know

- **Single-digit answers.** Only the values 2 to 9 exist for about 25 puzzles per level, so answers of 10 or more and all text answers are unique within a level, but a single-digit answer may repeat up to 4 times in a level (`MAX_SMALL` in `verify_bank.py`).
- **Granularity.** A sub-structure is a recognisable problem type or reasoning step. A new story or new numbers is not a new sub-structure. Where two sub-structures are close (for example two kinds of "difference and sum"), an auditor may argue they are one; the cap of 3 per family limits that risk.
- **Skeleton check** is a heuristic; two reviewed false positives are listed above. "Working backwards" is a lesson topic, so a puzzle of that type may resemble an extension item in idea; the wording and story differ.
- Owner preview `outputs/owner_review/teasers_preview/index.html` carries the answer key: do not publish it.

## Structure capacity for a full year (for the Jan-Oct plan)

A quarter has up to 92 days, and the cap is 1 per sub-structure per level per quarter, so a quarter needs up to 92 distinct sub-structures per level. A sub-structure may return in the next quarter (new story and numbers). Current taxonomy:

| Level | Sub-structures | Families | Against 92 per quarter |
|---|---|---|---|
| 1 | 61 | 33 | short by 31 |
| 2 | 80 | 35 | short by 12 |
| 3 | 102 | 41 | enough |
| 4 | 108 | 44 | enough |
| 5 | 109 | 46 | enough |
| 6 | 105 | 50 | enough |

Realistic distinct structures per level per year: about 61 (L1), 80 (L2), 102 (L3), 108 (L4), 109 (L5), 105 (L6) in a first pass; since a sub-structure can come back each quarter, a full year can carry up to 4 uses each (about 245 / 320 / 400 / 430 / 435 / 420 puzzle slots), against 365 needed. Levels 3 to 6 can cover a quarter with what exists, though the three hard quarters beyond Q4 need new story and number sets, not new structures. Levels 1 and 2 cannot fill a 92-day quarter at cap 1.
Options for the owner: (a) relax the cap to 2 per quarter for L1 and L2; (b) have about 31 new L1 and 12 new L2 sub-structures written and cited; (c) allow reuse after a gap of at least 45 days. L1 is the real constraint because the syllabus for ages 6 to 8 is narrow.
Every extra month must also pass the same checks, so the same fix-round work applies to each batch (taxonomy entry first, then `defs`).
