# Primary 5 semester booklets: build report

Branch `claude/great-fermi-1hv4vc`, 24 Oct 2026. Pipeline `school/p5/` (copied from `school/p2/`; P1, P2, other levels and `school/colour_by_code` not edited; a Primary 5 bank `banks_p5.py` and four percentage rules were added to the vendored copy `school/p5/cbc_vendor/`). Plan: `docs/school_books/p5_semester_booklets_plan.md`. Outcome wording note: `docs/school_books/p5_outcome_wording.md`. Not sent to anyone, no PR. The independent audit (`docs/audit_final/p5_semester_booklets_audit.md`) was applied in a second pass, listed below.

## What was built

Two booklets of 20 single-sided A4 pupil pages (`out/P5_S1_Puzzles.pdf`, `P5_S2_Puzzles.pdf`), front matter of 5 pages each (cover, DRAFT licence, two pages of teacher notes, contents with coverage), complete packs of 25 pages and answer keys (9 pages each). 10 one-star and 10 two-star pages in each booklet. Footers read S1-07 (P5-07) and S2-07 (P5-27).

Page table, mechanisms and outcome tags: plan section 4. Mechanisms: code word 16, lettered choices 6, true or false 2, route 4, matching 4, ordering 3, colour by code 2, balance 1, magic square 1, number-chain loop 1.

## Audit fixes applied (second pass)

- H1 P5-39: each claim is now stated about a named angle ("Given: angle x = a. Claim: angle y = b.") with the question "true (T), false (F) or not possible to tell (N)?"; the answer is forced by the printed shape text (which sides are parallel is printed for trapeziums).
- M1 P5-38 and P5-40: angle (first pass: see the round 2 section for the corrected sizes), apex labels sit above the apex and are no longer clipped; degree signs are part of the label. P5-36 and P5-37 labels enlarged in the same way.
- M2 P5-28 wording now "One dashed line meets the base at a right angle: circle its letter"; P5-29 height label above the apex and base label under the base, side label never on a slanted side; label backing removed so no halo cuts a side (P5-29, 30, 31).
- M3 own-material overlap: reframed P5-08 (paint), P5-16 (kites, club money, seeds, buns, paint, books), P5-21 (seeds, pencils), P5-24 (GST wording "The shop adds GST of 9% to each price"), P5-26 and P5-27 (sprinkler, kite, cook, baker, sand, cloth; bus, tailor, pens, farmer, cleaner, Ali; the "find the amount for one" line removed from the P5-27 instruction), P5-35 (tub, pond, paddling pool, bin, jug and sink, box). Scanned against `extension/data/l5_*.json` and `p5/content/*.js` by five-word runs: only generic instruction phrases remain ("find the area of each triangle", "how many minutes does the", "a right angle to the base"); the rate and tank skeletons themselves are shared with every rate and volume problem.
- M4 P5-25: all six items are one year of simple interest.
- M5 P5-29, 31, 33: figures enlarged (figure widths 50 mm in a 59 mm card for P5-29; labels 4.0 to 4.1 mm type). Correction to the first report: the 49 mm quoted there was the CARD width, not the figure width.
- Triangle Route P5-30: the FINISH and START tags covered the height label of the corner cell; route cells are now taller with the figure at the bottom so the tag sits above it.
- P5-27 answer boxes and units aligned; P5-16 spacing tightened so the code table no longer meets the check strip; P5-39 spacing tightened (validation found both overflows).
- Lows: teacher notes and `p5_outcome_wording.md` now cite the PDF and use its numbering (Percentage 1.1 to 1.4, Rate 1.1 and 1.2, Volume 2.1 to 2.6 with the PDF wording, Geometry 2.3 and 3.2 "without additional construction of lines"); scale statements made consistent (figures are sketches, the notes name P5-28 as the one page whose figures are drawn accurately); code words reseeded (below); the P5-27 key spacing fixed. Front-matter ink-loss limit kept at 35%.

## Validation

`python3 validate.py` run once at the end of the second pass: 740 checks, 0 failed after the round 2 pass (`out/validation_report.txt`, `out/verification.json`). The first run of this pass found three failures (two layout overflows, P5-16 and P5-39, and reading-load sentences of P5-16 and P5-35), all fixed, then rerun. Additions for Primary 5: no Primary 6 words on pupil pages or key; notation checks; reading load 16 words a sentence; rendered answer boxes at least 12 mm high and 11 mm wide; teacher-note statements; the key says the outcome lines are copied from the syllabus.

## Hand-solved from the rendered image

Phase 1: all 40 pages solved by hand from the render before comparing with the key. Second pass: because the code words changed, every page that changed (S1-01, 02, 03, 06, 08, 09, 10, 13 to 20 and S2-01 to 15, 17 to 20) was solved again by hand from a 90 dpi render of the final PDF (crops at 140 to 200 dpi for the P5-21 bars, the P5-30 route and the P5-36 route, which was also walked by hand: 8 boxes), plus S2-16. All agreed with the key. The pages the auditor solved only from text (S1-19, S1-20, S2-03 to S2-07, S2-15) were viewed as images and solved. Changed pages were also viewed in 1-bit at 100 dpi (S1-16, S2-06, 07, 09, 10, 11, 13, 15, 16, 18, 19, 20): legible. Code words (final, 31): FRUITS, PLACED, TOWARD, FAVOUR, MODEST, FIRMLY, STRAND, PODIUM, QUIRKY, PERIOD, FOURTH, MOVIES, HARDLY, ASPECT (Semester 1) and BRANDS, LAUGHS, FUSION, COSTLY, TYPING, DIGEST, HOURLY, BIRTHS, THIRDS, JOINED, SURELY, TALKED, FORMAT, BACKED, LIFTED, MATRIX, DEPTHS (Semester 2; P5-31 is THIRDS, P5-40 DEPTHS, P5-25 COSTLY, P5-26 TYPING). None equals a code word of P1 to P4 or P6 (read from each level's answer keys: 86 words in `gen/other_levels_words.json`; `validate.py` now checks this).

## Similarity check

Every pupil page text was compared with the private sources (`docs/books/private_*` and `docs/sasmo/private_*`, 23 files, 241 880 seven-word runs): 0 shared seven-word runs; a loose same-numbers-and-words scan gave three false positives (shared colour-tally wording, one rice sentence and a fraction ribbon sentence with different numbers and structure). The question TYPES (fraction of the remainder, unit conversions, GST) are ordinary school types and were taken from `p5_school_paper_patterns.md`; no item, scenario or number set was copied. This check is mine only; the audit should repeat it.

## Weak points (honest list)

1. **Syllabus wording.** Outcome lines copied from the PDF (pp. 41 and 42); the wording of everything else is ours.
2. **Average, pie charts and ratio** are in the older school papers but not in the Primary 5 Standard summary; excluded (owner may want a preview page, as the holiday programme has for ratio).
3. **Figures are small.** Cards with figures are about 59 mm wide (figures up to 50 mm); labels are 4 mm type. The angle figures in the route grid and lettered-choice cards are smaller; pupil trial should test P5-36, 37, 40 and the 20-part bars of P5-21.
4. **Figures are drawn to scale in most pages but the notes say not to rely on it.** Exception: P5-28 (Height Hunt) relies on the drawing being to scale; the pupil may use a paper corner. A tilted base makes the right angle harder to see than the horizontal ones.
5. **Magic square P5-10** has the well-known 3 by 3 structure; the check strip and the printed total are the check. The four given numbers always allow a line-by-line solution (tested), but a pupil who knows magic squares may shortcut.
6. **Number chain P5-12** does not detect two slips that cancel (a different wrong number carried on); the notes say so. A blank circle is seen at once.
7. **Put-the-answer-back page P5-07** has no code word: the check is substitution; it is weakest against a pupil who does not substitute.
8. **P5-39** uses the three-way statement form (true, false, not possible to tell) of the school papers; "not possible to tell" is always the trapezium angles on different sides.
9. **Interest** (P5-25) is one year of simple interest; the PDF says only "annual interest".
10. **GST** is 9% and stated on the page (7% in older papers).
11. **P5-21** bars of 20 parts are the smallest counted objects (3.6 mm wide, taller than 8 mm).
12. **Colour-by-code** pages use the vendored library with a new Primary 5 bank: answer boxes 9 mm (the audited P2 rule), the pencil-only colour letters are written in the part; a two-line question form was used on P5-22 so that the 9 mm box fits. Small text on the 1-bit copy of P5-05 is about 9 pt.
13. **ℓ glyph** comes from a fallback font (embedded, viewed).
14. No real photocopier test, no pupil trial.
15. Another process commits the working tree as Checkpoint commits, so some files may appear in commits earlier than mine.
16. The word list for the code-word test is about 242 000 words (not 262 000): a union of the P2 list, web2, gcide and wordfreq (183 000 most frequent). Nothing found by the P1 and P2 audits was lost; `siring`, `jailor` and `sonic` are also on the reject list.

## Decisions needed from the owner

- Accept the exclusion of average, pie charts and ratio from Primary 5 (or ask for a labelled preview page).
- Whether Semester 1 should carry fractions and decimals and Semester 2 the geometry (schools vary; the notes say to use any page when its topic is taught).
- Simple interest only (P5-25).
- Lawyer wording, pupil trial and photocopier test as for P1 and P2.
- What the colour-by-code library change should be: this pack vendored its own Primary 5 bank. A shared `banks_p5.py` in `school/colour_by_code` would let the gallery use it (not done, library untouched as instructed).

## Library changes wanted (not made)

`school/colour_by_code/banks_p5.py` and the four percentage rules in `textcheck.py` (now in `school/p5/cbc_vendor/`).

## Round 2 audit fixes (`docs/audit_final/p5_semester_booklets_audit_round2.md`)

- **M1 code word:** P5-31 MELODY repeated P3 S1-06. It is now THIRDS. `gen/other_levels_words.json` now holds all 86 code words read from the answer keys of P1 to P4 and P6 (``school/p5/refresh_other_words.py`; P3 to P6 are still being revised, so the list was re-read at the end and must be re-read once more before print); the base list that fixes the candidate order is `other_levels_words_base.json`, newer words are skipped when a page chooses its word. The corrected list is above (31 words; BIRTHS, P5-29, was missing from the first list). Because the page content depends on which words are tried, P5-25 (COSTLY) and P5-26 (TYPING) swapped words and P5-25 has new numbers; P5-40 is DEPTHS with new figures.
- **L1 P5-39:** the rows that ask "not possible to tell" now compare the two angles at the ends of the SAME parallel side of the trapezium (for example angle H and angle G when HG is parallel to EF). That answer is N whether "trapezium" means exactly one pair or at least one pair of parallel sides. The key note says so. All six rows re-solved: F, N, T, T, F, T = MATRIX.
- **L2 instruction sentences:** P5-38, P5-40, P5-36 and the two colour pages (P5-05, P5-22) now have at most 4 instruction sentences; `validate.py` counts sentences, not list entries.
- **L3 label sizes, corrected:** the first report quoted the SVG size before scaling. The figures sat in a column narrowed by the number circle and were shrunk by about 20%. Figure cards now put the figure on the full card width, so printed label sizes, measured from the PDF text spans, are: P5-29, 31, 33: 11.6 pt; P5-38: 11.9 to 13 pt; P5-40: 11.6 to 13 pt; P5-37: 11.0 pt (labels raised from 10.2); P5-36: 10.4 to 10.7 pt (labels raised, cells taller; the grid still limits it). P5-38 and P5-40 cards gained a title line ("Angle marked ?") and the interior labels were moved away from the sides; right triangles on P5-38 are drawn with the wider acute angle labelled; flat isosceles figures on P5-40 were removed. P5-36 and P5-37 stay flagged for the pupil trial and the photocopier test.
- **L4 overlap tweaks:** P5-16 item 4 is now a florist (roses, bouquets and a wedding display); P5-26 item 3 uses a cook with 14 or 16 pancakes in place of 15 and 90; P5-27 item 4 is a mechanic (bikes, days) in place of the eggs frame; P5-35 pond and tub dimensions no longer equal the extension tank (60 by 50 by 40) and tub base (40 by 30).
- **L5 key notes:** the notes of P5-28, 29 and 30 now count what the page really shows (tilted bases, heights outside the triangle, extra slanted-side lengths) and say none when there are none. The P5-18 key prints the correct classification and the true answer of each false statement.
- **L6 P5-40:** the "?" at the apex of the figures with two exterior angles now has an arc.
- **Checks re-run on the final build:** the private-source similarity script gives 0 shared seven-word runs (two loose same-number hits are false positives: the colour-tally wording and the code table of P5-16); `validate.py` scans pupil pages and keys for Primary 6 words (0 found) and now also checks the code words against other levels; 740 checks, 0 failed.
- **Hand-solved from the render after these changes:** S1-16 (PERIOD), S1-05 and S2-02 instruction lines (viewed), S2-05 (COSTLY: 1236, 60, 20, 40, 206, 2050), S2-06 (TYPING), S2-07 (DIGEST), S2-09 (BIRTHS), S2-11 (THIRDS: 48, 36, 18, 39, 34, 32), S2-13 (SURELY), S2-15 (FORMAT: 900 mL, 8, 115, 75, 35, 50), S2-16 (route walked), S2-17 (BACKED), S2-18 (LIFTED), S2-19 (MATRIX), S2-20 (DEPTHS: 128, 119, 112, 53, 84, 130). All agree with the keys. Viewed in colour and, for S2-16, 18 and 20 and earlier the other changed pages, in 1-bit at 100 dpi.

## Round 3 tidy (`docs/audit_final/p5_semester_booklets_audit_round3.md`)

- L1 P5-16: the story column has right padding, so the word "of" no longer touches the answer box (item 6 now wraps one word earlier).
- L2 P5-37 item 2: a label in a narrow sector (under 50 degrees) now sits near the ray tips, where both rays clear it; P5-37 figures are 4 mm taller. Angle labels on P5-36 and P5-37 raised from 3.9 and 4.0 to 4.2 (printed about 11 pt on P5-37 and 10.5 to 11 pt on P5-36 cells).
- L3 colour pages: the instruction is now three short sentences in place of the 16-word letter list: "Work out the answer in each part and find it in the key." "Colour the part." "No crayon? Write Y, R, B, G or O in it." (four sentences in all, the plan limit).
- L4 P5-30 note says the dotted base extension is thin and faint on a light copy and not needed. L5 P5-25 note: the decoy list no longer names a two-year decoy; it names the interest taken away from the money saved (the decoy actually used).
- L6 P5-36: START and FINISH tags are bolder (9.5 pt, weight 900, wider padding) on all route pages (P5-04, 11, 30, 36).
- L7 the other levels' code words were re-read from the final answer keys at the end (`school/p5/refresh_other_words.py`): 86 words, unchanged from the previous snapshot, no P5 word among them. P3 to P6 builders may still change words: run the script and `validate.py` again after their last build.
- Colour-page hardening (as P6): `BOX_SIDE` default in `cbc_vendor/layout.py` is now 9.0, the value the P5 colour pages use, so no code path gives a different sheet; `validate.py` compares the questions of each colour page with the key (S1 and S2). Before changing the instruction line the pupil and key pages of P5-05 and P5-22 were compared with the audited build: text identical on every page of both booklets and keys, and 70 dpi renders identical (pupil pages S1-05 and S2-02, all 9 and 10 key pages). After the instruction change only those three instruction lines differ.
- Hand-solved after this pass: S1-04 route walked (8 boxes), P5-16 (PERIOD), P5-37 (BACKED), P5-36 and P5-30 routes unchanged; validate.py 742 checks, 0 failed.
