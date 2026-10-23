# Print quote request (copy and send to each printer)

Hello, we are a small maths enrichment program in Singapore and would like a quote for printing workbooks, with delivery to individual homes in Singapore. Please quote for the six workbooks below. The files are ready to print: A4, BLACK AND WHITE (1-bit, 600 dpi, no colour at all), double-sided, flip on the long edge. Please quote on the cheaper end of the market: plain uncoated 80 to 100 gsm office-grade paper is fine for the pages.

**Specification**
- Paper: A4, 80 to 120 gsm; cheaper stock is fine for mono (please give prices for 80 / 100 / 120 gsm).
- Print: black and white (mono) only, both sides. Please quote mono double-sided, and as a comparison also full colour, so we can see the difference.
- Binding: spiral (plastic coil) or wire-o on the LEFT long edge. Please tell us which you offer and the cost difference.
- Cover: please quote (a) no separate cover, the first page is the cover, and (b) a clear front cover and card back.
- Pages that are intentionally blank are included in the file. Please do not remove them.
- Delivery: to home addresses in Singapore, one workbook per parcel (or a parcel for 2 siblings' workbooks). Please state the delivery time from our order, the packaging, and the cost per parcel.

| Workbook | Pages in the file | Sheets (double-sided) |
|---|---|---|
| Level 1 (ages 6-8) | 64 | 32 |
| Level 2 (ages 7-9) | 74 | 37 |
| Level 3 (ages 8-10) | 64 | 32 |
| Level 4 (ages 9-11) | 76 | 38 |
| Level 5 (ages 10-12) | 62 | 31 |
| Level 6 (ages 11-13) | 58 | 29 |

**How we would order**
- Our staff place one batch order each day by an afternoon cutoff time, listing the workbook, quantity, and for each parcel the recipient name, phone and address. Please tell us if you can take the batch as a spreadsheet or in one order, and what you need to do the same-day or next-day start.
- Typical volume at first: 5 to 30 workbooks a week, growing later. Please quote for 1-9, 10-49 and 50+ copies per order.

**Questions**
1. Price per workbook at the volumes above, with and without delivery.
2. Delivery time to Singapore addresses, and tracking numbers.
3. Do you accept re-prints for misprints or damaged parcels at no cost, and how are they reported?
4. Do you delete our files after printing? These are copyrighted materials and must not be reused or shared.
5. Sample: can we order one sample of Level 1 (and one of Level 4) to check quality before we commit?

Thank you.

---

## Term books (Level 1 and later levels): the standard paid-term issue

Printing is triggered by payment. Each paid term, the child receives that term's combined workbook books (printed, no extension workbooks). Answer keys are for tutors only and are never part of the child set. Files are made by `python3 print/make_term_books.py` from `term/l<L>/out/` and written to `outputs/print/term/` (same rules as the level workbooks: A4, black and white, double-sided, flip on the long edge, bound on the LEFT with a mirrored 12 mm gutter, even page count, blank pages are intentional).

**Quantities per paid child per term:** Level 1 Term 1 = 1 x Book 1 + 1 x Book 2; Level 1 Term 2 = 1 x Book 3 + 1 x Book 4 (2 books per child per term, 4 per child for a full year). Tutor answer keys: 1 set per tutor, not per child. The home-practice pack is optional (it is a separate stapled pack of loose sheets; the same sheets can be issued digitally).

**Spec (all books):** A4, 80 to 120 gsm (please quote 80, 100 and 120; the cheaper stock is acceptable), BLACK AND WHITE both sides (files in `outputs/print/bw/term/`), spiral or wire-o on the left long edge, quote (a) first page as cover and (b) clear front cover and card back. Kit (cut-out) pages have a blank back and a dashed tear line in the left margin; please keep blank pages. Optional: perforation along the dashed tear line on kit pages (please quote).

| File (outputs/print/term/) | Pages | Sheets | Issued to |
|---|---|---|---|
| L1_T1_Book1_Lessons01-05_Workbook | 46 | 23 | child, Term 1 |
| L1_T1_Book2_Lessons06-10_Workbook | 46 | 23 | child, Term 1 |
| L1_T2_Book3_Lessons11-15_Workbook | 44 | 22 | child, Term 2 |
| L1_T2_Book4_Lessons16-20_Workbook | 48 | 24 | child, Term 2 |
| Book1-4 AnswerKey_TUTOR | 22 / 30 / 22 / 28 | 11 / 15 / 11 / 14 | tutor only |
| Book1-4 HomePack (optional) | 12 / 14 / 12 / 14 | 6 / 7 / 6 / 7 | loose, stapled |

Page counts follow the current lesson builds; re-run the script (and re-check `term_books_spec.json`) after any rebuild before sending a quote.


---

## Black and white (owner decision, 23 Oct 2026): printed = B&W, soft copies = colour

Send the printer ONLY the files in `outputs/print/bw/` (holiday workbooks) and `outputs/print/bw/term/` (term books). They are 1-bit 600 dpi, so they print identically on any mono laser, digital press or photocopier, with no colour-management surprises. The colour print files in `outputs/print/` and `outputs/print/term/` and the designed PDFs are the SOFT COPIES (downloads) and stay colour. Page counts, sheets, blank backs, kit-page positions and the 12 mm binding gutter are identical in both versions.

**Guidance, B&W vs colour:** mono double-sided on 80 to 100 gsm is the default for every posted workbook (lowest cost; one-bit files print crisply and do not smudge). Choose colour only for a soft-copy buyer who prints at home, or for the covers if the printer offers a colour cover at small extra cost (the cover is a separate decision; ask for both prices). Colours in the books are never the only carrier of meaning: tier chips, counters, graph keys and kit shapes carry a pattern (hatching, dots, lines) in B&W. Crayons on the B&W page are fine for "colour it" tasks. Rebuild: see `docs/printing/README_bw.md`.
