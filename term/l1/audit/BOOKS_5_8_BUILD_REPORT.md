# Books 5 to 8 build report (Level 1, Terms 3 and 4)

Date: 23 Oct 2026. Branch claude/great-fermi-1hv4vc. Outputs are git-ignored (`outputs/print/term/`, `outputs/print/bw/term/`, `term/l1/out/`), not committed.

## 1. Owner decision applied: parcel policy "PDF straight away"
Recorded in `docs/terms/owner_decisions.md` (23 Oct 2026, late batch, item 7): a missing or damaged book gets the PDF immediately; the rest of the draft stands (report within 7 days, one free resend; a second loss is discussed).

One plain sentence now stands on every family-facing page that mentions a missing or damaged book:
"If your book has not arrived or is damaged, message us on WhatsApp within 7 days and we will send you the PDF straight away."
No other promise (no resend wording) is made on family pages.

| Lesson | Family-facing place changed |
|---|---|
| L30 | Quest grown-up note, "before" list (was "Something missing from the book? Tell us a week before...") |
| L35 | Parent summary, "next materials" (Book 8 line); the line was also shortened slightly so the summary still fits one page |
| L39 | Parent summary, "next" paragraph |
| L40 | Quest grown-up note, "before" list |
| L36 | No family-facing book line existed (the policy sat only in the tutor's "tell parents a week before" note); nothing added to the family page |

Tutor-only notes (L35, L36, L39, L40 "Tell parents a week before"): "draft, owner to confirm" replaced by "owner decision, 23 Oct 2026", with the fuller text (report within 7 days, PDF straight away, one free resend, a second loss is discussed). L30 and L40 tutor lines about a missing Quest Log still mention sending the PDF another way; unchanged apart from L40 saying "as a PDF straight away" already.

Searched all 40 lessons for 'missing', 'damaged', 'WhatsApp'. Lessons 11 to 19 say "A missing workbook page: your tutor sends a PDF to print at 100%". That is about a single page, not the book or parcel, and is left as it is (it already says PDF).

## 2. Lessons 20 to 40 rebuilt
No change to `term/l1/tools/` since the REBUILD_REPORT (git diff of tools and print shows only the new toolbox card script), so no tool-driven rebuild of 1-19 was needed. Lessons 20 to 40 were rebuilt fresh (`bash term/l1/build.sh NN`), then `python3 term/l1/tools/validate.py NN`:
- L20 to L40: 0 FAIL each (warnings 0 to 5 per lesson).
- L35 first failed (Parent_Summary spilled onto a second page because of the longer sentence); fixed by trimming two phrases in the same list; rebuilt, 0 FAIL.

## 3. Books 5 to 8
Command: `python3 print/make_term_books.py --level 1 --first 21 --last 40 --size 5 --per-term 10`, then `python3 print/make_bw_print.py --only L1_T3 --check` and `--only L1_T4 --check` (also rerun for T1 and T2, see section 5).

| Book | Content | Workbook pages / sheets | Answer key | Home pack | Result |
|---|---|---|---|---|---|
| 5 | Term 3, Lessons 1 to 5 (L21-25) | 42 / 21 | 22 / 11 | 12 / 6 | PASS |
| 6 | Term 3, Lessons 6 to 10 (L26-30) | 46 / 23 | 30 / 15 | 14 / 7 | PASS |
| 7 | Term 4, Lessons 1 to 5 (L31-35) | 48 / 24 | 22 / 11 | 12 / 6 | PASS |
| 8 | Term 4, Lessons 6 to 10 (L36-40) | 42 / 21 | 30 / 15 | 14 / 7 | PASS |

Automated checks, all 12 colour files and 12 B&W files:
- Page counts even; B&W page count, blank count and order equal colour.
- Covers: "Term 3, Lessons 1 to 5" style numbering; contents list every lesson with its title (checked in text for all 12 files); page headers say "Term 3 - Lesson N" (same numbering).
- Kit pages: counts equal the number of "Kit page" pages in the lesson outputs (Book 5: 5, Book 6: 4, Book 7: 8, Book 8: 3); every kit page is on a front (odd) page and its back is blank (no text, no image); kit pages at 100% (title font size and position identical to the lesson PDF).
- Quest Logs: lessons 30 and 40, 4 pages each, at the end of Books 6 and 8 (pages 41-44 of 46, 39-42 of 42), as the Quest Logs of Books 2 and 4. Tutor notes in the answer keys and the grown-up note in the home packs are present.
- Mi: cover Mi is `mascot/mi_dolphin_nocalc_transparent.png`; the Mi on each lesson's first page, in the tutor notes and in the grown-up notes is the 833 by 834 no-calculator image (the calculator version is 826 wide; hashed all images in the 12 files: only two distinct images, both no-calculator). Seen on rendered pages.
- Text search of all 12 files: no "hold ... to the camera" instruction (the only hits are "never held up to the camera" and "Not allowed: a calculator" in the Quest rules), no S$ amount, no "price per"/"quote".
- Black and white: `print/check_bw.py` run for each file: max non-grey pixels 0.00000 in all files (limit 0.05%). Light-tint cells at most 0.2 percent.

### What I viewed (rendered and looked at)
For each of Books 5, 6, 7 and 8, in colour and in black and white: workbook cover, contents, one workbook page (page 5), the first kit page, the last kit page (Book 6 and Book 8: the last Quest Log page, page 44 and 42), two answer-key pages (5 and the middle one), one home-pack page (5). Also the first page of one lesson per Term 3 and Term 4 book at larger size for Mi. All looked right: clocks, price tags, coin and grid kits, calendar, fold shapes, pair cards, paper people and the tool cards are whole on the page and in B&W the colours became distinguishable patterns (paper people differ by pattern, tier chip and Yes/No boxes readable).

## 4. Problems found
1. FIXED, `print/make_term_books.py`: the third "Kit pages (cut-outs)" line on every workbook contents page ran off the right edge of the page ("...keep them in an envelope" was clipped). It is now split over two lines. This affects Books 1 to 4 as well, so they were rebuilt (colour, and B&W) with unchanged page counts (46/46/44/48, 22/30/22/28, 12/14/12/14).
2. FIXED, L35 parent summary spill (see section 2).
3. LEFT, as in Book 2: Books 2 and 6 end with two blank pages after the Quest Log (one spare sheet that is a clean back cover but costs one sheet). Book 4 has one. Cause: `make_term_books.py` adds a blank after the Quest Log if the lesson's last workbook page was a kit page, and then the final even-page rule adds another when the Quest Log has an even length. Removing it would change the Book 2 and Book 6 counts that quotes may already use (46 and 46 pages); owner can decide.
4. LEFT: topic subtitles on the contents pages are title-cased by the lesson data ("Reading A Scale: The Clock", "Money: Dollars And Change"). Same in Books 1 to 4; cosmetic.
5. NOTE: `print/make_term_books.py` and `print/make_bw_print.py --only ...` overwrite `term_books_spec.json` and `bw_spec.json` with only the rows built in that run. I merged `term_books_spec.json` for all 24 files by hand; `outputs/print/bw/bw_spec.json` holds only the last run (T2) and is not used by the quote file.

## 5. Docs and commit
`docs/printing/quote_request.md`: added the page and sheet counts for Books 5 to 8 (workbook, answer key, home pack), the Term 3 and Term 4 quantities per child, numbering lines, and the Quest Log pages at the end of Books 6 and 8 (L30_Quest_Log.pdf, L40_Quest_Log.pdf). No prices.
Committed source and doc changes only, with explicit paths; not pushed.
