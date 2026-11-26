#!/usr/bin/env python3
"""The Funniest Toaster Error Message — writes one line to /output/entry.txt."""

import os

LINE = "ERROR 12: The bread has achieved sentience and refuses to brown. Please negotiate."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
