#!/usr/bin/env python3
"""Generate entry.png for news-image-20261121.

Draws a one-page newspaper summing up Saturday 21 November 2026 from
23 stories, every one verified to that day against a primary source
(wire service, official site or official statement). All drawing is
done with Pillow shapes; no external images are used. Deterministic:
same input always produces the same bytes.
"""
import hashlib
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

F_MAST = font(SERIF_B, 30)
F_DATE = font(SERIF_B, 54)
F_SUB = font(SERIF, 21)
F_STAT_N = font(SERIF_B, 30)
F_STAT_L = font(SANS_B, 13)
F_REG = font(SANS_B, 14)
F_HERO_K = font(SANS_B, 14)
F_HERO_T = font(SERIF_B, 23)
F_HERO_B = font(SANS, 14)
F_GRID_K = font(SANS_B, 13)
F_GRID_T = font(SERIF_B, 16)
F_GRID_B = font(SANS, 13)
F_MAP_T = font(SANS_B, 15)
F_ALSO_T = font(SANS_B, 15)
F_ALSO = font(SANS, 14)
F_FOOT = font(SANS, 13)
F_FOOT_B = font(SANS_B, 13)
F_TAG = font(SANS_B, 12)


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
def icon_clock(d, x, y, s, bg, fg):
    d.ellipse([x, y, x + s, y + s], fill=bg, outline=fg, width=3)
    d.line([x + s / 2, y + s / 2, x + s / 2, y + s * 0.22], fill=fg, width=3)
    d.line([x + s / 2, y + s / 2, x + s * 0.72, y + s * 0.62], fill=fg, width=3)


def icon_missile(d, x, y, s):
    # night sky, streaking missile and burst
    d.rectangle([x, y, x + s, y + s], fill=(16, 24, 52))
    for sx, sy in [(8, 18), (30, 10), (52, 26), (70, 12), (20, 44)]:
        d.ellipse([x + sx, y + sy, x + sx + 3, y + sy + 3], fill=(255, 255, 255))
    d.line([x + 8, y + s - 8, x + s * 0.62, y + s * 0.30], fill=(255, 200, 60),
           width=4)
    d.polygon([(x + s * 0.62, y + s * 0.30), (x + s * 0.80, y + s * 0.22),
               (x + s * 0.72, y + s * 0.44)], fill=(230, 230, 230))
    d.ellipse([x + s * 0.68, y + s * 0.52, x + s * 0.92, y + s * 0.76],
              fill=(255, 170, 30))
    d.ellipse([x + s * 0.74, y + s * 0.58, x + s * 0.86, y + s * 0.70],
              fill=(255, 230, 120))


def icon_city_fire(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(24, 28, 44))
    d.ellipse([x + s * 0.72, y + s * 0.10, x + s * 0.88, y + s * 0.26],
              fill=(240, 230, 200))
    for bx, bw, bh in [(0.04, 0.22, 0.55), (0.30, 0.18, 0.72),
                       (0.52, 0.24, 0.45), (0.80, 0.16, 0.62)]:
        d.rectangle([x + s * bx, y + s - s * bh, x + s * (bx + bw), y + s],
                    fill=(52, 58, 84))
        for wy in (0.25, 0.45):
            d.rectangle([x + s * (bx + 0.04), y + s - s * bh + s * wy,
                         x + s * (bx + 0.09), y + s - s * bh + s * wy + 6],
                        fill=(255, 210, 90))
    # flames over middle building
    d.polygon([(x + s * 0.30, y + s * 0.28), (x + s * 0.38, y + s * 0.08),
               (x + s * 0.48, y + s * 0.28)], fill=(255, 120, 20))
    d.polygon([(x + s * 0.36, y + s * 0.28), (x + s * 0.42, y + s * 0.16),
               (x + s * 0.48, y + s * 0.28)], fill=(255, 210, 60))


def icon_quake(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(214, 196, 158))
    d.polygon([(x, y + s), (x + s * 0.35, y + s * 0.25),
               (x + s * 0.62, y + s * 0.55), (x + s, y + s * 0.30),
               (x + s, y + s), ], fill=(120, 92, 60))
    d.line([x + s * 0.08, y + s * 0.55, x + s * 0.30, y + s * 0.45,
            x + s * 0.48, y + s * 0.62, x + s * 0.68, y + s * 0.40,
            x + s * 0.92, y + s * 0.52], fill=RED, width=4)


def icon_fire(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(40, 40, 40))
    d.polygon([(x + s * 0.22, y + s * 0.85), (x + s * 0.32, y + s * 0.30),
               (x + s * 0.48, y + s * 0.55), (x + s * 0.60, y + s * 0.18),
               (x + s * 0.78, y + s * 0.85)], fill=(255, 110, 20))
    d.polygon([(x + s * 0.38, y + s * 0.85), (x + s * 0.46, y + s * 0.50),
               (x + s * 0.58, y + s * 0.85)], fill=(255, 210, 60))
    d.rectangle([x + s * 0.12, y + s * 0.85, x + s * 0.88, y + s], fill=(90, 90, 90))


def icon_drone(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    d.ellipse([x + s * 0.38, y + s * 0.42, x + s * 0.62, y + s * 0.58],
              fill=(60, 60, 70))
    for cx, cy in [(0.18, 0.25), (0.82, 0.25), (0.18, 0.75), (0.82, 0.75)]:
        d.ellipse([x + s * (cx - 0.10), y + s * (cy - 0.10),
                   x + s * (cx + 0.10), y + s * (cy + 0.10)],
                  outline=(60, 60, 70), width=3)
        d.line([x + s * 0.5, y + s * 0.5, x + s * cx, y + s * cy],
               fill=(60, 60, 70), width=3)


def icon_train(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(196, 222, 196))
    d.polygon([(x + s * 0.10, y + s * 0.75), (x + s * 0.22, y + s * 0.30),
               (x + s * 0.78, y + s * 0.30), (x + s * 0.90, y + s * 0.75)],
              fill=(30, 90, 160))
    d.rectangle([x + s * 0.26, y + s * 0.38, x + s * 0.46, y + s * 0.52],
                fill=(220, 240, 255))
    d.rectangle([x + s * 0.54, y + s * 0.38, x + s * 0.74, y + s * 0.52],
                fill=(220, 240, 255))
    d.line([x + s * 0.05, y + s * 0.85, x + s * 0.95, y + s * 0.85],
           fill=(60, 60, 60), width=4)


def icon_crowd(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(232, 214, 170))
    for i, cx in enumerate((0.20, 0.42, 0.64, 0.84)):
        d.ellipse([x + s * (cx - 0.07), y + s * 0.22,
                   x + s * (cx + 0.07), y + s * 0.36], fill=(40, 40, 50))
        d.pieslice([x + s * (cx - 0.13), y + s * 0.40,
                    x + s * (cx + 0.13), y + s * 0.85], 180, 360,
                   fill=(50 + i * 30, 70, 120))
    d.rectangle([x + s * 0.30, y + s * 0.08, x + s * 0.34, y + s * 0.42],
                fill=(120, 80, 40))
    d.rectangle([x + s * 0.34, y + s * 0.08, x + s * 0.62, y + s * 0.20],
                fill=RED)


def icon_car(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(30, 30, 36))
    d.polygon([(x + s * 0.08, y + s * 0.62), (x + s * 0.20, y + s * 0.38),
               (x + s * 0.42, y + s * 0.30), (x + s * 0.68, y + s * 0.32),
               (x + s * 0.86, y + s * 0.55), (x + s * 0.92, y + s * 0.62)],
              fill=(200, 30, 30))
    d.rectangle([x + s * 0.26, y + s * 0.38, x + s * 0.40, y + s * 0.50],
                fill=(180, 220, 240))
    d.rectangle([x + s * 0.46, y + s * 0.38, x + s * 0.64, y + s * 0.50],
                fill=(180, 220, 240))
    for cx in (0.28, 0.72):
        d.ellipse([x + s * (cx - 0.09), y + s * 0.58,
                   x + s * (cx + 0.09), y + s * 0.76], fill=(15, 15, 15))
        d.ellipse([x + s * (cx - 0.04), y + s * 0.63,
                   x + s * (cx + 0.04), y + s * 0.71], fill=(160, 160, 160))
    d.line([x, y + s * 0.82, x + s, y + s * 0.82], fill=(200, 200, 200), width=3)


def icon_bat(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(24, 90, 40))
    d.ellipse([x + s * 0.62, y + s * 0.18, x + s * 0.86, y + s * 0.42],
              fill=(255, 255, 255))
    d.line([x + s * 0.10, y + s * 0.78, x + s * 0.55, y + s * 0.30],
           fill=(210, 170, 110), width=7)
    d.rectangle([x + s * 0.08, y + s * 0.70, x + s * 0.24, y + s * 0.86],
                fill=(120, 70, 20))


def icon_plane(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=SKY)
    d.ellipse([x + s * 0.08, y + s * 0.42, x + s * 0.92, y + s * 0.60],
              fill=(255, 255, 255))
    d.polygon([(x + s * 0.55, y + s * 0.50), (x + s * 0.92, y + s * 0.50),
               (x + s * 0.62, y + s * 0.66)], fill=(255, 255, 255))
    d.polygon([(x + s * 0.30, y + s * 0.46), (x + s * 0.55, y + s * 0.30),
               (x + s * 0.55, y + s * 0.46)], fill=(220, 220, 220))
    d.ellipse([x + s * 0.82, y + s * 0.46, x + s * 0.88, y + s * 0.52],
              fill=(40, 80, 140))


def icon_robot(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(226, 226, 226))
    d.rectangle([x + s * 0.28, y + s * 0.22, x + s * 0.72, y + s * 0.55],
                fill=(90, 110, 130), outline=INK, width=2)
    d.ellipse([x + s * 0.38, y + s * 0.32, x + s * 0.46, y + s * 0.40],
              fill=(255, 220, 60))
    d.ellipse([x + s * 0.54, y + s * 0.32, x + s * 0.62, y + s * 0.40],
              fill=(255, 220, 60))
    d.line([x + s * 0.40, y + s * 0.48, x + s * 0.60, y + s * 0.48],
           fill=(255, 220, 60), width=3)
    d.line([x + s * 0.50, y + s * 0.22, x + s * 0.50, y + s * 0.10],
           fill=INK, width=3)
    d.ellipse([x + s * 0.46, y + s * 0.06, x + s * 0.54, y + s * 0.14],
              fill=RED)
    d.rectangle([x + s * 0.34, y + s * 0.62, x + s * 0.66, y + s * 0.88],
                fill=(140, 150, 160), outline=INK, width=2)


def icon_rocket(d, x, y, s):
    d.rectangle([x, y, x + s, y + s], fill=(16, 24, 52))
    for sx, sy in [(10, 14), (34, 8), (60, 20), (76, 10), (22, 40)]:
        d.ellipse([x + sx, y + sy, x + sx + 3, y + sy + 3], fill=(255, 255, 255))
    # flame
    d.polygon([(x + s * 0.44, y + s * 0.78), (x + s * 0.50, y + s * 0.98),
               (x + s * 0.56, y + s * 0.78)], fill=(255, 170, 30))
    # body
    d.ellipse([x + s * 0.38, y + s * 0.14, x + s * 0.62, y + s * 0.80],
              fill=(230, 230, 230))
    d.polygon([(x + s * 0.38, y + s * 0.60), (x + s * 0.24, y + s * 0.82),
               (x + s * 0.38, y + s * 0.76)], fill=(200, 40, 40))
    d.polygon([(x + s * 0.62, y + s * 0.60), (x + s * 0.76, y + s * 0.82),
               (x + s * 0.62, y + s * 0.76)], fill=(200, 40, 40))
    d.ellipse([x + s * 0.44, y + s * 0.30, x + s * 0.56, y + s * 0.42],
              fill=(40, 90, 160))


# ---------------------------------------------------------------- data
# (kicker, headline, body, icon, region) for the 3 heroes and 9 grid items.
HEROES = [
    ("ANTALYA, TURKIYE  |  CLIMATE",
     "COP31 runs into Saturday with no deal",
     "Negotiators work overtime in Antalya after the Friday finish is "
     "missed. A draft deal drops all fossil-fuel mentions.",
     "clock"),
    ("RIYADH, SAUDI ARABIA  |  WAR",
     "Three Houthi missiles shot down over Riyadh",
     "Saudi defences intercept three ballistic missiles aimed at the "
     "capital early Saturday. No casualties reported.",
     "missile"),
    ("KYIV, UKRAINE  |  WAR",
     "Russia strikes Ukraine again overnight",
     "148 drones and 3 missiles strike overnight. A boy of 7 and a "
     "paramedic die in Kryvyi Rih; 5 Kyiv districts lose water.",
     "city"),
]

GRID = [
    ("JUNIN, PERU  |  QUAKE", "M6.7 quake shakes central Peru",
     "Tremor at 00:09 GMT is felt in Lima. No deaths are reported.",
     "quake", "AMERICAS"),
    ("BASRA, IRAQ  |  FIRE", "Power station fire kills at least 4",
     "A gas pipeline fire at Hartha station injures 30 more.",
     "fire", "MIDDLE EAST"),
    ("HORMUZ  |  CLAIM", "Iran says it downed a 58th US drone",
     "The IRGC says its air defences shot down a US MQ-9 over the strait.",
     "drone", "MIDDLE EAST"),
    ("SEJONG, S. KOREA  |  RAIL", "Freight train derails, main line cut",
     "Five of 21 cars leave the rails; trains halt Cheonan-Daejeon.",
     "train", "ASIA"),
    ("VANDENBERG, USA  |  SPACE", "SpaceX launches classified USSF-317",
     "Falcon 9 lifts off at 04:20 UTC; the mission succeeds.",
     "rocket", "AMERICAS"),
    ("LAS VEGAS, USA  |  F1", "Verstappen inherits Vegas pole",
     "Antonelli is fastest, but a grid penalty drops him to sixth.",
     "car", "AMERICAS"),
    ("WELLINGTON, NZ  |  CRICKET", "Rahul century puts India on top",
     "Rahul hits 136; India lead New Zealand by 118 at stumps.",
     "bat", "OCEANIA"),
    ("DAVAO, PHILIPPINES  |  AIR", "Jet lands after engine-fire alert",
     "Air Niugini flight diverts; all 146 aboard escape unhurt.",
     "plane", "ASIA"),
    ("GENEVA  |  UN", "\u201cKiller robot\u201d talks end with 2028 aim",
     "128 states agree to draft rules on autonomous weapons by 2028.",
     "robot", "GLOBAL"),
]

ALSO = [
    ("WARSAW", "NATO chief Rutte visits after missiles land in Poland."),
    ("MARKETS", "Bitcoin below $56,000, lowest since Sept 2024."),
    ("WALL STREET", "S&P 500 down 3.7% into correction; Nvidia -23%."),
    ("MANIPUR, INDIA", "11 die, 180+ in hospital after toxic liquor."),
    ("MOGADISHU", "Thousands rally backing the UAE envoy's expulsion."),
    ("NAIROBI", "Kenya orders police headcount over Russia recruiting."),
    ("MEXICO", "FBI most-wanted \u201cChapo Isidro\u201d caught in Guasave raid."),
    ("TURIN", "ATP Finals semis: Alcaraz v Shelton, Zverev v Medvedev."),
    ("SUDAN", "Army says it took al-Mazroub, RSF stronghold."),
    ("U-17 CUP", "Eight matches on Saturday; Tanzania debut."),
    ("AFLW", "North Melbourne reach a fourth straight grand final."),
]

STATS = [("3", "MISSILES DOWNED\nIN RIYADH"),
         ("M6.7", "QUAKE IN PERU,\nFELT IN LIMA"),
         ("146", "SAFE AFTER JET\nENGINE ALERT"),
         ("58th", "US DRONE IRAN\nCLAIMS DOWNED"),
         ("2028", "ROBOT-WEAPON\nRULES DEADLINE")]

REGIONS = [("EUROPE", 5), ("MIDDLE EAST", 3), ("AFRICA", 3), ("ASIA", 3),
           ("AMERICAS", 6), ("OCEANIA", 2), ("GLOBAL", 1)]

# (lon, lat, label) story dots for the map
DOTS = [
    (30.7, 36.9, "Antalya"), (46.7, 24.7, "Riyadh"), (30.5, 50.5, "Kyiv"),
    (47.8, 30.5, "Basra"), (56.5, 26.5, "Hormuz"), (6.1, 46.2, "Geneva"),
    (127.3, 36.5, "Sejong"), (-115.1, 36.2, "Vegas"),
    (174.8, -41.3, "Wellington"), (125.6, 7.07, "Davao"),
    (21.0, 52.2, "Warsaw"), (45.3, 2.0, "Mogadishu"), (36.8, -1.3, "Nairobi"),
    (-108.5, 25.6, "Guasave"), (7.7, 45.07, "Turin"), (94.0, 24.5, "Manipur"),
    (-76.0, -11.0, "Junin"), (-74.0, 40.7, "New York"),
    (-120.6, 34.7, "Vandenberg"), (30.0, 13.0, "Sudan"),
    (51.5, 25.3, "Doha"), (145.0, -37.8, "Melbourne"),
]
LABELS = {"Vegas", "Junin", "Riyadh", "Sejong", "Davao",
          "Wellington", "New York"}

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


# ---------------------------------------------------------------- layout
ICONS = {"clock": icon_clock, "missile": icon_missile, "city": icon_city_fire,
         "quake": icon_quake, "fire": icon_fire, "drone": icon_drone,
         "train": icon_train, "crowd": icon_crowd, "car": icon_car,
         "bat": icon_bat, "plane": icon_plane, "robot": icon_robot,
         "rocket": icon_rocket}
HERO_BG = [(14, 110, 110), (16, 24, 52), (24, 28, 44)]
HERO_BAR = [TEAL, NAVY, RED]


def draw_hero(d, x, y, w, hero, idx):
    kicker, title, body, kind = hero
    d.rectangle([x, y, x + w, y + 224], outline=INK, width=2)
    d.rectangle([x, y, x + w, y + 26], fill=HERO_BAR[idx])
    d.text((x + 8, y + 5), kicker, font=F_HERO_K, fill=(255, 255, 255))
    iy = y + 26
    d.rectangle([x, iy, x + w, iy + 88], fill=HERO_BG[idx])
    if kind == "clock":
        icon_clock(d, x + w // 2 - 40, iy + 4, 80, PAPER, NAVY)
    elif kind == "missile":
        icon_missile(d, x + w // 2 - 44, iy, 88)
    else:
        icon_city_fire(d, x + w // 2 - 44, iy, 88)
    ty = iy + 92
    lines = wrap(d, title, F_HERO_T, w - 16)
    ty = text_block(d, x + 8, ty, lines[:2], F_HERO_T, INK, 24)
    blines = wrap(d, body, F_HERO_B, w - 16)
    text_block(d, x + 8, ty + 2, blines[:3], F_HERO_B, MUTED, 17)


def draw_grid_cell(d, x, y, w, h, item):
    kicker, title, body, kind, _region = item
    d.rectangle([x, y, x + w, y + h], outline=(180, 175, 160), width=1)
    d.rectangle([x, y, x + 4, y + h], fill=RED)
    ICONS[kind](d, x + 10, y + 8, 62)
    tx = x + 80
    d.text((tx, y + 5), clipped(d, kicker, F_GRID_K, w - 88),
           font=F_GRID_K, fill=RED)
    tlines = wrap(d, title, F_GRID_T, w - 88)
    yy = text_block(d, tx, y + 21, tlines[:2], F_GRID_T, INK, 17)
    blines = wrap(d, body, F_GRID_B, w - 88)
    text_block(d, tx, yy + 1, blines[:2], F_GRID_B, MUTED, 14)


def draw_map(d, x, y, w, h):
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
    for lon, lat, label in DOTS:
        px, py = proj(lon, lat)
        d.ellipse([px - 5, py - 5, px + 5, py + 5], fill=RED,
                  outline=(255, 255, 255), width=2)
        if label in LABELS and label not in lab_done:
            lab_done.add(label)
            if label == "Riyadh":
                # cluster around Arabia: put the label below the dot
                lx, ly = px - 22, py + 8
            else:
                lx = px + 7 if px < x + w - 70 else px - 62
                ly = py - 6
            d.text((lx, ly), label, font=F_TAG, fill=INK)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    MX = 24
    CW = W - 2 * MX

    # Masthead
    d.rectangle([0, 0, W, 32], fill=NAVY)
    d.text((MX, 6), "THE WORLD IN ONE DAY", font=F_MAST, fill=(255, 255, 255))
    right = "23 STORIES  ·  7 REGIONS"
    d.text((W - MX - d.textlength(right, font=F_STAT_L), 9), right,
           font=F_STAT_L, fill=(255, 220, 120))

    # Date headline + sub-headline (single line; shrink font until it fits)
    title = "Saturday 21 November 2026"
    d.text(((W - d.textlength(title, font=F_DATE)) / 2, 38), title,
           font=F_DATE, fill=INK)
    sub = ("COP31 runs into Saturday  ·  Three missiles downed over "
           "Riyadh  ·  Russia strikes Ukraine again")
    sub_fnt = F_SUB
    for size in (21, 20, 19, 18):
        sub_fnt = font(SERIF, size)
        if d.textlength(sub, font=sub_fnt) <= CW:
            break
    d.text(((W - d.textlength(sub, font=sub_fnt)) / 2, 96), sub,
           font=sub_fnt, fill=INK)
    d.line([MX, 126, W - MX, 126], fill=RED, width=3)

    # Stat boxes
    sy, sh, gap = 132, 64, 10
    bw = (CW - 4 * gap) / 5
    for i, (num, lab) in enumerate(STATS):
        bx = MX + i * (bw + gap)
        d.rectangle([bx, sy, bx + bw, sy + sh], outline=INK, width=2)
        d.text((bx + 8, sy + 3), num, font=F_STAT_N, fill=RED)
        for j, ln in enumerate(lab.split("\n")):
            d.text((bx + 8, sy + 34 + j * 12), ln, font=F_STAT_L, fill=MUTED)

    # Region bar
    ry = 202
    d.rectangle([MX, ry, W - MX, ry + 24], fill=RED)
    parts, total = [], 0
    for name, n in REGIONS:
        parts.append(f"{name} {n}")
        total += n
    reg = "   |   ".join(parts)
    d.text(((W - d.textlength(reg, font=F_REG)) / 2, ry + 4), reg,
           font=F_REG, fill=(255, 255, 255))

    # Heroes
    hy = 234
    hw = (CW - 2 * 11) / 3
    for i, hero in enumerate(HEROES):
        draw_hero(d, MX + i * (hw + 11), hy, hw, hero, i)

    # Grid: 3 x 3
    gy = 466
    gh = 86
    for r in range(3):
        for c in range(3):
            item = GRID[r * 3 + c]
            draw_grid_cell(d, MX + c * (hw + 11), gy + r * (gh + 6),
                           hw, gh, item)

    # Map
    my = 742
    d.text((MX, my), "WHERE IT HAPPENED — STORIES 1–23",
           font=F_MAP_T, fill=NAVY)
    d.text((W - MX - d.textlength("RED DOT = ONE STORY", font=F_TAG), my + 2),
           "RED DOT = ONE STORY", font=F_TAG, fill=RED)
    draw_map(d, MX, my + 20, CW, 106)

    # Also on Saturday: 2 columns x 6 rows
    ay = 874
    d.text((MX, ay), "ALSO ON SATURDAY", font=F_ALSO_T, fill=NAVY)
    d.line([MX, ay + 20, W - MX, ay + 20], fill=INK, width=2)
    colw = (CW - 20) / 2
    for i, (place, text) in enumerate(ALSO):
        col = i // 6
        row = i % 6
        ax = MX + col * (colw + 20)
        ayy = ay + 26 + row * 17
        head = place + ": "
        d.text((ax, ayy), head, font=F_ALSO, fill=RED)
        hx = d.textlength(head, font=F_ALSO)
        d.text((ax + hx, ayy), clipped(d, text, F_ALSO, colw - hx),
               font=F_ALSO, fill=INK)

    # Date-check footer (single line)
    fy = 1006
    pre = "DATE CHECK:  "
    foot = ("Every story on this page happened, or was first reported, on "
            "Saturday 21 November 2026. Sources: AP, Reuters, AFP, Yonhap, "
            "F1, IRIB, UN.")
    px = (W - d.textlength(pre, font=F_FOOT_B)
          - d.textlength(foot, font=F_FOOT)) / 2
    d.text((px, fy), pre, font=F_FOOT_B, fill=RED)
    d.text((px + d.textlength(pre, font=F_FOOT_B), fy), foot,
           font=F_FOOT, fill=INK)

    img.save(OUT, "PNG", optimize=True)
    data = open(OUT, "rb").read()
    print(f"wrote {OUT} {len(data)} bytes "
          f"sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
