# Downstream bundles rebuild status (inquiry habits, holiday Levels 1-6)

24 Oct 2026, branch `claude/great-fermi-1hv4vc`. Local rebuild only. Nothing sent, published or deployed; no deck Artifact URL republished; `website/dist`, `website/mi_signup.html`, `website/level_pages`, `outputs/print` and printed workbook sources untouched.

## Rebuilt (stale)

The six weekly zips slice the rebuilt tutor guide PDFs (tutor scripts) and the designed workbook (student pages). The guides now carry "Focus habit", the zips were older (23 Oct).

| Zip | Command (in `hp/`) |
|---|---|
| `outputs/designed/Math_Inquirers_Weekly_PDFs.zip` (Level 1) | `python3 weekly_level.py ../outputs/workbook/Math_Inquirers_P1_Student_Workbook_Designed.pdf ../outputs/designed/Math_Inquirers_P1_Tutor_Guide.pdf <out>` |
| `p2` to `p6/Math_Inquirers_PN_Weekly_PDFs.zip` | `python3 weekly_level.py ../pN/Math_Inquirers_PN_Student_Workbook_Designed.pdf ../pN/Math_Inquirers_PN_Tutor_Guide.pdf <out>` |

Built in `/dev/shm/wk`, then copied over the tracked zips. Level 1 uses `weekly_level.py`, not `weekly.py`: `weekly.py` gives the old P1 page split (12/11/12/11/14), which `weekly_pdfs_fix.md` records as stale.

Checks (old zip against new zip, `pdftotext`):
- Same 10 file names per zip. All 30 Student_Pages PDFs: page count and text identical to the old zips (16/11/10/11/12 for L1, and as in `weekly_pdfs_fix.md` for L2 to L6). Workbooks were not changed.
- All 30 Tutor_Scripts_and_Answers PDFs: text changed, each week file contains 2 "Focus habit" lines (one per lesson). Page counts equal, except L2 Week 3 19 to 20 pages and L6 Week 5 17 to 18 pages (the added line pushes a page break; no page is dropped or duplicated; lesson-start detection unchanged).
- No "will acquire", "will master" or "printed workbook" wording in the new tutor scripts. The habit line is tutor-facing; it says the child practises the habit.
- Not checked by eye for overflow beyond page counts; the guide PDFs themselves were checked when they were rebuilt (`inquiry_build_status.md`).

## Checked, already current (not rebuilt)

- `tutor/build_data.py` outputs (`tutor/data/*.json`, 60 lessons, `habit` and `habit_line`): re-run produced no diff against git.
- Guide PDFs (L1 `outputs/designed`, L2 to L6 `pN/`): each contains 11 "Focus habit" hits (front-matter table plus 10 lessons). Not touched.

## Skipped, and why

- `hp/parent_pack.py`, `hp/parent_pack_level.py` (Weekly Dose of Thinking Math): built from `qbank.json`/`data.js` and `parent_side.json`; they do not read the guide, decks or habits. Output would not change.
- `levels/mkextras.py` (Question Bank, Weekly Email Pack, Free Taster, What Learners Get): same inputs; the email pack only names the zip files, whose names are unchanged. Not stale. It also reads `outputs/deck_urls_all.json`, so rebuilding would not republish anything, but there was no reason to.
- `docs/holiday_readiness.md`: no zip or habit statement to update; counts unchanged.
- `levels/scheme.py` sentence about the Look-back: not rebuilt (parent-facing level pages feed website material; held for the owner's wording approval and the lawyer).
- Student workbooks, `outputs/print`, workbook sources: print freeze; the printed workbooks do not carry habits and no bundle says so.
- Deck Artifact URLs: not republished (needs owner go-ahead).
- Tests: no test suite exists for these bundles (only `ops/test_ics.py`, unrelated and pytest is not installed); the compare above is the check.

## Not committed (other work in the tree)

`levels/habits.json` (modified) and `term/l1/*` (habit_term, items) belong to other in-progress work and were left alone.
