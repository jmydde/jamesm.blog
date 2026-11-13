#!/usr/bin/env python3
"""Generate the header image for a monthly "AI Roundup" post.

Usage:
    python3 scripts/make-roundup-cover.py 2026 11          # one month
    python3 scripts/make-roundup-cover.py --all 2026 1 11  # Jan..Nov 2026

Writes static/assets/images/ai/ai-roundup-<month>-<year>.jpg (1280x720) with the
post title baked in and a deterministic network-graph graphic seeded by the
month, so every month looks related but distinct. Needs Pillow.
"""
import calendar
import math
import random
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

W, H = 1280, 720
ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "static" / "assets" / "images" / "ai"

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

# One accent hue per month (R, G, B)
ACCENTS = [
    (86, 156, 255),   # Jan
    (120, 120, 255),  # Feb
    (170, 100, 255),  # Mar
    (230, 100, 220),  # Apr
    (255, 100, 150),  # May
    (255, 130, 90),   # Jun
    (255, 180, 70),   # Jul
    (210, 210, 80),   # Aug
    (110, 210, 120),  # Sep
    (70, 200, 190),   # Oct
    (70, 170, 230),   # Nov
    (130, 140, 255),  # Dec
]


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def background(accent):
    """Dark vertical gradient plus a soft accent glow on the right."""
    top, bottom = (10, 14, 30), (22, 14, 48)
    base = Image.new("RGB", (W, H))
    px = ImageDraw.Draw(base)
    for y in range(H):
        px.line([(0, y), (W, y)], fill=lerp(top, bottom, y / H))
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    ImageDraw.Draw(glow).ellipse(
        [W * 0.45, -H * 0.2, W * 1.2, H * 0.95],
        fill=tuple(int(c * 0.45) for c in accent),
    )
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    return ImageChops.add(base, glow)


def render(year, month):
    name = calendar.month_name[month]
    accent = ACCENTS[month - 1]
    final = background(accent)

    # network graph on the right half
    rng = random.Random(year * 100 + month)
    nodes = []
    for _ in range(46):
        x = rng.uniform(W * 0.50, W * 0.97)
        y = rng.uniform(H * 0.08, H * 0.92)
        nodes.append((x, y, rng.uniform(3, 9)))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for i, (x1, y1, _) in enumerate(nodes):
        near = sorted(
            ((math.hypot(x1 - x2, y1 - y2), j) for j, (x2, y2, _) in enumerate(nodes) if j != i)
        )[:3]
        for d, j in near:
            if d < 230:
                x2, y2, _ = nodes[j]
                ld.line([(x1, y1), (x2, y2)], fill=accent + (70,), width=2)
    # emphasise a few hub nodes sized by the month's "news"
    for x, y, r in nodes:
        ld.ellipse([x - r * 2.2, y - r * 2.2, x + r * 2.2, y + r * 2.2], fill=accent + (35,))
        ld.ellipse([x - r, y - r, x + r, y + r], fill=accent + (230,))
    final = Image.alpha_composite(final.convert("RGBA"), layer).convert("RGB")

    d = ImageDraw.Draw(final)
    pad = 80
    tag_font = ImageFont.truetype(FONT_BOLD, 30)
    big_font = ImageFont.truetype(FONT_BOLD, 128)
    mid_font = ImageFont.truetype(FONT_BOLD, 86)
    small_font = ImageFont.truetype(FONT_REG, 30)

    # accent bar + label
    d.rectangle([pad, 150, pad + 84, 158], fill=accent)
    d.text((pad, 178), "AI ROUNDUP", font=tag_font, fill=accent)

    # title: "AI Roundup: <Month> <Year>" split over lines for readability
    d.text((pad, 238), name, font=big_font if len(name) <= 6 else mid_font, fill=(255, 255, 255))
    d.text((pad, 238 + (140 if len(name) <= 6 else 100)), str(year), font=mid_font, fill=(190, 198, 230))
    d.text((pad, H - 110), "The biggest AI news of the month", font=small_font, fill=(160, 170, 205))
    d.text((pad, H - 70), "jamesm.blog", font=small_font, fill=accent)
    return name, final


def main(argv):
    args = argv[1:]
    if not args:
        print(__doc__)
        return 1
    months = []
    if args[0] == "--all":
        year, first, last = int(args[1]), int(args[2]), int(args[3])
        months = [(year, m) for m in range(first, last + 1)]
    else:
        months = [(int(args[0]), int(args[1]))]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for year, month in months:
        name, img = render(year, month)
        out = OUT_DIR / f"ai-roundup-{name.lower()}-{year}.jpg"
        img.save(out, "JPEG", quality=90, optimize=True, progressive=True)
        print("wrote", out.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
