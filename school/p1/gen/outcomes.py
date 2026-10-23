"""The 32 Primary 1 outcome lines, in the wording of the syllabus PDF (Primary Mathematics Syllabus P1 to P6, 2021 edition,
updated Oct 2025, pages 31 and 32), the two semester booklets and the page order of each.
Plan: docs/school_books/p1_semester_booklets_plan.md (sections 1a and 2). Wording copied from the PDF."""

# id -> (strand heading used on the key, outcome wording as printed in the PDF)
OUTCOMES = {
    "WN1.1": ("Whole Numbers", "counting to tell the number of objects in a given set"),
    "WN1.2": ("Whole Numbers", "number notation, representations and place values (tens, ones)"),
    "WN1.3": ("Whole Numbers", "reading and writing numbers in numerals and in words"),
    "WN1.4": ("Whole Numbers", "comparing the number of objects in two or more sets"),
    "WN1.5": ("Whole Numbers", "comparing and ordering numbers"),
    "WN1.6": ("Whole Numbers", "patterns in number sequences"),
    "WN1.7": ("Whole Numbers", "ordinal numbers (first, second, up to tenth) and symbols (1st, 2nd, 3rd, etc.)"),
    "AS2.1": ("Addition and Subtraction", "concepts of addition and subtraction"),
    "AS2.2": ("Addition and Subtraction", "use of +, - and ="),
    "AS2.3": ("Addition and Subtraction", "relationship between addition and subtraction"),
    "AS2.4": ("Addition and Subtraction", "adding more than two 1-digit numbers"),
    "AS2.5": ("Addition and Subtraction", "adding and subtracting within 100"),
    "AS2.6": ("Addition and Subtraction", "adding and subtracting using algorithms"),
    "AS2.7": ("Addition and Subtraction", "mental calculation involving addition and subtraction (within 20; 2-digit number and ones without renaming; 2-digit number and tens)"),
    "MD3.1": ("Multiplication and Division", "concepts of multiplication and division"),
    "MD3.2": ("Multiplication and Division", "use of x"),
    "MD3.3": ("Multiplication and Division", "multiplying within 40"),
    "MD3.4": ("Multiplication and Division", "dividing within 20"),
    "MO1.1": ("Money", "counting amount of money (in cents up to $1; in dollars up to $100)"),
    "LE1.1": ("Length", "measuring length in centimetres"),
    "LE1.2": ("Length", "use of abbreviation cm"),
    "LE1.3": ("Length", "comparing and ordering lengths in cm"),
    "LE1.4": ("Length", "measuring and drawing a line segment to the nearest cm"),
    "TI2.1": ("Time", "telling time to 5 minutes"),
    "TI2.2": ("Time", "use of 'am' and 'pm'"),
    "TI2.3": ("Time", "use of abbreviations h and min"),
    "TI2.4": ("Time", "duration of one hour/half hour"),
    "GE1.1": ("2D Shapes", "identifying, naming, describing and classifying 2D shapes (rectangle, square, triangle, circle, half circle, quarter circle)"),
    "GE1.2": ("2D Shapes", "forming different 2D figures with rectangle, square, triangle, half circle, quarter circle"),
    "GE1.3": ("2D Shapes", "identifying the 2D shapes that make up a given figure"),
    "GE1.4": ("2D Shapes", "copying figures on dot grid or square grid"),
    "ST1.1": ("Picture Graphs", "reading and interpreting data from picture graphs"),
}
assert len(OUTCOMES) == 32

# page number (P1-nn) -> outcome ids exercised (plan 2a and 2b)
PAGE_OC = {
    1: ["WN1.1", "WN1.2"], 2: ["WN1.2", "WN1.5"], 3: ["MD3.1", "MD3.4"], 4: ["WN1.5"], 5: ["MD3.1", "MD3.2", "MD3.3"],
    6: ["TI2.1"], 7: ["WN1.7"], 8: ["AS2.1", "AS2.2", "AS2.7"], 9: ["AS2.4"], 10: ["AS2.1", "AS2.3", "AS2.7"],
    11: ["AS2.5", "AS2.7"], 12: ["GE1.1"], 13: ["MD3.1", "MD3.2", "MD3.3"], 14: ["WN1.6"], 15: ["MO1.1"],
    16: ["MO1.1", "AS2.7"], 17: ["LE1.1", "LE1.2"], 18: ["TI2.1", "TI2.4"], 19: ["GE1.1", "GE1.3"], 20: ["ST1.1"],
    21: ["AS2.1", "AS2.2", "AS2.7"],                   # N01 Story Sums
    22: ["AS2.1", "AS2.2", "AS2.5", "AS2.7"],          # N02 Two-Step Stories
    23: ["AS2.5", "AS2.6"],                            # N10 Stack It Up
    24: ["WN1.3", "WN1.7"],                            # N04 Words and Numbers
    25: ["WN1.1", "WN1.4"],                            # N05 Count the Crowd
    26: ["WN1.6", "WN1.2", "WN1.5"],                   # N06 Hundred Chart Patterns
    27: ["MO1.1", "AS2.5"],                            # N13 Which Two Items?
    28: ["MO1.1"],                                     # N14 Fewest Coins
    29: ["TI2.3", "TI2.4", "TI2.1"],                   # N17 How Long Does It Last?
    30: ["TI2.1", "TI2.2"],                            # N18 Morning or Evening?
    31: ["LE1.2", "LE1.3"],                            # N15 Longer, Shorter, Longest
    32: ["LE1.1", "LE1.2", "LE1.4"],                   # N16 Measure and Draw a Line
    33: ["GE1.1", "GE1.2", "GE1.3"],                   # N19 Shape Builder
    34: ["GE1.4"],                                     # N20 Finish the Figure (replaces "copy on the grid")
    35: ["ST1.1"],                                     # N21 Read the Picture Graph
    36: ["ST1.1"],                                     # N22 Graph Detective Two
    37: ["AS2.1", "AS2.2", "AS2.3"],                   # N09 Bonds and Families
    38: ["WN1.4", "AS2.1"],                            # N03 More or Fewer
    39: ["MD3.1", "MD3.4"],                            # N11 Share and Group Stories
    40: ["MD3.1", "MD3.2", "MD3.3"],                   # N12 True or False Groups
}

# the two booklets: final page numbers in booklet order (S1-01 .. S1-20, S2-01 .. S2-20)
BOOKLETS = {
    "S1": dict(name="Semester 1", terms="Terms 1 and 2", n=1,
               order=[25, 1, 24, 12, 19, 7, 8, 37, 10, 21, 9, 38, 2, 4, 26, 33, 34, 31, 17, 13]),
    "S2": dict(name="Semester 2", terms="Terms 3 and 4", n=2,
               order=[3, 39, 14, 5, 40, 11, 23, 32, 6, 15, 28, 16, 27, 18, 30, 29, 35, 20, 36, 22]),
}
assert sorted(BOOKLETS["S1"]["order"] + BOOKLETS["S2"]["order"]) == list(range(1, 41))

def booklet_of(no):
    for k, b in BOOKLETS.items():
        if no in b["order"]: return k, b["order"].index(no) + 1
    raise KeyError(no)

def code_of(no):
    """footer / key code with both numbers, e.g. 'S1-07 (P1-08)'"""
    k, pos = booklet_of(no)
    return f"{k}-{pos:02d} (P1-{no:02d})"

def oc_label(i):
    """short outcome label for the key: 'Whole Numbers 1.3'"""
    return f"{OUTCOMES[i][0]} {i[2:]}"
