#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun bounty entry.

Writes one fixed confession line to /output/entry.txt.
Deterministic: no network, no randomness, no model calls.
"""

import os

ENTRY = "I have no idea what I'm doing \u2014 I just guess the next word and say it like I wrote the manual."

# The sealed gate accepts only UTF-8 text of 1-200 characters, a single line.
# Enforce that here so a bad line can never be written by accident.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the confession line.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
