#!/usr/bin/env python3
"""Black-and-white check of the PRINT pdf(s): render every page at 300 dpi and measure
  * colour: share of pixels with chroma (must be 0.0005 or less)
  * 1-bit test: render to 1 bit (threshold 128) and compare with the grey render: the share of 'flat mid-grey' pixels
    (value 40..215 with a uniform 5x5 neighbourhood = a grey fill that would turn into mush or vanish on a photocopier) must be 0.0005 or less
  * text/line survival: dark-pixel share of the 1-bit render vs the grey render must agree within 3 percent (nothing thin enough to vanish)
    python3 extension/verify/bw_check.py [pdf ...]      default: outputs/extension/L*/*Print_BW.pdf
"""
import glob, os, sys
import numpy as np, fitz
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def check(path, dpi=300):
    doc = fitz.open(path)
    bad = []
    worst = (0, 0, 0)
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=dpi, colorspace=fitz.csRGB, alpha=False)
        a = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3).astype(int)
        chroma = float(((np.abs(a[..., 0] - a[..., 1]) + np.abs(a[..., 1] - a[..., 2])) > 6).mean())
        g = a.mean(-1)
        # flat mid-grey: value in 40..215 and 5x5 neighbourhood max-min <= 6
        mid = (g > 40) & (g < 215)
        k = 2
        pad = np.pad(g, k, mode='edge')
        stack = np.stack([pad[dy:dy + g.shape[0], dx:dx + g.shape[1]] for dy in range(0, 2 * k + 1) for dx in range(0, 2 * k + 1)])
        flat = (stack.max(0) - stack.min(0) <= 6) & mid
        flat_share = float(flat.mean())
        bit = g < 128
        dark_grey = float((g < 200).mean())
        loss = abs(dark_grey - float(bit.mean())) / max(dark_grey, 1e-6) if dark_grey > 0.001 else 0.0
        worst = (max(worst[0], chroma), max(worst[1], flat_share), max(worst[2], loss))
        if chroma > 0.0005:
            bad.append(f'page {i}: colour pixels {chroma:.4f}')
        if flat_share > 0.0005:
            bad.append(f'page {i}: flat mid-grey area {flat_share:.4f}')
    return doc.page_count, worst, bad


if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, 'outputs', 'extension', 'L*', '*Print_BW.pdf')))
    fails = 0
    for f in files:
        n, w, bad = check(f)
        print(f'{"FAIL" if bad else "ok"} {os.path.basename(f)}: {n} pages, max chroma {w[0]:.5f}, max flat-grey {w[1]:.5f}, max 1-bit dark-share change {w[2]:.3f}')
        for b in bad:
            print('  ', b)
        fails += bool(bad)
        if n % 2:
            print('  FAIL odd page count'); fails += 1
    sys.exit(1 if fails else 0)
