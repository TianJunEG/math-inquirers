"""Semester 1, part A: P5-01 Millions; P5-02 Seven Digits; P5-03 Ten, Hundred, Thousand; P5-04 Multiples Route; P5-05 (colour by code, in pages_cbc);
P5-06 Brackets Match; P5-07 Both Sides Equal."""
import random, re, math, itertools
from fractions import Fraction
from .common import *
from .kit import *
from .kit5 import *
from .numwords import words, words_to_int

# =============================================================================== P5-01 Millions (lettered choices)
def digits_of(n): return [int(c) for c in str(n)]

def page01():
    rng = random.Random(5101)
    for _attempt in range(200):
        word = word_candidates(1, 6)[0]
        rows = []
        # 1. the value of a digit
        n1 = rng.choice([x for x in range(1_000_000, 9_999_999) if len(set(str(x))) == 7 and "0" not in str(x)])
        pos = rng.randint(2, 5); d = str(n1)[::-1][pos]
        v = int(d) * 10 ** pos
        rows.append(dict(q=f"In {num(n1)}, what is the value of the digit {d}?", opts=[num(v), num(v * 10), num(v // 10)], kind="value"))
        # 2. numeral to words (wrong: the other place values mixed up)
        a, b, c = rng.randint(1, 9), rng.randint(1, 9), rng.randint(1, 9)
        n2 = a * 1_000_000 + rng.choice([0, 0, 40, 400]) * 1000 + b * 100 + c * 10 + rng.choice([0, 5])
        n2w = [n2, (n2 // 1000) * 1000 + n2 % 1000 * 10 if False else n2 + 9000 if False else n2 * 10 // 10]
        right = words(n2)
        wrong1 = words(n2 + (900_000 if n2 % 1_000_000 < 100_000 else -n2 % 1_000_000 + 0) ) if False else None
        # wrong readings: millions digit and thousands group exchanged; a zero placed in the wrong group
        m, rest = divmod(n2, 1_000_000)
        alt1 = (rest // 1000) * 1000 + m if False else m * 1_000_000 + (rest // 10 if rest % 10 == 0 and rest > 0 else rest // 1000 * 1000 + rest % 1000) if False else None
        rows.append(None)
        # 3..6 are filled below
        break
    return None
