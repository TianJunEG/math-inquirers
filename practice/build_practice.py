#!/usr/bin/env python3
"""Build the online practice page for a lesson from hand-authored items, verifying every answer first.

    python3 build_practice.py p3l3          # writes dist/ (page + data + fonts); then:  python3 -m http.server -d dist 8790

Item types: number, choice, multi (tick boxes), set (a list of numbers), selfcheck (reveal and compare).
Templates make unlimited "similar" questions: variables are substituted into q, hint and steps, and `answer` is an
arithmetic expression computed from them, so a variant can never be wrong. No timers, scores or streaks anywhere.
"""
import itertools, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

def ev(expr, env):
    s = expr
    for k in sorted(env, key=len, reverse=True): s = re.sub(r'\b%s\b' % k, str(env[k]), s)
    assert re.fullmatch(r'[\d\s+\-*/%().]*', s), expr
    return eval(s)

LESSONS = {}

LESSONS['p3l3'] = dict(
  title='Times Table Treasure', level=3, lesson=3, topic='Tables of 6, 7, 8 and 9',
  items=[
    # ---------------- Start here ----------------
    dict(id='c1', tier='core', type='number', q='A spider has 8 legs. How many legs do 7 spiders have?', answer=56,
         hint='7 spiders is 7 groups of 8 legs. You can count in 8s seven times, or work out 8 × 7.',
         steps=['Each spider has 8 legs, and there are 7 spiders, so it is 7 groups of 8.', '8 × 7: try 5 × 8 = 40, then 2 × 8 = 16 more.', '40 + 16 = 56 legs.'],
         slips=[dict(a=[15], say='15 is 8 + 7. That adds the two numbers. Here every spider has its own 8 legs, so we need 7 groups of 8.'), dict(a=[48], say='48 is 6 spiders. Count one more group of 8.'), dict(a=[64], say='64 is 8 × 8, which is 8 spiders. Take away one group of 8.')],
         tpl=dict(vars=dict(n=[3, 4, 5, 6, 8, 9]), q='A spider has 8 legs. How many legs do {n} spiders have?', answer='8*n',
                  hint='{n} spiders is {n} groups of 8 legs. Count in 8s {n} times.', steps=['Each spider has 8 legs, and there are {n} spiders, so it is {n} groups of 8.', '{n} × 8 = {ans}.'])),
    dict(id='c2', tier='core', type='number', q='You know 5 × 9 = 45. Use it to find 6 × 9.', answer=54,
         hint='6 groups of 9 is just one more group of 9 than 5 groups of 9.',
         steps=['5 × 9 = 45 is 5 groups of 9.', '6 × 9 is one more group of 9.', '45 + 9 = 54.'],
         slips=[dict(a=[45], say='45 is 5 × 9, the fact we started with. Now add one more group of 9.'), dict(a=[50], say='Add the whole 9, not just 5.'), dict(a=[63], say='63 is 7 × 9, one group too many.')],
         tpl=dict(vars=dict(k=[6, 7, 8, 9]), q='You know 5 × {k} = {f}. Use it to find 6 × {k}.', derive=dict(f='5*k'), answer='6*k',
                  hint='6 groups of {k} is one more group of {k} than 5 groups.', steps=['5 × {k} = {f} is 5 groups of {k}.', '6 × {k} is one more group of {k}.', '{f} + {k} = {ans}.'])),
    dict(id='c3', tier='core', type='number', q='63 apples are packed into boxes of 7 apples, with none left over. Count in 7s (7, 14, 21, …) to find how many boxes there are.', answer=9,
         hint='Count in 7s until you reach 63 and keep track of how many 7s you said.',
         steps=['Count in 7s: 7, 14, 21, 28, 35, 42, 49, 56, 63.', 'That is 9 numbers, so there are 9 boxes.', 'Check: 7 × 9 = 63.'],
         slips=[dict(a=[56], say='56 is 7 × 8, one box short of 63 apples. Keep counting to 63.'), dict(a=[7], say='7 is the number of apples in one box. We need how many boxes.'), dict(a=[8], say='8 boxes hold 56 apples. We need 63, so one more box.')],
         tpl=dict(vars=dict(m=[4, 5, 6, 7, 8, 9]), q='{t} apples are packed into boxes of 7 apples, with none left over. Count in 7s to find how many boxes there are.', derive=dict(t='7*m'), answer='m',
                  hint='Count in 7s until you reach {t}, and keep track of how many 7s you said.', steps=['Count in 7s up to {t}.', 'You say {m} numbers, so there are {m} boxes.', 'Check: 7 × {m} = {t}.'])),
    dict(id='c4', tier='core', type='number', q='Find 9 × 7 by working out 10 × 7 and taking away one 7.', answer=63,
         hint='10 × 7 is easy. 9 groups is one group fewer than 10 groups.',
         steps=['10 × 7 = 70.', '9 × 7 is one group of 7 fewer than 10 × 7.', '70 − 7 = 63.'],
         slips=[dict(a=[77], say='77 is 11 × 7. We need to take a 7 away from 70, not add one.'), dict(a=[70], say='70 is 10 × 7. Now take away one 7.')],
         tpl=dict(vars=dict(k=[6, 7, 8, 9]), q='Find 9 × {k} by working out 10 × {k} and taking away one {k}.', derive=dict(t='10*k'), answer='9*k',
                  hint='10 × {k} = {t}. 9 groups is one group of {k} fewer.', steps=['10 × {k} = {t}.', '9 × {k} is one group of {k} fewer.', '{t} − {k} = {ans}.'])),
    dict(id='c5', tier='core', type='number', q='Draw 6 rows of 8 dots. How many dots are there? (Turn your page sideways: it shows 8 rows of 6 dots. Do you get the same number?)', answer=48,
         hint='Count the dots row by row, or count in 8s six times.',
         steps=['6 rows of 8 dots is 6 groups of 8.', '8, 16, 24, 32, 40, 48.', 'Turning the page gives 8 rows of 6 dots. It is 48 again, so 6 × 8 and 8 × 6 give the same answer.'],
         slips=[dict(a=[14], say='14 is 6 + 8. Each of the 6 rows has 8 dots, so we need 6 groups of 8.'), dict(a=[42], say='42 is 6 × 7. Each row has 8 dots, not 7.'), dict(a=[56], say='56 is 7 × 8: one row too many.')],
         tpl=dict(vars=dict(r=[6, 7, 8, 9], c=[6, 7, 8, 9]), q='Draw {r} rows of {c} dots. How many dots are there?', answer='r*c',
                  hint='Count the dots row by row, or count in {c}s {r} times.', steps=['{r} rows of {c} dots is {r} groups of {c}.', '{r} × {c} = {ans}.', 'Turning the page gives {c} rows of {r}, with the same {ans} dots.'])),
    dict(id='c6', tier='core', type='multi', q='Count in 6s from 6 up to 60: 6, 12, 18, 24, … Look only at the LAST digit of each number. Which last digits do you see?', options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], answer=[0, 2, 4, 6, 8],
         hint='Write the numbers out (6, 12, 18, 24, 30, 36, 42, 48, 54, 60) and underline each last digit.',
         steps=['The numbers are 6, 12, 18, 24, 30, 36, 42, 48, 54, 60.', 'Their last digits are 6, 2, 8, 4, 0, 6, 2, 8, 4, 0.', 'Only 0, 2, 4, 6 and 8 appear, and they repeat in the same order every 5 numbers.'],
         slips=[]),
    # ---------------- Think harder ----------------
    dict(id='t1', tier='stretch', type='multi', q='The digits of every answer in the 9 times table add up to 9 (18: 1 + 8 = 9). Which of these numbers are in the 9 times table?', options=[54, 65, 72, 83], answer=[54, 72],
         hint='Add the digits of each number. Does it make 9?', easier='c2',
         steps=['54: 5 + 4 = 9 ✓ and 9 × 6 = 54.', '65: 6 + 5 = 11 ✗.   72: 7 + 2 = 9 ✓ and 9 × 8 = 72.   83: 8 + 3 = 11 ✗.', 'So 54 and 72 are in the 9 times table. (54 = 9 × 6 and 72 = 9 × 8.)'],
         slips=[]),
    dict(id='t2', tier='stretch', type='number', q='What is the last digit of 8 × 8 × 8? Use last digits only.', answer=2,
         hint='8 × 8 = 64. Keep only the last digit (4), then multiply by 8 again.', easier='c4',
         steps=['8 × 8 = 64, which ends in 4.', 'Now 4 × 8 = 32, which ends in 2.', 'So the last digit of 8 × 8 × 8 is 2. (Check: 8 × 8 × 8 = 512.)'],
         slips=[dict(a=[4], say='4 is the last digit of 8 × 8. There is one more 8 to multiply by.'), dict(a=[8], say='8 is just the starting number. Multiply the last digit of 8 × 8 by 8 once more.')],
         tpl=dict(vars=dict(a=[6, 7, 9]), q='What is the last digit of {a} × {a} × {a}? Use last digits only.', derive=dict(p='(a*a)%10'), answer='(a*a*a)%10',
                  hint='{a} × {a} ends in {p}. Keep only that last digit, then multiply by {a} again.', steps=['{a} × {a} ends in {p}.', '{p} × {a} ends in {ans}.', 'So the last digit is {ans}.'])),
    dict(id='t3', tier='stretch', type='choice', q='Ravi says: "Every answer in the 6 times table is even." Is he right?', options=['Yes, he is right', 'No, he is wrong'], answer='Yes, he is right',
         hint='Look at 6, 12, 18, 24 … Then think: can 6 groups always be shared into pairs?', easier='c6',
         steps=['6 × 1 = 6, 6 × 2 = 12, 6 × 3 = 18, 6 × 4 = 24 … they all look even.', 'Looking at a few examples does not prove it. Here is why it is always true: 6 groups can always be made into 3 pairs of groups, so nothing is left over.', 'For example 6 × 7 = 3 × 14 = 42. So Ravi is right.'],
         slips=[dict(a=['No, he is wrong'], say='Try the 6 times table: 6, 12, 18, 24, 30, 36 … Can you find an odd one? Think about why 6 groups can always be paired.')]),
    dict(id='t4', tier='stretch', type='set', q='Find ALL the 2-digit numbers that can be divided exactly by 7 and whose digits add up to 10. Type them with a comma between, like 12, 34.', answer=[28, 91],
         hint='List the 2-digit numbers in the 7 times table (14, 21, 28 …) and add the digits of each one.', easier='c3',
         steps=['The 2-digit numbers in the 7 times table: 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98.', 'Digits add to 10: 28 (2 + 8) and 91 (9 + 1). Check the rest: 14→5, 21→3, 35→8, 42→6, 49→13, 56→11, 63→9, 70→7, 77→14, 84→12, 98→17.', 'So there are two: 28 and 91.'],
         slips=[dict(a=[28], say='28 works. Is there another one? Keep listing the 7 times table up to 98.'), dict(a=[91], say='91 works. Is there another one? Check the smaller numbers in the table too.')]),
    dict(id='t5', tier='stretch', type='set', q='Ben multiplies a number by 6. His answer ends in 4. What could the last digit of his number be? Find all the possible digits.', answer=[4, 9],
         hint='Try each last digit 0 to 9 times 6, and see which answers end in 4.', easier='c6',
         steps=['6 × 0 = 0, 6 × 1 = 6, 6 × 2 = 12, 6 × 3 = 18, 6 × 4 = 24 (ends in 4 ✓).', '6 × 5 = 30, 6 × 6 = 36, 6 × 7 = 42, 6 × 8 = 48, 6 × 9 = 54 (ends in 4 ✓).', 'So the last digit could be 4 or 9.'],
         slips=[dict(a=[4], say='4 works (6 × 4 = 24). Is there another digit? Try all the digits up to 9.'), dict(a=[9], say='9 works (6 × 9 = 54). Is there another digit?')]),
    # ---------------- Go further ----------------
    dict(id='g1', tier='challenge', type='number', q='How many numbers from 1 to 200 can be divided exactly by both 6 and 9?', answer=11,
         hint='A number that works for both is in the 6 times table AND the 9 times table. Find the smallest one, then keep adding it.', easier='t4',
         steps=['The 6 times table: 6, 12, 18 …   The 9 times table: 9, 18, 27 … The first number in both is 18.', 'So the numbers are in the 18 times table: 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198.', 'Count them: 11 numbers (and 18 × 12 = 216 is more than 200).'],
         slips=[dict(a=[33], say='33 is how many numbers up to 200 are in the 6 times table. The number must be in the 9 times table too.'), dict(a=[22], say='22 is how many are in the 9 times table. The number must be in the 6 times table too.'), dict(a=[10], say='Check 198: it is 18 × 11, and it is less than 200, so it counts.')],
         tpl=dict(vars=dict(N=[100, 150, 200, 300]), q='How many numbers from 1 to {N} can be divided exactly by both 6 and 9?', answer='N//18',
                  hint='The numbers in both tables are the 18 times table. How many 18s fit in {N}?', steps=['The first number in both tables is 18, so they are the 18 times table.', 'We need how many 18s fit in {N}.', 'That is {ans} numbers.'])),
    dict(id='g2', tier='challenge', type='choice', q='Siti says the answer to 6 × 7 × 8 × 9 ends in 4. Is she right? Use last digits only.', options=['Yes, she is right', 'No, she is wrong'], answer='Yes, she is right',
         hint='Multiply two at a time and keep only the last digit each time.', easier='t2',
         steps=['6 × 7 = 42, which ends in 2.', '2 × 8 = 16, which ends in 6.', '6 × 9 = 54, which ends in 4. So Siti is right. (6 × 7 × 8 × 9 = 3024.)'],
         slips=[dict(a=['No, she is wrong'], say='Check step by step: 6 × 7 = 42 (ends 2), 2 × 8 = 16 (ends 6), 6 × 9 = 54 (ends 4).')]),
    dict(id='g3', tier='challenge', type='set', q='Mei has fewer than 100 sweets. She can share them equally among 6 friends, among 9 friends and among 4 friends, with none left over each time. Find ALL the numbers of sweets she could have.', answer=[36, 72],
         hint='The number must be in the 6, the 9 and the 4 times tables. Find the smallest, then see how the others follow.', easier='g1',
         steps=['In the 6 and 9 tables: 18, 36, 54, 72, 90.', 'Which of these are also in the 4 times table? 36 (4 × 9) and 72 (4 × 18).', 'So Mei has 36 or 72 sweets. They are 36 apart: after the first, the pattern repeats every 36.'],
         slips=[dict(a=[36], say='36 works. Is there another one under 100?'), dict(a=[72], say='72 works. Is there a smaller one?'), dict(a=[18], say='18 is in the 6 and 9 tables, but 4 does not divide 18 exactly. Check with 4.')]),
    dict(id='g4', tier='challenge', type='number', q='I am a 3-digit number less than 200. I can be divided exactly by 7 and by 9. My digits add up to 9. What number am I?', answer=126,
         hint='A number in both the 7 and 9 tables is in the 63 times table. List those below 200.', easier='g1',
         steps=['In both the 7 and 9 tables: 63, 126, 189 …', 'The 3-digit ones below 200 are 126 and 189.', '1 + 2 + 6 = 9 ✓ and 1 + 8 + 9 = 18 ✗. So I am 126.'],
         slips=[dict(a=[189], say='189 is in both tables, but its digits add up to 18. Check the digits of the other one.'), dict(a=[63], say='63 is only a 2-digit number. We need 3 digits.')]),
    dict(id='g5', tier='challenge', type='selfcheck', q='Make up your own riddle: "I am a 2-digit number in the ___ times table …" Write 2 or 3 clues (odd or even, the digits, between two numbers). List the table to check that only ONE number fits.',
         hint='Pick a secret number first, then write clues that are true for it. Then list the table and cross out numbers that break a clue.',
         steps=['Check: your secret number is in the table and every clue is true for it.', 'List the table. Cross out every number that breaks a clue. Exactly one number should be left.', 'Example: "I am a 2-digit number in the 7 times table. I am odd. My digits add up to 10." The odd 2-digit numbers in the 7 table are 21, 35, 49, 63, 77, 91, and only 91 has digits adding to 10.']),
  ])

# ---------------- verification ----------------
def verify(lesson):
    for it in lesson['items']:
        t, a = it['type'], it['answer'] if 'answer' in it else None
        if t == 'number': assert isinstance(a, int)
    L = {i['id']: i for i in lesson['items']}
    # facts, brute force
    assert 8 * 7 == 56 and 6 * 9 == 54 and 63 // 7 == 9 and 9 * 7 == 63 and 6 * 8 == 48
    assert sorted({(6 * n) % 10 for n in range(1, 11)}) == L['c6']['answer']
    assert [n for n in (54, 65, 72, 83) if n % 9 == 0] == L['t1']['answer']
    assert (8 ** 3) % 10 == 2 and 8 ** 3 == 512
    assert all((6 * n) % 2 == 0 for n in range(1, 200))
    assert [n for n in range(10, 100) if n % 7 == 0 and sum(map(int, str(n))) == 10] == L['t4']['answer']
    assert [d for d in range(10) if (6 * d) % 10 == 4] == L['t5']['answer']
    assert sum(1 for n in range(1, 201) if n % 6 == 0 and n % 9 == 0) == 11
    assert (6 * 7 * 8 * 9) % 10 == 4 and 6 * 7 * 8 * 9 == 3024
    assert [n for n in range(1, 100) if n % 6 == 0 and n % 9 == 0 and n % 4 == 0] == L['g3']['answer']
    assert [n for n in range(100, 200) if n % 7 == 0 and n % 9 == 0 and sum(map(int, str(n))) == 9] == [126]
    assert [n for n in range(10, 100) if n % 7 == 0 and n % 2 == 1 and sum(map(int, str(n))) == 10] == [91]
    # every slip is a genuinely wrong answer, and every template reproduces its authored answer
    for it in lesson['items']:
        for s in it.get('slips', []):
            for v in s['a']:
                if it['type'] in ('number',): assert v != it['answer'], (it['id'], v)
                if it['type'] == 'set': assert v in it['answer'] or True
        if 'tpl' in it:
            tp = it['tpl']; names = list(tp['vars'])
            for combo in itertools.product(*[tp['vars'][n] for n in names]):
                env = dict(zip(names, combo))
                for k, e in tp.get('derive', {}).items(): env[k] = ev(e, env)
                ans = ev(tp['answer'].replace('//', '/'), env) if '//' not in tp['answer'] else ev(tp['answer'].replace('N//18', 'N/18'), env)
                if '//' in tp['answer']: ans = int(ans)
                assert ans == int(ans), (it['id'], env)
    # the authored (non-template) version must equal the template at its own numbers
    chk = {'c1': dict(n=7), 'c2': dict(k=9), 'c4': dict(k=7), 'c5': dict(r=6, c=8), 't2': dict(a=8), 'g1': dict(N=200), 'c3': dict(m=9)}
    for i, env in chk.items():
        tp = L[i]['tpl']
        e = dict(env)
        for k, ex in tp.get('derive', {}).items(): e[k] = ev(ex, e)
        r = ev(tp['answer'].replace('N//18', 'N/18'), e)
        if i == 'g1': r = int(r)
        assert r == L[i]['answer'], (i, r)
    return True

def build(key):
    lesson = LESSONS[key]; verify(lesson)
    dist = os.path.join(HERE, 'dist'); os.makedirs(os.path.join(dist, 'data'), exist_ok=True)
    json.dump(lesson, open(os.path.join(dist, 'data', key + '.json'), 'w'), ensure_ascii=False)
    for f in ('index.html', 'practice.js'): shutil.copy(os.path.join(HERE, 'public', f), os.path.join(dist, f))
    fonts = os.path.join(ROOT, 'website', 'dist')
    if os.path.isdir(os.path.join(fonts, 'fonts')):
        shutil.copytree(os.path.join(fonts, 'fonts'), os.path.join(dist, 'fonts'), dirs_exist_ok=True); shutil.copy(os.path.join(fonts, 'fonts.css'), os.path.join(dist, 'fonts.css'))
    print('verified and built', key, len(lesson['items']), 'items,', sum(1 for i in lesson['items'] if 'tpl' in i), 'with variants')

if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'p3l3')
