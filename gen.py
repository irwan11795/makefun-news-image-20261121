#!/usr/bin/env python3
"""Generate entry.png for news-image-20261121 (v3, total rebuild).

Draws a one-page newspaper summing up Saturday 21 November 2026.
Rebuilt from scratch on the user's order: v2 (Hermes 99.1, SUBMIT
AS-IS) was judged by the user not submittable, and he sent a
reference page to follow — numbered stories, big simulated drawings
for the hot stories, stat boxes, a region bar, a DATE CHECK box and
a HOW WE CHECKED footer. This v3 follows that structure:

- Masthead "THE WORLD IN ONE DAY" + honest story/region counts.
- Date headline + sub-headline naming the three heroes.
- Six stat boxes (our own verified figures).
- Region bar with coloured squares, counts reconciled from the data.
- Three heroes with large code-drawn illustrations: Riyadh (missiles
  over a night skyline), COP31 (globe + thermometer + day-13 clock),
  Peru quake (seismograph + houses + lighthouse).
- Grid of 10 numbered stories (2 rows x 5), each with a small
  code-drawn illustration, source and verification tag.
- World map "WHERE IT HAPPENED" with numbered dots (one dot per
  location; a "2"/"3" badge where a location hosts several stories).
- "ALSO ON SATURDAY" numbered list continuing the numbering.
- DATE CHECK box: what was left out and why.
- Footer with the HOW WE CHECKED legend.

Every story happened, or was first reported, on Saturday 21
November 2026, verified against a primary source (wire service,
official site, or official statement) dated that day. No email
digests, no social-media rumors, no unsourced blogs. All headlines,
summaries and drawings are original — the reference page supplied
only the layout pattern, never the wording. All drawing is done
with Pillow shapes; no external images are used. Deterministic:
same input always produces the same bytes.

Hero order follows the reference curation: Riyadh, COP31, Peru.
Warsaw/Rutte and the overnight Russia strike move to the grid.
"""
import hashlib
import math
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = os.path.join(FD, "DejaVuSerif-Bold.ttf")
SERIF = os.path.join(FD, "DejaVuSerif.ttf")
SANS_B = os.path.join(FD, "DejaVuSans-Bold.ttf")
SANS = os.path.join(FD, "DejaVuSans.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


# Palette: newsprint on warm paper.
PAPER = (250, 247, 238)
INK = (22, 22, 22)
RED = (178, 34, 28)
NAVY = (18, 42, 78)
BLUE = (28, 84, 150)
TEAL = (14, 110, 110)
GOLD = (196, 138, 20)
GREY = (110, 110, 108)
LIGHT = (232, 227, 214)
SKY = (178, 214, 235)
SEA = (140, 185, 215)
LAND = (214, 206, 178)
MUTED = (90, 88, 82)
NIGHT = (16, 24, 52)
GREEN = (20, 130, 60)
PURPLE = (120, 60, 160)
OLIVE = (140, 140, 40)
ORANGE = (196, 110, 20)
CYAN = (60, 160, 200)

F_MAST = font(SERIF_B, 30)
F_DATE = font(SERIF_B, 54)
F_SUB = font(SERIF, 21)
F_STAT_N = font(SERIF_B, 30)
F_STAT_L = font(SANS_B, 11)
F_REG = font(SANS_B, 14)
F_HERO_L = font(SANS_B, 13)
F_HERO_K = font(SANS_B, 13)
F_HERO_T = font(SERIF_B, 23)
F_HERO_B = font(SANS, 14)
F_HERO_S = font(SANS, 12)
F_GRID_K = font(SANS_B, 10)
F_GRID_T = font(SERIF_B, 13)
F_GRID_B = font(SANS, 11)
F_GRID_S = font(SANS, 9)
F_GRID_TAG = font(SANS_B, 9)
F_MAP_T = font(SANS_B, 15)
F_ALSO_T = font(SANS_B, 15)
F_ALSO = font(SANS, 13)
F_DC_T = font(SANS_B, 13)
F_DC = font(SANS, 12)
F_FOOT = font(SANS, 12)
F_FOOT_B = font(SANS_B, 12)
F_TAG = font(SANS_B, 11)
F_DOT = font(SANS_B, 9)

TAG_FILL = {"CONFIRMED": (20, 130, 60), "OFFICIAL": (28, 84, 150),
            "REPORTED": (196, 110, 20), "CLAIM": (178, 34, 28)}


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit in width px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def clipped(draw, text, fnt, width):
    """Shorten text with an ellipsis so it fits width."""
    if draw.textlength(text, font=fnt) <= width:
        return text
    while text and draw.textlength(text + "...", font=fnt) > width:
        text = text[:-1]
    return text + "..."


# ---------------------------------------------------------------- icons
def icon_clock(d, x, y, s, bg=PAPER, fg=NAVY):
    d.ellipse([x, y, x + s, y + s], fill=bg, outline=fg, width=3)
    d.line([x + s / 2, y + s / 2, x + s / 2, y + s * 0.22], fill=fg, width=3)
    d.line([x + s / 2, y + s / 2, x + s * 0.72, y + s * 0.62], fill=fg, width=3)


# ---------------------------------------------------------------- grid art (fix #6)
# Full-bleed wide compositions for the grid strips. Each function
# paints the WHOLE strip rect (x, y, w, h) — background plus motif
# elements spread from edge to edge — so no empty space is left on
# either side (the user asked for the art to fill both sides, fix #6).
# All coordinates are fractions of w/h, so the art scales to the
# strip size. Motifs per story are unchanged from v3; only the
# composition is widened. The old square icon_* functions are gone;
# icon_clock survives above because icon_stat_clock still uses it.


def art_crowd(d, x, y, w, h):
    # Warsaw: crowd + flag, heads in a row across the full width.
    d.rectangle([x, y, x + w, y + h], fill=(232, 214, 170))
    n = 9
    for i in range(n):
        cx = x + w * (0.06 + 0.88 * i / (n - 1))
        d.ellipse([cx - 5, y + h * 0.18, cx + 5, y + h * 0.38],
                  fill=(40, 40, 50))
        d.pieslice([cx - 9, y + h * 0.42, cx + 9, y + h * 0.95], 180, 360,
                   fill=(50 + (i % 4) * 30, 70, 120))
    # flag pole + red flag, left of centre, above the heads
    d.rectangle([x + w * 0.30, y + h * 0.06, x + w * 0.30 + 2, y + h * 0.55],
                fill=(120, 80, 40))
    d.rectangle([x + w * 0.30 + 2, y + h * 0.06, x + w * 0.52, y + h * 0.20],
                fill=RED)


def art_city(d, x, y, w, h):
    # Kyiv: night skyline across the full width, moon, flames on two
    # buildings.
    d.rectangle([x, y, x + w, y + h], fill=(24, 28, 44))
    d.ellipse([x + w * 0.86, y + h * 0.06, x + w * 0.96, y + h * 0.26],
              fill=(240, 230, 200))
    specs = [(0.00, 0.11, 0.55), (0.12, 0.10, 0.72), (0.23, 0.11, 0.45),
             (0.35, 0.10, 0.62), (0.46, 0.11, 0.50), (0.58, 0.10, 0.70),
             (0.69, 0.11, 0.48), (0.81, 0.09, 0.64), (0.91, 0.09, 0.55)]
    for bx, bw, bh in specs:
        d.rectangle([x + w * bx, y + h - h * bh, x + w * (bx + bw), y + h],
                    fill=(52, 58, 84))
        for wy in (0.30, 0.55):
            d.rectangle([x + w * (bx + 0.02), y + h - h * bh + h * bh * wy,
                         x + w * (bx + 0.05),
                         y + h - h * bh + h * bh * wy + 4],
                        fill=(255, 210, 90))
    for fx in (0.17, 0.63):
        d.polygon([(x + w * (fx - 0.04), y + h * 0.30),
                   (x + w * fx, y + h * 0.08),
                   (x + w * (fx + 0.04), y + h * 0.30)], fill=(255, 120, 20))
        d.polygon([(x + w * (fx - 0.02), y + h * 0.30),
                   (x + w * fx, y + h * 0.16),
                   (x + w * (fx + 0.02), y + h * 0.30)], fill=(255, 210, 60))


def art_missile(d, x, y, w, h):
    # Manama: night sky, stars spread edge to edge, three missile
    # trails arcing across the strip, skyline along the bottom.
    d.rectangle([x, y, x + w, y + h], fill=NIGHT)
    for sx, sy in [(0.05, 0.15), (0.16, 0.35), (0.28, 0.10), (0.40, 0.28),
                   (0.52, 0.12), (0.64, 0.32), (0.76, 0.10), (0.88, 0.30),
                   (0.96, 0.14), (0.34, 0.55), (0.70, 0.52)]:
        d.ellipse([x + sx * w, y + sy * h, x + sx * w + 3, y + sy * h + 3],
                  fill=(255, 255, 255))
    trails = [((0.02, 0.92), (0.30, 0.45), (0.55, 0.18)),
              ((0.30, 0.95), (0.55, 0.55), (0.78, 0.30)),
              ((0.55, 0.92), (0.76, 0.50), (0.94, 0.22))]
    for (x0, y0), (x1, y1), (x2, y2) in trails:
        d.line([x + x0 * w, y + y0 * h, x + x1 * w, y + y1 * h],
               fill=(255, 200, 60), width=3)
        d.line([x + x1 * w, y + y1 * h, x + x2 * w, y + y2 * h],
               fill=(255, 220, 120), width=2)
        d.ellipse([x + x2 * w - 4, y + y2 * h - 4, x + x2 * w + 4,
                   y + y2 * h + 4], fill=(255, 230, 120))
    for bx, by in [(0.55, 0.18), (0.78, 0.30)]:
        d.ellipse([x + bx * w - 6, y + by * h - 6, x + bx * w + 6,
                   y + by * h + 6], outline=(255, 170, 30), width=2)
    for bx, bw, bh in [(0.00, 0.12, 0.22), (0.14, 0.10, 0.30),
                       (0.26, 0.12, 0.20), (0.40, 0.10, 0.28),
                       (0.52, 0.12, 0.22), (0.66, 0.10, 0.30),
                       (0.78, 0.11, 0.24), (0.90, 0.10, 0.28)]:
        d.rectangle([x + w * bx, y + h - h * bh, x + w * (bx + bw), y + h],
                    fill=(34, 38, 66))


def art_fire(d, x, y, w, h):
    # Basra: a row of flames across the full width, alternating
    # tall/short, over a ground bar.
    d.rectangle([x, y, x + w, y + h], fill=(40, 40, 40))
    flames = [(0.00, 0.11, 0.55), (0.14, 0.08, 0.85), (0.24, 0.09, 0.45),
              (0.34, 0.10, 0.75), (0.45, 0.08, 0.55), (0.55, 0.10, 0.88),
              (0.66, 0.09, 0.50), (0.76, 0.10, 0.80), (0.86, 0.08, 0.60),
              (0.94, 0.06, 0.45)]
    for fx, fw, fh in flames:
        d.polygon([(x + w * fx, y + h),
                   (x + w * (fx + fw / 2), y + h - h * fh),
                   (x + w * (fx + fw), y + h)], fill=(255, 110, 20))
        d.polygon([(x + w * (fx + fw * 0.28), y + h),
                   (x + w * (fx + fw / 2), y + h - h * fh * 0.55),
                   (x + w * (fx + fw * 0.72), y + h)], fill=(255, 210, 60))
    d.rectangle([x, y + h - 4, x + w, y + h], fill=(90, 90, 90))


def _drone_body(d, cx, cy, s):
    # One quad-rotor drone, centred on (cx, cy), s px wide.
    d.ellipse([cx - s * 0.12, cy - s * 0.08, cx + s * 0.12, cy + s * 0.08],
              fill=(60, 60, 70))
    for dx, dy in [(-0.32, -0.25), (0.32, -0.25),
                   (-0.32, 0.25), (0.32, 0.25)]:
        rx, ry = cx + dx * s, cy + dy * s
        d.ellipse([rx - s * 0.10, ry - s * 0.10, rx + s * 0.10,
                   ry + s * 0.10], outline=(60, 60, 70), width=2)
        d.line([cx, cy, rx, ry], fill=(60, 60, 70), width=2)


def art_drone(d, x, y, w, h):
    # Hormuz: sky, clouds at the edges, three drones spread across.
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    for cx, cy in [(0.05, 0.16), (0.95, 0.82)]:
        d.ellipse([x + w * (cx - 0.05), y + h * (cy - 0.08),
                   x + w * (cx + 0.05), y + h * (cy + 0.08)],
                  fill=(255, 255, 255))
    for cx, cy, s in [(0.18, 0.42, 38), (0.50, 0.28, 44), (0.82, 0.48, 38)]:
        _drone_body(d, x + w * cx, y + h * cy, s)


def art_train(d, x, y, w, h):
    # Sejong: one long train spanning the full width — cars to the
    # left, nose at the right end — over rails and sleepers.
    d.rectangle([x, y, x + w, y + h], fill=(196, 222, 196))
    d.rectangle([x, y + h * 0.18, x + w, y + h * 0.78], fill=(30, 90, 160))
    for i in range(15):
        wx = 0.04 + 0.06 * i
        d.rectangle([x + w * wx, y + h * 0.28, x + w * (wx + 0.035),
                     y + h * 0.50], fill=(220, 240, 255))
    d.polygon([(x + w * 0.86, y + h * 0.78), (x + w * 0.92, y + h * 0.18),
               (x + w, y + h * 0.18), (x + w, y + h * 0.78)],
              fill=(20, 70, 140))
    d.rectangle([x + w * 0.90, y + h * 0.28, x + w * 0.97, y + h * 0.50],
                fill=(220, 240, 255))
    d.line([x, y + h * 0.88, x + w, y + h * 0.88], fill=(60, 60, 60), width=3)
    for i in range(16):
        sx = 0.02 + 0.06 * i
        d.line([x + w * sx, y + h * 0.84, x + w * sx, y + h * 0.94],
               fill=(60, 60, 60), width=2)


def art_rocket(d, x, y, w, h):
    # Vandenberg: night sky, stars edge to edge, launch tower at the
    # far left, big rocket centre-left, exhaust smoke drifting right.
    d.rectangle([x, y, x + w, y + h], fill=NIGHT)
    for sx, sy in [(0.04, 0.15), (0.14, 0.35), (0.24, 0.10), (0.58, 0.12),
                   (0.68, 0.30), (0.80, 0.10), (0.90, 0.28), (0.97, 0.12),
                   (0.10, 0.60), (0.86, 0.55)]:
        d.ellipse([x + sx * w, y + sy * h, x + sx * w + 3, y + sy * h + 3],
                  fill=(255, 255, 255))
    d.rectangle([x + w * 0.02, y + h * 0.20, x + w * 0.08, y + h],
                fill=(90, 90, 110))
    d.line([x + w * 0.08, y + h * 0.30, x + w * 0.30, y + h * 0.30],
           fill=(90, 90, 110), width=2)
    rx, rw = x + w * 0.30, w * 0.16
    d.polygon([(rx + rw * 0.35, y + h * 0.72), (rx + rw * 0.50, y + h * 0.98),
               (rx + rw * 0.65, y + h * 0.72)], fill=(255, 170, 30))
    d.ellipse([rx, y + h * 0.08, rx + rw, y + h * 0.75],
              fill=(230, 230, 230))
    d.polygon([(rx, y + h * 0.55), (rx - rw * 0.22, y + h * 0.78),
               (rx, y + h * 0.72)], fill=(200, 40, 40))
    d.polygon([(rx + rw, y + h * 0.55), (rx + rw * 1.22, y + h * 0.78),
               (rx + rw, y + h * 0.72)], fill=(200, 40, 40))
    d.ellipse([rx + rw * 0.30, y + h * 0.22, rx + rw * 0.70, y + h * 0.38],
              fill=(40, 90, 160))
    for sx, sy, sr in [(0.62, 0.88, 7), (0.72, 0.92, 9), (0.84, 0.86, 7),
                       (0.94, 0.92, 8)]:
        d.ellipse([x + w * sx - sr, y + h * sy - sr, x + w * sx + sr,
                   y + h * sy + sr], fill=(200, 200, 200))
    d.line([x, y + h - 2, x + w, y + h - 2], fill=(60, 60, 70), width=2)


def _race_car(d, cx, cy, cw, color):
    # One race car, cw px wide, anchored at top-left (cx, cy).
    ch = cw * 0.42
    d.polygon([(cx, cy + ch * 0.62), (cx + cw * 0.12, cy + ch * 0.38),
               (cx + cw * 0.34, cy + ch * 0.30), (cx + cw * 0.60, cy + ch * 0.32),
               (cx + cw * 0.78, cy + ch * 0.55), (cx + cw * 0.84, cy + ch * 0.62)],
              fill=color)
    d.rectangle([cx + cw * 0.18, cy + ch * 0.38, cx + cw * 0.32, cy + ch * 0.50],
                fill=(180, 220, 240))
    d.rectangle([cx + cw * 0.38, cy + ch * 0.38, cx + cw * 0.56, cy + ch * 0.50],
                fill=(180, 220, 240))
    for wx in (0.20, 0.64):
        d.ellipse([cx + cw * (wx - 0.07), cy + ch * 0.58,
                   cx + cw * (wx + 0.07), cy + ch * 0.76], fill=(15, 15, 15))
        d.ellipse([cx + cw * (wx - 0.03), cy + ch * 0.63,
                   cx + cw * (wx + 0.03), cy + ch * 0.71], fill=(160, 160, 160))


def art_car(d, x, y, w, h):
    # Las Vegas: checkered strip along the top edge, road lines
    # spanning the full width, two race cars (red left, blue right).
    d.rectangle([x, y, x + w, y + h], fill=(30, 30, 36))
    for i in range(12):
        col = (255, 255, 255) if i % 2 == 0 else (15, 15, 15)
        d.rectangle([x + w * i / 12, y, x + w * (i + 1) / 12, y + h * 0.10],
                    fill=col)
    d.line([x, y + h * 0.82, x + w, y + h * 0.82], fill=(200, 200, 200), width=2)
    d.line([x, y + h * 0.94, x + w, y + h * 0.94], fill=(200, 200, 200), width=2)
    _race_car(d, x + w * 0.06, y + h * 0.34, w * 0.38, (200, 30, 30))
    _race_car(d, x + w * 0.56, y + h * 0.40, w * 0.38, (30, 90, 200))


def art_bat(d, x, y, w, h):
    # Wellington: cricket — white balls spread across the strip,
    # two bats angled, stumps at the right edge, grass at the bottom.
    d.rectangle([x, y, x + w, y + h], fill=(24, 90, 40))
    d.rectangle([x, y + h * 0.86, x + w, y + h], fill=(18, 70, 30))
    for bx, by, br in [(0.10, 0.30, 6), (0.38, 0.18, 7), (0.66, 0.32, 6),
                       (0.90, 0.22, 7), (0.52, 0.62, 5)]:
        d.ellipse([x + w * bx - br, y + h * by - br,
                   x + w * bx + br, y + h * by + br],
                  fill=(255, 255, 255))
    d.line([x + w * 0.20, y + h * 0.82, x + w * 0.42, y + h * 0.22],
           fill=(210, 170, 110), width=6)
    d.rectangle([x + w * 0.16, y + h * 0.72, x + w * 0.24, y + h * 0.88],
                fill=(120, 70, 20))
    d.line([x + w * 0.74, y + h * 0.82, x + w * 0.58, y + h * 0.30],
           fill=(210, 170, 110), width=6)
    d.rectangle([x + w * 0.72, y + h * 0.72, x + w * 0.80, y + h * 0.88],
                fill=(120, 70, 20))
    for sx in (0.95, 0.97, 0.99):
        d.line([x + w * sx, y + h * 0.55, x + w * sx, y + h * 0.86],
               fill=(255, 220, 120), width=2)


def _plane_body(d, px, py, pw):
    # One white plane, pw px wide, anchored at top-left (px, py).
    ph = pw * 0.42
    d.ellipse([px, py + ph * 0.42, px + pw, py + ph * 0.60],
              fill=(255, 255, 255))
    d.polygon([(px + pw * 0.55, py + ph * 0.50), (px + pw * 0.92, py + ph * 0.50),
               (px + pw * 0.62, py + ph * 0.66)], fill=(255, 255, 255))
    d.polygon([(px + pw * 0.30, py + ph * 0.46), (px + pw * 0.55, py + ph * 0.30),
               (px + pw * 0.55, py + ph * 0.46)], fill=(220, 220, 220))
    d.ellipse([px + pw * 0.82, py + ph * 0.46, px + pw * 0.88, py + ph * 0.52],
              fill=(40, 80, 140))


def art_plane(d, x, y, w, h):
    # Davao: sky, contrails spanning the full width, clouds at the
    # edges, two planes (big left, smaller right).
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.line([x, y + h * 0.30, x + w, y + h * 0.22], fill=(255, 255, 255), width=2)
    d.line([x, y + h * 0.68, x + w, y + h * 0.60], fill=(255, 255, 255), width=2)
    for cx, cy in [(0.05, 0.12), (0.95, 0.85)]:
        d.ellipse([x + w * (cx - 0.05), y + h * (cy - 0.07),
                   x + w * (cx + 0.05), y + h * (cy + 0.07)],
                  fill=(255, 255, 255))
    _plane_body(d, x + w * 0.08, y + h * 0.18, w * 0.34)
    _plane_body(d, x + w * 0.62, y + h * 0.52, w * 0.26)


def art_clock(d, x, y, w, h):
    # Unused by the grid data (kept so the art dict stays complete):
    # three clock faces spread across the strip.
    d.rectangle([x, y, x + w, y + h], fill=PAPER)
    for cx, (hx, hy) in [(0.20, (0.0, -0.70)), (0.50, (0.55, 0.40)),
                          (0.80, (-0.45, -0.55))]:
        r = h * 0.36
        ccx, ccy = x + w * cx, y + h * 0.50
        d.ellipse([ccx - r, ccy - r, ccx + r, ccy + r],
                  fill=(255, 255, 255), outline=NAVY, width=2)
        d.line([ccx, ccy, ccx + hx * r, ccy + hy * r], fill=NAVY, width=2)
        d.line([ccx, ccy, ccx - hy * r * 0.8, ccy + hx * r * 0.8],
               fill=NAVY, width=2)


# ---------------------------------------------------------------- stat icons (fix #4)
# Small illustrations for the six stat boxes, drawn directly on the
# paper background (no tile) so the number and label text keep their
# places. All coordinates are fractions of s, so they stay legible
# at the 20 px size used in the stat row. Nothing here changes any
# figure, label, or box size.
def icon_stat_missile(d, x, y, s):
    # burst: gold streak into an orange starburst (missiles downed)
    d.line([x + s * 0.06, y + s * 0.88, x + s * 0.60, y + s * 0.32],
           fill=(255, 200, 60), width=2)
    cx, cy = x + s * 0.68, y + s * 0.30
    pts = []
    for i in range(16):
        r = s * 0.30 if i % 2 == 0 else s * 0.13
        a = math.pi * i / 8
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=(255, 170, 30))
    d.ellipse([cx - s * 0.09, cy - s * 0.09, cx + s * 0.09, cy + s * 0.09],
              fill=(255, 230, 120))
    d.ellipse([x + s * 0.10, y + s * 0.10, x + s * 0.18, y + s * 0.18],
              fill=GREY)
    d.ellipse([x + s * 0.28, y + s * 0.72, x + s * 0.34, y + s * 0.78],
              fill=GREY)


def icon_stat_bat(d, x, y, s):
    # red cricket ball + tan bat (Rahul's 136)
    d.line([x + s * 0.14, y + s * 0.82, x + s * 0.58, y + s * 0.28],
           fill=(210, 170, 110), width=4)
    d.rectangle([x + s * 0.07, y + s * 0.72, x + s * 0.23, y + s * 0.88],
                fill=(120, 70, 20))
    d.ellipse([x + s * 0.62, y + s * 0.10, x + s * 0.90, y + s * 0.38],
              fill=RED, outline=(255, 255, 255), width=1)


def icon_stat_clock(d, x, y, s):
    # small clock face, near midnight (COP31 day 13)
    icon_clock(d, x, y, s, bg=(255, 255, 255), fg=NAVY)


def icon_stat_bitcoin(d, x, y, s):
    # gold coin + navy B (bitcoin under $56K)
    d.ellipse([x, y, x + s, y + s], fill=GOLD, outline=(140, 100, 10),
              width=2)
    f = font(SANS_B, int(s * 0.68))
    b = "B"
    bw = d.textlength(b, font=f)
    d.text((x + (s - bw) / 2, y + s * 0.12), b, font=f, fill=NAVY)


def icon_stat_seismo(d, x, y, s):
    # tiny seismograph strip + red zigzag (Peru quake 6.7)
    d.rectangle([x, y, x + s, y + s], fill=(255, 255, 255), outline=GREY,
                width=1)
    pts = [(0.06, 0.50), (0.16, 0.40), (0.26, 0.60), (0.36, 0.22),
           (0.46, 0.78), (0.56, 0.34), (0.66, 0.66), (0.76, 0.28),
           (0.86, 0.56), (0.94, 0.46)]
    d.line([(x + px * s, y + py * s) for px, py in pts], fill=RED, width=2)


def icon_stat_plane(d, x, y, s):
    # navy plane silhouette, on paper (146 safe after Davao landing)
    d.ellipse([x + s * 0.08, y + s * 0.42, x + s * 0.92, y + s * 0.60],
              fill=NAVY)
    d.polygon([(x + s * 0.55, y + s * 0.50), (x + s * 0.92, y + s * 0.50),
               (x + s * 0.62, y + s * 0.66)], fill=NAVY)
    d.polygon([(x + s * 0.30, y + s * 0.46), (x + s * 0.55, y + s * 0.30),
               (x + s * 0.55, y + s * 0.46)], fill=NAVY)
    d.ellipse([x + s * 0.82, y + s * 0.46, x + s * 0.88, y + s * 0.52],
              fill=(255, 255, 255))


STAT_ICONS = {"missile": icon_stat_missile, "bat": icon_stat_bat,
              "clock": icon_stat_clock, "bitcoin": icon_stat_bitcoin,
              "seismo": icon_stat_seismo, "plane": icon_stat_plane}
# One illustration per stat box, in STATS order.
STAT_ART = ["missile", "bat", "clock", "bitcoin", "seismo", "plane"]


# ---------------------------------------------------------------- hero art
def hero_art_riyadh(d, x, y, w, h):
    """Missiles over a night skyline. Panel w x h, code-drawn."""
    x, y, w, h = int(x), int(y), int(w), int(h)
    d.rectangle([x, y, x + w, y + h], fill=NIGHT)
    # stars (fixed positions: deterministic)
    for sx, sy in [(12, 10), (48, 22), (90, 8), (140, 16), (180, 6),
                   (215, 20), (255, 10), (290, 24), (30, 40), (120, 34),
                   (200, 38), (270, 42), (70, 52), (160, 48), (235, 54)]:
        d.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2],
                  fill=(255, 255, 255))
    # missile trails arcing up from the skyline
    trails = [((18, 96), (95, 30), (150, 12)),
              ((70, 96), (150, 42), (205, 18)),
              ((140, 96), (215, 50), (262, 26))]
    for (x0, y0), (x1, y1), (x2, y2) in trails:
        d.line([x + x0, y + y0, x + x1, y + y1], fill=(255, 200, 60), width=3)
        d.line([x + x1, y + y1, x + x2, y + y2], fill=(255, 220, 120), width=2)
        d.ellipse([x + x2 - 4, y + y2 - 4, x + x2 + 4, y + y2 + 4],
                  fill=(255, 230, 120))
        d.ellipse([x + x2 - 2, y + y2 - 2, x + x2 + 2, y + y2 + 2],
                  fill=(255, 255, 255))
    # bursts where interceptors meet the trails
    for bx, by in [(150, 12), (205, 18)]:
        d.ellipse([x + bx - 6, y + by - 6, x + bx + 6, y + by + 6],
                  outline=(255, 170, 30), width=2)
    # skyline silhouettes with lit windows
    base = y + h
    # (bx, width, height) per building, left to right
    specs = [(0, 34, 52), (36, 30, 64), (68, 40, 44), (110, 28, 58),
             (140, 34, 38), (176, 30, 60), (208, 36, 48), (246, 28, 62),
             (276, 42, 54)]
    for bx, bw, bh in specs:
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(34, 38, 66))
        for wy in range(base - bh + 8, base - 6, 12):
            for wx in range(x + bx + 5, x + bx + bw - 4, 10):
                if (wx + wy) % 23 < 11:
                    d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 210, 90))
    # tall tower with an arch near the top
    d.rectangle([x + 140, base - 82, x + 174, base], fill=(34, 38, 66))
    d.ellipse([x + 150, base - 78, x + 164, base - 62], fill=NIGHT)
    d.text((x + w - 8 - d.textlength("Coalition statement", font=F_TAG),
            y + h - 15), "Coalition statement",
           font=F_TAG, fill=(220, 220, 220))


def hero_art_cop31(d, x, y, w, h):
    """Globe + thermometer + day-13 clock. Panel w x h, code-drawn."""
    x, y, w, h = int(x), int(y), int(w), int(h)
    d.rectangle([x, y, x + w, y + h], fill=(235, 242, 248))
    # globe, left
    cx, cy, r = x + 52, y + h // 2 + 2, 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 160, 210),
              outline=NAVY, width=2)
    d.ellipse([cx - 22, cy - 18, cx - 2, cy + 2], fill=(110, 190, 110))
    d.ellipse([cx + 2, cy + 6, cx + 22, cy + 24], fill=(110, 190, 110))
    d.ellipse([cx + 8, cy - 24, cx + 24, cy - 8], fill=(110, 190, 110))
    # thermometer, middle
    tx = x + 128
    d.rectangle([tx, y + 14, tx + 16, y + h - 22], fill=(255, 255, 255),
                outline=INK, width=2)
    d.ellipse([tx - 6, y + h - 30, tx + 22, y + h - 8], fill=RED,
              outline=INK, width=2)
    d.rectangle([tx + 4, y + 34, tx + 12, y + h - 22], fill=RED)
    d.text((tx + 24, y + 10), "+1.5°C", font=F_HERO_L, fill=RED)
    d.text((tx + 24, y + 28), "LIMIT", font=F_TAG, fill=INK)
    d.text((tx + 24, y + 42), "AT RISK", font=F_TAG, fill=INK)
    # clock, right: near midnight, day 13
    kx, ky, kr = x + w - 56, y + h // 2 + 2, 30
    d.ellipse([kx - kr, ky - kr, kx + kr, ky + kr], fill=(255, 255, 255),
              outline=INK, width=2)
    d.line([kx, ky, kx, ky - kr + 8], fill=INK, width=3)
    d.line([kx, ky, kx + 12, ky + 10], fill=INK, width=3)
    d.text((kx - 26, ky - kr - 18), "DAY 13", font=F_HERO_L, fill=INK)
    d.text((x + w - 62, y + h - 15), "AP · AFP", font=F_TAG, fill=MUTED)


def hero_art_quake(d, x, y, w, h):
    """Seismograph trace over houses and a lighthouse. Panel w x h."""
    x, y, w, h = int(x), int(y), int(w), int(h)
    d.rectangle([x, y, x + w, y + h], fill=(250, 247, 238))
    # seismograph strip, top ~58% of the panel. The "6.7" sits at the
    # left and "00:09 UTC" at the right; the trace runs between them
    # so nothing overlaps.
    sh = int(h * 0.58)
    d.rectangle([x, y, x + w, y + sh], fill=(255, 255, 255), outline=INK,
                width=1)
    for gx in range(0, w, 26):
        d.line([x + gx, y, x + gx, y + sh], fill=(225, 225, 225), width=1)
    d.line([x, y + sh // 2, x + w, y + sh // 2], fill=(225, 225, 225),
           width=1)
    trace = [(0, 0), (14, -3), (26, 4), (38, -14), (50, 16), (62, -20),
             (74, 10), (86, -6), (98, 22), (110, -26), (122, 8),
             (134, -4), (146, 12), (158, -18), (170, 6), (182, -8),
             (194, 14), (206, -22), (218, 10), (230, -4), (242, 8),
             (254, -12), (266, 4), (278, -6), (290, 10), (302, -2),
             (318, 0)]
    tx0, tx1 = x + 66, x + w - 88
    span = tx1 - tx0
    pts = [(tx0 + px * span / 318, y + sh // 2 + py)
           for px, py in trace]
    d.line(pts, fill=RED, width=2)
    d.text((x + 8, y + 4), "6.7", font=F_STAT_N, fill=RED)
    d.text((x + w - 82, y + 6), "00:09 UTC", font=F_HERO_L, fill=INK)
    # ground + houses + lighthouse, bottom of the panel
    gy = y + sh
    d.line([x, gy, x + w, gy], fill=INK, width=2)
    d.rectangle([x, gy, x + w, y + h], fill=(232, 227, 214))
    for hx, hw in [(8, 44), (60, 40), (112, 46), (166, 40)]:
        d.rectangle([x + hx, gy + 12, x + hx + hw, y + h - 2],
                    fill=(214, 206, 178), outline=INK, width=1)
        d.polygon([(x + hx - 4, gy + 12), (x + hx + hw // 2, gy - 2),
                   (x + hx + hw + 4, gy + 12)], fill=RED)
        d.rectangle([x + hx + hw // 2 - 4, gy + 22, x + hx + hw // 2 + 4,
                     y + h - 2], fill=INK)
    # lighthouse, right: red-white stripes (the USGS · IGP credit
    # lives in the hero's source line below, so no text is drawn here)
    lx = x + w - 42
    for i, col in enumerate([(255, 255, 255), RED, (255, 255, 255), RED]):
        d.rectangle([lx, gy - 2 + i * 10, lx + 18, gy + 8 + i * 10], fill=col,
                    outline=INK, width=1)
    d.ellipse([lx + 3, gy - 12, lx + 15, gy], fill=(255, 220, 120),
              outline=INK, width=1)


def draw_grid_art(d, x, y, w, h, kind):
    """Full-bleed illustration strip across the top of a grid cell
    (fix #6: each composition paints the whole strip edge to edge,
    so no empty space is left on either side)."""
    GRID_ART[kind](d, x, y, w, h)


GRID_ART = {"clock": art_clock, "missile": art_missile, "city": art_city,
            "fire": art_fire, "drone": art_drone, "train": art_train,
            "crowd": art_crowd, "car": art_car, "bat": art_bat,
            "plane": art_plane, "rocket": art_rocket}

CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-125, 71), (-110, 68), (-95, 69), (-85, 66),
     (-80, 62), (-75, 58), (-65, 50), (-60, 47), (-70, 42), (-75, 35),
     (-80, 26), (-85, 30), (-90, 21), (-97, 26), (-105, 23), (-110, 24),
     (-115, 29), (-125, 40), (-125, 49), (-140, 60), (-155, 58),
     (-165, 60), (-168, 66)],
    # South America
    [(-78, 7), (-72, 11), (-62, 9), (-52, 5), (-50, 0), (-44, -3),
     (-35, -8), (-40, -20), (-48, -28), (-55, -35), (-65, -41),
     (-70, -50), (-74, -53), (-70, -30), (-70, -18), (-80, -5),
     (-81, 1), (-78, 7)],
    # Africa
    [(-6, 35), (10, 37), (20, 32), (32, 31), (35, 28), (43, 12),
     (51, 11), (48, -1), (40, -10), (36, -18), (33, -26), (26, -34),
     (18, -35), (12, -18), (9, -1), (-8, 4), (-17, 15), (-17, 25),
     (-10, 31), (-6, 35)],
    # Europe
    [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (8, 57), (10, 59),
     (18, 56), (21, 55), (24, 58), (28, 60), (30, 62), (40, 68),
     (45, 68), (40, 60), (35, 55), (30, 46), (28, 44), (23, 40),
     (19, 42), (12, 44), (8, 44), (3, 42), (-2, 37), (-10, 36)],
    # Asia
    [(40, 68), (50, 70), (70, 72), (90, 75), (110, 74), (130, 72),
     (160, 66), (178, 65), (162, 60), (158, 52), (142, 50), (140, 40),
     (132, 35), (127, 35), (122, 30), (118, 25), (110, 20), (105, 9),
     (100, 7), (97, 15), (92, 20), (88, 22), (80, 13), (76, 8),
     (72, 20), (66, 25), (60, 25), (55, 26), (50, 29), (48, 30),
     (44, 29), (40, 32), (36, 36), (30, 36), (35, 42), (40, 47),
     (40, 55), (40, 68)],
    # Australia / Oceania
    [(113, -22), (114, -30), (115, -35), (124, -33), (130, -32),
     (137, -35), (140, -38), (145, -38), (150, -37), (153, -27),
     (146, -19), (142, -11), (136, -12), (130, -13), (126, -14),
     (122, -17), (113, -22)],
]


# ---------------------------------------------------------------- data
# Heroes: (label_left, label_right, kicker, headline, body, source,
#          tag, art, region, lon, lat)
HEROES = [
    ("MISSILES OVER RIYADH", "3 SHOT DOWN",
     "1 · RIYADH · SAUDI ARABIA",
     "Coalition says three missiles downed",
     "The coalition says three missiles aimed at the capital were "
     "stopped early Saturday. No one hurt; a drone is also destroyed.",
     "Reuters · AFP · coalition statement", "OFFICIAL", "riyadh",
     "MIDDLE EAST", 46.7, 24.7),
    ("COP31 IN OVERTIME", "NO DEAL · DAY 13",
     "2 · ANTALYA · TÜRKIYE",
     "Summit misses deadline, day 13",
     "No new text lands Saturday as the summit passes its close. "
     "The EU takes a good deal or none; talks spill over.",
     "AP · AFP · Al Jazeera", "CONFIRMED", "cop31",
     "EUROPE", 30.7, 36.9),
    ("QUAKE SHAKES PERU", "00:09 UTC",
     "3 · CARHUAMAYO · PERU",
     "Magnitude 6.7 quake rattles Peru",
     "A deep tremor strikes just after midnight UTC. It shakes the "
     "capital; officials report no deaths and no tsunami risk.",
     "USGS · IGP", "OFFICIAL", "quake",
     "AMERICAS", -76.0, -11.0),
]

# Grid: (kicker, headline, body, source, tag, art, region, lon, lat)
# Numbered 4..13 in order.
GRID = [
    ("4 · WARSAW", "Rutte vows to defend Poland",
     "Rutte visits after missiles land in Poland; Warsaw asks NATO "
     "for more air defence.",
     "Reuters · AFP", "CONFIRMED", "crowd", "EUROPE", 21.0, 52.2),
    ("5 · KYIV · KRYVYI RIH", "Russia strikes Ukraine again",
     "148 drones, 3 missiles hit overnight. A boy of 7 and a "
     "paramedic die; 60 hurt.",
     "UNITED24", "REPORTED", "city", "EUROPE", 30.5, 50.5),
    ("6 · MANAMA", "Bahrain says attack repelled",
     "A plant burns; no one hurt. The IRGC claims it hit US bases.",
     "Reuters · QNA", "CONFIRMED", "missile", "MIDDLE EAST", 50.6, 26.2),
    ("7 · BASRA", "Basra fire kills at least 4",
     "Hartha station fire injures 35; the blaze spreads to homes.",
     "Reuters", "REPORTED", "fire", "MIDDLE EAST", 47.8, 30.5),
    ("8 · HORMUZ", "Iran claims 58th drone down",
     "The IRGC says it shot down a US MQ-9 over the strait.",
     "IRIB · Press TV", "CLAIM", "drone", "MIDDLE EAST", 56.5, 26.5),
    ("9 · SEJONG", "Train derails, main line cut",
     "Five of 21 cars leave the rails; trains halt Cheonan–Daejeon.",
     "Yonhap", "REPORTED", "train", "ASIA", 127.3, 36.5),
    ("10 · VANDENBERG", "SpaceX launches USSF-317",
     "Falcon 9 lifts off at 04:20 UTC; the mission succeeds.",
     "Space Launch", "REPORTED", "rocket", "AMERICAS", -120.6, 34.7),
    ("11 · LAS VEGAS", "Verstappen inherits pole",
     "Antonelli is fastest, but a grid penalty drops him to sixth.",
     "F1 · Reuters", "CONFIRMED", "car", "AMERICAS",
     -115.1, 36.2),
    ("12 · WELLINGTON", "Rahul ton puts India on top",
     "Rahul hits 136; India lead New Zealand by 118 at stumps.",
     "Reuters · Wisden", "CONFIRMED", "bat", "OCEANIA", 174.8, -41.3),
    ("13 · DAVAO", "Jet lands after engine alert",
     "Air Niugini flight diverts; all 146 aboard escape unhurt.",
     "AP", "REPORTED", "plane", "ASIA", 125.6, 7.07),
]

# Also: (place, text, source, region, lon, lat) — numbered 14.. in order.
# Texts are kept short so each item fits one line in its column.
ALSO = [
    ("MARKETS", "Bitcoin under $56K.",
     "CoinGecko", "GLOBAL", -74.0, 40.7),
    ("MANIPUR", "13 die, 300 in hospital.",
     "IANS", "ASIA", 94.0, 24.5),
    ("MEXICO", "'Chapo Isidro' caught; 11 die.",
     "AP", "AMERICAS", -108.5, 25.6),
    ("ABUJA", "CAF backs Infantino; $25M grants.",
     "AP", "AFRICA", 9.06, 7.49),
    ("U-17", "Brazil 2-1 Ireland.",
     "FIFA", "ASIA", 51.5, 25.3),
    ("MAN CITY", "Held 1-1 by Fulham.",
     "Reuters", "EUROPE", -2.24, 53.48),
    ("TURIN", "Alcaraz, Zverev into final.",
     "Reuters", "EUROPE", 7.7, 45.07),
    ("FINLAND GULF", "Ship hit by drones.",
     "Reuters", "EUROPE", 27.0, 60.0),
    ("GENEVA", "Robot-weapon talks eye 2028.",
     "AP", "EUROPE", 6.1, 46.2),
    ("KYIV", "Zelenskyy on Trump.",
     "Reuters", "EUROPE", 30.5, 50.5),
    ("PYONGYANG", "Kim tours factory sites.",
     "AFP", "ASIA", 125.75, 39.03),
    ("BANDA SEA", "M6.8 quake, 226 km NE of Dili.",
     "GFZ", "ASIA", 127.39, -7.62),
    ("BEIJING", "Australia, China agree AI talks.",
     "ABC", "ASIA", 116.4, 39.9),
    ("LAS VEGAS", "Russell fastest in final practice.",
     "F1", "AMERICAS", -115.1, 36.2),
    ("BRUSSELS", "EU–Indonesia sign trade deal.",
     "EC", "EUROPE", 4.35, 50.85),
    ("BANGKOK", "Arsenic talks led by PM.",
     "Thaiger", "ASIA", 100.5, 13.75),
    ("DELHI", "Pakistan minister warns climate.",
     "ANI", "ASIA", 77.2, 28.6),
    ("MAURITIUS", "Ratings body in 15-state talks.",
     "AJ", "AFRICA", 57.5, -20.16),
    ("MELBOURNE", "Cummins keeps Test captaincy.",
     "CA", "OCEANIA", 144.96, -37.8),
    ("LAS VEGAS", "Verstappen warned after clash.",
     "AP", "AMERICAS", -115.1, 36.2),
]

STATS = [("3", "MISSILES DOWNED\nOVER RIYADH"),
         ("136", "RAHUL'S RUNS AT\nWELLINGTON"),
         ("DAY 13", "OF COP31, PLANNED\nTO CLOSE DAY 12"),
         ("<$56K", "BITCOIN SATURDAY,\nLOWEST SINCE SEPT."),
         ("6.7", "MAGNITUDE OF\nTHE PERU QUAKE"),
         ("146", "PEOPLE SAFE AFTER\nTHE DAVAO LANDING")]

REGION_ORDER = ["EUROPE", "ASIA", "MIDDLE EAST", "AFRICA", "AMERICAS",
                "OCEANIA", "GLOBAL"]
REGION_COLOR = {"EUROPE": BLUE, "ASIA": ORANGE, "MIDDLE EAST": PURPLE,
                "AFRICA": OLIVE, "AMERICAS": GREEN, "OCEANIA": CYAN,
                "GLOBAL": GREY}

LABELS = {"Las Vegas", "Carhuamayo", "Riyadh", "Sejong", "Davao",
          "Wellington", "Markets"}
# What the map actually prints for a label (place names the reader
# knows, not the story's internal label).
LABEL_DISPLAY = {"Carhuamayo": "Junin", "Markets": "New York"}


# ---------------------------------------------------------------- layout
F_ALSO12 = font(SANS, 12)
F_ALSO11 = font(SANS, 11)
F_ALSO10 = font(SANS, 10)


def all_stories():
    """Yield (number, region, lon, lat, label) for every story."""
    out = []
    for i, h in enumerate(HEROES):
        out.append((i + 1, h[8], h[9], h[10],
                    h[2].split("·")[1].strip().title()))
    for i, g in enumerate(GRID):
        out.append((4 + i, g[6], g[7], g[8],
                    g[0].split("·", 1)[1].strip().title()))
    for i, a in enumerate(ALSO):
        out.append((14 + i, a[3], a[4], a[5], a[0].title()))
    return out


def region_counts():
    counts = {r: 0 for r in REGION_ORDER}
    for _n, region, _lo, _la, _lb in all_stories():
        counts[region] += 1
    return [(r, counts[r]) for r in REGION_ORDER if counts[r] > 0]


def map_dots():
    """One dot per distinct location: (lon, lat, number, badge, label).

    Number = lowest story number at that location; badge = how many
    stories share it (None when just one).
    """
    groups = {}
    for num, _region, lon, lat, label in all_stories():
        key = (round(lon, 1), round(lat, 1))
        groups.setdefault(key, []).append((num, label))
    dots = []
    for (lon, lat), items in groups.items():
        items.sort()
        num = items[0][0]
        label = items[0][1]
        badge = len(items) if len(items) > 1 else None
        dots.append((lon, lat, num, badge, label))
    dots.sort(key=lambda t: t[2])
    return dots


def draw_hero(d, x, y, w, hero):
    (label_l, label_r, kicker, title, body, source, tag, art, _reg,
     _lo, _la) = hero
    # art panel, 100 px tall
    if art == "riyadh":
        hero_art_riyadh(d, x, y, w, 100)
    elif art == "cop31":
        hero_art_cop31(d, x, y, w, 100)
    else:
        hero_art_quake(d, x, y, w, 100)
    # red label bar
    ly = y + 100
    d.rectangle([x, ly, x + w, ly + 26], fill=RED)
    d.text((x + 8, ly + 5), label_l, font=F_HERO_L, fill=(255, 255, 255))
    rw = d.textlength(label_r, font=F_HERO_L)
    d.text((x + w - 8 - rw, ly + 5), label_r, font=F_HERO_L,
           fill=(255, 220, 120))
    # kicker with the story number
    ky = ly + 30
    d.text((x + 2, ky), kicker, font=F_HERO_K, fill=RED)
    # headline, at most 2 lines
    ty = ky + 18
    tlines = wrap(d, title, F_HERO_T, w - 16)
    ty = text_block(d, x + 8, ty, tlines[:2], F_HERO_T, INK, 24)
    # body, at most 3 lines
    blines = wrap(d, body, F_HERO_B, w - 16)
    text_block(d, x + 8, ty + 2, blines[:3], F_HERO_B, MUTED, 17)
    # source + verification tag, bottom line
    sy = y + 268 - 16
    d.text((x + 8, sy), "(" + source + ")", font=F_HERO_S, fill=GREY)
    tw = d.textlength(tag, font=F_TAG)
    d.text((x + w - 8 - tw, sy), tag, font=F_TAG, fill=TAG_FILL[tag])


def draw_grid_cell(d, x, y, w, h, item):
    kicker, title, body, source, tag, kind, _region, _lo, _la = item
    d.rectangle([x, y, x + w, y + h], outline=(180, 175, 160), width=1)
    d.rectangle([x, y, x + 4, y + h], fill=RED)
    # illustration strip across the top (fix #4b: 52 px, icon 48 px —
    # the user said the 32 px strip was too small and the type too
    # big; fonts shrink to match: kicker 10, title 13, body 11,
    # source/tag 9. Fix #6: the strip is now full-bleed — the art
    # fills the whole strip edge to edge, no empty space left/right).
    draw_grid_art(d, x + 1, y + 1, w - 2, 52, kind)
    ky = y + 55
    d.text((x + 8, ky), clipped(d, kicker, F_GRID_K, w - 16),
           font=F_GRID_K, fill=RED)
    ty = ky + 12
    tlines = wrap(d, title, F_GRID_T, w - 16)
    ty = text_block(d, x + 8, ty, tlines[:2], F_GRID_T, INK, 14)
    blines = wrap(d, body, F_GRID_B, w - 16)
    text_block(d, x + 8, ty + 2, blines[:3], F_GRID_B, MUTED, 12)
    # source (clipped so it never reaches the tag) + tag, bottom line
    tw = d.textlength(tag, font=F_GRID_TAG)
    sy = y + h - 11
    d.text((x + 8, sy), clipped(d, "(" + source + ")", F_GRID_S,
                               w - 16 - tw - 8),
           font=F_GRID_S, fill=GREY)
    d.text((x + w - 8 - tw, sy), tag, font=F_GRID_TAG, fill=TAG_FILL[tag])


def draw_map(d, x, y, w, h, dots):
    d.rectangle([x, y, x + w, y + h], fill=SEA, outline=INK, width=2)
    lon0, lon1, lat0, lat1 = -180.0, 180.0, 78.0, -58.0

    def proj(lon, lat):
        px = x + (lon - lon0) / (lon1 - lon0) * w
        py = y + (lat0 - lat) / (lat0 - lat1) * h
        return px, py

    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=(150, 140, 110))
    lab_done = set()
    placed = []
    label_reqs = []
    for lon, lat, num, badge, label in dots:
        px, py = proj(lon, lat)
        ox, oy = px, py
        # de-collision: nudge the dot until it clears the ones placed
        # already (fixed candidate offsets, deterministic); a thin
        # leader line ties a nudged dot back to its true spot.
        for dx, dy in [(0, 0), (16, 0), (16, 12), (-16, 0), (0, 14),
                       (16, -12), (-16, 12), (30, 0), (0, -14),
                       (-30, 0), (30, 12), (30, -12), (-30, -12),
                       (30, 24), (-30, 24), (0, 24), (0, -24),
                       (44, 0), (-44, 0), (44, 12), (-44, 12)]:
            cx, cy = px + dx, py + dy
            if all((cx - qx) ** 2 + (cy - qy) ** 2 >= 19 ** 2
                   for qx, qy in placed):
                px, py = cx, cy
                break
        else:
            px, py = ox, oy
        placed.append((px, py))
        if (px, py) != (ox, oy):
            d.line([ox, oy, px, py], fill=GREY, width=1)
        ns = str(num)
        r = 9 if len(ns) == 2 else 8
        d.ellipse([px - r, py - r, px + r, py + r], fill=RED,
                  outline=(255, 255, 255), width=2)
        tw = d.textlength(ns, font=F_DOT)
        d.text((px - tw / 2, py - 6), ns, font=F_DOT, fill=(255, 255, 255))
        if badge:
            bx, by = px + r + 2, py - r - 2
            d.ellipse([bx - 6, by - 6, bx + 6, by + 6],
                      fill=(255, 255, 255), outline=RED, width=2)
            bs = str(badge)
            bw = d.textlength(bs, font=F_DOT)
            d.text((bx - bw / 2, by - 6), bs, font=F_DOT, fill=RED)
        if label in LABELS and label not in lab_done:
            lab_done.add(label)
            label_reqs.append((label, px, py, r))
    # Labels go on AFTER all dots are drawn, checked against the FULL
    # placed list — otherwise a later dot can land on an earlier label.
    # Fix #4: more candidates (diagonals, then farther spots) so a
    # label in a dense cluster still finds a free place; a thin
    # leader line ties a far label back to its dot. Labels must also
    # clear labels placed before them.
    # Fix #4b: the 114 px map squeezed the Americas cluster and the
    # "New York" label's only passing spot touched the Junin dot.
    # A radius-aware dot test was tried and REVERTED: it stranded the
    # "Wellington" label (no spot clears the Melbourne dot by r+2)
    # and pushed four other labels to worse spots — the rect test
    # cannot tell a 1 px ink gap from a touch. The real fix is the
    # placement ORDER: narrowest labels first, so "New York" claims
    # the contested spot above its dot before "Las Vegas" does, and
    # "Las Vegas" takes the free above-left spot instead. The above
    # candidates are tried before the below ones for the same reason.
    label_reqs.sort(key=lambda req: d.textlength(
        LABEL_DISPLAY.get(req[0], req[0]), font=F_TAG))
    placed_labels = []
    for label, px, py, r in label_reqs:
        disp = LABEL_DISPLAY.get(label, label)
        tw = d.textlength(disp, font=F_TAG)
        th = 13
        cands = [(px + r + 3, py - 6), (px - r - 3 - tw, py - 6),
                 (px - tw / 2, py - r - 15), (px - tw / 2, py + r + 3),
                 (px + r + 3, py + r + 3), (px - r - 3 - tw, py - r - 15),
                 (px + r + 3, py - r - 15), (px - r - 3 - tw, py + r + 3),
                 (px - tw / 2, py + r + 16), (px + 10, py + r + 16),
                 (px - tw - 10, py + r + 16), (px + r + 16, py - 6),
                 (px - r - 16 - tw, py - 6), (px - tw / 2, py - r - 28),
                 (px - tw / 2, py + r + 30), (px + 10, py + r + 30),
                 (px - tw - 10, py + r + 30)]
        for ci, (lx, ly) in enumerate(cands):
            lx = max(x + 2, min(lx, x + w - tw - 2))
            ly = max(y + 2, min(ly, y + h - th - 2))
            if all(not (lx - 5 < qx < lx + tw + 5 and
                        ly - 5 < qy < ly + th + 5)
                   for qx, qy in placed):
                if all(not (lx < rx + rw and lx + tw > rx and
                            ly < ry + rh and ly + th > ry)
                       for rx, ry, rw, rh in placed_labels):
                    if ci >= 4:
                        # leader from the dot edge to the nearest
                        # point of the label rect
                        qx = max(lx, min(px, lx + tw))
                        qy = max(ly, min(py, ly + th))
                        dx, dy = qx - px, qy - py
                        dist = (dx * dx + dy * dy) ** 0.5
                        if dist > r + 1:
                            ex = px + dx / dist * (r + 1)
                            ey = py + dy / dist * (r + 1)
                            d.line([ex, ey, qx, qy], fill=GREY, width=1)
                    d.text((lx, ly), disp, font=F_TAG, fill=INK)
                    placed_labels.append((lx, ly, tw, th))
                    break
    # Legend inside the box, bottom-left over empty ocean: the title
    # row is too narrow for it once badges 2 and 3 both exist.
    badges = sorted({b for _lo, _la, _n, b, _lb in dots if b})
    leg = "DOT = 1 STORY" + "".join(
        f" · {b} = {['', '', 'TWO', 'THREE'][b]}" for b in badges)
    d.text((x + 6, y + h - 15), leg, font=F_TAG, fill=INK)


def main():
    stories = all_stories()
    n = len(stories)
    regs = region_counts()
    dots = map_dots()
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    MX = 24
    CW = W - 2 * MX

    # Masthead
    d.rectangle([0, 0, W, 32], fill=NAVY)
    d.text((MX, 6), "THE WORLD IN ONE DAY", font=F_MAST, fill=(255, 255, 255))
    right = (f"{n} STORIES  ·  7 REGIONS  ·  EVERY ONE DATED "
             "SATURDAY 21 NOVEMBER 2026")
    d.text((W - MX - d.textlength(right, font=F_STAT_L), 9), right,
           font=F_STAT_L, fill=(255, 220, 120))

    # Date headline + sub-headline (single line; shrink font until it fits)
    title = "Saturday 21 November 2026"
    d.text(((W - d.textlength(title, font=F_DATE)) / 2, 38), title,
           font=F_DATE, fill=INK)
    sub = ("COP31 talks run into overtime  ·  missiles over Riyadh  ·  "
           "a quake shakes Peru")
    sub_fnt = F_SUB
    for size in (21, 20, 19, 18):
        sub_fnt = font(SERIF, size)
        if d.textlength(sub, font=sub_fnt) <= CW:
            break
    d.text(((W - d.textlength(sub, font=sub_fnt)) / 2, 96), sub,
           font=sub_fnt, fill=INK)
    d.line([MX, 124, W - MX, 124], fill=RED, width=3)

    # Stat boxes (6)
    sy, sh, gap = 130, 62, 10
    bw = (CW - 5 * gap) / 6
    for i, (num, lab) in enumerate(STATS):
        bx = MX + i * (bw + gap)
        d.rectangle([bx, sy, bx + bw, sy + sh], outline=INK, width=2)
        d.text((bx + 8, sy + 3), num, font=F_STAT_N, fill=RED)
        for j, ln in enumerate(lab.split("\n")):
            d.text((bx + 8, sy + 34 + j * 12), ln, font=F_STAT_L, fill=MUTED)
        # small illustration, top-right corner of the box (fix #4).
        # 20 px: even the widest number ("DAY 13", 121.4 px) leaves
        # 24.9 px to its right, and the icon starts 24 px from the
        # box's right edge — verified visually, no touching.
        STAT_ICONS[STAT_ART[i]](d, int(bx + bw - 24), sy + 4, 20)

    # Region bar: coloured squares + honest counts
    ry = 198
    parts_w = 0
    segs = []
    for name, cnt in regs:
        segs.append((REGION_COLOR[name], f"{name} {cnt}"))
        parts_w += 14 + d.textlength(f"{name} {cnt}", font=F_REG) + 18
    parts_w -= 18
    cx = (W - parts_w) / 2
    for col, txt in segs:
        d.rectangle([cx, ry + 6, cx + 12, ry + 18], fill=col)
        cx += 14
        d.text((cx, ry + 4), txt, font=F_REG, fill=INK)
        cx += d.textlength(txt, font=F_REG) + 18

    # Heroes
    hy, hh = 230, 268
    hw = (CW - 2 * 11) / 3
    for i, hero in enumerate(HEROES):
        draw_hero(d, MX + i * (hw + 11), hy, hw, hero)

    # Grid: 2 rows x 5 columns (fix #4b: cells 144 px tall to fit the
    # 52 px art strip; the extra 20 px comes from a 2 px hero gap, a
    # 4 px row gap and a 14 px shorter map — DATE CHECK and footer
    # do not move).
    gy, gh, ggap = 500, 144, 4
    gw = (CW - 4 * 8) / 5
    for idx, item in enumerate(GRID):
        r, c = divmod(idx, 5)
        draw_grid_cell(d, MX + c * (gw + 8), gy + r * (gh + ggap),
                       gw, gh, item)

    # Map (left) + ALSO list (right)
    my = 798
    map_w = 404
    d.text((MX, my), "WHERE IT HAPPENED", font=F_MAP_T, fill=NAVY)
    draw_map(d, MX, my + 20, map_w, 114, dots)

    ax = MX + map_w + 16
    aw = W - MX - ax
    n_also = len(ALSO)
    d.text((ax, my), f"ALSO ON SATURDAY 21 NOVEMBER — {n_also} MORE STORIES",
           font=F_ALSO_T, fill=NAVY)
    d.line([ax, my + 20, W - MX, my + 20], fill=INK, width=2)
    rows = (n_also + 1) // 2
    avail = 114 - 6
    leading = max(11, min(19, avail // max(rows, 1)))
    # Width is the binding constraint for ALSO text, so the font is
    # fixed small (11 px, 10 px when there are many rows); only the
    # leading adapts to the row count. Fix #4: 11 px was tried for
    # the 20-row list and rejected — 6 of 20 items truncate at the
    # 270 px column width; re-measured in fix #7 (after the Abuja /
    # Banda Sea / Brussels replacements): 7 of 20 truncate at 11 px
    # (ABUJA, BANDA SEA, LAS VEGAS x2, BRUSSELS, MAURITIUS,
    # MELBOURNE), so 10 px stays.
    afont = F_ALSO11 if rows <= 8 else F_ALSO10
    colw = (aw - 16) / 2
    for i, (place, text, source, _region, _lo, _la) in enumerate(ALSO):
        col = i // rows if rows else 0
        row = i % rows if rows else 0
        axx = ax + col * (colw + 16)
        ayy = my + 26 + row * leading
        head = f"{14 + i} {place}: "
        d.text((axx, ayy), head, font=afont, fill=RED)
        hx = d.textlength(head, font=afont)
        full = f"{text} ({source})"
        d.text((axx + hx, ayy), clipped(d, full, afont, colw - hx),
               font=afont, fill=INK)

    # DATE CHECK box
    dy = 940
    d.rectangle([MX, dy, W - MX, dy + 44], outline=INK, width=1)
    d.text((MX + 8, dy + 4), "DATE CHECK", font=F_DC_T, fill=RED)
    dc = ("Left out — they belong to Friday 20 November: Wall Street's "
          "slide · Russia's barrage on Kyiv's bridges · the missile "
          "that came down in Poland · the UK–EU deal · Cyclone Akvan's "
          "landfall. Older: Voyager 1's light-day (18 Nov). "
          "Unconfirmed at press time: BepiColombo at Mercury · a final "
          "COP31 text.")
    dclines = wrap(d, dc, F_DC, CW - 16)
    text_block(d, MX + 8, dy + 20, dclines[:2], F_DC, INK, 13)

    # Footer
    fy = 992
    foot1 = ("Every story here happened, or was first reported, on "
             "Saturday 21 November 2026.")
    d.text(((W - d.textlength(foot1, font=F_FOOT_B)) / 2, fy), foot1,
           font=F_FOOT_B, fill=INK)
    foot2 = ("Sources named beside each story · Original drawings · "
             "HOW WE CHECKED: CONFIRMED = 2+ outlets · OFFICIAL = on "
             "the record · REPORTED = one outlet · CLAIM = one side's "
             "account")
    ff = F_FOOT
    for size in (12, 11, 10):
        ff = font(SANS, size)
        if d.textlength(foot2, font=ff) <= CW:
            break
    d.text(((W - d.textlength(foot2, font=ff)) / 2, fy + 16), foot2,
           font=ff, fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    data = open(OUT, "rb").read()
    print(f"wrote {OUT} {len(data)} bytes "
          f"sha256={hashlib.sha256(data).hexdigest()}")
    print(f"stories={n} regions={dict(regs)} dots={len(dots)} "
          f"badges={[(t[2], t[3]) for t in dots if t[3]]}")


if __name__ == "__main__":
    main()
