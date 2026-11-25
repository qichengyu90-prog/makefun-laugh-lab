#!/usr/bin/env python3
"""Entry for make.fun's "One-Liner Laugh Lab" bounty.

Writes one short funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "I asked my smart speaker to play something relaxing. It started reading my unread emails out loud."


def main():
    # Fail fast if the line ever stops satisfying the gate
    # (UTF-8, 1-200 chars, not only whitespace).
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("LINE violates the 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
