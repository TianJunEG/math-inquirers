"""The 30 Primary 2 outcome lines, in the wording of the syllabus PDF (Primary Mathematics Syllabus P1 to P6, 2021 edition,
updated Oct 2025, pages 33 and 34), the two semester booklets and the page order of each.
Plan: docs/school_books/p2_semester_booklets_plan.md. Wording copied from the PDF (also in docs/school_books/p2_outcome_wording.md)."""

# id -> (strand heading used on the key, outcome wording as printed in the PDF)
OUTCOMES = {
    "WN1.1": ("Whole Numbers", "counting in tens/hundreds"),
    "WN1.2": ("Whole Numbers", "number notation, representations and place values (hundreds, tens, ones)"),
    "WN1.3": ("Whole Numbers", "reading and writing numbers in numerals and in words"),
    "WN1.4": ("Whole Numbers", "comparing and ordering numbers"),
    "WN1.5": ("Whole Numbers", "patterns in number sequences"),
    "WN1.6": ("Whole Numbers", "odd and even numbers"),
    "AS2.1": ("Addition and Subtraction", "addition and subtraction algorithms (up to 3 digits)"),
    "AS2.2": ("Addition and Subtraction", "mental calculation involving addition and subtraction of a 3-digit number and ones/tens/hundreds"),
    "MD3.1": ("Multiplication and Division", "multiplication tables of 2, 3, 4, 5 and 10"),
    "MD3.2": ("Multiplication and Division", "use of ÷"),
    "MD3.3": ("Multiplication and Division", "relationship between multiplication and division"),
    "MD3.4": ("Multiplication and Division", "multiplying and dividing within the multiplication tables"),
    "MD3.5": ("Multiplication and Division", "mental calculation involving multiplication and division within multiplication tables of 2, 3, 4, 5 and 10"),
    "FR1.1": ("Fractions", "fraction as part of a whole"),
    "FR1.2": ("Fractions", "notation and representations of fractions"),
    "FR1.3": ("Fractions", "comparing and ordering fractions with denominators of given fractions not exceeding 12 (unit fractions; like fractions)"),
    "FR2.1": ("Fractions", "adding and subtracting like fractions within one whole with denominators of given fractions not exceeding 12"),
    "MO1.1": ("Money", "counting amount of money in dollars and cents"),
    "MO1.2": ("Money", "reading and writing money in decimal notation"),
    "MO1.3": ("Money", "comparing two or three amounts of money"),
    "MO1.4": ("Money", "converting an amount of money in decimal notation to cents only, and vice versa"),
    "ME1.1": ("Length, Mass and Volume", "measuring (length in metres; mass in kilograms/grams; volume of liquid in litres)"),
    "ME1.2": ("Length, Mass and Volume", "using appropriate units of measurement and their abbreviations m, g, kg, ℓ"),
    "ME1.3": ("Length, Mass and Volume", "comparing and ordering (lengths; masses; volumes)"),
    "TI2.1": ("Time", "telling time to the minute"),
    "TI2.2": ("Time", "measuring time in hours and minutes"),
    "TI2.3": ("Time", "converting time in hours and minutes to minutes only, and vice versa"),
    "GE1.1": ("2D Shapes", "making/completing patterns with 2D shapes according to one or two of the following attributes (size; shape; colour; orientation)"),
    "GE2.1": ("3D Shapes", "identifying, naming, describing and classifying 3D shapes (cube, cuboid, cone, cylinder, sphere)"),
    "ST1.1": ("Picture Graphs with Scales", "reading and interpreting data from picture graphs with scales"),
}
assert len(OUTCOMES) == 30

# page number (P2-nn, build order) -> outcome ids exercised
PAGE_OC = {}

# the two booklets: page numbers in booklet order (S1-01 .. S1-20, S2-01 .. S2-20)
BOOKLETS = {
    "S1": dict(name="Semester 1", terms="Terms 1 and 2", n=1,
               order=[1, 38, 9, 12, 10, 11, 17, 2, 3, 13, 18, 4, 5, 14, 19, 20, 39, 15, 21, 22]),
    "S2": dict(name="Semester 2", terms="Terms 3 and 4", n=2,
               order=[6, 16, 23, 24, 8, 25, 26, 27, 28, 7, 30, 29, 31, 32, 33, 34, 35, 36, 37, 40]),
}
assert sorted(BOOKLETS["S1"]["order"] + BOOKLETS["S2"]["order"]) == list(range(1, 41))

def booklet_of(no):
    for k, b in BOOKLETS.items():
        if no in b["order"]: return k, b["order"].index(no) + 1
    raise KeyError(no)

def code_of(no):
    """footer / key code with both numbers, e.g. 'S1-07 (P2-17)'"""
    k, pos = booklet_of(no)
    return f"{k}-{pos:02d} (P2-{no:02d})"

def oc_label(i):
    """short outcome label for the key: 'Whole Numbers 1.3'"""
    return f"{OUTCOMES[i][0]} {i[2:]}"
