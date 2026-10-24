# Reproducing the committed school PDFs exactly

Checked 23 Oct 2026 in the Claude Code container (Linux, Playwright 1.56.0, Chromium 141 / Skia/PDF m141 in `/opt/pw-browsers`).

## The cause of "a fresh build differs from the committed PDF"

Every level's `render.py` (P1 to P6) loads its web fonts with `@font-face ... url('../../../fonts/node_modules/@fontsource/...woff2')`, and `school/p?/cbc_vendor/sheet.py` does the same with a `font_rel` path. That path is **relative to the HTML file**, i.e. relative to the `--outdir`. It resolves to `<repo>/fonts/node_modules/@fontsource` only when the outdir is exactly three levels below the repo root (`school/pN/out`, the default).

With `--outdir /tmp/some/scratch` the path points nowhere, the `@font-face` fails silently, and Chromium falls back through `'Nunito Sans', Arial, sans-serif` and `'Fredoka'` to the system fonts. This container has no Nunito Sans or Fredoka installed (`fc-list` has 119 entries, none of them those two; `fc-match` gives Inter or Liberation). Result: `pdffonts` of a fresh scratch build shows only `LiberationSans`, `LiberationSans-Bold` and `LiberationSerif-Bold`. The committed PDFs embed `FredokaLight-SemiBold/Bold` and `NunitoSans12ptExtraLight12pt-Regular/Bold/ExtraBold` (the @fontsource woff2 files) plus a little Liberation (the Arial fallback for stray glyphs). The metrics differ, so text wraps differently and the layout checks in `validate.py` then fail: P3 "S2 pupil page 08 layout", P4 "no flat grey tint areas" (FrontMatter), P6 "6 DRAFT stamps", "front page 02 layout", "S2 key page 01 layout". These are all artefacts of the missing fonts, not code regressions. Old and new code differ equally, as the colour-page note found.

The Chromium version is not the cause: the committed PDFs and the fresh builds both say `Creator: Chromium`, `Producer: Skia/PDF m141`.

`fonts/node_modules` is git-ignored, so it must exist: `cd fonts && npm ci` (package.json pins `@fontsource/fredoka` 5.2.8 and `@fontsource/nunito-sans` 5.2.7). It is present in this container.

## Recipe

Option A: build into the default `out/` (overwrites the committed files, so only do this on purpose or on a copy of the repo):

    cd school/p3 && python3 build.py && python3 validate.py

Option B: build into a scratch dir and keep the fonts reachable. Mirror the depth so `../../../fonts` resolves:

    S=/path/to/scratch
    mkdir -p $S/school/p3/out
    ln -sfn /home/user/math-inquirers/fonts $S/fonts        # $S/school/p3/out/../../../fonts == $S/fonts
    cd /home/user/math-inquirers/school/p3
    python3 build.py --outdir $S/school/p3/out
    python3 validate.py --outdir $S/school/p3/out

(Any outdir works if it is `<dir>/<x>/<y>/<z>` with `<dir>/fonts` linked to the repo `fonts` folder.) No env var or fontconfig change is needed; installing the fonts system-wide is not needed either. Without the link the build still "succeeds", so check with:

    pdffonts $S/school/p3/out/P3_S2_Puzzles.pdf     # must list FredokaLight-* and NunitoSans12pt...

If it lists only Liberation fonts, the build is not faithful and its validate.py failures are meaningless.

Caveat: `validate.py` also builds a long-school-name test into `tempfile.mkdtemp()` (no fonts there); it only checks footer text, so it still passes.

## Result of the check

Built all six levels (both semesters, `build.py --outdir`, fonts linked as in option B) and compared every committed `school/pN/out/*.pdf` (8 per level, 48 files) with the fresh one: `pdftotext -layout` text and the md5 of every page rendered at 70 dpi (`pdftoppm -r 70`).

| Level | Committed PDFs matching a faithful fresh build |
|---|---|
| P1 | all 8 identical (text and every page) |
| P2 | all 8 identical |
| P3 | all 8 identical |
| P4 | all 8 identical |
| P5 | all 8 identical |
| P6 | all 8 identical |

So all committed PDFs of P1 to P6 are reproduced exactly (text and 70 dpi pixels) by the current code when the fonts are reachable. (This was the working tree on branch claude/great-fermi-1hv4vc at the time; P3 had had other builders' edits committed by then.) `validate.py --outdir` on these faithful builds: P3 755 checks 0 failed, P4 746 checks 0 failed, P6 753 checks 0 failed, matching the committed validation reports. A build into `/tmp` without the fonts link reproduces none of them.

Not compared: HTML files in `out/`, `verification.json`, and PDF metadata dates (the CreationDate differs on every build, as expected). `school/colour_by_code/build.py` uses `HERE`-based font paths and is not affected by the outdir.

## Suggested hardening (not done; pipeline code untouched)

Make the `FONT` path absolute (from `__file__`) in the six `render.py` files and in `cbc_vendor/sheet.py`, or make `build.py` fail loudly when `pdffonts` shows no Nunito/Fredoka.
