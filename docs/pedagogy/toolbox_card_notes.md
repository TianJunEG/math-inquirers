# A5 toolbox card: build notes (23 Oct 2026)

Decision D7 (owner): build the card for the Inquirer Kit. Spec source: `docs/pedagogy/spine_routine_spec.md` (sections 1 and 3).

## What was built
- `print/make_toolbox_card.py` builds three cards from `levels/spine.json` and `levels/spine_icons/*.svg` (via `levels/spine_icons.py`). Idempotent: re-running overwrites the same six files (page content is identical; PDF metadata timestamps differ). Needs playwright chromium, PyMuPDF, Pillow. `--band A|B|C` builds one.
- Outputs in `outputs/kit/` (about 55-65 KB each): `Math_Inquirers_Toolbox_Card_<A_6-8|B_8-10|C_10-13>_PRINT_BW.pdf` (printer file, 1-bit 600 dpi, only black and white pixels) and `_SCREEN_colour.pdf` (vector, navy ink, yellow header, pale icon discs).
- Layout (rebuilt 24 Oct 2026, see `term/l1/audit/TOOLBOX_CARD_FIXES.md`): A5 portrait, 2 pages, no bleed, no crop marks, flip on the long edge. Front: "Toolbox Card", large "AGES 6-8" box, eight rows (icon in a ring, numbered name, band definition at 12 pt); tools 1, 2, 3 and 8 carry a small "Term 1" tag on card A. Back: a reusable reference, not a write-on sheet: the intro, the three band prompts (numbered circles, no tick boxes), one drawing box ("Draw or write one word. Use a pencil." on band A) and a "When I am stuck" panel (Wait. Try a tool. Try a smaller case. Ask.), plus the publisher line. Removed: yes/not-yet boxes, "My tool today", "My name", the still-stuck and pass tick boxes. Wording is the spec's (`levels/spine.json`).
- No Mi on the card (new elements carry no Mi per the spec). No calculator, no MOE/GEP/SASMO claim, no result promise.
- B&W: no grey fills, no tints (white fill in the B&W file); the colour file's tints are decoration only, never the only cue. Icons are the stroke-only 3-unit icons, drawn at 11.5 mm (the spec requires legibility at 10 mm).

## Kit and print documentation
- `docs/printing/quote_request.md`: new section "Inquirer Kit: A5 strategy toolbox card": three files, A5, double-sided, quantity 1 per child per workbook plus about 10 percent spare, stock suggestions (250 gsm card preferred, 170 gsm alternative, optional matt lamination), no prices.
- `levels/spine.json` `kit_line` = "Eight tools: see your Inquirer Kit card" already names the card and the Inquirer Kit: valid, unchanged.
- Not changed (other agents / out of scope): the cut-out pages in the workbooks (`hp/kit.js`), `levels/mkextras.py` kit list line and the website "takes home" lists still describe the kit as workbook cut-out pages only. Suggest adding "a toolbox card" to those wording lines once the owner confirms the card ships in the parcel (D7 print route); parents' wording should say "your child will practise", no outcomes.

## Checks done
Rendered both sides of A, B, C (B&W and colour) at 80 dpi and looked: no clipping, longest band C definitions wrap to two lines, icons readable. Not done: a physical 600 dpi proof at 100 percent; do one print on the printer's sample run. Print with "actual size", not "fit to page".

## Open points
- Band overlap: Levels 3 and 4 share card B; ages 8 and 10 appear on two cards (as in the spec).
- If the card is not printed (D7 alternative), send the colour PDF in the welcome message; the card works on A4 plain paper cut in half is not supported, print at A5 or scale.
