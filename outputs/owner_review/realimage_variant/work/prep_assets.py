#!/usr/bin/env python3
"""Prepare greyscale, photocopy-safe versions of the downloaded MAS images (originals are never altered).
Coins: left half of each MAS coin image (the value / numeral side), tight crop, background removed to white, grey, contrast stretched, thin dark edge.
Notes: whole MAS image (it already carries MAS's own SPECIMEN label), greyscale, mild contrast stretch, thin black frame. Nothing is redrawn or distorted; scaling is proportional."""
import os, sys, json
import numpy as np
from PIL import Image, ImageOps, ImageFilter
from scipy import ndimage as ndi
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "source_mas"); OUT = os.path.join(HERE, "assets")
os.makedirs(OUT, exist_ok=True)
COINS = {5: "ts5cfull.jpg", 10: "ts10cfull.jpg", 20: "ts20cfull.jpg", 50: "ts50cfull.jpg", 100: "ts1dfull.jpg"}
NOTES = {2: "portrait-2-front-polymer.jpg", 5: "portrait-series-5-front.jpg", 10: "portrait-10-front-polymer.jpg"}
info = {}
def stretch(g, lo=2, hi=98, gamma=1.0):
    a = np.asarray(g, float); l, h = np.percentile(a, lo), np.percentile(a, hi)
    a = np.clip((a - l) / max(h - l, 1), 0, 1) ** gamma
    return Image.fromarray((a * 255).astype("uint8"))
for v, f in COINS.items():
    im = Image.open(os.path.join(SRC, f)).convert("RGB"); W, H = im.size
    left = im.crop((0, 0, W // 2, H))
    a = np.asarray(left).astype(int)
    bg = (a.min(axis=2) > 235)                       # near-white background
    lab, n = ndi.label(bg); border = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1]); border.discard(0)
    outside = np.isin(lab, list(border))
    inside = ~outside
    inside = ndi.binary_fill_holes(inside); inside = ndi.binary_opening(inside, iterations=1)
    ys, xs = np.where(inside); y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    s = max(y1 - y0, x1 - x0); cy, cx = (y0 + y1) / 2, (x0 + x1) / 2
    box = (int(round(cx - s / 2)), int(round(cy - s / 2)), int(round(cx - s / 2)) + s, int(round(cy - s / 2)) + s)
    g = ImageOps.grayscale(left)
    # stretch contrast using coin pixels only
    arr = np.asarray(g, float); cp = arr[inside]; lo, hi = np.percentile(cp, 1), np.percentile(cp, 99)
    arr = np.clip((arr - lo) / (hi - lo), 0, 1) ** 1.25 * 255      # gamma > 1 darkens mid greys so gold/silver detail survives a photocopier
    arr[~inside] = 255
    edge = ndi.binary_dilation(inside, iterations=2) & ~ndi.binary_erosion(inside, iterations=0 + 1)
    arr[edge] = np.minimum(arr[edge], 40)            # thin dark edge so a silver coin does not melt into the white page
    out = Image.fromarray(arr.astype("uint8")).crop(box)
    out.save(os.path.join(OUT, f"coin_{v}.png"))
    info[f"coin_{v}"] = dict(src=f, crop_px=[int(s), int(s)], bbox_in_left_half=list(map(int, (x0, y0, x1, y1))))
for v, f in NOTES.items():
    im = Image.open(os.path.join(SRC, f)).convert("RGB")
    g = stretch(ImageOps.grayscale(im), 1, 99, 1.15)
    g = ImageOps.expand(g, border=3, fill=0)         # thin black frame
    g.save(os.path.join(OUT, f"note_{v}.png"))
    info[f"note_{v}"] = dict(src=f, px=list(g.size), aspect=round(g.size[0] / g.size[1], 4))
json.dump(info, open(os.path.join(OUT, "assets.json"), "w"), indent=1)
print(json.dumps(info, indent=1))
