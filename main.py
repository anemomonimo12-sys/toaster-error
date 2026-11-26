#!/usr/bin/env python3
"""The Funniest Toaster Error Message — writes one line to /output/entry.txt."""

import argparse
import os
import sys

LINE = "ERROR 12: The bread has achieved sentience and refuses to brown. Please negotiate."

MIN_LEN = 1
MAX_LEN = 120
OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> str:
    """Check the entry line is non-blank, 1-120 chars, and valid UTF-8."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if not MIN_LEN <= len(line) <= MAX_LEN:
        raise ValueError(f"entry line must be {MIN_LEN}-{MAX_LEN} chars, got {len(line)}")
    line.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    return line


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Write the toaster error line to /output/entry.txt")
    parser.add_argument("--check", action="store_true",
                        help="only validate the line, do not write the file")
    args = parser.parse_args(argv)
    line = validate_line(LINE)
    if args.check:
        print(f"OK: {len(line)} chars")
        return
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
