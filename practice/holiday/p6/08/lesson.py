"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 8: Secret Codes (clock / modular arithmetic; Caesar codes, lists and letters).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l8.js workbook(): Start here Q1 to Q5; the Finish page: the Investigation
(p6/content/gaps.json lesson 8) and the exit slip (l8.js lesson.exit); Think harder = the first three l8.js qbank.stretch questions plus the one moved there from Start here
(l8.js moved); Go further = the last three l8.js qbank.challenge questions).  Every answer is recomputed by an INDEPENDENT checker below: clock and week answers by counting on one
hour (or day) at a time, remainders by taking away the divisor again and again, Caesar codes by moving along the alphabet one letter at a time, the code machine of Q3 by running
its three blocks on the list `alphabet` (item 1 is A), and a crack by trying every shift.  build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page.
"""
import os, re, sys
from fractions import Fraction
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w4lib as W       # noqa: E402

M = W.MINUS
ABC = W.ABC
META = dict(level=6, lesson=8, key='p6', title='Secret Codes', workbook_title='SECRET CODES', topic='Clock (Modular) Arithmetic', strand='Number and coding',
            sources=['p6/content/l8.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. Letters have numbers: A is 0, B is 1, C is 2 and so on up to Z, which is 25. The code number of a letter is (letter number + shift) mod 26.',
                   'n mod m is the remainder when n is divided by m. A clock wraps round after 12, a week after 7 days and the alphabet after 26 letters. To decode, shift back (add 26 if you go below 0).',
                   'Type coded and decoded words in capital or small letters; the spaces do not matter.'])
CL, CD = 'Clock arithmetic', 'Secret codes'

_src = open(os.path.join(HERE_, '..', '..', '..', '..', 'p6', 'content', 'l8.js'), encoding='utf-8').read()
LOOP_TXT = ['set {n} to {(item # of (letter) in alphabet) − 1}', 'set {m} to {(n + shift) mod 26}', 'set {code} to {join (code) (item (m + 1) of alphabet)}']
for _t in LOOP_TXT:                      # the three blocks drawn here are the printed ones
    assert _t in _src, _t
LOOP = [[[('t', 'set n to')], [('s', '(item # of (letter) in alphabet) − 1')]],
        [[('t', 'set m to'), ('s', '(n + shift) mod 26')]],
        [[('t', 'set code to')], [('s', 'join (code) (item (m + 1) of alphabet)')]]]
CODE_LABEL = 'Three blocks: set n to (item number of the letter in alphabet) minus 1; set m to (n + shift) mod 26; set code to join code and item (m + 1) of alphabet.'


def strip():
    return W.letter_strip()


def clockweek():
    return W.clock_week('Two circles to count round. Left: the 12 hours of a clock, 12 at the top. Right: the 7 days of a week, with Saturday marked.')


def machine(message, shift):
    """Runs the three blocks of the code machine on `message`: the list alphabet has item 1 = A, so the program uses item numbers and the checker does too."""
    alphabet = list(ABC)          # item 1 is A
    code = ''
    for letter in message:
        n = alphabet.index(letter) + 1 - 1            # item # of (letter) in alphabet, minus 1
        m = remainder(n + shift, 26)
        code = code + alphabet[m + 1 - 1]             # item (m + 1) of alphabet
    return code


def remainder(n, m):
    """n mod m by taking m away (or adding m) until the answer is from 0 to m - 1."""
    while n >= m:
        n -= m
    while n < 0:
        n += m
    return n


def crack_word(coded, words):
    """Shifts that turn the coded word into one of `words` (a Caesar shift moves every letter the same distance)."""
    return [(k, w) for w in words for k in range(26) if W.shift_text(w, k) == coded]


COMMON3 = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN', 'HER', 'WAS', 'ONE', 'OUR', 'OUT', 'DAY', 'GET', 'HAS', 'HIM', 'HIS', 'HOW', 'ITS', 'NEW', 'NOW', 'OLD', 'SEE', 'TWO', 'WHO', 'BOY', 'DID', 'LET']
MSG4 = 'BPM SMG QA CVLMZ BPM UIB'


def twice_word(msg):
    ws = msg.split()
    return [w for w in sorted(set(ws)) if ws.count(w) == 2 and len(w) == 3]


def jump_visits(jump):
    pos, seen = 0, [0]
    while True:
        pos = remainder(pos + jump, 12)
        if pos == 0:
            return seen
        seen.append(pos)


DAYS = W.DAYS

ITEMS = [
    # ================= Start here (workbook Lesson 8, Q1 to Q5)
    dict(id='1a', tier='core', no='1(a)', type='number', strand=CL, skill='clock arithmetic', answer=3, svg=clockweek(), label='1(a)',
         q='Clock and calendar puzzles. A clock wraps round after 12; a week wraps round after 7 days. It is 8 o\'clock. What time is it 7 hours later?',
         check=lambda: W.clock_after(8, 7),
         hint='Count on 7 hours round the clock face. What happens after 12?',
         steps=['Count on: 9, 10, 11, 12, 1, 2, 3.', '8 + 7 = 15, and after 12 the clock starts again: 15 − 12 = 3.', 'It is 3 o\'clock.'],
         src=['It is 8 o’clock. 7 hours later it is']),
    dict(id='1b', tier='core', no='1(b)', type='number', strand=CL, skill='clock arithmetic', answer=5, svg=clockweek(), label='1(b)',
         q='Clock puzzles. It is 11 o\'clock. What time is it 30 hours later? (Count 12 hours at a time.)',
         check=lambda: W.clock_after(11, 30),
         hint='12 hours later it is the same time again. How many hours are left after you take away whole turns of the clock?',
         steps=['30 hours is two whole turns of the clock (24 hours) and 6 more hours.', '11 o\'clock + 6 hours = 17, and 17 − 12 = 5.', 'It is 5 o\'clock.'],
         src=['It is 11 o’clock. 30 hours later (count 12 hours at a time):']),
    dict(id='1c', tier='core', no='1(c)', type='number', strand=CL, skill='clock arithmetic going backwards', answer=7, svg=clockweek(), label='1(c)',
         q='Clock puzzles. It is 4 o\'clock. What time was it 9 hours ago?',
         check=lambda: W.clock_after(4, -9),
         hint='Count back 9 hours round the clock face. What happens when you go back past 1?',
         steps=['Count back from 4: 3, 2, 1, then 12, 11, 10, 9, 8, 7.', f'4 {M} 9 = {M}5, and below the start of the clock we add 12: {M}5 + 12 = 7.', 'It was 7 o\'clock.'],
         src=['It is 4 o’clock. 9 hours ago it was']),
    dict(id='1d', tier='core', no='1(d)', type='choice', strand=CL, skill='calendar arithmetic', options=DAYS, answer='Monday', svg=clockweek(), label='1(d)',
         q='Calendar puzzles. A week wraps round after 7 days. Today is Saturday. What day of the week will it be in 100 days?',
         check=lambda: W.day_after('Saturday', 100),
         hint='How many whole weeks are in 100 days, and how many days are left over?',
         steps=['100 = 14 weeks and 2 days (100 mod 7 = 2).', 'Whole weeks bring you back to Saturday. Count on 2 more days: Sunday, Monday.', 'It will be Monday.'],
         src=['Today is Saturday. In 100 days:']),
    dict(id='1e', tier='core', no='1(e)', type='choice', strand=CL, skill='calendar arithmetic going backwards', options=DAYS, answer='Thursday', svg=clockweek(), label='1(e)',
         q='Calendar puzzles. Today is Saturday. What day of the week was it 30 days ago?',
         check=lambda: W.day_after('Saturday', -30),
         hint='How many whole weeks are in 30 days, and how many days are left over? Then count back.',
         steps=['30 = 4 weeks and 2 days (30 mod 7 = 2).', 'Whole weeks take you back to Saturday. Count back 2 more days: Friday, Thursday.', 'It was Thursday.'],
         src=['Today is Saturday. 30 days ago it was']),

    dict(id='2a', tier='core', no='2(a)', type='text', strand=CD, skill='coding with a Caesar shift', svg=strip(), label='2(a)', accept=['WPGGH'], shown='WPGGH',
         q='Caesar codes. Code number = (letter number + shift) mod 26. Code the word PIZZA with a shift of 7. Type the coded word.',
         check=lambda: W.shift_text('PIZZA', 7),
         hint='Change each letter to its number, add the shift, and take away 26 if you go past 25. Then change back to a letter.',
         steps=['P = 15, 15 + 7 = 22 = W. I = 8, 8 + 7 = 15 = P.', 'Z = 25, 25 + 7 = 32, and 32 − 26 = 6 = G (and the second Z gives G again). A = 0, 0 + 7 = 7 = H.', 'PIZZA with a shift of 7 is WPGGH.'],
         src=['Code the word PIZZA with a shift of 7.']),
    dict(id='2b', tier='core', no='2(b)', type='text', strand=CD, skill='decoding a Caesar shift', svg=strip(), label='2(b)', accept=['CODE IS FUN'], shown='CODE IS FUN',
         q='Caesar codes. Decode this message. It was made with a shift of 10:   MYNO SC PEX   Type the decoded message.',
         check=lambda: W.shift_text('MYNO SC PEX', -10),
         hint='To decode, take the shift away from each letter number. If you go below 0, add 26.',
         steps=['MYNO: M = 12, 12 − 10 = 2 = C. Y = 24, 24 − 10 = 14 = O. N = 13, 13 − 10 = 3 = D. O = 14, 14 − 10 = 4 = E.', 'SC: S = 18, 18 − 10 = 8 = I. C = 2, 2 − 10 = −8, and −8 + 26 = 18 = S. PEX: P = 15 gives 5 = F, E = 4 gives −6 + 26 = 20 = U, X = 23 gives 13 = N.',
                'The message is CODE IS FUN.'],
         src=['Decode this message. It was made with a shift of 10:   MYNO SC PEX']),
    dict(id='2c', tier='core', no='2(c)', type='number', strand=CD, skill='decoding by shifting forward', answer=16, svg=strip(), label='2(c)',
         q='Caesar codes. Ben wants to decode a message made with shift 10 by shifting FORWARD instead. Which shift should he use?',
         check=lambda: next(f for f in range(1, 26) if W.shift_text(W.shift_text(ABC, 10), f) == ABC),
         hint='Shifting forward by the right amount takes you all the way round the 26 letters to the same place as shifting back 10.',
         steps=['Shifting back 10 lands on the same letter as shifting forward 26 − 10.', '26 − 10 = 16.', 'Ben should use a shift of 16. (Check: A + 10 = K, and K + 16 = 26, which is A again.)'],
         src=['Ben wants to decode shift 10 by shifting FORWARD instead. Which shift should he use?']),

    dict(id='3W', tier='core', no='3 (W)', type='fields', strand=CD, skill='tracing the code machine', label='3 W', svg=W.code_stack(LOOP, CODE_LABEL),
         q='Trace the code. The Scratch code machine has a list called alphabet (item 1 is A). For each letter of the message WAY, with shift = 5, it does the three blocks drawn. Fill in the row for the letter W.',
         frame='n {f1}   n + 5 {f2}   m {f3}', answer=[22, 27, 1], check=lambda: (lambda n: [n, n + 5, remainder(n + 5, 26)])(ABC.index('W')),
         hint='n is the letter number (A is 0). Add the shift. Then take away 26 if you go past 25.',
         steps=['W is letter number 22.', '22 + 5 = 27, and 27 is past 25, so m = 27 − 26 = 1.', 'Item 2 of the list is B, so W becomes B.'],
         src=['Trace the code. The Scratch code machine has a list called alphabet (item 1 is A).']),
    dict(id='3A', tier='core', no='3 (A)', type='fields', strand=CD, skill='tracing the code machine', label='3 A', svg=W.code_stack(LOOP, CODE_LABEL),
         q='Trace the code. The Scratch code machine has a list called alphabet (item 1 is A). For each letter of the message WAY, with shift = 5, it does the three blocks drawn. Fill in the row for the letter A.',
         frame='n {f1}   n + 5 {f2}   m {f3}', answer=[0, 5, 5], check=lambda: (lambda n: [n, n + 5, remainder(n + 5, 26)])(ABC.index('A')),
         hint='n is the letter number (A is 0). Add the shift. Then take away 26 if you go past 25.',
         steps=['A is letter number 0.', '0 + 5 = 5, which is not past 25, so m = 5.', 'Item 6 of the list is F, so A becomes F.'],
         src=['Trace the code. The Scratch code machine has a list called alphabet (item 1 is A).']),
    dict(id='3Y', tier='core', no='3 (Y)', type='fields', strand=CD, skill='tracing the code machine', label='3 Y', svg=W.code_stack(LOOP, CODE_LABEL),
         q='Trace the code. The Scratch code machine has a list called alphabet (item 1 is A). For each letter of the message WAY, with shift = 5, it does the three blocks drawn. Fill in the row for the letter Y.',
         frame='n {f1}   n + 5 {f2}   m {f3}', answer=[24, 29, 3], check=lambda: (lambda n: [n, n + 5, remainder(n + 5, 26)])(ABC.index('Y')),
         hint='n is the letter number (A is 0). Add the shift. Then take away 26 if you go past 25.',
         steps=['Y is letter number 24.', '24 + 5 = 29, and 29 is past 25, so m = 29 − 26 = 3.', 'Item 4 of the list is D, so Y becomes D.'],
         src=['Trace the code. The Scratch code machine has a list called alphabet (item 1 is A).']),
    dict(id='3a', tier='core', no='3(a)', type='text', strand=CD, skill='tracing the code machine', label='3(a)', accept=['BFD'], shown='BFD', svg=W.code_stack(LOOP, CODE_LABEL),
         q='Trace the code. The code machine runs the three blocks on every letter of WAY with shift = 5. At the end the program says the code. What does it say?',
         check=lambda: machine('WAY', 5),
         hint='Each letter becomes the list item numbered m + 1. Put the three code letters together in order.',
         steps=['W gives B, A gives F, Y gives D.', 'join puts them in order: the program says BFD.'],
         src=['At the end the program says the code. What does it say?']),

    dict(id='4a1', tier='core', no='4(a) repeated', type='text', strand=CD, skill='cracking a code', label='4(a) twice', accept=['BPM'], shown='BPM', svg=strip(),
         q='Crack the code. Mei found this message. It was made with a Caesar shift, but she does not know which one:  BPM SMG QA CVLMZ BPM UIB.  Which 3-letter word appears twice?',
         check=lambda: (lambda w: w[0] if len(w) == 1 else None)(twice_word(MSG4)),
         hint='Read through the six words. Look for a word that is repeated.',
         steps=['The words are BPM, SMG, QA, CVLMZ, BPM, UIB.', 'BPM appears twice.'],
         src=['Which 3-letter word appears twice?']),
    dict(id='4a2', tier='core', no='4(a) English', type='text', strand=CD, skill='cracking a code', label='4(a) English', accept=['THE'], shown='THE', svg=strip(),
         q='Crack the code. Mei found a message made with a Caesar shift:  BPM SMG QA CVLMZ BPM UIB.  A 3-letter word appears twice in it. What common English word could it be?',
         check=lambda: (lambda c: c[0][1] if len({w for k, w in c}) == 1 else None)(crack_word('BPM', COMMON3)),
         hint='Which 3-letter English word do you see most often in sentences? In a Caesar code every letter moves the same distance, so a good guess must fit all three letters.',
         steps=['A Caesar shift moves every letter the same distance, so the guess must fit all three letters.', 'BPM could be THE: T (19) + 8 = 27, 27 − 26 = 1 = B; H (7) + 8 = 15 = P; E (4) + 8 = 12 = M.', 'No other common 3-letter word fits all three letters, so the word is probably THE.'],
         src=['What English word could it be?']),
    dict(id='4b', tier='core', no='4(b)', type='number', strand=CD, skill='finding the shift', answer=8, svg=strip(), label='4(b)',
         q='Crack the code. Mei thinks the repeated word is THE. If she is right, what shift turns T into B?',
         check=lambda: next(k for k in range(26) if W.shift_text('T', k) == 'B'),
         hint='T is 19 and B is 1. How far do you move from T to get to B, going forwards round the alphabet?',
         steps=['T = 19 and B = 1.', '19 + 8 = 27, and 27 − 26 = 1, so 8 steps forward from T lands on B.', 'The shift is 8.'],
         src=['If you are right, what shift turns T into B?']),
    dict(id='4c', tier='core', no='4(c)', type='text', strand=CD, skill='decoding the first word', label='4(c)', accept=['THE'], shown='THE', svg=strip(),
         q='Crack the code. Mei found a message made with a Caesar shift:  BPM SMG QA CVLMZ BPM UIB.  Decode the first word of the message with the shift you found in (b). Type the decoded word.',
         check=lambda: W.shift_text('BPM', -next(k for k in range(26) if W.shift_text('T', k) == 'B')),
         hint='To decode, take the shift away from each letter number. If you go below 0, add 26.',
         steps=['B = 1, 1 − 8 = −7, and −7 + 26 = 19 = T.', 'P = 15, 15 − 8 = 7 = H. M = 12, 12 − 8 = 4 = E.', 'The first word is THE.'],
         src=['Decode the first word of the message with that shift:']),

    dict(id='5a', tier='core', no='Bonus 5(a)', type='number', strand=CD, skill='two shifts in a row', answer=15, svg=strip(), label='Bonus 5(a)',
         q='Bonus question: two shifts in a row. Shifts add up like jumps on a 26-hour clock. (Example: shift 2 then shift 3 moves A to C to F, the same as shift 5.) Shift 6, then shift 9 is the same as one shift of what?',
         check=lambda: next(s for s in range(1, 26) if W.shift_text(W.shift_text(ABC, 6), 9) == W.shift_text(ABC, s)),
         hint='Add the two shifts. If the answer is more than 25, take away 26.',
         steps=['6 + 9 = 15.', '15 is not more than 25, so it is one shift of 15.'],
         src=['Shift 6, then shift 9 is the same as one shift of']),
    dict(id='5b', tier='core', no='Bonus 5(b)', type='number', strand=CD, skill='two shifts in a row', answer=5, svg=strip(), label='Bonus 5(b)',
         q='Bonus question: two shifts in a row. Shifts add up like jumps on a 26-hour clock. Shift 19, then shift 12 is the same as one shift of what?',
         check=lambda: next(s for s in range(1, 26) if W.shift_text(W.shift_text(ABC, 19), 12) == W.shift_text(ABC, s)),
         hint='Add the two shifts. If the answer is more than 25, take away 26.',
         steps=['19 + 12 = 31.', '31 is more than 25, so take away 26: 31 − 26 = 5.', 'It is one shift of 5.'],
         src=['Shift 19, then shift 12:  one shift of']),
    dict(id='5c', tier='core', no='Bonus 5(c)', type='choice', strand=CD, skill='shifts that add up to 26', svg=strip(), label='Bonus 5(c)',
         options=['The original message back', 'A message coded with a shift of 9', 'A message coded with a shift of 17', 'A message coded with a shift of 8'], answer='The original message back',
         q='Bonus question: two shifts in a row. Ben codes a message with shift 9, then codes the result with shift 17. What does he get?',
         check=lambda: 'The original message back' if W.shift_text(W.shift_text(ABC, 9), 17) == ABC else None,
         hint='Add the two shifts, then take away 26 if the answer is more than 25. What single shift is that?',
         steps=['9 + 17 = 26, which is 0 after wrapping round the 26 letters.', 'A shift of 0 changes nothing, so Ben gets the original message back.'],
         src=['Ben codes a message with shift 9, then codes the result with shift 17. What does he get? Why?']),
    dict(id='5c-why', tier='core', no='Bonus 5(c) why', type='selfcheck', strand=CD, skill='explaining a full turn', svg=strip(), label='5(c) why',
         q='Bonus question: Ben codes a message with shift 9, then codes the result with shift 17. Explain what happens to each letter and why. Write your reason, then check it against the worked solution.',
         facts=dict(total=26), check=lambda: dict(total=9 + 17),
         hint='Think of the 26 letters as a 26-hour clock. Where does a letter end up after the two jumps?',
         steps=['The two shifts move each letter 9 + 17 = 26 places along the alphabet.', '26 places is a full turn of the alphabet, so each letter lands back on itself.', 'So Ben gets his original message back.'],
         src=['Ben codes a message with shift 9, then codes the result with shift 17. What does he get? Why?']),
    dict(id='5d', tier='core', no='Bonus 5(d)', type='number', strand=CD, skill='a shift that undoes itself', answer=13, svg=strip(), label='Bonus 5(d)',
         q='Bonus question: two shifts in a row. Which shift (not 0), used twice, always gives back the original message?',
         check=lambda: (lambda s: s.pop() if len(s) == 1 else None)({k for k in range(1, 26) if W.shift_text(W.shift_text(ABC, k), k) == ABC}),
         hint='The two equal shifts must add up to a full turn of the alphabet. How many letters are there altogether?',
         steps=['Two equal shifts add up to 2 × shift, and this must be 26 (a full turn).', '26 ÷ 2 = 13.', 'The shift is 13.'],
         src=['Which shift (not 0), used twice, always gives back the original message?']),

    dict(id='Xa', tier='core', no='Exit slip (a)', type='text', strand=CD, skill='coding with a large shift', label='Exit (a)', accept=['GH'], shown='GH',
         q='Code the word HI with a shift of 25. Type the coded word.',
         check=lambda: W.shift_text('HI', 25),
         hint='H is 7 and I is 8. Add 25 to each, and take away 26 if the answer is past 25.',
         steps=['H = 7, 7 + 25 = 32, and 32 − 26 = 6 = G.', 'I = 8, 8 + 25 = 33, and 33 − 26 = 7 = H.', 'HI becomes GH.'],
         src=['Code the word HI with a shift of 25. What do you notice?']),
    dict(id='Xb', tier='core', no='Exit slip (b)', type='selfcheck', strand=CD, skill='a shift of 25', label='Exit (b)',
         q='Code the word HI with a shift of 25. What do you notice? Write what you see, then check it against the worked solution.',
         facts=dict(back=1), check=lambda: dict(back=next(k for k in range(1, 26) if W.shift_text('HI', 25) == W.shift_text('HI', -k))),
         hint='Compare each coded letter with the letter you started with. Which way and how far has it moved?',
         steps=['Each letter moved back by 1: H became G and I became H.', 'A shift of 25 is the same as shifting back 1, because 25 = 26 − 1.'],
         src=['Code the word HI with a shift of 25. What do you notice?']),

    # ================= Investigation (printed on the Finish page)
    dict(id='I1', tier='invest', no='Investigation first step', type='text', strand=CD, skill='two shifts that add up to 26', svg=strip(), label='Inv first', accept=['C'], shown='C',
         q='Is it always true? First step: code the letter C with shift 8. Then shift your answer by 18. What letter do you land on?',
         check=lambda: W.shift_text(W.shift_text('C', 8), 18),
         hint='Code C with shift 8 first, then code the letter you get with shift 18.',
         steps=['C = 2, 2 + 8 = 10 = K.', 'K = 10, 10 + 18 = 28, and 28 − 26 = 2 = C.', 'You land on C.'],
         src=['First step: code the letter C with shift 8. Then shift your answer by 18. Where do you land?']),
    dict(id='I2', tier='invest', no='Investigation 2', type='text', strand=CD, skill='coding a word', svg=strip(), label='Inv 2', accept=['KIB'], shown='KIB',
         q='Is it always true? Code the word CAT with a shift of 8. What do you get?',
         check=lambda: W.shift_text('CAT', 8),
         hint='C = 2, A = 0, T = 19. Add 8 to each, and wrap round if you go past 25.',
         steps=['C: 2 + 8 = 10 = K. A: 0 + 8 = 8 = I.', 'T: 19 + 8 = 27, and 27 − 26 = 1 = B.', 'CAT with shift 8 is KIB.'],
         src=['Code the word CAT with a shift of 8.']),
    dict(id='I3', tier='invest', no='Investigation 3', type='text', strand=CD, skill='two shifts that add up to 26', svg=strip(), label='Inv 3', accept=['CAT'], shown='CAT',
         q='Is it always true? Code the word CAT with a shift of 8. Then code your answer with a shift of 18. What word do you get?',
         check=lambda: W.shift_text(W.shift_text('CAT', 8), 18),
         hint='Code CAT with shift 8 first. Then code that answer with shift 18, letter by letter.',
         steps=['CAT with shift 8 is KIB.', 'KIB with shift 18: K = 10 + 18 = 28 → 2 = C; I = 8 + 18 = 26 → 0 = A; B = 1 + 18 = 19 = T.', 'You get CAT again.'],
         src=['Then code your answer with a shift of 18.']),
    dict(id='I4', tier='invest', no='Investigation 4', type='text', strand=CD, skill='two shifts that add up to 26', svg=strip(), label='Inv 4', accept=['CAT'], shown='CAT',
         q='Is it always true? Choose two other shifts that add up to 26 (not 8 and 18). Code CAT with the first shift, then code your answer with the second shift. What word do you get?',
         check=lambda: 'CAT' if all(W.shift_text(W.shift_text('CAT', a), 26 - a) == 'CAT' for a in range(1, 26)) else None,
         hint='Try a pair such as the two numbers in a sum that makes 26. Work each letter out and wrap round when you go past 25.',
         steps=['Whatever pair you choose, the two shifts move each letter 26 places in all.', 'Example: 5 and 21. C → H → C, A → F → A, T → Y → T.', 'You get CAT again.'],
         src=['Try two other shifts that add up to 26.']),
    dict(id='I5', tier='invest', no='Investigation (a)', type='choice', strand=CD, skill='is it always true', options=['Yes', 'No'], answer='Yes', svg=strip(), label='Inv (a)',
         q='Is it always true that two shifts that add up to 26 undo each other? Test it on a few words.',
         check=lambda: 'Yes' if all(W.shift_text(W.shift_text(w, a), 26 - a) == w for w in ('CAT', 'ZOO', 'MATHS', ABC) for a in range(1, 26)) else 'No',
         hint='Test two or three other pairs of shifts that add up to 26. Does any pair fail?',
         steps=['Check every pair, from 1 and 25 up to 25 and 1: each time the coded word comes back to the original.', 'So two shifts that add up to 26 always undo each other.'],
         src=['(a) Is it always true that two such shifts undo each other? Explain.']),
    dict(id='I5-why', tier='invest', no='Investigation (a) explain', type='selfcheck', strand=CD, skill='explaining a full circle', svg=strip(), label='Inv (a) why',
         q='Think about coding a message with one shift, and then coding the result with a second shift so that the two shifts add up to 26. Explain what happens to each letter and why. Write your reason, then check it against the worked solution.',
         facts=dict(places=26), check=lambda: dict(places=8 + 18),
         hint='Where does a letter end up after moving a places along the alphabet and then 26 − a more places?',
         steps=['If the shifts are a and 26 − a, every letter moves a + (26 − a) = 26 places in all.', '26 places is a full circle round the alphabet, so every letter lands where it started.'],
         src=['Explain.']),
    dict(id='I6', tier='invest', no='Investigation (b)', type='set', strand=CD, skill='a shift that is its own decoder', answer=[13], svg=strip(), label='Inv (b)',
         q='Is there a shift that is its own decoder, so that coding a message twice with it gives back the original? Find ALL of the shifts from 1 to 25 that work, and type them.',
         check=lambda: [k for k in range(1, 26) if W.shift_text(W.shift_text(ABC, k), k) == ABC],
         hint='Coding twice with the shift k moves each letter 2 × k places. When does that make a full circle (or several full circles)?',
         steps=['Coding twice with shift k moves each letter 2 × k places, and this must be a multiple of 26.', '2 × 13 = 26 works. For any other shift from 1 to 25, 2 × k is not a multiple of 26 (checked for every shift).', 'Only 13 works. (A shift of 13 is called ROT13.)'],
         src=['(b) Is there a shift that is its own decoder, so that coding twice gives back the original? Find ALL of them.']),

    # ================= Think harder (first three Think harder questions, then the one moved from Start here)
    dict(id='T1', tier='stretch', no='T1', type='text', strand=CD, skill='a repeating pattern', label='T1', accept=['E'], shown='E',
         q='The pattern CODECODECODE… goes on and on. What is the 100th letter?',
         check=lambda: ('CODE' * 30)[100 - 1],
         hint='The pattern repeats every 4 letters. What does the 4th letter, the 8th letter and the 12th letter have in common?',
         steps=['The pattern repeats in groups of 4: C, O, D, E.', '100 ÷ 4 = 25 exactly, so the 100th letter is the last letter of the 25th group (100 mod 4 = 0).', 'The 100th letter is E.'],
         src=['The pattern CODECODECODE… goes on and on. What is the 100th letter?']),
    dict(id='T2', tier='stretch', no='T2', type='number', strand=CL, skill='clock arithmetic with a big number', answer=2, label='T2',
         q='It is 10 o\'clock now. What time will it be 1000 hours from now (on a 12-hour clock)?',
         check=lambda: W.clock_after(10, 1000),
         hint='12 hours later it is the same time. How many hours are left over after you take away whole turns of the clock?',
         steps=['1000 ÷ 12 = 83 remainder 4, so 1000 hours is 83 whole turns and 4 more hours.', '10 + 4 = 14, and 14 − 12 = 2.', 'It will be 2 o\'clock.'],
         src=['It is 10 o’clock now. What time will it be 1000 hours from now (on a 12-hour clock)?']),
    dict(id='T3', tier='stretch', no='T3', type='number', strand=CL, skill='remainders', answer=23, label='T3',
         q='Find the smallest number bigger than 10 that leaves a remainder of 3 when it is divided by 4 and also when it is divided by 5.',
         check=lambda: next(n for n in range(11, 1000) if remainder(n, 4) == 3 and remainder(n, 5) == 3),
         hint='The number is 3 more than a number that is in both the 4 times table and the 5 times table. What is the first such number above 0?',
         steps=['The number minus 3 must be in both the 4 and the 5 times tables, so it is a multiple of 20.', 'The smallest numbers are 3, 23, 43, ... and 3 is not bigger than 10.', 'The answer is 23. (Check: 23 = 5 × 4 + 3 and 23 = 4 × 5 + 3.)'],
         src=['Find the smallest number bigger than 10 that leaves a remainder of 3 when it is divided by 4 and also when it is divided by 5.']),
    dict(id='T4a', tier='stretch', no='T4(a)', type='fields', strand=CL, skill='mod as a remainder', label='T4 (a)',
         q='Work out each mod. (n mod m is the remainder when n is divided by m.)',
         frame='29 mod 12 = {f1}   50 mod 7 = {f2}   100 mod 26 = {f3}', answer=[5, 1, 22],
         check=lambda: [remainder(29, 12), remainder(50, 7), remainder(100, 26)],
         hint='Take away the number you divide by as many times as you can. What is left?',
         steps=['29 = 2 × 12 + 5, so 29 mod 12 = 5.', '50 = 7 × 7 + 1, so 50 mod 7 = 1.', '100 = 3 × 26 + 22, so 100 mod 26 = 22.'],
         src=['(a) Work out 29 mod 12, 50 mod 7 and 100 mod 26.']),
    dict(id='T4b', tier='stretch', no='T4(b)', type='text', strand=CD, skill='decoding a whole message', label='T4 (b)', svg=strip(), accept=['THE KEY IS UNDER THE MAT'], shown='THE KEY IS UNDER THE MAT',
         q='Decode the whole message from Q4 (BPM SMG QA CVLMZ BPM UIB) with the shift you found there. Type the decoded message.',
         check=lambda: W.shift_text(MSG4, -next(k for k in range(26) if W.shift_text('T', k) == 'B')),
         hint='Take the shift away from the number of every letter, and add 26 whenever you go below 0.',
         steps=['The shift is 8. BPM is THE (from Q4).', 'SMG: S = 18 − 8 = 10 = K; M = 12 − 8 = 4 = E; G = 6 − 8 = −2, + 26 = 24 = Y. So SMG is KEY.', 'QA is IS, CVLMZ is UNDER, BPM is THE, UIB is MAT.',
                'The message is THE KEY IS UNDER THE MAT.'],
         src=['(b) Decode the whole message from Q4 (BPM SMG QA CVLMZ BPM UIB) with the shift you found.']),

    # ================= Go further (last three Go further questions)
    dict(id='C1', tier='challenge', no='C1', type='selfcheck', open=True, marking_mode='open', strand=CD, skill='writing and cracking a code', label='C1', svg=strip(),
         q='Write your own secret message of at least 8 letters and code it with a shift of your choice. Write clear instructions telling a friend how to decode it, and explain how a friend could crack it without being told the shift. If you can, give it to a friend to decode. Then compare with the worked example.',
         hint='Code each letter with your shift, then decode your own message to check it works. To crack a code you can try every shift from 1 to 25, or look for a short word.',
         steps=['Open: many messages work. Check your code by decoding it again.', 'A friend can crack it by trying every shift from 1 to 25, or by looking at the commonest letter (often E) or a short word (A or I).', 'Example: MEET AT SIX with a shift of 3 is PHHW DW VLA.'],
         src=['Write your own secret message of at least 8 letters and code it with a shift of your choice.']),
    dict(id='C2', tier='challenge', no='C2', type='number', strand=CD, skill='two shifts that make one shift', answer=21, label='C2', svg=strip(),
         q='Ali codes a message with a shift of 7. Mei codes Ali\'s result with another shift. The final message is the same as the original coded with a shift of 2. What shift did Mei use?',
         check=lambda: next(k for k in range(0, 26) if W.shift_text(W.shift_text(ABC, 7), k) == W.shift_text(ABC, 2)),
         hint='The two shifts together must make a shift of 2. They add up to 2, or to 2 plus a full turn of 26.',
         steps=['The shifts add up like jumps on a 26-letter clock: 7 + Mei\'s shift lands on 2.', '7 + 21 = 28, and 28 − 26 = 2.', 'Mei used a shift of 21.'],
         src=['Ali codes a message with a shift of 7. Mei codes Ali’s result with another shift.']),
    dict(id='C3a', tier='challenge', no='C3(a)', type='choice', strand=CL, skill='jumps round a clock', options=['Yes', 'No'], answer='Yes', label='C3 (a)',
         svg=W.jump_rings('Two clock circles with 12 at the top marked as the start, to draw the jumps on.'),
         q='Start at 12 on a clock and keep jumping forward 5 hours. Do you land on every number before you get back to 12?',
         check=lambda: 'Yes' if len(jump_visits(5)) == 12 else 'No',
         hint='Draw the jumps on the left clock, or list the hours you reach: 5, 10, ... Keep going until you reach 12 again.',
         steps=['Jumps of 5 land on 5, 10, 3, 8, 1, 6, 11, 4, 9, 2, 7 and then 12.', 'That is all 12 numbers.'],
         sol_fig=lambda f: W.jump_rings('Left: jumps of 5 hours join all 12 numbers in one loop. Right: jumps of 4 hours join only 12, 4 and 8.', jump=(5, 4)),
         src=['Start at 12 on a clock and keep jumping forward 5 hours. Do you land on every number before you get back to 12?']),
    dict(id='C3b', tier='challenge', no='C3(b)', type='choice', strand=CL, skill='jumps round a clock', options=['Yes', 'No'], answer='No', label='C3 (b)',
         svg=W.jump_rings('Two clock circles with 12 at the top marked as the start, to draw the jumps on.'),
         q='Start at 12 on a clock and keep jumping forward 4 hours. Do you land on every number before you get back to 12?',
         check=lambda: 'Yes' if len(jump_visits(4)) == 12 else 'No',
         hint='Draw the jumps on the right clock, or list the hours you reach: 4, 8, ... Keep going until you reach 12 again.',
         steps=['Jumps of 4 land on 4, 8 and then 12.', 'It lands on only 3 of the 12 numbers (12, 4 and 8).'],
         sol_fig=lambda f: W.jump_rings('Left: jumps of 5 hours join all 12 numbers in one loop. Right: jumps of 4 hours join only 12, 4 and 8.', jump=(5, 4)),
         src=['What about jumps of 4 hours?']),
    dict(id='C3c', tier='challenge', no='C3(c)', type='selfcheck', strand=CL, skill='why jumps miss numbers', label='C3 (c)',
         svg=W.jump_rings('Two clock circles with 12 at the top marked as the start, to draw the jumps on.'),
         q='Compare jumps of 5 hours with jumps of 4 hours round the 12-hour clock. Explain what you notice and why it happens. Write your reason, then check it against the worked solution.',
         facts=dict(five=12, four=3), check=lambda: dict(five=len(jump_visits(5)), four=len(jump_visits(4))),
         hint='Look at the numbers 5 and 4. Which one shares a factor with 12 (other than 1)?',
         steps=['Jumps of 5 reach all 12 numbers, but jumps of 4 reach only 3 of them (12, 4 and 8).', 'The number 4 shares a factor with 12 (4 and 12 are both in the 4 times table), so the jumps keep landing on the same few numbers.', 'The number 5 shares no factor with 12 except 1, so the jumps reach every number.'],
         sol_fig=lambda f: W.jump_rings('Left: jumps of 5 hours join all 12 numbers in one loop. Right: jumps of 4 hours join only 12, 4 and 8.', jump=(5, 4)),
         src=['Do you land on every number before you get back to 12? What about jumps of 4 hours?']),
]

for _it in ITEMS:
    _it['q'] = re.sub(r'\s{2,}', ' ', _it['q'])
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

P.finish(ITEMS)


def _sum_lists():
    a_list, b_list = [6, 9, 12, 15, 22], [2, 5, 7, 9, 13]
    assert all(a + b != 26 for a in a_list for b in b_list)
    return a_list, b_list


_A, _B = _sum_lists()

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
VARIANTS = {
    '1a': dict(base=dict(s=8, h=7),
               tpl=dict(vars=dict(s=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], h=[3, 5, 7, 9, 14, 20, 25, 30]), derive=dict(tot='s+h'),
                        q="Clock puzzle. It is {s} o'clock. What time is it {h} hours later?", answer='(s+h-1)%12+1',
                        hint='Count on {h} hours round the clock face. What happens after 12?',
                        steps=['{s} + {h} = {tot}.', 'The clock wraps round after 12, so take away 12 as many times as you can, keeping a number from 1 to 12.', 'It is {ans} o\'clock.']),
               oracle=lambda e: W.clock_after(e['s'], e['h'])),
    '2c': dict(base=dict(k=10),
               tpl=dict(vars=dict(k=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 18, 20, 22]),
                        q='Caesar codes. Ben wants to decode a message made with a shift of {k} by shifting FORWARD instead. Which shift should he use?', answer='26-k',
                        hint='Shifting forward by the right amount takes you all the way round the 26 letters to the same place as shifting back {k}.',
                        steps=['Shifting back {k} lands on the same letter as shifting forward 26 − {k}.', '26 − {k} = {ans}.']),
               oracle=lambda e: next(f for f in range(1, 26) if W.shift_text(W.shift_text(ABC, e['k']), f) == ABC)),
    '5a': dict(base=dict(a=6, b=9),
               tpl=dict(vars=dict(a=_A, b=_B), derive=dict(tot='a+b'),
                        q='Two shifts in a row. Shift {a}, then shift {b} is the same as one shift of what? (Shifts add up like jumps on a 26-hour clock.)', answer='(a+b)%26',
                        hint='Add the two shifts. If the answer is more than 25, take away 26.',
                        steps=['{a} + {b} = {tot}.', 'If the total is more than 25, take away 26.', 'It is one shift of {ans}.']),
               oracle=lambda e: next(s for s in range(1, 26) if W.shift_text(W.shift_text(ABC, e['a']), e['b']) == W.shift_text(ABC, s))),
    'T2': dict(base=dict(s=10, h=1000),
               tpl=dict(vars=dict(s=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], h=[100, 200, 500, 1000, 1500, 2000]), derive=dict(tot='s+h'),
                        q="It is {s} o'clock now. What time will it be {h} hours from now (on a 12-hour clock)?", answer='(s+h-1)%12+1',
                        hint='12 hours later it is the same time. How many hours are left over after you take away whole turns of the clock?',
                        steps=['{s} + {h} = {tot}.', 'The clock wraps round after 12, so take away 12 as many times as you can, keeping a number from 1 to 12.', 'It will be {ans} o\'clock.']),
               oracle=lambda e: W.clock_after(e['s'], e['h'])),
}
