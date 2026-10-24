# Coin and note style sample (review only)

**HELD BACK: not for use in any book until the lawyer answers question 10.**

Written 24 Oct 2026. This is a one-page A4 review sample, not part of any book, generator output, PDF pack, website or deck.

## What it is
An original illustration of the five current coins and the five Portrait-series notes, drawn from scratch as SVG code (`make_sample.py`). The owner's AI-style reference picture was used only as a look guide (soft gradients, rounded outlines, pastel notes). Nothing was traced, and the reference's errors were not copied: no garbled words, no purple $50, no Merlion over a portrait, and the $1 coin has the correct brass ring with a silver centre (the reference had it the other way round).

Files: `coin_note_style_sample.pdf` (vector, A4), `.png` (200 dpi), `.svg` (source), `make_sample.py` (builds all), `verify.py` and `verify_report.txt` (checks, all PASS), `spec.json` (geometry written by the generator).

## Sources (read 24 Oct 2026)
- Coin diameters, materials, edges: MAS Circulation Currency: Coins (5c 16.75, 10c 18.50, 20c 21.00, 50c 23.00, $1 24.65 mm with inner circle 16 mm), as recorded in `docs/school_books/coin_note_specs.md` and re-confirmed in `docs/audit_final/coin_redraw_check.md`. Cross-check read today: Wikipedia "Singapore dollar", coin table (5c brass-plated steel, plain edge; 10c nickel-plated steel, interrupted reeding; 20c reeded; 50c scalloped; $1 bi-metallic, brass outer ring and nickel inner, reeded).
- Note sizes and colours: Wikipedia "Singapore Portrait Series currency notes" table, read today: $2 126 x 63 purple, $5 133 x 66 green, $10 141 x 69 red, $50 156 x 74 blue, $100 162 x 77 orange. The $2, $5, $10 sizes agree with the MAS page cited in `coin_note_specs.md`. The $50 and $100 sizes come from Wikipedia only; I could not read them on the MAS page (it is script-rendered). Treat them as unconfirmed against MAS.
- Reproduction rules: `docs/school_books/coin_reproduction_check.md` (MAS "Using Images of Singapore Currency", read 23 Oct 2026).
- Decisions: COINS-FIX-SIZE (coin sizes real proportions, notes 2:1 and larger for higher values, "Pictures are not actual size"), COINS-B-ASK-LAWYER (our redraw in books; real-image variant held back) in `docs/terms/owner_decisions.md`.

## What is on the sheet
- Coins at 80% of real size (same as P1/P2 pages), one scale for all five. Words: numeral and CENTS; $1 coin shows only "$1". The word DOLLAR (in the reference) is left off because I could not confirm it on a real coin; the owner can check with a real coin. Edge hints on the face rim follow the edge types above (5c plain, 10c interrupted reeding, 20c reeded, 50c scalloped, $1 reeded). Colours: brass tone for 5c and the $1 ring, silver for the rest.
- Notes at exactly 60% of real size, real aspect ratios (2.00 to 2.11 : 1), growing with value. Words: SINGAPORE, the numeral, SPECIMEN. No other words on any note. Plain dots and wave lines replace small print. A generic rosette stands in for the crest. The portrait area is a neutral silhouette (head and shoulders, no face, no likeness).
- SPECIMEN runs across the full width of each note in a band below the portrait area, so the portrait area is not covered.
- Sheet text outside the artwork: title, the held-back banner, captions with real sizes, "Pictures are not actual size." and short notes. `verify_report.txt` lists them.

## What is NOT included
Real portrait or any likeness, coat of arms, Merlion or other national symbols, real designs of the reverse, serial numbers, signatures, security features, $1000 and $10000 notes, the real coin motifs, and the word DOLLAR on the $1 coin. The note colours are pastel (lighter than real notes) on purpose so they cannot pass as genuine.

## Verification (run `python3 make_sample.py` then `python3 verify.py`; needs cairosvg, Pillow, numpy, tesseract)
- Words: every string drawn is in the whitelist (SINGAPORE, SPECIMEN, CENTS, numerals, $1). Tesseract on the 400 dpi render found no other word on the artwork; its only extra output was dot patterns read as "eee" noise and cut-off pieces of SINGAPORE.
- Coin diameters measured from pixels: within 0.25% of 0.80 x spec (50c -0.09%); ratios to the $1 coin match 0.680 / 0.751 / 0.852 / 0.933 within 1%.
- Notes: aspect ratios equal the real ratios; sampled hues match purple, green, red, blue, orange.

## MAS conditions: met and not met
Met (as far as this sheet goes): notes proportionally scaled; SPECIMEN across each note; notes at 60% (the rule is at least 150% or at most 60% in both directions); one side only; printed as paper (not coin or note material); no portrait or President's image distorted (none drawn); nothing offensive; not mistakable for genuine (pastel, SPECIMEN, wrong sizes). The scale line "Pictures are not actual size." is on the sheet.
Cannot be met or settled here:
- Print scale: the PDF must be printed at 100% (no "fit to page") to stay at 60%; any enlargement is allowed only to 150% or more, never between 60% and 150%. Anything below 60% is fine.
- Whether a sold, photocopiable workbook counts as an "educational publication" (no permission needed) or "merchandise" (permission needed): open, lawyer question 10 (owner decision D1). Until answered this sample is not used.
- The SPECIMEN rule says "across a whole flat note"; a horizontal band that avoids the portrait area is my reading, not confirmed by MAS. Ask the lawyer or MAS.
- The MAS page gives no size rule for coins; coins here are 80% of real size by the owner's COINS-FIX-SIZE choice.
- Coins and notes are at different scales, hence the "not actual size" line.
- Whether a coin-style design at all is acceptable beyond the sizes and the word CENTS was not judged; no real coin was in hand to compare.

HELD BACK: not for use in any book until the lawyer answers question 10.
