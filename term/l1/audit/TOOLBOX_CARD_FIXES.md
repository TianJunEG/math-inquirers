# Toolbox Card fixes (owner decision CARD-FIX-ALL, 24 Oct 2026)

Fixes to `print/make_toolbox_card.py` per `term/l1/audit/TOOLBOX_CARD_AUDIT.md`. Rebuilt all six PDFs in `outputs/kit/` (cards A, B, C; PRINT_BW 1-bit 600 dpi and SCREEN_colour). `print/check_bw.py` passes on all three B&W files (no non-grey pixels, no blank pages). Every page was viewed at 110 dpi 1-bit. Colour-file text was compared with `levels/spine.json`: all eight names, all band definitions (A, B, C) and the three look-back prompts of each band match exactly; the stuck routine is present; "In my head" appears nowhere. `levels/spine.json`, `term/l1/lessons/*` and `term/l1/tools/*` were not edited.

## Per audit finding

| Finding | What changed |
|---|---|
| H1 stuck routine missing | Back now has a "When I am stuck" panel with four lines in the exact lesson words (l20.json line 712, l30.json lines 869 and 3391): Wait. / Try a tool. / Try a smaller case. / Ask. On all three cards (it is the same routine at every age). Bullets are dots, not numbers, so they are not mistaken for tool numbers 1 to 8. |
| H2 single-use back | Back is a reusable reference: the intro line, the three prompts for the band exactly as in spine.json (numbered circles, no tick boxes), one real drawing box (A: 48 mm, "Draw or write one word. Use a pencil."; B and C: "I checked by ... Use a pencil.") and the stuck panel. Removed: yes/not-yet boxes, "My tool today", "My name", the "I am still stuck" tick box, the "pass" box (the intro still says "You can pass"). Pencil and rubber work on the box; no laminate (see proof request). |
| H3 ninth tool "In my head" | Card lists eight tools only and says nothing about a ninth. "No tool" is a lesson and Quest Log matter: see the pointer list below. |
| M1 text size | Definitions 12 pt (were 10), tool names 14 pt (12.5), helper lines (subtitle, AGES, intro, drawing-box caption, footer, term tag) 10.5 pt or more. Row text re-flowed to two lines where needed; band C and B definitions still fit. |
| M2 four tools in Term 1 | Tools 1 Spot the pattern, 2 List every way, 3 Draw it, 8 Act it out (the four of Lesson 10, `l10.json` "Our four tools") carry a small "Term 1" tag on card A. All eight remain visible. Cards B and C have no tag (they are not Term 1 cards; the term program is Level 1 only). |
| M3 publisher line | Back, 9 pt: "Math Inquirers. (c) 2026 Preciouslyours Pte Ltd." (c is the real copyright sign). Matches the P2 booklet footer ("(c) 2026 Preciouslyours Pte Ltd.") and cover ("Preciouslyours Pte Ltd, trading as Math Inquirers"). No MOE or SASMO claim, no price, no email, no licence wording. Footer on the front fixed to "Math Inquirers | Inquirer Kit". |
| M4 one name | Both pages say "Toolbox Card" (front title, back subtitle, PDF titles "Toolbox Card A/B/C"). Lessons must follow (below). |
| M5 dotted line | No dotted line remains (replaced by a drawing box with a 0.5 mm solid border). All strokes are 0.3 mm or heavier. |
| M6 soft copy | Not a card change. The colour file is unchanged in layout. The welcome-message advice ("also send the PRINT_BW file, print at 100 percent, both sides, flip on the long edge") needs to be written by whoever owns the welcome message. |
| L1 reading words | Not changed: wording is spine.json (single source). Note for the owner. |
| L2 "pass" | Removed with the box; "You can pass" is in the intro. |
| L3 "which problem" | Not changed: the intro is spine.json wording. |
| L4 icons | Not changed. Icons 1, 2, 7 are the smallest detail; check on the printer proof. |
| L5 metadata | Titles set ("Toolbox Card A" etc., author Math Inquirers) in both files. B&W page box is still 3500 x 4958 px at 600 dpi (148.2 x 209.9 mm): tell the printer 100 percent and trim to A5. |
| L6 name variants | Prose, left as is; the stuck chant now exists on the card in the same words. |

Kept: A5 (148 x 210 mm), margins 9 to 10 mm sides and 8 to 9 mm top/bottom, 2 pages with identical header frames front and back (flip on the long edge), no bleed.

## Not done, and why

- No edit to spine.json, lessons or lesson tools (instructed). B and C wording kept from spine.json: it has band B and C definitions and prompts and the card uses them verbatim. spine.json has no band B/C stuck routine, so all bands use the one routine.
- No "No tool" line on the card (the card must not list a ninth tool).
- No Term 1 tag on B and C.
- No physical proof, no child reading test, no photocopier test (cannot be done here).
- `docs/printing/quote_request.md` not changed: size and stock spec did not change.
- Cut-out pieces are still called "tool cards" in the lessons; the card cannot rename them.
- Check: the 12 pt text is set in Liberation Sans; at 12 pt the C-band back prompts take two lines and still fit.

## Changes OTHER agents must make (do not edit from the card task)

1. "In my head" becomes "No tool":
   - `term/l1/lessons/l20.json` line 3303 (kit page tool list: `["sun", "In my head"]`) and the "7 tool cards" counts at lines 58, 3317 (and L20 objectives/script that say "six tools": the kit page then has six tools plus a "No tool" piece; say six tools and one "No tool" card, or drop the piece).
   - `term/l1/tools/b_quest.py` line 142 (appends `<span class="tp">In my head</span>` to every Tool-I-used row, so L10, L20, L30, L40 Quest Logs), and the text at line 215 ("or In my head") and line 226 ("and In my head").
   - `term/l1/lessons/l10.json` line 1640 and the L20 and L30 quest tutor notes that mention "In my head" (grep `In my head` in `term/l1/lessons`).
   - Then rebuild the four Quest Log PDFs (L10, L20, L30, L40).
   - Lessons 29 and 30 say "7 tool cards" (l29.json lines 1058, 3124; l30.json lines 65, 333, 336, 3828, 3829): count and name should match the one name decision below.
2. One name "Toolbox Card" (cut-outs should be "tool pieces" or "tool cut-outs", not "tool cards"):
   - `term/l1/lessons/l01.json` line 275 says "Toolbox card" (capital C) and the tutor_prep line; `l10.json` line 3641, `l30.json` line 869, `l40.json` lines 28 and 368 say "toolbox card": change to "Toolbox Card".
   - Cut-out pages: `l20.json` lines 58, 69, 162, 293, 1203, 1473, 2632, 3316-3317; `l29.json` lines 1058, 3124; `l30.json` lines 65, 73, 83, 182, 223, 245, 333, 336, 977, 3035, 3084, 3804, 3812, 3828-3829 ("tool cards").
   - `levels/spine.json` `kit_line` "Eight tools: see your Inquirer Kit card": owner/spine owner to change to "Toolbox Card" (and every deck/workbook that reads it).
   - Book 1 contents page and `term/l1/SPINE_TERM_DESIGN.md` line 124 (now out of date: card has Term 1 tags, a reusable back and a stuck chant).
3. Wording that depends on the card back: `l30.json` line 869 says a child "may tick I am still stuck on the look-back page" (workbook page 5, not the card: fine, but do not point children to the card for it). L1 script and tutor prep should say where the card back is used: "keep it open at the Look back side when you check your work".
4. `docs/pedagogy/toolbox_card_notes.md` and `docs/pedagogy/spine_routine_spec.md` section 3 still describe the old back (write-on sheet); update them.
5. Welcome-message / L1 tutor prep: offer PRINT_BW as the soft copy; "print at 100 percent, both sides, flip on the long edge".

## Uncertain

- Whether the owner wants the publisher line to include "trading as Math Inquirers" (used on P2 cover) rather than the footer form used here.
- "Use a pencil." in the drawing box is my short addition for reuse.
- The "Term 1" tag is correct for the Level 1 term program only; for Level 1 holiday children it is harmless.
