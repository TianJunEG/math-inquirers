"""Independent checks for Level 1 Unit 3 (Picture graphs). Each check rebuilds the data from the question text (never from the book
answer) and recomputes: counting, differences, totals, constraint search by brute force."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


games = {'Skipping': 7, 'Tag': 7, 'Catch': 5, 'Hopscotch': 4, 'Marbles': 3}
stickers = {'Ali': 6, 'Mei': 9, 'Ben': 3, 'Siti': 5}
cookies = {'Monday': 4, 'Tuesday': 6, 'Wednesday': 8, 'Thursday': 5, 'Friday': 7}
books = {'Kumar': 8, 'Aisha': 3}


def most(d):
    m = max(d.values()); w = [k for k, v in d.items() if v == m]; assert len(w) == 1; return w[0]


def fewest(d):
    m = min(d.values()); w = [k for k, v in d.items() if v == m]; assert len(w) == 1; return w[0]


@check('L1U03-L01')
def _():
    return s([5 - 2])


@check('L1U03-S01')
def _():
    ties = sorted({k for k in games for j in games if k != j and games[k] == games[j]})
    return {'a': s([games['Catch']]), 'b': [fewest(games)], 'c': ties}


@check('L1U03-S02')
def _():
    return {'a': s([games['Skipping'] - games['Hopscotch']]), 'b': s([sum(games.values())])}


@check('L1U03-S03')
def _():
    tf = lambda b: ['True' if b else 'False']
    return {'a': tf(games['Catch'] > games['Hopscotch']), 'b': tf(games['Marbles'] == 4)}


@check('L1U03-S04')
def _():
    asked = 5   # the size of the school is not given and 5 friends are a small part of it
    return ['We cannot tell'] if asked < 10 else ['Yes']


@check('L1U03-S05')
def _():
    return {'a': [most(stickers)], 'b': s([stickers['Ben']]), 'c': s([stickers['Mei'] - stickers['Siti']])}


@check('L1U03-S06')
def _():
    return {'a': s([stickers['Ali'] + stickers['Ben']]), 'b': s([stickers['Ben'] + 2])}


@check('L1U03-S07')
def _():
    return s([sum([7, 4, 2])])


@check('L1U03-S08')
def _():
    return {'a': [most(cookies)], 'b': s([cookies['Thursday']]), 'c': s([cookies['Friday'] - cookies['Monday']])}


@check('L1U03-S09')
def _():
    ali = 5
    return s([ali + 3])


@check('L1U03-S10')
def _():
    return s([12 - 7])


@check('L1U03-T01')
def _():
    key = 2
    pics = {'Drawing': 4, 'Singing': 3, 'Chess': 5 + 0.5}
    kids = {k: v * key for k, v in pics.items()}   # a half picture is half of 2 = 1 child
    return {'a': s([int(kids['Chess'])]), 'b': s([int(kids['Chess'] - kids['Singing'])])}


@check('L1U03-T02')
def _():
    seen = [9, 6, 8]
    farm = [x for x in range(0, 31) if sum(seen) + x == 30]
    assert len(farm) == 1
    votes = {'Zoo': 9, 'Museum': 6, 'Beach': 8, 'Farm': farm[0]}
    return {'a': s(farm), 'b': [most(votes)]}


@check('L1U03-T03')
def _():
    p, q = 6 * 1, 2 * 5
    return {'a': s([p, q]), 'b': ['Graph P' if p > q else 'Graph Q']}


@check('L1U03-G01')
def _():
    sols = []
    for lily in range(0, 25):
        for jamie in range(0, 25):
            ray = jamie
            if 7 + lily + jamie + ray == 24 and lily == 7 - 2:
                sols.append((lily, jamie))
    assert len(sols) == 1
    return {'a': s([sols[0][0]]), 'b': s([sols[0][1]])}


@check('L1U03-G02')
def _():
    sols = [(k, k + 2, k + 1) for k in range(0, 19) if k + (k + 2) + (k + 1) == 18]
    assert len(sols) == 1
    return {'a': s([sols[0][0]]), 'b': s([sols[0][1]]), 'c': s([sols[0][2]])}


@check('L1U03-G03')
def _():
    wei = sum([2] * 6)
    siti = [n for n in range(0, 20) if 3 * n == wei]
    assert len(siti) == 1
    return {'a': s([wei]), 'b': s(siti)}


@check('L1U03-C01')
def _():
    return s([books['Kumar']])


@check('L1U03-C02')
def _():
    return s([books['Kumar'] - books['Aisha']])


@check('L1U03-C03')
def _():
    return s([sum(books.values())])


@check('L1U03-C04')
def _():
    return [fewest(books)]
