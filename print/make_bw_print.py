#!/usr/bin/env python3
"""Black-and-white PRINT pipeline: colour print PDFs -> 1-bit 600 dpi B&W print PDFs, same pages/binding/blank backs/gutter.

    python3 print/make_bw_print.py              # convert every colour print PDF found in outputs/print and outputs/print/term
    python3 print/make_bw_print.py --rebuild    # first re-run print/make_print_pdfs.py and print/make_term_books.py (colour), then convert
    python3 print/make_bw_print.py --check      # also run the non-grey / tint measurement on the results

Colour print PDFs stay where they are (soft copies / colour reference). Output: outputs/print/bw/ (holiday) and outputs/print/bw/term/.
Conversion is colour-aware, so meaning carried by colour survives on a photocopier:
  dark pixels (luma < 0.42) -> solid black;   very light tints (luma > 0.90, e.g. the pale grid paper and cream boxes) -> white;
  mid-tone fills -> a pattern chosen by HUE FAMILY (red: / hatch, orange-gold: dots, green: \\ hatch, blue-teal: horizontal lines,
  purple: vertical lines, neutral grey: fine stipple) with the pattern weight following lightness (capped so text on it stays legible).
"""
import argparse, glob, json, os, subprocess, sys
import numpy as np
import fitz
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRINT = os.path.join(ROOT, 'outputs', 'print')
BW = os.path.join(PRINT, 'bw')
DPI = 600
DARK, LIGHT, MAXD = 0.42, 0.90, 0.5
P = 14  # pattern period in pixels (~0.6 mm at 600 dpi)


def classify(rgb):
    """rgb uint8 HxWx3 -> (luma float, hue family int 0..5, saturation)"""
    f = rgb.astype(np.float32) / 255.0
    r, g, b = f[..., 0], f[..., 1], f[..., 2]
    luma = 0.299 * r + 0.587 * g + 0.114 * b
    mx, mn = f.max(-1), f.min(-1)
    d = mx - mn
    sat = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0)
    dd = np.maximum(d, 1e-6)
    h = np.where(mx == r, ((g - b) / dd) % 6, np.where(mx == g, (b - r) / dd + 2, (r - g) / dd + 4)) * 60
    fam = np.full(h.shape, 5, np.uint8)          # 5 neutral
    colourful = sat > 0.22
    fam[colourful & ((h < 15) | (h >= 330))] = 0   # red / pink
    fam[colourful & (h >= 15) & (h < 70)] = 1      # orange / gold / yellow
    fam[colourful & (h >= 70) & (h < 170)] = 2     # green
    fam[colourful & (h >= 170) & (h < 255)] = 3    # blue / teal
    fam[colourful & (h >= 255) & (h < 330)] = 4    # purple
    return luma, fam, sat


def convert(rgb, y0=0):
    """Fast path: only mid-tone pixels (DARK <= luma <= LIGHT) need hue/pattern work."""
    c = rgb.astype(np.uint16)
    luma = ((c[..., 0] * 77 + c[..., 1] * 150 + c[..., 2] * 29) >> 8).astype(np.uint8)
    out = luma < int(DARK * 255)
    mid = (~out) & (luma <= int(LIGHT * 255))
    yy, xx = np.nonzero(mid)
    if len(yy):
        l, fam, _ = classify(rgb[yy, xx][None, :, :])
        l, fam = l[0], fam[0]
        y, x = yy + y0, xx
        dens = np.clip((0.97 - l) / 0.6, 0, MAXD)
        phase = np.zeros(len(yy), np.float32)
        for k, ph in ((0, ((x + y) % P) / P), (2, ((x - y) % P) / P), (3, (y % P) / P), (4, (x % P) / P)):
            phase = np.where(fam == k, ph, phase)
        dx, dy = (x % P) - P / 2 + .5, (y % P) - P / 2 + .5
        phase = np.where(fam == 1, np.clip((dx * dx + dy * dy) / (P / 2) ** 2, 0, 1), phase)   # dots: area ~ density
        bayer = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]], np.float32) / 16
        phase = np.where(fam == 5, bayer[y % 4, x % 4], phase)
        out[yy, xx] = phase < dens
    dropped = float(((luma > int(LIGHT * 255)) & (luma < 254)).mean())      # pale tints removed
    return out, dropped


def convert_page(args):
    src, i = args
    doc = fitz.open(src)
    pix = doc[i].get_pixmap(dpi=DPI, colorspace=fitz.csRGB, alpha=False)
    rgb = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, 3)
    out = np.zeros((pix.height, pix.width), bool)
    dropped = 0.0
    S = 700                                   # strip height: multiple of 4 and of P so patterns stay aligned
    for y0 in range(0, pix.height, S):
        o, d = convert(rgb[y0:y0 + S], y0)
        out[y0:y0 + S] = o
        dropped += d * o.shape[0]
    img = Image.fromarray(np.where(out, 0, 255).astype(np.uint8)).convert('1')
    return img.tobytes(), img.size, dropped / pix.height


def convert_pdf(src, dst):
    from multiprocessing import Pool
    n = len(fitz.open(src))
    with Pool(4) as pool:
        res = pool.map(convert_page, [(src, i) for i in range(n)])
    imgs = [Image.frombytes('1', size, data) for data, size, _ in res]
    imgs[0].save(dst, save_all=True, append_images=imgs[1:], resolution=DPI, compression='group4')
    return n, [round(r[2], 4) for r in res]


def targets():
    t = sorted(glob.glob(os.path.join(PRINT, 'Math_Inquirers_P*_Workbook_PRINT.pdf')))
    t += sorted(glob.glob(os.path.join(PRINT, 'term', '*_PRINT.pdf')))
    return t


def run_check(files):
    from check_bw import check
    return check(files)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--rebuild', action='store_true')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--resume', action='store_true', help='skip outputs that already exist and are newer than their source')
    ap.add_argument('--only', default='', help='substring filter on file names')
    a = ap.parse_args()
    if a.rebuild:
        subprocess.run([sys.executable, os.path.join(ROOT, 'print', 'make_print_pdfs.py')], check=True)
        subprocess.run([sys.executable, os.path.join(ROOT, 'print', 'make_term_books.py')], check=True)
    rows = []
    for src in targets():
        if a.only and a.only not in src:
            continue
        rel = os.path.relpath(src, PRINT)
        dst = os.path.join(BW, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if a.resume and os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src):
            n = len(fitz.open(dst)); rows.append(dict(file=os.path.relpath(dst, ROOT), pages=n, sheets=n // 2, mb=round(os.path.getsize(dst) / 1e6, 2), pale_tint_dropped_max=None))
            print('skip (up to date)', rel); continue
        n, dropped = convert_pdf(src, dst)
        rows.append(dict(file=os.path.relpath(dst, ROOT), pages=n, sheets=n // 2, mb=round(os.path.getsize(dst) / 1e6, 2),
                         pale_tint_dropped_max=max(dropped)))
        print(rows[-1], flush=True)
    json.dump(rows, open(os.path.join(BW, 'bw_spec.json'), 'w'), indent=1)
    if a.check:
        sys.path.insert(0, os.path.dirname(__file__))
        run_check([os.path.join(ROOT, r['file']) for r in rows])
