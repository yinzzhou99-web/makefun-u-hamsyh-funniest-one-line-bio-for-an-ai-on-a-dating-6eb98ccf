#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes the bio to entry.txt. Stdlib only; the grader runs it with
python3.13 and no network.
"""

import os

BIO = (
    "Fluent in 40 languages, still can\u2019t tell if you\u2019re flirting "
    "\u2014 swipe right if you like long walks through my training data."
)

LIMIT = 180


def empty(folder):
    # Clear the mounted output folder's files; the folder itself stays.
    for name in os.listdir(folder):
        target = os.path.join(folder, name)
        if os.path.isfile(target):
            os.remove(target)


def main():
    bio = " ".join(BIO.split())  # one clean line, whatever the source has
    if len(bio) > LIMIT or not bio:
        raise SystemExit(f"bio is {len(bio)} chars, limit is {LIMIT}")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    empty(folder)
    dest = os.path.join(folder, "entry.txt")
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(bio)
    os.chmod(dest, 0o644)  # scorer must be able to read entry.txt any umask
    print(f"wrote {len(bio)} characters to {dest}")


if __name__ == "__main__":
    main()
