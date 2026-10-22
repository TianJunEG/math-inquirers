# Fix pass, Lesson 16 (Skip-Count Tables; Term 2 lesson 6)

Inputs: the three L16 audits, owner decisions, TERM_WIDE_AUDIT, AUTHORING batch 4. Changed: `lessons/l16.json`, `verify/l16_checks.py` (110 checks), `AUDIT_L16.md`, `out/l16/`. Validator 0 FAIL 0 WARN; fills 94/96/97/89/97%; slow class about 82 of 90.

| Finding | Action |
|---|---|
| WB1 / G2 no 0 on the 100 square (M) | The kit page cannot print a zero cell (shared kit code ignores `zero`), so every instruction now says: counter just to the left of the 1, off the square, that is 0 (slide, script, kit intro, materials) |
| WB2 / G7 key one order (M) | S2, S4, E3 keys say the other order is also right; E3 watch-for is now "6 + 5 = 11"; the reading-order sentence moved to page 1 (hint_p1); parent page says either order is fine |
| WB3 / G4 T3 repeats class, T1 untaught (M) | New slide s-m3c "Double it" (2 x 6, 4 x 6) with a reveal answer; T1 now 2 x 5 and 4 x 5; T3 is 50, 27, 65; checks assert no reuse of class numbers; Your turn is 7 x 2, 9 x 2, 2 x 10 (not printed earlier) |
| WB4 / G3 Start here timing (M) | Page slots 8:00 and 7:30, choice time 2:50, waits 30 s in the warm-up cut to five questions; no part OVER in the slow model; S5 kept |
| WB5, WB6 G1 | Key watch-for "16 or 24"; stem "Here are the 4s up to 40. Ring each number..." |
| WB7 Investigation | "Which of 10, 15, 20 and 25 are in both...? Write the last digit of each one you find." |
| WB8 yellow | "Colour the 2s." |
| WB10, WB12, G6 numbering | Shorter header; guide and notes use "Lessons 5 to 8 of Term 2" and "Term 2 Lesson 5"; family pages print Term 2 Lesson N |
| WB9 tick line, WB11 | Not changed: template line under the table; blank band not needed now |
| G1 answers on slides | reveal slides for s-m1, s-m2, s-m3c; s-rem1 shades only up to 18; s-rem2 shows two jumps; s-opt table removed |
| G5, G8 | Greet, notice, then start recording; "so I can see you" |
| G7 talk numbers | Model answer now matches the tested numbers 15, 40, 28, 33 |
| G9, G10 | Ticks only; no colour or star for marking |
| G11 brain break | Tutor counts; children show 5 fingers on every fifth number and clap on every second; slide, script, cue and note match |
| G12 small workbook thumbnails | Not changed: template |
| G13, P-L16-10 hand-off | Goodbye, slide and parent page: next workbook printed (tutor sends it ahead) with its groups mat, counters, plates |
| G14, G15, G16 | Not changed (owner artwork; term line is the plan's Term 2 line; menu is sound) |
| P-L16-1 no pictures online | Not changed: no templated number-line or 100-square figure in the runner; listed below |
| P-L16-2 ordered-list message | Not changed: shared runner; list capped at 30 for the 2s (15 numbers) |
| P-L16-3 numbering | As WB12 |
| P-L16-4 c4 formula | Now `((n%5)+4)//5` (0 only when the last digit is 5 or 0); validator verifies all variants |
| P-L16-5 c2 products to 90 | Variants 2 to 4 only |
| P-L16-7, P-L16-8 | Parent: dots or 24 buttons; do not chant the table |
| P-L16-9 home layout | H4 and H5 use boxes |
| P-L16-6, 11, 12 | Not changed: runner slips for variants, term line, extra t3 template |

Template needs: a zero cell on the kit 100 square (`zero` in `kit_figure`), figures for templated number lines and 100 squares in the runner, a clearer ordered-list message.
