# releases/: approved final files only

Why: the repository reached 4.5 GB because generated build outputs (term/l1/out, black-and-white print PDFs) were committed on every rebuild. From 23 Oct 2026 those are NOT tracked (see .gitignore). Rebuild them with the build scripts (term/l1/build.sh NN, print/make_term_books.py, print/make_bw_print.py).

Rule: the sandbox that builds these files is temporary. When the owner APPROVES a final book or pack, copy that one final PDF here (colour and black-and-white as needed), name it with its version (for example `L1_T1_Book1_Workbook_v1.pdf`), and commit it once. Do not commit work-in-progress builds here. Never overwrite a file that families or printers already have: add v2 instead.

Nothing has been approved yet, so this folder is empty on purpose.
