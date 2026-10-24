"""Measure real rendered PDFs (pdftoppm pixel check), not the layout model."""
import os, subprocess, tempfile, glob
from PIL import Image


def pdf_pages(path):
    from pypdf import PdfReader
    return len(PdfReader(path).pages)


def pdf_fill(path, top_mm=14.0, bottom_mm=16.0, dpi=50):
    """Per page: (lowest dark-ink row inside the margins - top margin) / printable height."""
    out = []
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(['pdftoppm', '-r', str(dpi), '-gray', '-png', path, os.path.join(td, 'p')], check=True)
        for f in sorted(glob.glob(os.path.join(td, 'p-*.png'))):
            im = Image.open(f).convert('L'); w, h = im.size
            px = dpi / 25.4
            top, bot = int(top_mm * px), int(h - bottom_mm * px)
            last = top
            data = im.load()
            for y in range(bot - 1, top - 1, -1):
                if any(data[x, y] < 170 for x in range(0, w, 2)):
                    last = y; break
            out.append(max(0.0, (last - top) / (bot - top)))
    return out
