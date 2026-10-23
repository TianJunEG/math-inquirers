"""Level 6 Unit 8: Secret codes (clock arithmetic, mod, Caesar codes).  Follows holiday lesson 8."""
from lib import *

U = 'L6U08'
I = []
X = '×'
M = '−'
LET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def alpha():
    """the letter table: A = 0 ... Z = 25, in two blocks of 13"""
    rows = []
    for a in (0, 13):
        rows.append([{'t': LET[k], 'shade': True} for k in range(a, a + 13)])
        rows.append([str(k) for k in range(a, a + 13)])
    return {'type': 'l6_grid', 'rows': rows, 'cw': [9] * 13, 'ch': 8, 'fs': 16}


learn = {
    'intro': 'On a clock, counting past 12 goes back to 1. n mod m is the remainder when n is divided by m. '
             'A Caesar code moves every letter along the alphabet: number the letters A = 0 to Z = 25, add the shift, then take mod 26.',
    'example': {
        'problem': 'Code the word ZIP with a shift of 7.',
        'figure': alpha(),
        'steps': ['Letter numbers: Z = 25, I = 8, P = 15.',
                  'Add the shift 7 to each: 32, 15 and 22.',
                  f'Take mod 26: 32 {M} 26 = 6. The numbers are 6, 15 and 22.',
                  'Back to letters: 6 = G, 15 = P, 22 = W.'],
        'answer': 'ZIP becomes GPW.'},
    'howto': {'title': 'How to code and decode',
              'steps': ['Write the letter numbers, A = 0 to Z = 25.',
                        f'To code, add the shift. If the total is 26 or more, take away 26.',
                        f'To decode, take away the shift. If the total is below 0, add 26.',
                        'Change the numbers back into letters.']},
    'try': IT(U, 'L', 1, 0, 'Code the word JAB with a shift of 12. {l}',
              'J = 9, A = 0 and B = 1. Adding 12 gives 21, 12 and 13. 21 = V, 12 = M and 13 = N. The code is VMN.',
              answer=A(['VMN'], 'VMN')),
}

# ---------------------------------------------------------------- Start here
I.append(IT(U, 'S', 1, 1,
            'The clock shows 8 o\'clock now. A clock goes back to 1 after 12.',
            f'(a) 8 + 7 = 15, and 15 {M} 12 = 3. (b) 5 {M} 9 = {M}4, and {M}4 + 12 = 8. (c) 7 + 50 = 57. 57 {M} 48 = 9 (4 full turns of 12 are 48), so it is 9 o\'clock.',
            fig={'type': 'l6_clock', 'hand': 8, 'r': 21},
            parts=[P('a', 'In 7 hours it will be {b} o\'clock.', [3]),
                   P('b', 'It is 5 o\'clock. 9 hours earlier the clock showed {b}.', [8]),
                   P('c', 'At 7 o\'clock, 50 hours later it is {b} o\'clock.', [9])],
            figside=True))
I.append(IT(U, 'S', 2, 1,
            'n mod m means: divide n by m and keep the remainder. Find each one.',
            '38 = 5 × 7 + 3, so 3. 100 = 8 × 12 + 4, so 4. 59 = 2 × 26 + 7, so 7. 500 = 19 × 26 + 6, so 6.',
            parts=[P('a', '38 mod 7 = {b}', [3]),
                   P('b', '100 mod 12 = {b}', [4]),
                   P('c', '59 mod 26 = {b}', [7]),
                   P('d', '500 mod 26 = {b}', [6])],
            partsrow=True, space={'rows': ['Working:']}))
I.append(IT(U, 'S', 3, 1,
            'Today is Thursday. A week is a clock with 7 days.',
            '40 mod 7 = 5. Thursday and 5 more days: Fri, Sat, Sun, Mon, Tue. 100 mod 7 = 2, so Thursday + 2 is Saturday. '
            '20 mod 7 = 6. Back 6 days from Thursday: Wed, Tue, Mon, Sun, Sat, Fri.',
            fig=grid([['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']], [19] * 7, ch=9),
            parts=[P('a', '40 days later it is {l}', ['Tuesday']),
                   P('b', '100 days later it is {l}', ['Saturday']),
                   P('c', '20 days ago it was {l}', ['Friday'])]))
I.append(IT(U, 'S', 4, 2,
            'Use the letter table to code each word. Add the shift to every letter number.',
            f'HELP: 7, 4, 11, 15 plus 3 is 10, 7, 14, 18, which is KHOS. MAZE: 12, 0, 25, 4 plus 5 is 17, 5, 30, 9. 30 {M} 26 = 4, so the numbers 17, 5, 4, 9 are RFEJ.',
            fig=alpha(),
            parts=[P('a', 'HELP with a shift of 3: {l}', ['KHOS']),
                   P('b', 'MAZE with a shift of 5: {l}', ['RFEJ'])]))
I.append(IT(U, 'S', 5, 2,
            'Decode each word. Take the shift away from every letter number. If a number is below 0, add 26.',
            f'FXAT: 5, 23, 0, 19 minus 9 is {M}4, 14, {M}9, 10. Adding 26 to the negatives gives 22, 14, 17, 10, which is WORK. '
            f'YNZC: 24, 13, 25, 2 minus 13 is 11, 0, 12, {M}11. Adding 26 gives 11, 0, 12, 15, which is LAMP.',
            fig=alpha(),
            parts=[P('a', 'FXAT, shift 9: {l}', ['WORK']),
                   P('b', 'YNZC, shift 13: {l}', ['LAMP'])]))
I.append(IT(U, 'S', 6, 2,
            'This code changes the number of one letter. Predict what the sprite says.',
            f'X is 23, and 23 + 9 = 32. 32 mod 26 = 6, and 6 is G. For letter 17: 17 + 9 = 26, and 26 mod 26 = 0, which is A.',
            fig=code([['var', 'set letter to (23)'], ['var', 'set shift to (9)'], ['var', 'set total to (letter + shift)'], ['var', 'set out to (total mod 26)'], ['look', 'say (out)']]),
            parts=[P('a', 'It says {b}.', [6]),
                   P('b', 'The code letter is {b}.', ['G']),
                   P('c', 'With letter 17, it says {b}.', [0])],
            figside=True))
I.append(IT(U, 'S', 7, 2,
            'The word THE was coded as AOL. Then the next word, XBPJR, was coded with the same shift.',
            f'T = 19 and A = 0, so the shift took 19 to 26, which is 0: the shift is 7. Decode XBPJR: 23, 1, 15, 9, 17 minus 7 is 16, {M}6, 8, 2, 10. '
            f'Adding 26 to {M}6 gives 20. The numbers 16, 20, 8, 2, 10 are QUICK.',
            fig=alpha(),
            parts=[P('a', 'The shift is {b}.', [7]),
                   P('b', 'XBPJR decodes to {l}', ['QUICK'])]))
I.append(IT(U, 'S', 8, 3,
            'Two Caesar shifts can be combined into one shift.',
            f'15 + 18 = 33, and 33 mod 26 = 7. To undo a shift of 7, go back 7, which is the same as going forward 26 {M} 7 = 19. A shift of 26 is a full turn round the alphabet, so nothing changes.',
            parts=[P('a', 'A shift of 15, then a shift of 18, equals one shift of {b}.', [7]),
                   P('b', 'To undo a shift of 7, you can use a shift of {b}.', [19]),
                   P('c', 'A shift of 26 makes the message   {circ:the same|reversed}', ['the same'])]))
I.append(IT(U, 'S', 9, 3,
            'A 24-hour clock goes back to 0 after 23. Write only the hour.',
            f'(a) 22 + 7 = 29, and 29 {M} 24 = 5. (b) 3 {M} 5 = {M}2, and {M}2 + 24 = 22. (c) 100 mod 24 = 4, so 9 + 4 = 13.',
            parts=[P('a', '22:00 and 7 hours later is {b}:00.', [5]),
                   P('b', '03:00 and 5 hours earlier is {b}:00.', [22]),
                   P('c', '09:00 and 100 hours later is {b}:00.', [13])]))
I.append(IT(U, 'S', 10, 3,
            'This code adds 7 each time and keeps the number on the 26-letter clock. Predict what it says.',
            f'total goes 7, 14, 21, then 28. 28 is more than 25, so 26 is taken away: 2. The 5th is 2 + 7 = 9. The 3rd number, 21, is the letter V.',
            fig=code([['var', 'set total to (0)'], ['ctl', 'repeat (5)', [['var', 'change total by (7)'], ['ctl', 'if <(total) {gt} (25)> then', [['var', f'change total by ({M}26)']]], ['look', 'say (total) for (1) seconds']]]]),
            parts=[P('a', 'The 4th number it says is {b}.', [2]),
                   P('b', 'The 5th number it says is {b}.', [9]),
                   P('c', 'The 3rd number it says is the letter {b}.', ['V'])],
            figside=True))
I.append(IT(U, 'S', 11, 3,
            'Start at 12 on a clock with 12 numbers. Keep jumping the same number of hours.',
            'Jumps of 7: 7, 2, 9, 4, 11, 6, 1, 8, 3, 10, 5, 12. All 12 numbers. Jumps of 9: 9, 6, 3, 12. Only 4 numbers, because 9 and 12 share a factor, 3.',
            fig={'type': 'l6_clock', 'ring': [12], 'r': 20},
            parts=[P('a', 'Jumps of 7 visit {b} different numbers.', [12]),
                   P('b', 'Jumps of 9 visit {b} different numbers.', [4])],
            figside=True))

# ---------------------------------------------------------------- Think harder
I.append(IT(U, 'T', 1, 4,
            'A number has remainder 3 when divided by 5. It has remainder 4 when divided by 7.',
            'Numbers with remainder 3 when divided by 5: 3, 8, 13, 18, 23, ... Of these, 18 = 2 × 7 + 4 is the first with remainder 4 when divided by 7. '
            'The pattern repeats every 5 × 7 = 35, so the next is 18 + 35 = 53.',
            parts=[P('a', 'The smallest such number is {b}.', [18]),
                   P('b', 'The next one is {b}.', [53])],
            hint='List the numbers that leave remainder 3 when divided by 5.', space={'rows': ['Working:', '', '']}))
I.append(IT(U, 'T', 2, 4,
            '10 January is a Tuesday. This year has 28 days in February.',
            'From 10 Jan to 10 Feb is 31 days, to 10 Mar is 28 more, and to 10 Apr is 31 more: 31 + 28 + 31 = 90 days. '
            '90 mod 7 = 6, because 90 = 12 × 7 + 6. Tuesday and 6 more days is Monday.',
            parts=[P('a', 'From 10 January to 10 April is {b} days.', [90]),
                   P('b', '90 mod 7 = {b}', [6]),
                   P('c', '10 April is a {l}', ['Monday'])],
            hint='January has 31 days, February 28 and March 31.', partsrow=True, space={'rows': ['Working:', '']}))
I.append(IT(U, 'T', 3, 4,
            'Mei sends the message QIIX EX RSSR. She says EX is the word AT coded with the same shift.',
            f'A = 0 became E = 4, so the shift is 4. Decode each letter by taking away 4. QIIX: 16, 8, 8, 23 minus 4 is 12, 4, 4, 19: MEET. EX: AT. RSSR: 17, 18, 18, 17 minus 4 is 13, 14, 14, 13: NOON.',
            parts=[P('a', 'The shift is {b}.', [4]),
                   P('b', 'The message is {l}', ['MEET AT NOON'])],
            hint='A is 0 and its code letter is E. How far is that?', space={'rows': ['Working:', '']}))

# ---------------------------------------------------------------- Go further
I.append(IT(U, 'G', 1, 5,
            'Beyond Level 6: A code with a changing shift.\nThe 1st letter moves 1, the 2nd moves 2, the 3rd moves 3, then the shifts repeat 1, 2, 3, ... ',
            f'MATHS: 12, 0, 19, 7, 18 plus 1, 2, 3, 1, 2 is 13, 2, 22, 8, 20: NCWIU. DQGFU: 3, 16, 6, 5, 20 minus 1, 2, 3, 1, 2 is 2, 14, 3, 4, 18: CODES. '
            f'The same letter can be coded in different ways, so counting the commonest letter does not work.',
            parts=[P('a', 'Code MATHS: {l}', ['NCWIU']),
                   P('b', 'Decode DQGFU: {l}', ['CODES']),
                   P('c', 'Why is this code harder to crack than a Caesar code?   {circ:the same letter is coded in different ways|every letter moves the same amount}', ['the same letter is coded in different ways'])],
            hint='Use the shifts 1, 2, 3, 1, 2 in turn, one for each letter.'))
I.append(IT(U, 'G', 2, 5,
            'A sprite goes round a 12-hour clock in jumps of 5 hours. Predict where it ends.',
            f'The 1st jump goes from 9 to 14, which is more than 12, so 12 is taken away: 2. After 100 jumps it has moved 500 hours: 9 + 500 = 509. '
            f'509 mod 12 = 5 (509 = 42 {X} 12 + 5), so it ends at 5.',
            fig=code([['var', 'set hour to (9)'], ['ctl', 'repeat (100)', [['var', 'change hour by (5)'], ['ctl', 'if <(hour) {gt} (12)> then', [['var', f'change hour by ({M}12)']]]]], ['look', 'say (hour)']]),
            parts=[P('a', 'After 1 jump the hour is {b}.', [2]),
                   P('b', 'After 100 jumps the hour is {b}.', [5])],
            hint='Find 9 + 500, then take away full turns of 12.', figside=True))
I.append(IT(U, 'G', 3, 5,
            'Beyond Level 6: Check digits.\nA code of 4 digits ends with a check digit. The 4 digits must add up to a multiple of 10. The check digit is the last digit.',
            f'4 + 7 + 2 = 13, and the next multiple of 10 is 20, so the check digit is 7. 9 + 8 + 1 = 18, so the check digit is 2. 5 + 3 + 6 = 14, so the last digit must be 6, not 9: the code is not valid.',
            parts=[P('a', 'The first 3 digits are 4, 7, 2. The check digit is {b}.', [7]),
                   P('b', 'The first 3 digits are 9, 8, 1. The check digit is {b}.', [2]),
                   P('c', 'Is the code 5 3 6 9 valid?   {circ:Yes|No}', ['No'])],
            hint='What must you add to the first 3 digits to reach a multiple of 10?', space={'rows': ['Working:']}))

# ---------------------------------------------------------------- Check yourself
I.append(IT(U, 'C', 1, 6,
            'It is 9 o\'clock. In 40 hours it will be {b} o\'clock.',
            f'9 + 40 = 49. 49 mod 12 = 1, because 4 {X} 12 = 48. It will be 1 o\'clock.',
            answer=A([1], '1')))
I.append(IT(U, 'C', 2, 6,
            'Code NOW with a shift of 6.  {l}',
            f'N = 13, O = 14, W = 22. Adding 6 gives 19, 20, 28. 28 {M} 26 = 2. The numbers 19, 20, 2 are T, U, C: TUC.',
            answer=A(['TUC'], 'TUC')))
I.append(IT(U, 'C', 3, 6,
            'EVQ was coded with a shift of 4. Decode it.  {l}',
            f'E = 4, V = 21, Q = 16. Taking away 4 gives 0, 17, 12: A, R, M. The word is ARM.',
            answer=A(['ARM'], 'ARM')))
I.append(IT(U, 'C', 4, 6,
            'Today is Friday. In 30 days it will be {l}',
            f'30 mod 7 = 2. Friday and 2 more days is Sunday.',
            answer=A(['Sunday'], 'Sunday')))

write_unit(8, 'Secret codes', 'Clock arithmetic and codes',
           'I can do clock arithmetic with mod. I can code and decode a secret message with a shift.', learn, I)
