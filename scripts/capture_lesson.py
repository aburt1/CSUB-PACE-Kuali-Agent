#!/usr/bin/env python3
"""Append a team lesson to references/lessons-learned.md."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import textwrap


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--title", required=True)
    parser.add_argument("--observed", required=True)
    parser.add_argument("--rule", required=True)
    parser.add_argument("--better", required=True)
    parser.add_argument("--pressure-test", default="")
    args = parser.parse_args()

    root = Path(args.skill_root)
    lessons = root / "references" / "lessons-learned.md"
    title = args.title.strip().rstrip(".")
    block = [
        "",
        f"## {title}",
        "",
        f"Date: {date.today().isoformat()}",
        "",
        "Observed failure:",
        textwrap.fill(args.observed.strip(), width=88),
        "",
        "Rule:",
        textwrap.fill(args.rule.strip(), width=88),
        "",
        "Better behavior:",
        textwrap.fill(args.better.strip(), width=88),
    ]
    if args.pressure_test.strip():
        block += ["", "Pressure-test prompt:", args.pressure_test.strip()]
    with lessons.open("a", encoding="utf-8") as f:
        f.write("\n".join(block) + "\n")
    print(f"Appended lesson to {lessons}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
