# Wording review, Lesson 3 (Digit Cards)

Changes in `lessons/l03.json` (maths and answers unchanged; all `val` fields unchanged). Old -> new, reason.

| # | Where | Old | New | Reason |
|---|---|---|---|---|
| 1 | Whole lesson (workbook, slides, script, online, home, parent) | bigger / biggest | greater / greatest ("Write the greater number", "the greatest number", online "Which number is the greatest?") | Rule 13 |
| 2 | Explore, slides | "Which pile is bigger? ..." / "The pile with more bars is bigger." | "Which pile has more? Which number is greater?" / "The pile with more bars has the greater number." | A pile of bars has more, not "greater" |
| 3 | S1 | "Use both cards to make two numbers." | "Make two numbers with both cards." | Plainer |
| 4 | S3 | "Mei's bars and squares are in the picture. Ben has 4 tens bars and 1 ones square." | "Look at the picture for Mei. Ben has 4 bars and 1 square." | Kit words are "bar" and "square"; "4 tens bars" was odd |
| 5 | S4, E2, T1, T2, G1 | "Make the biggest and the smallest number." | "Use the cards 6 and 2." + (a) "The greatest number is ___" (b) "The smallest number is ___" (T1, G1: "Make the greatest number. Then make the smallest number.") | Two jobs in one sentence |
| 6 | S5, E3, home 2 | "Write these numbers in order. Start with the smallest" | "Arrange these in order. Begin with the smallest number: ..." | School-paper command |
| 7 | S6 | "Ravi says 19 is bigger than 21, because 9 is bigger than 2. Is he right? Write why." | "Ravi says that 19 is greater than 21." (a) "Is Ravi right? Circle Yes or No." (b) "The greater number is ___" | Wrong reasoning removed from the stem; circle Yes/No; no hidden second question |
| 8 | S7 | "bigger than 50 / smaller than 50" | "greater than 50 / smaller than 50" | Rule 13 |
| 9 | S8 | "Siti has 25 stickers. Ravi has 52. Draw bars and squares. Who has more?" | "Siti has 25 stickers. Ravi has 52 stickers. Draw bars and squares in the box." + frame "___ has more stickers." | Numerals with the noun; question is the frame |
| 10 | T2 | "Be careful with the 0." | removed | Hint in the stem |
| 11 | T1, T2 | "Use any two cards. What is the biggest...? What is the smallest?" | "Use two cards to make the greatest number..." with frames | Two questions in one sentence |
| 12 | T3, G3, online items 9, 12 | "Clue 1... Clue 2... Clue 3..." | one paragraph ("I make a 3-digit number with the cards 2, 5 and 8. Each card is used once. My number is greater than 500 and less than 600. ... What number am I?") | Riddle as one paragraph |
| 13 | T4 | "How many different two-digit numbers... Write them all." | "Use two different cards each time. Write all the two-digit numbers you can make." + frame "There are ___ numbers." | Separate jobs; noun after the blank |
| 14 | G1 | "In a 3-digit number like 357, the left card counts the hundreds. ..." | "Use all three cards to make 3-digit numbers." | No teaching inside the question |
| 15 | G2 | "A two-digit number uses two cards. How many different numbers can you make if... And if...?" | "Make two-digit numbers. How many numbers can you make?" + two frames | Shorter; frames carry the two cases |
| 16 | Talk, slide | "Mei says: for the smallest number, put the smallest card on the left. Do you agree?..." | "Is this always right? Put the smallest card on the left to make the smallest number. Try the cards 3 and 8. Then try 0 and 5. Circle Yes or No. I know because ___." | Circle plus one frame |
| 17 | Sneak-peek 2 (and slide, script) | "Who has the bigger number, Ali or Mei? Write the name, and why." | "Who has the greater number? Circle Ali or Mei. I know because ___." | Circle plus one frame |
| 18 | Home 1, 3, 4 | "Which one is bigger?"; "Ben says 38 is bigger than 41, because 8 is more than 1. Is he right? Say why."; "What is the smallest...? And the greatest?" | "Circle the greater number."; "Ben says 38 is greater than 41. Is Ben right? Circle Yes or No. I know because ___."; "Write the smallest and the greatest two-digit numbers." | Rules 13, 18, 19 |
| 19 | Choice slide, menu slide | "Always, sometimes or never?"; "MEI SAYS" | "A pattern to find"; "TALK ABOUT IT" | Matches the investigation |
| 20 | Workbook | S6 answer line removed | page fills 89, 94, 95, 90, 93% | Page count unchanged (5 + 2 kit pages) |

## Not fixed / for the owner
- Rule 25 mismatches (left unchanged): G1, G3 and online items 10, 12 use 3-digit numbers (above P1); T3 and G3 are riddle puzzles with two or three clues (enrichment, kept at Think harder and Go further); numbers up to 99 in start questions and exit tickets.
- Validator copy check blocks reusing wording quoted in docs/books/school_paper_wording_patterns.md. The recommended phrases "Arrange the numbers in order. Begin with the smallest.", "Make the greatest number and the smallest number." and "Is ... correct? Circle Yes or No." fail the check word for word, so close variants are used. The doc may need rewording or the check an exception.
- Home sheet prints `[]` literally; home items use `___` (template: tools/b_print.py).
