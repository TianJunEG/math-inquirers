"""The 34 Primary 3 outcome lines, the two semester booklets and the page order of each.
Wording: as recorded in docs/school_books/p3_outcome_wording.md (the syllabus PDF itself is not in the repository; the wording was recorded
from pages 35 and 36 of the PDF by the paused Primary 3 note and docs/moe/syllabus_by_level.md, and must be re-read against the PDF before print).
Plan: docs/school_books/p3_semester_booklets_plan.md."""

# id -> (strand heading used on the key, outcome wording)
OUTCOMES = {
    "WN1.1": ("Whole Numbers", "counting in hundreds/thousands"),
    "WN1.2": ("Whole Numbers", "number notation, representations and place values"),
    "WN1.3": ("Whole Numbers", "reading and writing numbers in numerals and in words"),
    "WN1.4": ("Whole Numbers", "comparing and ordering numbers"),
    "WN1.5": ("Whole Numbers", "patterns in number sequences"),
    "AS2.1": ("Addition and Subtraction", "addition and subtraction algorithms (up to 4 digits)"),
    "AS2.2": ("Addition and Subtraction", "mental calculation involving addition and subtraction of two 2-digit numbers"),
    "MD3.1": ("Multiplication and Division", "multiplication tables of 6, 7, 8 and 9"),
    "MD3.2": ("Multiplication and Division", "multiplying and dividing within the multiplication tables"),
    "MD3.3": ("Multiplication and Division", "division with remainder"),
    "MD3.4": ("Multiplication and Division", "multiplication and division algorithms (up to 3 digits by 1 digit)"),
    "MD3.5": ("Multiplication and Division", "mental calculation involving multiplication and division within the multiplication tables"),
    "FR1.1": ("Fractions", "equivalent fractions"),
    "FR1.2": ("Fractions", "simplest form"),
    "FR1.3": ("Fractions", "comparing and ordering unlike fractions (denominators not exceeding 12)"),
    "FR1.4": ("Fractions", "finding an equivalent fraction given the denominator or numerator"),
    "FR2.1": ("Fractions", "adding and subtracting two related fractions within one whole"),
    "MO1.1": ("Money", "adding and subtracting money in decimal notation"),
    "ME1.1": ("Length, Mass and Volume", "measuring length in kilometres and volume in millilitres"),
    "ME1.2": ("Length, Mass and Volume", "compound units"),
    "ME1.3": ("Length, Mass and Volume", "converting units (km and m, m and cm, kg and g, l and ml)"),
    "TI2.1": ("Time", "measuring time in seconds"),
    "TI2.2": ("Time", "finding the starting time, finishing time or duration given the other two quantities"),
    "TI2.3": ("Time", "24-hour clock"),
    "AP1.1": ("Area and Perimeter", "concepts of area and perimeter"),
    "AP1.2": ("Area and Perimeter", "area in square units, cm2 and m2"),
    "AP1.3": ("Area and Perimeter", "perimeter of a rectilinear figure, a rectangle and a square"),
    "AP1.4": ("Area and Perimeter", "area of a rectangle and a square"),
    "AN1.1": ("Angles", "concept of an angle"),
    "AN1.2": ("Angles", "right angles; angles greater than or smaller than a right angle"),
    "PP2.1": ("Perpendicular and Parallel Lines", "identifying perpendicular and parallel lines"),
    "PP2.2": ("Perpendicular and Parallel Lines", "drawing perpendicular and parallel lines"),
    "BG1.1": ("Bar Graphs", "reading and interpreting bar graphs"),
    "BG1.2": ("Bar Graphs", "bar graphs with different scales on the axis"),
}
assert len(OUTCOMES) == 34

# page number (P3-nn) -> outcome ids exercised (filled from the pages when build.py runs)
PAGE_OC = {}

# the two booklets: page numbers in booklet order (S1-01 .. S1-20, S2-01 .. S2-20); numbers 1..20 are Semester 1 and 21..40 Semester 2
BOOKLETS = {
    "S1": dict(name="Semester 1", terms="Terms 1 and 2", n=1, order=list(range(1, 21))),
    "S2": dict(name="Semester 2", terms="Terms 3 and 4", n=2, order=list(range(21, 41))),
}
assert sorted(BOOKLETS["S1"]["order"] + BOOKLETS["S2"]["order"]) == list(range(1, 41))

def booklet_of(no):
    for k, b in BOOKLETS.items():
        if no in b["order"]: return k, b["order"].index(no) + 1
    raise KeyError(no)

def code_of(no):
    """footer / key code with both numbers, e.g. 'S2-07 (P3-27)'"""
    k, pos = booklet_of(no)
    return f"{k}-{pos:02d} (P3-{no:02d})"

def oc_label(i):
    """short outcome label for the key: 'Whole Numbers 1.3'"""
    return f"{OUTCOMES[i][0]} {i[2:]}"
