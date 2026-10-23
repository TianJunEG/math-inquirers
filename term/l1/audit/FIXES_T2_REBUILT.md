# Fixes after FINAL_AUDIT_T2_REBUILT

- M1 numbering. print/make_term_books.py now uses the number within the term everywhere: cover "Term 2, Lessons 1 to 5" / "6 to 10", contents rows "Lesson 1..10", file names and PDF titles (Book3_Lessons01-05, Book4_Lessons06-10); answer keys and home packs share the cover code, so they match the page headers ("Term 2 - Lesson 1"). Books 1-2 were already consistent (Term 1 lessons 1-10). The B&W files are made from the colour books, so they inherit it (old Lessons11-15 / 16-20 files deleted). L10 goodbye slide, next-materials, parent text and tutor guide now say "Term 2 Lesson 1" (l10.json); L8 tutor note "Lesson 19" is now "Term 2 Lesson 9". validate.py leak check allows "Term N, Lesson 1" / "its Lesson 1".
- M2 L16 T1 B&W. tools/figs2.py array(): shaded rows get a dark box (survives B&W); L16 wording says "in the box" (T1, slides, hint, notes). Colour keeps the shading too.
- M3 recording order. l01-l10.json now run: greet (do), hello, recording notice, "Start the recording now" (do), then REC, same wording as L11-L20. Tutor-prep line replaced by the L11 wording; the unconfirmed "children's video is excluded; names kept off the screen" claim in l01 note removed. DO lines timed 1 s and 3 s so timing still passes.
- M5 L14 T3(c): "Add any two odd numbers. Is the total odd? Circle one." (Always / Sometimes / Never; answer Never).
- M4 Quest Log. It was already in the printed books (4 pages end of Book 2, 3 pages end of Book 4); the audit missed it. Documented in docs/printing/quote_request.md (also the loose copy tutors send a week before); L10/L20 grown-up notes now say so. Page counts unchanged (46/22/12, 46/30/14, 44/22/12, 48/28/14), quote table only renamed.
- Low: contents kit note no longer clipped at the right edge.
- Rebuilt: lessons 01-10, 14, 16, 20 (validate 0 FAIL), colour books, B&W books and check_bw.
- Not fixed: other Lows (L1-L3, L4-L10 of the audit).
