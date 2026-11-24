#!/usr/bin/env python3
"""Print the entry line for the 'Alien Field Notes: The Two-Day Earth' make.fun bounty.

Competition: u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000
"""
from pathlib import Path


def main() -> int:
    # Resolve entry.txt next to this script so the grader can run from any cwd.
    entry = Path(__file__).with_name("entry.txt")
    print(entry.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
