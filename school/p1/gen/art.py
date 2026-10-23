"""Extra friendly line-art objects (pure black and white) for the new pages. Registered into common.OBJ_PATHS so obj_g() draws them."""
from . import common
from .common import OBJ_ST, OBJ_PATHS, obj_g

OBJ_PATHS.update({
    "bird": f'<polygon points="4,10.5 0.8,7 2,13" {OBJ_ST}/><ellipse cx="9" cy="11.5" rx="6.3" ry="4.3" {OBJ_ST}/><circle cx="14.2" cy="7" r="3.1" {OBJ_ST}/><polygon points="16.9,6.2 19.6,7.4 16.8,8.4" {OBJ_ST}/><path d="M6,11 Q9,15 12,11" {OBJ_ST} fill="none"/><circle cx="14.6" cy="6.3" r="0.8" fill="#000"/>',
    "flower": ''.join(f'<circle cx="{10 + 4.3 * __import__("math").sin(i * 1.2566):.2f}" cy="{7.5 - 4.3 * __import__("math").cos(i * 1.2566):.2f}" r="3" {OBJ_ST}/>' for i in range(5)) + f'<circle cx="10" cy="7.5" r="2" {OBJ_ST}/><path d="M10,12 L10,19" {OBJ_ST} fill="none"/>',
    "sweet": f'<path d="M5,10 L1,6 L1,14 Z" {OBJ_ST}/><path d="M15,10 L19,6 L19,14 Z" {OBJ_ST}/><circle cx="10" cy="10" r="5.2" {OBJ_ST}/><path d="M7,8 Q10,6 13,8" {OBJ_ST} fill="none"/>',
    "ball": f'<circle cx="10" cy="10" r="8.5" {OBJ_ST}/><path d="M1.8,9 Q10,13.5 18.2,9" {OBJ_ST} fill="none"/><path d="M10,1.5 Q6,10 10,18.5" {OBJ_ST} fill="none"/>',
    "car": f'<path d="M1.5,13 L1.5,9.5 L5,9.5 L7,5.5 L13,5.5 L15,9.5 L18.5,9.5 L18.5,13 Z" {OBJ_ST}/><circle cx="6" cy="13.5" r="2.4" {OBJ_ST}/><circle cx="14" cy="13.5" r="2.4" {OBJ_ST}/>',
    "kite": f'<path d="M10,1.5 L16,8 L10,15 L4,8 Z" {OBJ_ST}/><path d="M10,1.5 L10,15 M4,8 L16,8" {OBJ_ST} fill="none"/><path d="M10,15 C8,17 12,17.5 10,19.5" {OBJ_ST} fill="none"/>',
    "drum": f'<ellipse cx="10" cy="5.5" rx="7.5" ry="2.6" {OBJ_ST}/><path d="M2.5,5.5 L2.5,15 C2.5,18.5 17.5,18.5 17.5,15 L17.5,5.5" {OBJ_ST}/><path d="M5,8 L9,16 M15,8 L11,16" {OBJ_ST} fill="none"/>',
    "boat": f'<path d="M2,12 L18,12 L15,17 L5,17 Z" {OBJ_ST}/><path d="M10,2.5 L10,12 M10,3 L16,10.5 L10,10.5 Z" {OBJ_ST}/>',
    "cup": f'<path d="M3,5 L14,5 L13,15 C13,17 4,17 4,15 Z" {OBJ_ST}/><path d="M14,7 C19,7 19,13 13.5,12.5" {OBJ_ST} fill="none"/>',
})
# singular, plural
NAMES = {"apple": ("apple", "apples"), "star": ("star", "stars"), "fish": ("fish", "fish"), "balloon": ("balloon", "balloons"),
         "bird": ("bird", "birds"), "flower": ("flower", "flowers"), "sweet": ("sweet", "sweets"), "ball": ("ball", "balls"),
         "car": ("car", "cars"), "kite": ("kite", "kites"), "drum": ("drum", "drums"), "boat": ("boat", "boats"), "cup": ("cup", "cups")}

def row_svg(kind, n, size=6.0, pitch=6.8, per_row=12, gap_after=None, x0=0.5):
    """n objects of one kind in rows of at most per_row; returns (svg, w, h)"""
    rows = (n + per_row - 1) // per_row
    w = x0 * 2 + min(n, per_row) * pitch; h = rows * (size + 1.6) + 0.6
    inner = "".join(obj_g(kind, x0 + (i % per_row) * pitch, 0.5 + (i // per_row) * (size + 1.6), size) for i in range(n))
    return common.svg(round(w, 1), round(h, 1), inner), w, h

def count_objs(svg_text):
    """independent counter: objects of each kind in a drawn svg"""
    import re
    out = {}
    for k in re.findall(r'class="obj" data-k="(\w+)"', svg_text): out[k] = out.get(k, 0) + 1
    return out
