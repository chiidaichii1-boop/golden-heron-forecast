#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather, at most 140 characters, for the invented
city of Toastville, to /output/entry.txt. Stdlib only, deterministic.
"""
import os

ENTRY = (
    # Verified: 132 characters, within the 1-140 gate; invented city
    # named first, weather the whole point, smile saved for the last clause.
    "Toastville: scattered showers of marmalade, with a 40% chance of "
    "falling toast. Commuters are advised to carry butter, just in case."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Gate: 1 to 140 UTF-8 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-140 character gate")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
