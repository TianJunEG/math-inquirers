"""The galleries. Each level keeps its own GALLERY list inside its bank file (banks_pN.py); this module only gathers them.
Every worksheet is one picture + one topic bank + one tier (1 = one star, 2 = two stars)."""
from banks import gallery, levels
GALLERY = [g for n in levels() for g in gallery(n)]      # all levels (older callers)
def gallery_for(level): return gallery(level)
