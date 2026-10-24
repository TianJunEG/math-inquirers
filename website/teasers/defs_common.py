"""Shared helpers for the puzzle definition files (defs_l1.py ... defs_l6.py)."""
import string
from fractions import Fraction as Fr

LEVEL_AGES = {1: '6-8', 2: '7-9', 3: '8-10', 4: '9-11', 5: '10-12', 6: '11-13'}

UNIT_SYN = {
    'cm': ['cm', 'centimetre', 'centimetres', 'centimeter', 'centimeters'],
    'm': ['m', 'metre', 'metres', 'meter', 'meters'],
    'km': ['km', 'kilometre', 'kilometres', 'kilometer', 'kilometers'],
    'kg': ['kg', 'kilogram', 'kilograms', 'kilogramme', 'kilogrammes'],
    'g': ['g', 'gram', 'grams'],
    'L': ['l', 'litre', 'litres', 'liter', 'liters'],
    'ml': ['ml', 'millilitre', 'millilitres', 'milliliter', 'milliliters'],
    'minutes': ['min', 'mins', 'minute', 'minutes'],
    'hours': ['h', 'hr', 'hrs', 'hour', 'hours'],
    'seconds': ['s', 'sec', 'secs', 'second', 'seconds'],
    'days': ['day', 'days'],
    'years': ['year', 'years'],
    'km/h': ['km/h', 'kmh', 'km/hr', 'kph', 'km per hour', 'kilometres per hour'],
    'm/min': ['m/min', 'm per min', 'm per minute', 'metres per minute'],
    '°': ['°', 'deg', 'degree', 'degrees'],
    '%': ['%', 'percent', 'per cent'],
    'cm²': ['cm²', 'cm2', 'cm^2', 'sq cm', 'square cm', 'square centimetres', 'square centimeters'],
    'm²': ['m²', 'm2', 'm^2', 'sq m', 'square m', 'square metres', 'square meters'],
    'cm³': ['cm³', 'cm3', 'cm^3', 'cubic cm', 'cubic centimetres', 'cubic centimeters'],
    'cents': ['c', 'cent', 'cents'],
    'dollars': ['dollar', 'dollars'],
    "o'clock": ["o'clock", 'oclock', "o’clock"],
}


class Fmt(string.Formatter):
    """Format specs: m = cents as dollars, n = thousands commas, j = list joined with 'and', o = ordinal,
    x = fraction as mixed number, f = fraction a/b, d = decimal, c = plain comma-less int."""

    def format_field(self, v, spec):
        if spec == 'm':
            c = int(v)
            return '$%d' % (c // 100) if c % 100 == 0 else '$%d.%02d' % (c // 100, c % 100)
        if spec == 'n':
            return '{:,}'.format(int(v))
        if spec == 'j':
            xs = [str(x) for x in v]
            return xs[0] if len(xs) == 1 else ', '.join(xs[:-1]) + ' and ' + xs[-1]
        if spec == 'o':
            n = int(v)
            suf = 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
            return '%d%s' % (n, suf)
        if spec == 'x':
            return show_frac(Fr(v), mixed=True)
        if spec == 'f':
            return show_frac(Fr(v), mixed=False)
        if spec == 'd':
            return dec_str(Fr(v))
        if spec == 'M':   # [whole, num, den] as a mixed number
            return '%d %d/%d' % tuple(v) if v[1] else str(v[0])
        return super().format_field(v, spec)


FMT = Fmt()


def dec_str(v):
    """Shortest exact decimal for a Fraction (denominator must be 2^a 5^b)."""
    v = Fr(v)
    if v == int(v):
        return str(int(v))
    d = v.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    assert d == 1, 'not a terminating decimal: %s' % v
    s = '%.6f' % float(v)
    s = s.rstrip('0').rstrip('.')
    assert Fr(s) == v, (s, v)
    return s


def show_frac(v, mixed):
    v = Fr(v)
    if v.denominator == 1:
        return str(v.numerator)
    if mixed and v > 1:
        w = v.numerator // v.denominator
        r = v - w
        return '%d %d/%d' % (w, r.numerator, r.denominator)
    return '%d/%d' % (v.numerator, v.denominator)


def P(frame, kind, topic, q, hint, why, p, t=None, unit=None, fmt='int', big=None, code=None,
      units=None, prefix=None, accept=None, exact=False, w=None, xq=None, sub=None):
    """One puzzle definition.  p = parameters handed to the solver and to the independent checker;
    t = text-only values (names, nouns) that appear in the wording; w = extra typical wrong answers;
    sub = the maths sub-structure id in taxonomy.json ('family.sub'); verify_bank.py enforces the per-quarter caps on it."""
    return dict(frame=frame, kind=kind, topic=topic, q=q, hint=hint, why=why, p=p, t=t or {}, unit=unit,
                fmt=fmt, big=big, code=code, units=units, prefix=prefix, accept=accept, exact=exact,
                w=w or [], sub=sub)
