# Level 3 Extension Workbook: progress

Pipeline: `extension/l3/src/uNN.py` (generator, writes `extension/data/l3_uNN.json`) + `extension/l3/src/short.py` (shortened Why lines, applied by `lib.Unit.save`)
+ `extension/verify/l3_uNN_checks.py` (independent answer checks) + figure plug-ins `extension/tools/figs_l3_*.py` (types `l3_*`).
Quick view: `python3 extension/tools/build.py --level 3 --units N --no-bw`.
Resume: run `python3 extension/l3/src/uNN.py` for any unit to rewrite its json; units are independent.

Status: all 10 units written, checked and built. The audit fix pass (AUDIT.md) is done.

Fix pass (23 Oct): about 25 holiday-clone items replaced by new contexts (L3-REPLACE-ALL); Learn it content added for U1, U4 (more models), U5 (leftover person), U6 (equivalent fractions); `{bw}` boxes for pm, 24-hour and money answers; U10 Check yourself graph labels fixed; U8 S10 arc, U7 S7 labels, U7 T3, U3 S10, U5 G4(b), U10 T3 graph; beyond labels now use the `beyond` key; Welcome keys set in `config/levels.json` (`welcome_equipment`, no notes, no print note); Whys shortened so the book is exactly 100 pages (L3-TRIM).

Build: 100 pages (soft and print). Gates: run_checks (459 answers), dup_check (0 FAIL), wording_lint, build (no overflow), bw_check, check_bw, fill_check all pass.
Open: certificate plaque and the DRAFT licence line are shared assets (not edited). Resume point: none.
