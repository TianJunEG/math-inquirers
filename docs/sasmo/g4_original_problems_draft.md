# Original Go further practice problems for Level 4 (ages 9-11)

**Draft, not yet in the program.** Written for the gaps found in `g4_analysis.md` (one Grade 4 paper, so the evidence is thin; several gap types are also supported by the Grade 2 and Grade 3 papers). Every problem is new: own context, numbers and wording; none is a copy or light rewording of a contest problem. Every answer was worked by hand and then confirmed by a short brute-force script (all candidates tried, answers unique). They have not been tried with children or reviewed by a tutor, so check reading load and difficulty before use. They stay inside the P4 level rules in `p4/SPEC.md` (no percentages, ratio, speed, negative numbers or numbers above 100 000). **One flag for the owner:** the cryptarithm items (section 1) use capital letters that stand for digits, which is not the "algebra letters" the SPEC bans, but you may want to say so on the page.

Ten gap types, three problems each (30 problems). Drawing-only types (the knot and rope item) are not drafted because they cannot be written as text. Items that need a drawing in the program (the spinner, the triangle figure) are given in words so the designer can draw them. Suggested homes use the term-plan lesson numbers (T.L) and the holiday lessons (L1 to L10).

## 1. Letter-digit addition [draft, not yet in the program] (suggested for 2.1 G or 1.1 T, or L2)

In each sum, different letters stand for different digits, the same letter for the same digit, and no number starts with 0.

**1.1** BB + CB = CDA. What is the 3-digit number CDA?
Answer: 106. Solution: two 2-digit numbers add to less than 200, so C = 1; then BB + 1B = 12 x B + 10, which is a 3-digit number with a 1 in front only for B = 8 (B = 9 gives 118, and D would be 1 again), so 88 + 18 = 106.

**1.2** BAC + BCC = ADD. What is the 3-digit number ADD?
Answer: 766. Solution: the ones column must carry (if it does not, A would equal C); working left from there gives A = C - 1 and C = 2 x B + 2, so B = 3 (B = 2 repeats a digit): 378 + 388 = 766.

**1.3** ACA + DDC = BBAB. What is the 4-digit number BBAB?
Answer: 1141. Solution: two 3-digit numbers add to under 2000, so B = 1; the ones column gives A + C = 11, and the tens and hundreds columns then leave only A = 4, C = 7, D = 6: 474 + 667 = 1141.

## 2. Divisibility tests and counting multiples [draft, not yet in the program] (suggested for 1.3 T/G or 2.2 G; first needs a Start here on "digits add to a multiple of 3")

**2.1** Ravi's locker code is a 4-digit number of the form 5 _ 8 _ . The two missing digits are the same, and the code can be divided exactly by 6. What is the code?
Answer: 5484. Solution: it must be even and in the 3 table; the digit sum is 13 + 2 x (missing digit), and the missing digit has to be even, so it is 4 (digit sum 21); the other even digits (0, 2, 6, 8) give sums 13, 17, 25, 29.

**2.2** Mei has the digit cards 1, 2, 3 and 5. She makes every 3-digit number she can using three different cards. How many of her numbers can be divided exactly by 3?
Answer: 12. Solution: a number is in the 3 table when its digits add to a multiple of 3; 1 + 2 + 3 = 6 and 1 + 3 + 5 = 9 work, the other two sets of three give 8 and 10; each good set can be arranged in 6 ways, 6 + 6 = 12.

**2.3** How many whole numbers from 100 to 200 can be divided exactly by 6 but not by 4?
Answer: 9. Solution: the multiples of 6 from 102 to 198 are 17 numbers; the multiples of 12 among them (108 to 192) are 8 numbers; 17 - 8 = 9.

## 3. Sums by pairing [draft, not yet in the program] (suggested for 1.2 T or 4.3 T, not only G)

**3.1** Find 21 + 23 + 25 + ... + 37 + 39 (every odd number from 21 to 39).
Answer: 300. Solution: 10 numbers; the first and last add to 60, and so do the second and second-to-last; 5 pairs of 60 is 300.

**3.2** On day 1 Ali reads 3 pages of a book. On each next day he reads 2 more pages than the day before. He does this for 12 days. How many pages has he read altogether?
Answer: 168. Solution: the pages are 3, 5, 7, ..., 25; pair the first and last (28), 6 pairs of 28 is 168.

**3.3** Find 2 3/8 + 3 1/5 + 4 5/8 + 5 4/5 + 6 1/4 + 7 3/4.
Answer: 30. Solution: the whole numbers add to 27; the fractions pair up into three wholes (3/8 + 5/8, 1/5 + 4/5, 1/4 + 3/4), so 27 + 3 = 30.

## 4. Chance and possible totals [draft, not yet in the program] (suggested as a short routine inside 4.5 or 1.9; the SPEC lists no probability, so this is extension)

**4.1** A fair spinner has 12 equal sectors numbered 1 to 12. Put these five events in order from least likely to most likely: (a) an even number, (b) a multiple of 3, (c) a prime number, (d) a number bigger than 7, (e) a number that is not a multiple of 4.
Answer: (b), then (c) and (d) equally likely, then (a), then (e). Solution: the numbers of sectors are 4, 5, 5, 6 and 9.

**4.2** Ben has five dice, each numbered 1 to 6. He rolls them all and adds the numbers on top. (a) What are the smallest and the largest total he can get? (b) How many different totals are possible?
Answer: (a) 5 and 30. (b) 26. Solution: every whole number from 5 to 30 can be made (move one die at a time), so 30 - 5 + 1 = 26.

**4.3** A red die and a blue die are rolled together. In how many of the 36 equally likely results is the total a multiple of 4?
Answer: 9. Solution: total 4 can be made 3 ways, total 8 can be made 5 ways, total 12 one way; 3 + 5 + 1 = 9.

## 5. Timetables and weekdays [draft, not yet in the program] (suggested for 3.8 T)

**5.1** A children's theatre has two shows. The Puppet Show lasts 75 minutes and starts at 10:00, 11:30, 13:15 and 15:00. The Magic Show lasts 50 minutes and starts at 10:20, 12:10, 14:05 and 15:40. A class arrives at 10:30 and watches both shows, one after the other, with no walking time. What is the earliest time they can finish?
Answer: 14:30. Solution: Magic first gives 12:10 to 13:00 and then Puppet 13:15 to 14:30; Puppet first gives 11:30 to 12:45 and then Magic 14:05 to 14:55.

**5.2** Four days after the day before yesterday is Thursday. What day of the week will it be 50 days from today?
Answer: Wednesday. Solution: the day before yesterday plus 4 is today plus 2, so today is Tuesday; 50 = 7 x 7 + 1, so 50 days on is one day later than Tuesday.

**5.3** Mei must visit the library and the pool today, in either order. She starts at the library door at 9:00. The library takes 40 minutes (it is open until 12:00). The pool is a 15-minute walk away and has 60-minute sessions that start at 9:30, 10:45 and 12:00. Walking back takes 15 minutes too. What is the earliest time she can finish both?
Answer: 11:25. Solution: pool first means a 9:15 arrival, the 9:30 session to 10:30, the walk back to 10:45 and the library to 11:25; library first would end at 11:45 after waiting for the 10:45 session.

## 6. Best buy per unit [draft, not yet in the program] (suggested for 2.7 T)

**6.1** Which pack of pens is the best buy: A, 8 pens for $6; B, 12 pens for $8; C, 20 pens for $15; D, 5 pens for $4?
Answer: B. Solution: the cost of one pen is 3/4, 2/3, 3/4 and 4/5 of a dollar; in twelfths of a dollar that is 9, 8, 9 and 9 3/5, so B is smallest.

**6.2** Siti compares three rolls of ribbon: 6 m for $9, 4 m for $5.20 and 10 m for $14.50. Which roll is cheapest per metre, and what is the cost of one metre of it?
Answer: the 4 m roll, $1.30 a metre. Solution: $9 / 6 = $1.50, $5.20 / 4 = $1.30, $14.50 / 10 = $1.45.

**6.3** A baker sells buns in packs of 3 for $2.40 and packs of 5 for $3.75. Ali wants exactly 15 buns and buys only whole packs. What is the cheapest way, and what does he pay?
Answer: three packs of 5, $11.25. Solution: the only ways to make 15 are five packs of 3 ($12.00) or three packs of 5 ($11.25).

## 7. Digit products and digit clues [draft, not yet in the program] (suggested for 1.1 G)

**7.1** What is the largest 3-digit number whose digits multiply to 40?
Answer: 851. Solution: only two sets of three digits multiply to 40, {1, 5, 8} and {2, 4, 5}; the largest number from them starts with 8 and then 5, 1.

**7.2** What is the smallest 4-digit number whose digits multiply to 360?
Answer: 1589. Solution: try a first digit of 1; the other three digits must multiply to 360, and 5, 8, 9 is the only set of single digits that does (360 = 5 x 72 and 72 = 8 x 9), so the smallest arrangement is 1589.

**7.3** Three 2-digit numbers use the digits 1, 2, 3, 4, 5 and 6 once each. The digits of the biggest number add up to 7. In the middle number the tens digit is 3 more than the ones digit. Exactly two of the three numbers are odd. Find all three numbers.
Answer: 43, 52 and 61. Solution: the biggest has digits adding to 7, and the middle one is 41, 52 or 63; trying each against the three clues leaves only 43, 52, 61.

## 8. Balance-scale chains [draft, not yet in the program] (suggested for 4.7 T)

**8.1** A coconut balances a papaya and a kiwi. A durian and a kiwi balance two papayas. Two coconuts balance five kiwis. Put the four fruits in order from heaviest to lightest.
Answer: coconut, durian, papaya, kiwi. Solution: call a kiwi 2 units; two coconuts are 10 units so a coconut is 5; a papaya is 5 - 2 = 3; a durian is 2 x 3 - 2 = 4.

**8.2** Three apples balance two pears. Four pears balance three mangoes. How many apples balance six mangoes?
Answer: 12. Solution: four pears are the same as six apples, so three mangoes are six apples and one mango is two apples; six mangoes are 12 apples.

**8.3** Two melons balance three pineapples. A pineapple and a melon together have a mass of 2 1/2 kg. What is the mass of one pineapple, and of one melon?
Answer: pineapple 1 kg, melon 1 1/2 kg. Solution: six pineapples balance four melons, so a melon is 3 halves of a pineapple; together they are 5 halves of a pineapple, which is 2 1/2 kg, so a pineapple is 1 kg.

## 9. Growing gaps and rules found from diagrams [draft, not yet in the program] (suggested for 4.3 S and T)

**9.1** The numbers 5, 6, 8, 11, 15, 20, ... follow a pattern. What is the 10th number?
Answer: 50. Solution: the gaps are 1, 2, 3, 4, 5 and keep growing by 1, so the next numbers are 26, 33, 41, 50.

**9.2** The numbers 3, 4, 6, 10, 18, ... follow a pattern where each gap is twice the gap before. What is the 8th number?
Answer: 130. Solution: the gaps are 1, 2, 4, 8, 16, 32, 64, which add to 127; 3 + 127 = 130.

**9.3** Four boxes each have a left number, a right number and a top number. (left 3, right 2, top 13), (left 5, right 1, top 27), (left 4, right 6, top 28), (left 2, right 4, top 12). The same rule works for all four. What is the top number when the left number is 6 and the right number is 5?
Answer: 46. Solution: the rule is left times left plus 2 times the right number (9 + 4, 25 + 2, 16 + 12, 4 + 8); 36 + 10 = 46.

## 10. Counting without listing [draft, not yet in the program] (suggested for 4.5 T, 3.1 or 3.9 for triangles)

**10.1** A big triangle has 4 straight lines drawn from its top corner to the bottom side, so the bottom side is cut into 5 parts. How many triangles are there in the picture (of any size)?
Answer: 15. Solution: every triangle uses the top corner and two of the 6 points on the bottom side (including the two bottom corners), and 6 x 5 / 2 = 15.

**10.2** Ravi has 3 shirts (red, blue, green), 4 pairs of shorts (navy, grey, black, white) and 2 caps. He wears one of each, but never the red shirt with the navy shorts. How many different outfits can he make?
Answer: 22. Solution: 3 x 4 x 2 = 24, and the red shirt with navy shorts is 2 of those (one for each cap); 24 - 2 = 22.

**10.3** A date such as 05/09 is written with four digits (day then month). In the 365 days of 2021, how many dates have no digit 1 in their four-digit form?
Answer: 142. Solution: the month must be one of 02 to 09; the days with no 1 are 2 to 9, 20, 22 to 29 and 30 (18 days, but February stops at 28 so it has 16); seven months with 18 days plus February with 16 is 126 + 16 = 142.
