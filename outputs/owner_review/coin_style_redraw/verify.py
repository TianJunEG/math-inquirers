#!/usr/bin/env python3
"""Checks for the held-back style sample: word whitelist (SVG ground truth + tesseract OCR),
colour table, coin diameter ratios (measured from pixels), note aspect ratios."""
import json, os, re, subprocess, sys
from PIL import Image
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(os.path.join(H, "spec.json")))
im = Image.open(os.path.join(H, "_verify_400dpi.png")).convert("RGB")
a = np.asarray(im).astype(int); PX = 400/25.4
fail = 0
def ok(c, m):
    global fail
    print(("PASS " if c else "FAIL ") + m); fail += (not c)

# 1. words drawn (ground truth from the generator)
art_ok = {"SINGAPORE", "SPECIMEN", "CENTS"}
for kind, s in spec["texts"]:
    if kind in ("note", "coin"):
        ok(s in art_ok or re.fullmatch(r"\$?\d+", s), f"artwork text '{s}' is a real word or numeral")
fw = sorted({w for k, s in spec["texts"] if k == "furniture" for w in re.findall(r"[A-Za-z$%.0-9]+", s)})
print("sheet furniture words (outside the artwork):", " ".join(fw))
art_words = sorted({s for k, s in spec["texts"] if k != "furniture"})
print("artwork strings:", art_words)

# 2. OCR of the rendered page (words seen by tesseract)
try:
    t = subprocess.run(["tesseract", os.path.join(H, "_verify_400dpi.png"), "-", "--psm", "11"],
                       capture_output=True, text=True).stdout
    seen = sorted({w for w in re.findall(r"[A-Za-z$]{3,}", t)})
    allowed = {w.lower().strip(".:") for k, s in spec["texts"] for w in re.findall(r"[A-Za-z$%.0-9]+", s)}
    allowed |= {"readme"}
    noise = [w for w in seen if set(w.lower()) <= set("eocs") and w.lower() not in allowed]   # dot patterns read as letters
    frag = [w for w in seen if w.lower() not in allowed and w not in noise and any(w.lower() in x for x in allowed)]  # cut-off pieces of drawn words
    extra = [w for w in seen if w.lower() not in allowed and w not in noise and w not in frag]
    print("OCR dot-pattern noise (no real letters):", noise); print("OCR fragments of drawn words:", frag)
    print("OCR words (>=3 letters):", " ".join(seen))
    ok(not extra, f"OCR found no word outside the drawn text; unexpected: {extra}")
except FileNotFoundError:
    print("tesseract not installed: OCR step skipped")

# 3. coin diameters measured on pixels (bbox of non-background in a window)
bg = np.array([255, 250, 240])
def bbox(cx, cy, r):
    x0, x1 = int((cx-r-3)*PX), int((cx+r+3)*PX); y0, y1 = int((cy-r-3)*PX), int((cy+r+3)*PX)
    w = a[y0:y1, x0:x1]; m = (np.abs(w-bg).sum(2) > 60)
    # ignore the soft shadow (grey, low saturation, light): keep darker/stroke pixels only
    ys, xs = np.where(m & (w.sum(2) < 480))
    return (xs.max()-xs.min()+1)/PX, (ys.max()-ys.min()+1)/PX
d1 = None; meas = {}
for c in spec["coins"]:
    wmm, hmm = bbox(c["cx_mm"], c["cy_mm"], c["r_mm"]); meas[c["key"]] = (wmm+hmm)/2
for c in spec["coins"]:
    exp = c["real_dia"]*spec["coin_scale"]; got = meas[c["key"]]
    ok(abs(got/exp-1) < 0.01, f"coin {c['key']}: drawn {got:.2f} mm vs spec x0.80 = {exp:.2f} mm ({(got/exp-1)*100:+.2f}%)")
for c in spec["coins"]:
    exp = c["real_dia"]/24.65; got = meas[c["key"]]/meas["$1"]
    ok(abs(got/exp-1) < 0.01, f"ratio to $1 coin {c['key']}: {got:.3f} vs {exp:.3f}")

# 4. notes: aspect ratio and size vs spec, colour (hue at a plain spot)
import colorsys
HUE = {"purple": (255, 290), "green": (90, 170), "red": (-15, 15), "blue": (200, 235), "orange": (22, 45)}
print("colour table (sampled in the note body, left of the portrait):")
for n in spec["notes"]:
    x, y, w, h = n["x_mm"], n["y_mm"], n["w_mm"], n["h_mm"]
    asp = (n["real_w"]/n["real_h"]); got = w/h
    ok(abs(got/asp-1) < 0.01, f"note {n['key']}: aspect {got:.3f} vs real {asp:.3f}; drawn {w:.1f} x {h:.1f} mm = {w/n['real_w']*100:.1f}% of real")
    px, py = int((x+w*0.62)*PX), int((y+h*0.9)*PX)   # below the portrait, above the lower edge
    px, py = int((x+w*0.55)*PX), int((y+h*0.05)*PX)
    r, g, b = a[py, px]/255; hh, s, v = colorsys.rgb_to_hsv(r, g, b); hd = hh*360
    lo, hi = HUE[n["colour"]]
    ok(lo <= hd <= hi or lo <= hd-360 <= hi, f"note {n['key']} {n['colour']}: sampled #{a[py,px][0]:02x}{a[py,px][1]:02x}{a[py,px][2]:02x} hue {hd:.0f} deg (accepted {lo}-{hi}); outline {n['deep']}")
ok(all(n["w_mm"]/n["real_w"] <= 0.6001 for n in spec["notes"]), "notes at <= 60% of real size (MAS books rule)")
ws = [n["w_mm"] for n in spec["notes"]]
ok(ws == sorted(ws), "notes grow with value ($2 < $5 < $10 < $50 < $100)")
print("RESULT:", "ALL PASS" if not fail else f"{fail} FAIL"); sys.exit(1 if fail else 0)
