#!/usr/bin/env python3
# ABOUTME: Color correction for raw lightboard images — brightness, channel, saturation, gamma, rolloff

from PIL import Image, ImageEnhance
import sys

def correct_board_image(src_path, dst_path):
    img = Image.open(src_path).convert('RGB')

    # 1. Brightness x1.20
    img = ImageEnhance.Brightness(img).enhance(1.20)

    # 2. Channel adjustments: r x1.06, g x0.90, b x0.99
    r, g, b = img.split()
    r = r.point(lambda v: min(255, int(v * 1.06)))
    g = g.point(lambda v: min(255, int(v * 0.90)))
    b = b.point(lambda v: min(255, int(v * 0.99)))
    img = Image.merge('RGB', (r, g, b))

    # 3. Saturation x1.05
    img = ImageEnhance.Color(img).enhance(1.05)

    # 4. Gamma 0.88 (midtone lift)
    gamma_lut = [int(255 * (v / 255) ** 0.88) for v in range(256)]
    r, g, b = img.split()
    r = r.point(gamma_lut)
    g = g.point(gamma_lut)
    b = b.point(gamma_lut)
    img = Image.merge('RGB', (r, g, b))

    # 5. Highlight rolloff: values above 180 compressed by factor 0.65
    rolloff_lut = [v if v <= 180 else int(180 + (v - 180) * 0.65) for v in range(256)]
    r, g, b = img.split()
    r = r.point(rolloff_lut)
    g = g.point(rolloff_lut)
    b = b.point(rolloff_lut)
    img = Image.merge('RGB', (r, g, b))

    # 6. Resize: long side max 1920px
    w, h = img.size
    max_side = max(w, h)
    if max_side > 1920:
        scale = 1920 / max_side
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    img.save(dst_path, format='JPEG', quality=90)
    print(f"Corrected: {src_path} -> {dst_path}")

if __name__ == '__main__':
    correct_board_image(sys.argv[1], sys.argv[2])
