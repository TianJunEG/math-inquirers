# Fix pass: Math Inquirers P1 (ages 6-8)

Nothing committed. Shared files (levels/*, rebuild/slidekit.py, diag/build_diag.py, website/*) not edited. Verification: `python3 docs/audit/verify_fixpass_p1.py` prints ALL PASS and DIAG PASS.

## Safeguarding correction applied
No private one-to-one messages anywhere (guide rule "No private messages to children" kept). Invitations are to the whole group ("When you have finished Start here, you can choose Think harder, Go further or the Investigation"). A child who ticks "I am still stuck (my tutor will come and help)" gets a check-in in the open session (quick visit to the shared breakout room or a hand signal, parent nearby). Sneak-peek answers are shown on own paper to the tutor on camera, or everyone holds paper to the camera at once; never boards, never private chat.

## Across all ten lessons
1. Labels: Start here / Think harder / Go further / Investigation. The fast-track box is replaced on page 1 by "After question 3 you may choose: carry on, or try Think harder." Tutor never announces who is on which page; pairs are not split unless both agree. Removed "early finishers", "strong thinkers", "gifted", "Stretch", "Challenge" as page labels from slides, notes, workbook (PDF and Word), guide, parent pack, trial6 and question-bank text (parent_pack_level.py is shared and still has the old line; see below).
2. Warm-up check is now Sneak-peek puzzles (minutes 7-10): Q1 access, Q2 thinking, notes and script say these are ideas not yet learnt, guessing and "I do not know" are welcome, nobody is marked. Timeline in deck, script, guide, workbook: game 0-5, quick questions 5-7, sneak-peek 7-10, explore 10-25, mini-lesson 25-35, break 35-40, worksheet 40-72, talk 72-80, exit 80-88, look-back 88-90.
3. Look-back: 2 minutes, on a page every child reaches ("Choose and look back"). Prompts "Something I did well", "The hardest part was ...", "What helped me" (includes "I asked for help"), "I am still stuck (my tutor will come and help)", pass always allowed. Never collected or read out in front of the group.
4. Talk time: volunteers first, pass allowed, no cold-calling, no tallies or rankings.
5. Investigation printed with an "Easy first step" on the shared third page of every lesson; model answers kept.
6. Go further what-if card on every explore1 slide (nobody waits). Low-child fixes: L6, L8, L1, L5, L10 per the review (see below), with drawn tables, bar tables and a ruler picture, no unicode glyphs.
7. Minute labels added to title, routine, rules and end slides.

## Per lesson
- L1: number strip 0-50 printed in the kit; Q4 and ws2 go up to 30 (answers 10, 20, 30); qbank stretch "up to 50" shared numbers; Go further what-if.
- L2: hint no longer gives the corners away ("For a small total, use small numbers in the corners"); "Think harder:" in core becomes "If you have time:".
- L3: warm-up uses thumbs/hands (no typing); spare page break removed; tally rows shortened.
- L4: Q4 marked "If you have time".
- L5: teaching bar moved before the worksheet with times 40-58; Q3 split into steps with a pre-filled bar table; "Draw the children as circles first."
- L6: cents-only warm-up (3 cent tags), Q2 25c with "there are 4 ways", dollars moved to Think harder T5, ws1/ws2 rebuilt, exit "Show one way to make 30c", qbank "all ways to make 30c" (6 ways).
- L7: exit rebuilt (hexagon, 6 sides and 6 corners); house image and row heights fixed so Q2 stays on page 1.
- L8: grid pre-crossed for Ali/cat and Ali/dog, Q5 and Q6 "If you have time", odd/even boxed strip, no "fewest" competition in the warm-up, T5 riddles.
- L9: column "How far off my guess was"; Q6 ruler picture (hp/ruler_q6.png); Q3b hint shortened.
- L10: card choice ("You may swap with another pair later"); whiteboard round replaces the relay; report-back optional; one-line what-if.

## Diagnostic (diag/content/p1.json only)
Changed: W3 -> "Count in 2s: 2, 4, 6, __, __" (8, 10); M4 -> dot graph (Apples 5, Bananas 3, Grapes 2, answer 3); S1 -> ruler (pencil 2 to 7, answer 5 cm); S2 kept; topics updated. Added fields in the same shape the P2 file uses: childNote, scoring (main six, 4 to 6 join, 2 to 3 chat + taster, 0 to 1 taster first, stretch as a flag), parent (join/support/down/stretchRow/strongBox/gentleBox), tutorKey (header, accept without "$2.05", rushing note, prereq note). Wording has no "failure" and no "one level down". All answers verified in Python (S2 unique, M6 unique, etc.).

### Build changes needed in diag/build_diag.py (not edited)
1. Read `childNote` for the "How it works" card instead of the hard-coded "Read a question aloud if they ask..." text.
2. Read `visual` on a question: `dotgraph` draws one row per [label, count] with filled circles; `ruler` draws a 0-10 cm ruler with a pencil bar from pencilStart to pencilEnd (no mm ticks).
3. Remove the hard-coded "(for example $2.05 and 2.05)"; use `tutorKey.accept`.
4. Move the answer key (page 3) and result page (page 4) into a second PDF "Math_Inquirers_P1_For_The_Tutor.pdf" so the child file has pages 1-2 only; show `tutorKey.header`, `rushing`, `prereq`.
5. Score on the main six: replace the "6 to 8 / 4 or 5 / 0 to 3" table with rows from `scoring.join/support/down` and `parent.join/support/down`, plus `parent.stretchRow`. Score line from `scoring.scoreLine` (warm-up /4, main /6, stretch bonus /2). Remove the warm-up-2-or-less rule.
6. Replace the "Not yet?" box with `parent.gentleBox`; remove the "failure" and "one level down" text for P1 (the `down` variable for P1 must not be used).
7. Replace "Your child has the foundations and will be well challenged" with `parent.join`.
8. Page 2 needs the Brain stretchers intro line from `childNote` (hard on purpose, fine to skip).

## Page counts (before -> after)
- Designed student workbook: 48 -> 58 (exactly +1 page per lesson: the "Choose and look back" page; this is the maximum the brief allows).
- Word student workbook: about 63 -> 61 (LibreOffice render).
- Tutor guide PDF: 72 -> 74.
- Decks: slide counts unchanged per lesson (L5 reordered; L6 and L10 warm-up slides replaced in place).
- Overflow check after restyle: only explore1 slides sit at 933-977 against the 990 footer (acceptable), plus l10-cards and l10-chwalk which already overflowed before this pass.

## Not done / flags
- `hp/parent_pack_level.py` (shared by P2-P6) still says "Challenge is for strong thinkers"; needs a one-line change by whoever owns shared files.
- `hp/deck/data.js` is shared; guide.js uses a local override for warm-up games.
- No "you you" typo was found in the current text.
