# Toolbox Card A (ages 6-8): independent audit

23 Oct 2026. Branch `claude/great-fermi-1hv4vc`. Nothing was edited except this report; nothing pushed.

Audited: `outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_PRINT_BW.pdf` and `..._SCREEN_colour.pdf` (Cards B and C read only for spine consistency). Method: pages rendered at 110, 150, 300 and 600 dpi and viewed; B&W file is a 1-bit 600 dpi image PDF (no text layer), so its wording was checked by eye and by overlaying it on the colour file; colour-file text was extracted and compared string by string with `levels/spine.json`. Lessons 1-40 JSON, `spine_term.json`, Quest Log PDFs (L10-L40) and Book 1 contents page were searched for tool names.

## Verdict: NOT print-ready as it stands

The front side is accurate, legible and matches `spine.json` exactly. The card should not go to the printer (order Fri 6 Nov) until the three Highs are decided, because they change the artwork. All fixes are small layout or wording edits in `print/make_toolbox_card.py`, and one wording line in a few lessons. No technical print fault (size, margins, 1-bit, registration) blocks it.

## What passed

- Page size 420 x 594.96 pt (148.2 x 209.9 mm: A5 within 0.3 mm), 2 pages, portrait both sides, flip on the long edge. Front and back header frames sit at the same position (top ink 39 px at 110 dpi on both pages), so duplex show-through lines up.
- Margins: ink starts 10.2 mm from left and right, 9.0 mm from top, 8.1 mm from bottom. Nothing runs to the edge, so no bleed is needed and a +-1 mm trim is safe.
- B&W file: 1-bit CCITT, 600 dpi, only black and white. No grey. All strokes 0.3 mm or heavier except the dotted line (see M5).
- All 8 names and all 8 band-A definitions match `levels/spine.json` character for character. The three look-back prompts, the intro line, "I am still stuck (my tutor will come)" and "pass" match too. Cards B and C also match spine.json (names, band definitions, prompts), and all three cards use the same names in the same order.
- Colour and B&W say the same thing (same HTML, one CSS variable swap: yellow header and pale icon discs become white). Overlay of colour dark pixels on B&W ink: 82% and 86% (the rest is anti-aliasing and heavier 1-bit strokes). No colour-only cue.
- Icons are stroke-only, 11.5 mm in a 15 mm ring, all eight legible at 1-bit 300 and 600 dpi and at 110 dpi screen size.
- No MOE, GEP or SASMO claim, no price, no outcome promise, no calculator. No Mi on the card (as the spec says: new elements carry no Mi), so there is no mascot-rule breach. Font is Liberation Sans (open licence).
- Spec wording rules for 6-8 year olds: sentences 4 to 10 words, no jargon beyond the words below.

## Highs

**H1. The stuck routine is missing from the card, but two lessons say it is on the card.**
Lesson 30 slide 18 note: "The stuck routine, in the same words as the toolbox card: Wait. Try a tool. Try a smaller case. Ask." Lesson 20 (slide and script) and Lesson 30 (script) teach the same four-line chant. `docs/pedagogy/term_review.md` line 141 proposed adding it to the toolbox card. The card (front or back) carries no such line; the only stuck item is the tick box "I am still stuck". A tutor who points children to the card finds nothing.
Fix: add the four-line chant to the card in the 6-8 words as written (for example under the eight rows or at the head of the back), or change the two L30/L20 notes to drop "same words as the toolbox card". Adding it is better: it is the persistence outcome of the spine.

**H2. The back is a single-use write-on sheet that no lesson mentions, which is a poor fit for a durable kit item.**
- Back = "Look back" for one problem (tick, tick, one word), "My tool today" line, name line. It can be filled in once. The card is meant to sit on the table for all 40 lessons ("Keep it where you do your maths and point to it in class", Book 1 contents page).
- The routine it duplicates already lives on page 5 of every lesson workbook ("Children fill in the look-back box on page 5", L1 script). No lesson script, tutor guide line or parent page tells the child or tutor to use the card back (searched all 40 lessons: card references are only L1 script and tutor prep, L30 slide note, L40 slide and script, all about the front).
- Q3 says "Draw or write one word" but gives one thin dotted line about 12 mm high. A child cannot draw in it. About 26 mm of the page above "My tool today" is blank (between the Q3 box and the tool box).
- "My tool today" asks a 6-year-old to write a tool name such as "Try something simpler" (21 letters). The workbook look-back and the Quest log use circle or tick instead (and spec section 3 said "Tool I used: eight small icons with tick boxes"). The front already numbers the tools 1 to 8.
- "I am still stuck (my tutor will come)": on a loose card nobody collects, the box does nothing. In the lessons, the route is a tick on the workbook look-back page which the grown-up photographs and sends (L1 STUCK note). A box on the card promises help that cannot reach the tutor.
Fix (recommended): make the back a reusable reference, not a form. Keep the three look-back questions as a checklist to read (no boxes or lines), add the stuck chant from H1, drop the name line or move it to a small corner, and drop "My tool today" and the stuck tick. If the owner wants to keep a write-on back, then say in one line in every lesson script when it is used, give Q3 a real drawing box (use the blank 26 mm), replace "My tool today" with a row of eight number circles to ring, and print on uncoated stock so pencil takes.

**H3. A ninth tool, "In my head", exists in the lessons and Quest logs but not on the card or in spine.json.**
- Lesson 20 kit page: "7 tool cards" (Draw it, Act it out, Spot the pattern, List every way, Make a table, Work backwards, **In my head** with a sun icon) while the same lesson says "six tools" in objectives, parent summary and script. `RETROFIT_REPORT.md` line 32 records this as "kept".
- Every Quest Log (L10, L20, L30, L40) adds "In my head" at the end of the "Tool I used" row under each gate (`term/l1/tools/b_quest.py` line 142 appends it to every row). L40 therefore shows 8 card tools plus a ninth non-card option.
- Neither the card, `levels/spine.json` nor the toolbox says "In my head", and the tool is not taught anywhere. The owner's rule is a single source for the eight names.
Fix: owner decision. Either (a) keep it as a fixed catch-all, rename it so it is clearly not a ninth tool (for example "No tool" or "Just knew it"), put the same word on L20 kit cards, Quest rows and the card's tool pointer, and make L20 say seven; or (b) remove it everywhere so the row shows exactly the card's tools met so far. Do not print the card before deciding, because option (a) may want one line on the card.

## Mediums

**M1. Text size is small for ages 6-8.** Definitions are 10 pt, tool names 12.5 pt, intro and "yes / not yet" 11 pt, "Draw or write one word" 8.5 pt, stuck line 9.5 pt, footer 8.5 pt, number circles 8.5 pt, "AGES" 9 pt. Early-reader guidance is usually 12 pt or more (14 pt for the youngest) with generous leading. Rows are about 20 mm tall and the longest definition is 10 words, so there is room. Fix: definitions 12 pt (two lines where needed), names 14 pt, helper text not below 10 pt, "pass"/stuck line 11 pt.

**M2. The card shows all eight tools from day one but Term 1 teaches four.** Lesson 10 (Book 2): "Our four tools: Draw it, Act it out, Spot the pattern, List every way", while the child's card lists eight. `term_review.md` line 99 and 104 designed the toolbox card to "show only the tools introduced so far". CARD-BOOK1 ships one eight-tool card with Book 1 and the Book 1 contents page calls it "the tools we use all year". Not wrong, but a child will ask why four are missing from lesson 10. Fix: one line in L1 and L10 scripts ("You will meet the other four later"), or a small corner mark on the card next to tools 3, 8, 1 and 2 ("Term 1") if space allows. Note the numbering follows the spine order, not the order met (Draw it, Act it out, Spot the pattern, List every way = 3, 8, 1, 2), so "Today's tool is 3" is not how any lesson speaks; names only, which is fine.

**M3. No publisher or copyright line on the card.** The only footer is "Math Inquirers Inquirer Kit" (reads as a repeated word; likely meant "Math Inquirers | Inquirer Kit"). Owner approved the line "Preciouslyours Pte Ltd, trading as Math Inquirers" (PUBLISHER-OK). The extension book licence page uses "(c) 2026 Preciouslyours Pte Ltd (UEN 201507566K), trading as Math Inquirers. All rights reserved." Fix: footer "Math Inquirers | Inquirer Kit" and a second line "(c) 2026 Preciouslyours Pte Ltd, trading as Math Inquirers" at 8 pt or more on the back (or front). Leave out a contact email (the temporary pypteltd@gmail.com is to be replaced) and any licence wording (still a lawyer draft).

**M4. Card name differs from how lessons call it.** The front says "My Toolbox". Book 1 says "Toolbox Card", lessons 1 and 40 say "Toolbox card", `spine.json` `kit_line` says "your Inquirer Kit card", and lessons 20, 30 and 39 use "tool cards" for the cut-out pieces in the workbook kit page ("Lay your 7 tool cards in a row"). A child has two different things both called tool cards or toolbox card. Fix: one name. Suggest the front title "My Toolbox card" (and the cut-outs "tool pieces" or "tool cut-outs"), and align `kit_line`/`kit_note`.

**M5. Dotted writing line is fine-dotted and thin (about 0.45 mm).** In the 1-bit render the line breaks into near-continuous specks; on a worn photocopier or a laser at low toner it can vanish. It is the only mark under 0.5 pt that the file has. Fix: use a solid 0.35 mm line (like "My tool today") or dashes at least 1 mm long.

**M6. Soft-copy fallback prints badly on a home mono printer and is not designed for it.** L1 tutor prep: "or send the colour PDF with the welcome message". The colour file prints a yellow header and pale disc fills (mid-grey and light grey on mono), A5 page size (many home printers default to A4 "fit", which scales it), and back-to-back printing needs flip on the long edge. Fix: also offer the PRINT_BW PDF (it is already safe on any mono printer), and add "print at 100%, both sides, flip on long edge" to the welcome message (this line is not on the card or in the lessons).

## Lows

- L1. Reading and word choice (ages 6-8): "so none is missed" (none, missed passive), "rows and columns" (columns is new before Term 2), "undo", "grows", "test it", "counters". "Try it with smaller numbers first": "it" is unclear. "Nobody reads it out": "it" is unclear; "Nobody reads yours out" is clearer. These are spine.json wording (single source), so edits must be made there and then in all decks and workbooks; the owner can leave them, since tutors read them aloud in Lesson 1 and say "Say it with me".
- L2. Bottom-row boxes "I am still stuck (my tutor will come)" and "pass": "pass" alone, with no verb, sits far from the intro line "You can pass". Fix: "I pass" or "pass (skip)" or put "You can pass" next to it.
- L3. Intro "Pick one problem from today" does not say which one (the spec said the last or hardest). Add "the last one, or the hardest".
- L4. Icon 2 (List every way) is drawn as a 3x3 block of small squares and dots. The spec said three ruled lines with tick boxes; the picture reads as a dot grid. Still legible and distinct from icon 4, but icon 4 (table) and icon 2 (dot grid) look related at a glance. Icon 1's shapes are about 2.4 mm, the smallest detail on the card; icon 7's small grid about 3.5 mm. All readable at 600 dpi 1-bit; confirm on the printer proof.
- L5. Colour PDF metadata title is "Toolbox card A"; B&W file title is the file name. Set a proper title and author. B&W PDF page boxes are 148.17 x 209.9 mm (from the 3500 x 4958 px image at 600 dpi), not exactly 148 x 210; tell the printer to print at 100% and trim to A5.
- L6. Minor name-variant uses in lessons (descriptive, not tool labels): "go backwards" (L6, L10), "working backwards" (L20, L24, L39, L40), "make a list" (L20, L36), "list all the ways" (L15, L17), "smaller case" (L20, L30: stuck chant; the card says "smaller numbers"/"Try something simpler"), "acting it out" (L20, L30, L39), "guess-and-check" (L39), "draw a picture" (many). Left as is is fine for prose; the stuck chant "Try a smaller case" should be the same words as the card's tool 7 (see H1).
- L7. Card header reads "AGES 6-8" with a hyphen; elsewhere "ages 6-8" matches, so no change needed.
- L8. Hand-solving examples: the card has no worked examples and no maths content, so there was nothing to hand-solve and no arithmetic to verify. A one-word example per tool (for example "Draw it: draw a bar") is optional; not recommended on an A5 card at 12 pt.

## Strategy table (card A)

Lesson usage: "main" and "also" from `term/l1/spine_term.json` (the tool-of-the-day chip on each workbook page 1; names are generated from `spine.json`, so they match); "named in text" = lessons whose JSON mentions the exact card name. Example on card: none for any tool (see L8). Quest rows show the card names in spine order plus the extra "In my head" (H3).

| # | Name on card | One-line description on card | Example on card | Matches spine.json (name and band A line) | Lessons where it is the main tool | Lessons where it is "also" | Lessons whose text names it (exact card name) |
|---|---|---|---|---|---|---|---|
| 1 | Spot the pattern | Look for what repeats or grows. | none | Yes | 4, 6, 16, 21, 27, 35 | 14, 22, 28 | 4, 6, 10, 16, 20, 21, 27, 30, 35, 39, 40 |
| 2 | List every way | Write each way down, in order, so none is missed. | none | Yes | 3, 24, 26, 33 | 15, 17, 36 | 3, 10, 20, 24, 26, 30, 33, 39, 40 |
| 3 | Draw it | Draw a picture or a bar of what the story says. | none | Yes | 2, 7, 9, 12, 18, 19, 22, 31 | 1, 5, 6, 8, 11, 15, 23, 25, 32, 34, 38 | 1, 2, 4, 6, 7, 9, 10, 12, 15, 17-22, 28, 30-32, 34, 37-40 |
| 4 | Make a table | Put what you know in rows and columns. | none | Yes | 15, 28, 32, 37 | 19, 26, 36 | 15, 20, 27, 28, 30, 32, 37, 39, 40 |
| 5 | Work backwards | Start at the end and undo each step. | none | Yes | 13, 23, 29, 38 | 12, 18, 24, 28, 31, 37 | 7, 10, 13, 20, 23-25, 28-31, 37-40 |
| 6 | Guess and check | Pick a number, test it, then try a better one. | none | Yes | 25 | 24 | 25, 26, 30, 39, 40 |
| 7 | Try something simpler | Try it with smaller numbers first. | none | Yes | 36 | 33 | 30, 36, 39, 40 |
| 8 | Act it out | Use counters, paper or people to show it. | none | Yes | 1, 5, 8, 11, 14, 17, 34 | 2, 3, 4, 7, 9, 13, 16, 21, 27, 35 | 1, 5, 8, 10, 11, 12, 14, 17, 20, 27, 30, 34, 39, 40 |
| - | "In my head" (NOT on card, NOT in spine.json) | none | none | **Not in spine.json** | none | none | Quest Log tool rows L10, L20, L30, L40; L20 kit page (7th tool card, sun icon); L20 and L30 quest tutor notes |
| - | Choose the tool (lessons 10, 20, 30, 39, 40) | n/a | n/a | n/a | 10, 20, 30, 39, 40 | | L10 "four tools" (Draw it, Act it out, Spot the pattern, List every way: all four on card); L20 "six tools"; L30 "seven tools"; L39 and L40 "eight tools" (all names on card, exactly) |

Checks behind the table: every `main` and `also` id in `spine_term.json` is one of the eight spine ids (no stray ids); every one belongs to its term's tool set (`tools_met`); Quest Log rows (all four terms) use the exact card names; the Level 1 workbook chip text ("Use counters, paper or people to show it. Also useful: Draw it") equals the card line. Count: 40 lessons, 35 with a main tool, 5 choose lessons (10, 20, 30, 39, 40). Lesson 10 names four tools, L20 six, L30 seven, L39 and L40 all eight.

## Printer proof (what to ask for)

From `docs/printing/quote_request.md` (section "Inquirer Kit: A5 strategy toolbox card"): A5 148 x 210 mm, 2 pages per file (page 1 front, page 2 back), double-sided, flip on the long edge, no bleed, no crop marks, B&W 1-bit 600 dpi, 1 card per child per Book 1 issue (the note says one per workbook issued; CARD-BOOK1 says once, with Book 1) plus about 10 percent spare. Stock options given: 250 gsm card (preferred, handled every lesson), 170 gsm silk or uncoated, optional matt lamination; quote per 50, 100 and 250.

To add to the printer message:
1. Physical proof of the final artwork (not a screen proof) on the real stock, printed 100% (no fit to page), both sides, before the 6 Nov order. Check: the dotted line, the smallest icon details (icons 1, 2, 7), the 0.3 mm row rules, small text, and that front and back registration stays within about 1 mm.
2. Stock: 250 gsm uncoated or matt-coated (pencil must take; no gloss). If matt lamination is quoted, note that a laminated back cannot be pencilled; either print the back as reference only (see H2) or quote a matt varnish or aqueous coat instead.
3. Finishing: trim to A5 148 x 210 mm (tolerance +-1 mm); corners rounded 3 mm radius (child-safe, harder to dog-ear); a quote for a plain cut and for a rounded corner.
4. The envelope: A5 flat, with Book 1, loose (not stapled or glued into the book).
5. Machine: confirm the printer accepts the 1-bit CCITT PDF and does not recompress it; ask for a mono duplex print with no screening on the 1-bit file.
6. Durability for a child: 250 gsm minimum, matt finish, rounded corners; consider a wipe-clean laminate only if the back is made reference-only; a spare card per child, since the card is handled every lesson for a year (or the colour soft copy as the replacement).

## What I could not check

- No physical print: I did not see the card on paper, at 100%, at 600 dpi, through a photocopier, or with a child's hand and pencil. 1-bit appearance was judged from 300 and 600 dpi renders.
- No child reading test (reading load judged by word count and word difficulty only). No test with real 6 to 8 year olds of icon recognition, "Draw or write one word" or the yes / not yet boxes.
- The B&W file has no text layer (image only), and there is no OCR on this machine (no `tesseract`), so its wording was checked by eye and by overlaying it on the colour file, not by text extraction. Cards B and C were checked by colour-file text only.
- Similarity: I searched the private source text we hold (`docs/books/private_*`, `docs/sasmo/private_*`, which hold notes and extraction scripts only) for the card's definitions and found none; the eight strategy names appear in them only as ordinary words (Draw it, Work backwards, Guess and check, Make a table, List every way). I could not check the source paper PDFs themselves or any published textbook, so I cannot say the eight generic strategy names are unused elsewhere (they are standard heuristics names, short common phrases, and not protectable on their own). The icons are in-house SVGs (`levels/spine_icons/*.svg`); I saw no sign of copied art, but I did not run an image search against published icon sets.
- I did not check the font licence beyond the family name (Liberation Sans, an open licence) or the printer's colour of the stock.
- Lesson 1 to 40 searches were text-pattern searches of the JSON: a card name written in an unusual spelling or in a picture-only slide would be missed. Slide images and the deck PDFs were not read; the tutor guide and workbook builds were read through their JSON, not as rendered files (only Book 1's colour print was opened).
- Mi usage: I checked the card (no Mi) against the owner decisions I could find (small, few slides, no numbers in speech, no calculator, none on new elements); I did not find a separate `mascot/` rules document, only the pose files.
- I could not confirm whether the owner intends one card per child per Book 1 (CARD-BOOK1) or per workbook (quote request); the two documents differ slightly.
