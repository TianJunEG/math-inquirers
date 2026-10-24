#!/usr/bin/env python3
"""Photocopy simulation: render a PDF page at 150 dpi, grey, slight blur (toner spread), then 1-bit threshold. usage: sim.py in.pdf outprefix [thr]"""
import sys, subprocess, os
from PIL import Image, ImageFilter
pdf, pre = sys.argv[1], sys.argv[2]; thr = int(sys.argv[3]) if len(sys.argv) > 3 else 128
subprocess.run(["pdftoppm", "-r", "150", "-gray", "-png", pdf, pre + "_g150"], check=True)
import glob
for f in sorted(glob.glob(pre + "_g150-*.png")):
    im = Image.open(f).filter(ImageFilter.GaussianBlur(0.6))
    im.point(lambda x: 255 if x > thr else 0).convert("1").save(f.replace("_g150", "_bw150"))
