"""Builds gen/words_en.txt.gz for Primary 6: every word of 2 to 9 letters from three public lists
(the P1/P2 129 000-word list, `english_words` web2 = 262 866 entries, and `wordfreq` top 150 000 English words).
A wrong placement that spells ANY of them counts as a wrong answer that the pupil's "do the letters spell a word?" check would accept.
Run once:  python3 gen/make_words.py"""
import gzip, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
words = set(gzip.open(os.path.join(HERE, "words_en.txt.gz"), "rt").read().split())
n0 = len(words)
from english_words import get_english_words_set
words |= {w.lower() for w in get_english_words_set(["web2"], lower=True)}
import wordfreq
words |= {w for w in wordfreq.top_n_list("en", 150000)}
words = {w for w in words if re.fullmatch(r"[a-z]{2,9}", w)}
with gzip.open(os.path.join(HERE, "words_en.txt.gz"), "wt") as f:
    f.write("\n".join(sorted(words)))
print(n0, "->", len(words))
