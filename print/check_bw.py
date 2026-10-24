#!/usr/bin/env python3
"""Check B&W print PDFs: share of non-grey pixels (must be ~0), share of ink pages, and light-tint risk.
    python3 print/check_bw.py [files...]      (default: everything in outputs/print/bw)
"""
import glob, os, sys
import numpy as np, fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check(files, dpi=100):
    bad = 0
    for f in files:
        doc = fitz.open(f)
        worst_col, worst_light, blank = 0, 0, 0
        for page in doc:
            pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csRGB, alpha=False)
            a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3).astype(int)
            nongrey = float((np.abs(a[..., 0] - a[..., 1]) + np.abs(a[..., 1] - a[..., 2]) > 6).mean())
            grey = a.mean(-1)
            ink = float((grey < 128).mean())
            # area at 100 dpi whose local average darkness is 1-15% (a light tint that would not reproduce reliably)
            k = 8
            h, w = grey.shape[0] // k * k, grey.shape[1] // k * k
            cell = (grey[:h, :w] < 128).reshape(h // k, k, w // k, k).mean((1, 3))
            light = float(((cell > 0.01) & (cell < 0.15)).mean())
            worst_col = max(worst_col, nongrey)
            worst_light = max(worst_light, light)
            blank += ink < 0.0005
        flag = 'FAIL' if worst_col > 0.0005 else 'ok'
        bad += flag == 'FAIL'
        print(f'{flag} {os.path.basename(f)}: pages={len(doc)} blank={blank} max non-grey={worst_col:.5f} max light-tint cells={worst_light:.3f}')
    return bad


if __name__ == '__main__':
    fs = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'outputs/print/bw/**/*.pdf'), recursive=True))
    sys.exit(1 if check(fs) else 0)
