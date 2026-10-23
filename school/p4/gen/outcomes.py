"""The 42 Primary 4 outcome lines, in the wording of the syllabus PDF (Primary Mathematics Syllabus P1 to P6, 2021 edition,
updated Oct 2025, pages 37 to 40), the two semester booklets and the page order of each.
Plan: docs/school_books/p4_semester_booklets_plan.md. Wording copied from the PDF (also in docs/school_books/p4_outcome_wording.md)."""

# id -> (heading used on the key, outcome wording as printed in the PDF)
# id letters: NU numbers up to 100 000, FM factors and multiples, FO four operations, MI mixed numbers and improper fractions, FS fraction of a set,
# FA fractions: addition and subtraction, DP decimals up to 3 decimal places, DA decimals: addition and subtraction, DM decimals: multiplication and division,
# AP area and perimeter, AN angles, RS rectangle and square, LS line symmetry, NT nets, ST tables, line graphs and pie charts
OUTCOMES = {
    "NU1.1": ("Numbers up to 100 000", "number notation, representations and place values (ten thousands, thousands, hundreds, tens, ones)"),
    "NU1.2": ("Numbers up to 100 000", "reading and writing numbers in numerals and in words"),
    "NU1.3": ("Numbers up to 100 000", "comparing and ordering numbers"),
    "NU1.4": ("Numbers up to 100 000", "patterns in number sequences"),
    "NU1.5": ("Numbers up to 100 000", "rounding numbers to the nearest 10, 100 or 1000"),
    "NU1.6": ("Numbers up to 100 000", "use of ≈"),
    "FM2.1": ("Factors and Multiples", "factors, multiples and their relationship"),
    "FM2.2": ("Factors and Multiples", "determining if a 1-digit number is a factor of a given number within 100"),
    "FM2.3": ("Factors and Multiples", "finding the common factors of two given numbers"),
    "FM2.4": ("Factors and Multiples", "determining if a number is a multiple of a given 1-digit number"),
    "FM2.5": ("Factors and Multiples", "finding the common multiples of two given 1-digit numbers"),
    "FO3.1": ("Four Operations", "multiplication algorithm (up to 4 digits by 1 digit; up to 3 digits by 2 digits)"),
    "FO3.2": ("Four Operations", "division algorithm (up to 4 digits by 1 digit)"),
    "MI1.1": ("Mixed Numbers and Improper Fractions", "mixed numbers, improper fractions and their relationship"),
    "FS2.1": ("Fraction of a Set", "fraction as part of a set"),
    "FA3.1": ("Fractions: Addition and Subtraction", "adding and subtracting fractions with denominators of given fractions not exceeding 12 and not more than two different denominators"),
    "DP1.1": ("Decimals up to 3 decimal places", "notation, representations and place values (tenths, hundredths, thousandths)"),
    "DP1.2": ("Decimals up to 3 decimal places", "comparing and ordering decimals"),
    "DP1.3": ("Decimals up to 3 decimal places", "expressing decimals as fractions"),
    "DP1.4": ("Decimals up to 3 decimal places", "expressing fractions as decimals when the denominator is a factor of 10 or 100"),
    "DP1.5": ("Decimals up to 3 decimal places", "rounding decimals to the nearest whole number, 1 decimal place, 2 decimal places"),
    "DA2.1": ("Decimals: Addition and Subtraction", "adding and subtracting decimals (up to 2 decimal places)"),
    "DM3.1": ("Decimals: Multiplication and Division", "multiplying and dividing decimals (up to 2 decimal places) by a 1-digit whole number"),
    "DM3.2": ("Decimals: Multiplication and Division", "dividing a whole number by a whole number with quotient as a decimal"),
    "DM3.3": ("Decimals: Multiplication and Division", "rounding answers to a specified degree of accuracy"),
    "AP1.1": ("Area and Perimeter", "finding one dimension of a rectangle given the other dimension and its area/perimeter"),
    "AP1.2": ("Area and Perimeter", "finding the length of one side of a square given its area/perimeter"),
    "AP1.3": ("Area and Perimeter", "finding the area and perimeter of composite figures made up of rectangles and squares"),
    "AN1.1": ("Angles", "using notation such as ∠ABC and ∠a to name angles"),
    "AN1.2": ("Angles", "measuring angles in degrees"),
    "AN1.3": ("Angles", "drawing an angle of given size"),
    "RS2.1": ("Rectangle and Square", "properties of rectangle and square, excluding diagonal properties"),
    "RS2.2": ("Rectangle and Square", "drawing rectangles and squares"),
    "LS3.1": ("Line Symmetry", "identifying symmetric figures"),
    "LS3.2": ("Line Symmetry", "determining whether a straight line is a line of symmetry of a symmetric figure"),
    "LS3.3": ("Line Symmetry", "completing a symmetric figure with respect to a given line of symmetry on square grid"),
    "NT4.1": ("Nets", "identifying 2D representations of cube, cuboid, cone, cylinder, prism, pyramid"),
    "NT4.2": ("Nets", "drawing 2D representations of cube, cuboid, prism, pyramid"),
    "NT4.3": ("Nets", "identifying the nets of 3D solids (cube, cuboid, prism, pyramid)"),
    "NT4.4": ("Nets", "identifying the solid which can be formed by a given net"),
    "ST1.1": ("Tables, Line Graphs and Pie Charts", "completing a table from given data"),
    "ST1.2": ("Tables, Line Graphs and Pie Charts", "reading and interpreting data from tables/line graphs/pie charts"),
}
assert len(OUTCOMES) == 42

# page number (P4-nn, build order) -> outcome ids exercised (filled by build.py from the pages)
PAGE_OC = {}

# the two booklets: page numbers in booklet order (S1-01 .. S1-20, S2-01 .. S2-20)
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
    """footer / key code with both numbers, e.g. 'S1-07 (P4-07)'"""
    k, pos = booklet_of(no)
    return f"{k}-{pos:02d} (P4-{no:02d})"

def oc_label(i):
    """short outcome label for the key: 'Numbers up to 100 000 1.5'"""
    return f"{OUTCOMES[i][0]} {i[2:]}"
