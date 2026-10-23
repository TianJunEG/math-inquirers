"""Whole numbers in words (British, as in school papers) and an independent reader that turns the words back into a number."""
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()

def below100(n):
    return ONES[n] if n < 20 else TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")

def below1000(n):
    h, r = divmod(n, 100)
    if h == 0: return below100(r)
    return ONES[h] + " hundred" + (" and " + below100(r) if r else "")

def words(n):
    """4 305 070 -> 'four million, three hundred and five thousand and seventy'"""
    assert 0 < n < 10 ** 8
    parts = []
    m, rest = divmod(n, 1_000_000)
    if m: parts.append(below1000(m) + " million")
    t, o = divmod(rest, 1000)
    if t: parts.append(below1000(t) + " thousand")
    tail = None
    if o:
        if parts and o < 100: tail = "and " + below1000(o)
        else: parts.append(below1000(o))
    out = ", ".join(parts)
    return out + (" " + tail if tail else "")

def words_to_int(s):
    """independent reader: words -> int ('and', commas and hyphens ignored)"""
    toks = s.lower().replace(",", " ").replace("-", " ").split()
    total = 0; cur = 0
    for t in toks:
        if t == "and": continue
        if t in ONES: cur += ONES.index(t)
        elif t in TENS: cur += TENS.index(t) * 10
        elif t == "hundred": cur *= 100
        elif t == "thousand": total += cur * 1000; cur = 0
        elif t == "million": total += cur * 1_000_000; cur = 0
        else: raise ValueError(t)
    return total + cur
