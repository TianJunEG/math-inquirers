# Real-image variant of four money pages (held back, for owner review)

What it is: the four money pages with the original line art replaced by official MAS images of real Singapore coins and notes, to see what the "option C" look (docs/owner_kit/coin_online_comparison_23oct.md, docs/school_books/coin_reproduction_check.md) would be. Built 23 Oct 2026.

It is NOT in the booklets. The booklets and the school/ builds are unchanged and still use the original art. Do not print, sell or send this PDF. Footer says "REAL-IMAGE VARIANT, not for use". It stays held until a lawyer confirms the MAS educational-publication exemption applies to our sold, photocopy-licensed workbooks (question 10 in docs/owner_kit/lawyer_email_draft.md).

## Files
- `money_pages_real_variant.pdf`: 4 A4 pages in this order: P2 S2-01 Dollars and Cents (P2-06), P2 S2-04 Purse Match (P2-24), P1 S2-10 Coin Purses (P1-15), P1 S2-11 Fewest Coins (P1-28).
- `preview_*.png` (100 dpi), `photocopy_1bit150dpi_*.png` (150 dpi, light blur, 1-bit threshold at 128: the photocopy simulation).
- `CONDITIONS.md`: the exact MAS conditions and a pass/unknown table. `source_mas/`: downloaded originals, gazette PDF, `SOURCES.md` (URLs, date).
- `work/`: `prep_assets.py` (greyscale/photocopy-safe versions), `realart.py`, `make_variant.py`, `sim.py`, `assets/`.
- Same questions, answers, layout and page code as the booklet pages (only the coin/note pictures differ, and the footer text). Rebuild: `python3 work/make_variant.py` (about 1 minute). The code switch is `MONEY_ART=real` in `school/p1/gen/pages_measure.py` and `school/p2/gen/art2.py` (off by default). Check done: all 14 default HTML/JSON outputs (both booklets of P1 and P2: pupil, front, key, verification.json) hash identical before and after the change, so the default builds are unchanged. The generators' own self-checks on the four pages pass.

## How the pictures were made
- Coins: left coin (value side: numeral plus landmark) cropped from each MAS 260x130 image, background made white, greyscale, local-contrast boost, thin dark edge. Printed at 0.80 of real diameter (5c 13.4 mm, 10c 14.8, 20c 16.8, 50c 18.4, $1 19.7), the same as the booklet art. Colour (gold/silver) is lost, as with all B&W pages.
- Notes: full MAS front image of $2, $5, $10 (with MAS's own SPECIMEN label), greyscale, local-contrast boost, thin vector frame. Printed at 0.30 of real size in both directions ($2 37.8 x 18.8 mm, $5 39.9 x 19.8, $10 42.3 x 20.9). Layout rows were kept; the rows with notes are a little taller than in the booklet (booklet notes are 0.215 of real size).

## Conditions checklist (details and wording in CONDITIONS.md)
| Condition | Status |
|---|---|
| Educational-publication exemption covers our sold workbook | UNKNOWN (lawyer/MAS) |
| Dignity and integrity | pass (our reading) |
| Not mistakable for genuine (greyscale, paper, notes 30%, SPECIMEN) | pass (our reading); coins at 80% size are the closest call, no coin size rule exists |
| No distortion of President / national symbols | pass for shape; UNKNOWN for the contrast-boosted tones |
| Not offensive | pass |
| Different material from real notes/coins | pass (paper, B&W copy) |
| Notes proportional | pass (aspect within 1%; MAS image margins unknown) |
| Notes at most 60% in both directions | pass (30%) |
| SPECIMEN bold black diagonal, not over portrait | pass (MAS's own label, not changed). It does not span the whole note; the gazette says "diagonally across the reproduction" and "not cover any part of the portrait" |
| One-sided only | pass |
| Coins: size rule | none exists |

## Copyright and licensing of the MAS image files: UNKNOWN
The MAS currency pages only give the rules above (what permission under the Currency Act is needed). They say nothing about copyright in the image files themselves, and the MAS website terms of use were not read. The images are MAS's own photographs, so copyright in the files probably sits with MAS or its photographer; the currency exemption may not cover that. A lawyer should confirm. Also unconfirmed: the Currency Act text itself.

## Legibility findings (150 dpi 1-bit photocopy simulation)
- Plain greyscale (no processing) fails: the gold coins (5c, $1) and the pale note backgrounds go white and the numerals disappear at 128 threshold. So the pictures were contrast-boosted (see CONDITIONS.md on the distortion risk).
- Coins after processing: all five values still read as numeral plus landmark, drawn as outlines. Fine detail (landmarks, "CENTS", "DOLLAR" lettering) is mush. The numeral is the only thing a pupil needs and it reads, but less clearly than the original large "50" / "cents" art; the $1 (a "1" beside the Merlion) is the weakest, and 5c and 10c numerals are about 5 mm tall. Source images are 76 to 106 px across: at 0.80 scale that is 131 to 148 dpi, so they are at the limit and cannot go bigger than about 1.0x of real size without looking soft. Bigger coins are possible only at the cost of layout.
- Notes at 0.30 (about 38 to 42 mm wide): the SPECIMEN label, the large numeral and "TWO/FIVE/TEN DOLLARS" read; the "2" on the $2 is pale and reads as a swirl, so a pupil leans on the words "TWO DOLLARS" (very small, about 1 mm letters). Serial numbers and fine print are unreadable (not needed). At the booklet's 0.215 scale the SPECIMEN label and words are not legible after photocopy; about 0.30 is the least that works, 0.40 or more (up to the 0.60 maximum, $2 about 76 mm wide) would be safer but would need layout changes (one note per line).
- Photocopying a worksheet with sharp page-level thresholds is harsher than a real copier's halftone; a real copier at 150 to 300 dpi should do a little better than this simulation, but test with the school's copier.
