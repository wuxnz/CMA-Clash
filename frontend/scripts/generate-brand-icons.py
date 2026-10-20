#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 CMA Clash contributors
# SPDX-License-Identifier: MPL-2.0
"""Rasterize static/icons/cma-clash-mark.svg into favicon/PWA assets."""

from __future__ import annotations

import struct
import zlib
from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "static"
SRC = STATIC / "icons" / "cma-clash-mark.svg"
ARTIFACTS = Path("/opt/cursor/artifacts")


def png_bytes(size: int, pad: float = 0.0) -> bytes:
    return cairosvg.svg2png(
        url=str(SRC),
        output_width=size,
        output_height=size,
        scale=1.0,
    )


def write_png(path: Path, size: int) -> None:
    path.write_bytes(png_bytes(size))


def write_maskable(path: Path, size: int) -> None:
    """Icon with extra padding for Android maskable safe zone."""
    inner = int(size * 0.72)
    pad = (size - inner) // 2
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">
      <rect width="{size}" height="{size}" fill="#0b0f1a"/>
      <g transform="translate({pad},{pad}) scale({inner / 128})">
        {SRC.read_text().split('<svg', 1)[1].split('>', 1)[1].rsplit('</svg>', 1)[0]}
      </g>
    </svg>"""
    path.write_bytes(
        cairosvg.svg2png(bytestring=svg.encode(), output_width=size, output_height=size)
    )


def write_ico(path: Path) -> None:
    sizes = [16, 32, 48]
    images = []
    for s in sizes:
        data = png_bytes(s)
        images.append((s, data))

    # Minimal ICO builder (PNG embedded)
    offset = 6 + 16 * len(images)
    parts = [struct.pack("<HHH", 0, 1, len(images))]
    for s, data in images:
        parts.append(
            struct.pack(
                "<BBBBHHII",
                s,
                s,
                0,
                0,
                1,
                32,
                len(data),
                offset,
            )
        )
        offset += len(data)
    for _, data in images:
        parts.append(data)
    path.write_bytes(b"".join(parts))


def write_og(path: Path) -> None:
    w, h = 1200, 630
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
      <rect width="{w}" height="{h}" fill="#0b0f1a"/>
      <text x="600" y="280" text-anchor="middle" fill="#f8fafc" font-family="system-ui,sans-serif" font-size="72" font-weight="700">CMA Clash</text>
      <text x="600" y="360" text-anchor="middle" fill="#94a3b8" font-family="system-ui,sans-serif" font-size="32">Gamified CCMA exam prep</text>
      <g transform="translate(536,380) scale(2)">
        {SRC.read_text().split('<svg', 1)[1].split('>', 1)[1].rsplit('</svg>', 1)[0]}
      </g>
    </svg>"""
    path.write_bytes(cairosvg.svg2png(bytestring=svg.encode(), output_width=w, output_height=h))


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Missing {SRC}")
    write_png(STATIC / "favicon-16x16.png", 16)
    write_png(STATIC / "favicon-32x32.png", 32)
    write_png(STATIC / "apple-touch-icon.png", 180)
    write_png(STATIC / "android-chrome-192x192.png", 192)
    write_png(STATIC / "android-chrome-512x512.png", 512)
    write_maskable(STATIC / "android-chrome-maskable-512x512.png", 512)
    write_ico(STATIC / "favicon.ico")
    (STATIC / "logo-mark.svg").write_text(SRC.read_text())
    write_og(STATIC / "og-image.png")
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_png(ARTIFACTS / "cma-clash-icon-preview.png", 256)
    print("Wrote brand icons to", STATIC)


if __name__ == "__main__":
    main()
