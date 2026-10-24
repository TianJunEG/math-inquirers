"""Level registry. A level is one file `banks_pN.py` in this folder that defines

    LEVEL   = N
    RULES   = dict(allow_division_sign=bool, time_words_only=bool)      # wording rules the verifier applies to that level's pages
    BANKS   = {bank_id: Bank(...)}                                       # the topic banks (see qcore.py)
    GALLERY = [dict(id=..., picture=..., bank=..., tier=1 or 2, seed=...), ...]   # the worksheets of that level

Dropping such a file into this folder is all that is needed: build.py, verify.py and compat.py find every banks_pN.py, write
out/pN/ and verify it. Pictures (pictures.py) are shared by all levels. `get_bank(level, id)` is what sheet.py uses."""
import glob, importlib, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
from qcore import *          # noqa: F401,F403  (re-exported so a bank file can also import from here)

LEVELS = {}
for _p in sorted(glob.glob(os.path.join(HERE, "banks_p[0-9].py"))):
    _n = int(re.search(r"banks_p(\d)\.py$", _p).group(1))
    _m = importlib.import_module(f"banks_p{_n}")
    assert _m.LEVEL == _n, f"{_p}: LEVEL must be {_n}"
    LEVELS[_n] = _m

def levels(): return sorted(LEVELS)
def banks(level): return LEVELS[level].BANKS
def get_bank(level, bank_id): return LEVELS[level].BANKS[bank_id]
def gallery(level):
    out = []
    for g in LEVELS[level].GALLERY:
        g = dict(g); g["level"] = level; out.append(g)
    return out
def rules(level): return getattr(LEVELS[level], "RULES", {})

BANKS = LEVELS[1].BANKS      # Primary 1 banks (kept for older callers)
