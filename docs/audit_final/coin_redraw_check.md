# Coin and note redraw: independent check (23 Oct 2026)

Branch claude/great-fermi-1hv4vc, HEAD d63259e. Reference commit for diffs: 25b1d3d (parent of a2c174f). Nothing was edited except this report.

## Verdict

PASS with 2 minor issues and 1 wording issue to fix. The specs are confirmed, the four pages follow them, all four hand-solves match the key, and the money colour sheets verify. Two pages (P2-24, P1-28) do not use one single coin scale.

## 1. Spec values

Fetched the MAS pages on 23 Oct 2026.

- MAS Circulation Currency: Coins (Third Series, 2013 to present): 5c 16.75, 10c 18.50, 20c 21.00, 50c 23.00, $1 24.65 mm (inner circle 16). All five CONFIRMED. The same page lists the older Second Series (20c 21.36, 50c 24.66, $1 22.40), which explains the earlier wrong values.
- MAS Circulation Currency: Notes (Portrait series): $2 126x63, $5 133x66, $10 141x69 mm. All three CONFIRMED.
- Not confirmed here: the claim in the specs doc that polymer notes share the paper sizes (MAS 2005 and 2007 releases). I did not fetch those releases. It does not change any figure.
- I did not use a second source (a numismatic catalogue). The specs doc cites Wikipedia as a cross-check, which I did not re-check.

## 2. Drawn proportions (measured from vector PDFs, school/p1/out and school/p2/out)

Diameters include stroke width, so each is about 0.1 mm over the nominal figure (nominal = real x 0.80). Ratios to the $1 coin match the spec: 5c 0.68, 10c 0.75, 20c 0.85, 50c 0.93.

- P2 S2-01 (P2-06), page 1: coins 13.4 / 14.8 / 16.8 / 18.4 / 19.8 mm. Notes $2 27.1x13.5 (2.01:1), $5 28.6x14.2 (2.01:1), $10 30.3x14.8 (2.05:1). Real ratios are 2.00, 2.02 and 2.04. Constant scale, notes 2:1 and growing with value. PASS.
- P1 S2-10 (P1-15), page 10: coins 13.4 / 14.8 / 16.8 / 18.4 mm, one scale. No notes. PASS.
- P2 S2-04 (P2-24), page 4: ISSUE (minor). Coin scale is constant within a purse but differs between purses. Purses U, A and M are at 1.00 (19.8 / 18.4 / 16.8 mm). Purse P is at 0.983 ($1 would be 18.09, 10c 14.55, 5c 13.17). Purses S and C are at about 0.967 ($1 19.14, 5c 12.96, 10c 14.33, 20c 16.27). So a $1 coin measures 19.14 mm in purse S and 19.8 mm in purse A. This looks like per-purse shrinking to fit. A pupil comparing purses may notice. Ask for a single scale (0.967 for every purse would fit).
- P1 S2-11 (P1-28), page 11: ISSUE (minor). The "Coins:" tray and the two inline coins in items 3 and 4 are at 1.0 (13.4 / 14.8 / 16.8 / 18.4). The four purse coins in item 5 are at 1.20 (16.0 / 17.8 / 20.2 / 22.0). Ratios inside each group are correct, but the same 5c coin appears at two sizes on one page. Either unify the scale or accept it because the purses are a separate task. Pupils are not asked to compare the groups.

## 3. Hand-solve from the rendered images

All four match the key and the code table.

- P2-06: $2.65 S, $1.85 A, $2.90 I, $6.15 L, $10.25 O, $2.45 R. Word SAILOR. Matches the key.
- P2-24: purses S $2.10, P $1.15, C $1.40, U $2.20, A $3.00, M $1.70. Amounts 1 to 6 give C, A, M, P, U, S. Word CAMPUS. Matches the key. Within the page all six totals are distinct.
- P1-15: 80, 60, 40, 25, 95 give P, I, A, N, O. Word PIANO. Matches.
- P1-28: 2, 3, 9, 4, and 1 tick (only 20+10 makes 30¢) give S, T, A, M, P. Word STAMP. Matches.

Code words are unique inside each of the four answer keys (no repeated word per book). I could not re-run the anagram test, because there is no word list on this machine. Not re-verified, taken from the key's statement.

## 4. 1-bit view (pdftoppm -mono 150 dpi, enlarged 2x)

P2-06 and P1-15 checked. "cents" and "dollar" are legible on every coin, including the 5c. No overflow and no clutter. Strokes are solid. The "cents" word on the 5c fills about 85 percent of the lower chord, so the margin is tight but clean. PASS.

## 5. "Pictures are not actual size."

Present in the Photocopying section of the front matter of P1 S1, P1 S2, P2 S1 and P2 S2. It is in the front-matter teacher notes, not in the per-page answer-key notes. The wording is in school/p1/render.py:313 and school/p2/render.py:312. PASS.

WORDING ISSUE: P2 S1 and S2 front matter (line 129 and 127: "drawn larger than real") and P2_S2_Answer_Key.txt (lines 44 and 91: "drawn larger than real") are now false. Coins are drawn at 0.80 of real size and notes at 0.215. The same phrase is in the comment at school/colour_by_code/art.py:48. Change to "drawn smaller than real" or "not actual size". The P1 key wording ("sizes in the true proportion") is fine.

## 6. Change against 25b1d3d

- Byte-identical and text-identical: all P1 S1/S2 and P2 S1 PDFs (Puzzles, Answer_Key, FrontMatter).
- School files changed in a2c174f and later: P2 S2 Puzzles, Answer_Key, FrontMatter and Complete_Pack, plus validation_report.txt.
- P2_S2_FrontMatter text is identical; only the PDF bytes differ.
- P2_S2 content that changed: only S2-04 (P2-24). Purse contents were rebuilt (the coin count went from 43 to 45) and the amounts changed: 1.35 / 2.50 / 1.55 / 1.15 / 1.70 / 1.20 became 1.40 / 3.00 / 1.70 / 1.15 / 2.20 / 2.10. The key was updated consistently. The code word is unchanged in role (CAMPUS). The old key's amounts are gone from the PDFs. No other page changed in text.
- Because P1 and P2 S1 are unchanged since before a2c174f, the new proportions in P1 were already in the output at that point. P1 S2 measured as redrawn above.
- Other changes in the range (extension data, outputs/extension, docs/owner_kit/coin_comparison_sheet.md, build reports, owner_review PDF) are outside the scope of this check.

## 7. colour_by_code money sheets

school/colour_by_code/out/p1/verification.txt (CBC-07) and out/p2/verification.txt (CBC-P2-07): all lines PASS, 0 FAIL in either file. These include independent re-solve of all 13 (P1) and 15 (P2) questions, tallies, no repeated questions, and 30000/30000 single-slip detection for CBC-P2-07. COIN_R in school/colour_by_code/art.py (4.42 / 4.88 / 5.54 / 6.07 / 6.50 mm radius) gives ratios 0.68 / 0.75 / 0.85 / 0.93, so it follows the spec. Recorded results were read, not re-run.

## Issues list

1. (Low, wording) "drawn larger than real" is false in P2 S1 and S2 front matter, P2_S2_Answer_Key, and the art.py comment.
2. (Low, art) P2-24 coin scale varies per purse (1.00 / 0.983 / 0.967).
3. (Low, art) P1-28 purse coins are 1.2 times the size of the tray coins.
4. (Info) The second source for the specs was not re-checked beyond MAS, and the polymer-size claim was not fetched.
