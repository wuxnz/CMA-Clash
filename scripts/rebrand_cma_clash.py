#!/usr/bin/env python3
"""User-facing rebrand: ClassQuiz -> CMA Clash (skip internal package paths in code)."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    "node_modules",
    ".svelte-kit",
    "build",
    "cma-clash-research",
    "migrations",
    "classquiz/seed/banks",
}

SKIP_SUFFIX = {".png", ".jpg", ".webp", ".gif", ".mp3", ".lock", ".license", ".pyc"}


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return True
    if path.suffix in SKIP_SUFFIX:
        return True
    if path.name == "rebrand_cma_clash.py":
        return True
    return False


VALUE_REPLACEMENTS = [
    ("ClassQuiz-Quiz", "CMA Clash quiz"),
    ("ClassQuiz-Quizzes", "CMA Clash quizzes"),
    ("ClassQuiz-Quiz", "CMA Clash quiz"),
    ("ClassQuiz-Backup-Code", "CMA-Clash-Backup-Code"),
    ("ClassQuiz-", "CMA-Clash-"),
    ("ClassQuiz", "CMA Clash"),
    ("classquiz.de", ""),
    ("https://classquiz.de", ""),
    ("http://classquiz.de", ""),
    ("classquiz.de/", "/"),
    ("#classquiz:", "#cma-clash:"),
    ("translate.mawoka.eu/engage/classquiz", "hosted.weblate.org"),
    ("hosted.weblate.org/engage/classquiz", "hosted.weblate.org/engage/cma-clash"),
    ("report@mawoka.eu", "abuse@example.com"),
    ("deleteme@mawoka.eu", "privacy@example.com"),
    ("https://mawoka.eu/contact", "/docs"),
    ("https://mawoka.eu/?utm_source=ClassQuiz&utm_medium=Email", "/"),
    ("https://mawoka.eu/?utm_source=CMA Clash&utm_medium=Email", "/"),
    ("Send with love by <a href='/'", "CMA Clash — <a href='/'"),
    ("Made with ❤️ by {{mawoka_link}}", "CMA Clash — built with ❤️"),
    ("Gemacht mit ❤️ von {{mawoka_link}}", "CMA Clash — mit ❤️ gebaut"),
    ("{{mawoka_link}}", "CMA Clash"),
    ("If you find this useful, please consider {{donate_link}}.", ""),
    ("Wenn ClassQuiz hilfreich ist, würde eine {{donate_link}} helfen.", ""),
]


def transform_text(text: str, *, allow_module_paths: bool) -> str:
    if not allow_module_paths:
        # preserve python module paths in dev docs
        placeholders = {}
        for i, m in enumerate(re.finditer(r"\bclassquiz(?:\.[a-z_]+)+", text)):
            key = f"__CLASSQUIZ_MOD_{i}__"
            placeholders[key] = m.group(0)
            text = text.replace(m.group(0), key, 1)
        for m in re.finditer(r"classquiz:app"):
            key = f"__CLASSQUIZ_APP__"
            placeholders[key] = m.group(0)
            text = text.replace(m.group(0), key, 1)

    for old, new in VALUE_REPLACEMENTS:
        text = text.replace(old, new)

    text = re.sub(
        r"If you find this useful, please consider \{\{donate_link\}\}\.",
        "",
        text,
    )
    text = text.replace("navbar.donate", "navbar.donate")  # key unchanged

    if not allow_module_paths:
        for key, val in placeholders.items():
            text = text.replace(key, val)
    return text


def process_locales():
    locale_dir = ROOT / "frontend/src/lib/i18n/locales"
    for path in locale_dir.glob("*.json"):
        if path.name.endswith(".license"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        raw = json.dumps(data, ensure_ascii=False, indent=4)
        raw = transform_text(raw, allow_module_paths=False)
        # fix double spaces from empty donate strings
        raw = re.sub(r'",\s*"donate":\s*""', '",\n        "donate": ""', raw)
        path.write_text(raw + "\n", encoding="utf-8")


def process_file(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    allow_modules = "docs/develop" in str(path) or "docs/self-host" in str(path)
    new = transform_text(text, allow_module_paths=allow_modules)
    if new != text:
        path.write_text(new, encoding="utf-8")


def main():
    process_locales()
    patterns = [
        "frontend/src/**/*.svelte",
        "frontend/src/**/*.ts",
        "frontend/src/**/*.js",
        "frontend/static/**",
        "classquiz/emails/**",
        "docs/**",
        "*.md",
        ".github/**",
        "CONTACT.md",
        "CONTRIBUTING.md",
        "README_CMA_CLASH.md",
        "docker-compose*.yml",
        "frontend/README.md",
    ]
    for pattern in patterns:
        for path in ROOT.glob(pattern):
            if path.is_file() and not should_skip(path):
                process_file(path)


if __name__ == "__main__":
    main()
