# Level 3 Extension Workbook: progress

Pipeline: `extension/l3/src/uNN.py` (generator, writes `extension/data/l3_uNN.json`) + `extension/l3/src/short.py` (shortened Why lines, applied by `lib.Unit.save`)
+ `extension/verify/l3_uNN_checks.py` (independent answer checks) + figure plug-ins `extension/tools/figs_l3_*.py` (types `l3_*`).
Quick view: `python3 extension/tools/build.py --level 3 --units N --no-bw`.
Resume: run `python3 extension/l3/src/uNN.py` for any unit to rewrite its json; units are independent.

Status: all 10 units written, checked and built. The audit fix pass (AUDIT.md) is done.

Fix pass (23 Oct): about 25 holiday-clone items replaced by new contexts (L3-REPLACE-ALL); Learn it content added for U1, U4 (more models), U5 (leftover person), U6 (equivalent fractions); `{bw}` boxes for pm, 24-hour and money answers; U10 Check yourself graph labels fixed; U8 S10 arc, U7 S7 labels, U7 T3, U3 S10, U5 G4(b), U10 T3 graph; beyond labels now use the `beyond` key; Welcome keys set in `config/levels.json` (`welcome_equipment`, no notes, no print note); Whys shortened so the book is exactly 100 pages (L3-TRIM).

Round-2 audit fixes (AUDIT_ROUND2.md, 23 Oct): C1-C8 clone items replaced with new stories and frames (U6 T2 equal fractions with a sum; U5 S5 reverse division; U5 S6b greatest number with remainder 5; U5 T3 same answer and remainder; U7 Try and C2; U3 C2 split a product; U10 S6 cafe meals and C3 height order; U4 S10 zoo, T1 shelves, S11 name fixed); U8 label C moved, dent defined on the Learn page, Check 2 reworded; U9 Learn examples and S4 changed; Whys restored (U3 S10, U7 C1, U2 T3); U4 and U5 Learn pages have worked lines; U10 L1-L3 polish.

Round-3 fixes (AUDIT_ROUND3.md): U6 T2 (order fractions with 24ths), U5 T3 (wheel with 8 seats), U5 S5 (list adding 5, same remainder), U5 S6(b) (6 times table with remainder 1), U8 T3 (steps shape, 14 corners and 5 dents), U8 Check 2 (Y instead of T), U7 Learn Try wording, U4 T1 wording. Rebuilt with the current shared tools (clean trophy plaque, no repeated Contents titles); the DRAFT licence line stays by owner decision. The vector print file is in extension/l3/build_extras/.

Build: 100 pages (soft and print). Gates: run_checks (462 answers), dup_check (0 FAIL), wording_lint, build (no overflow), bw_check, check_bw, fill_check all pass.
Open: certificate plaque and the DRAFT licence line are shared assets (not edited). Resume point: none.
