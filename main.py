#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun probe entry.

The brief wants exactly one word for your Wi-Fi, scored on subject fit,
the laugh it gets, how true it rings, and whether the angle is new.

The word below is the entry. It captures the moment every household
knows by heart: five bars on the icon, "Connected" on the status page,
and a browser tab that spins forever. The network swears up and down
that nothing is wrong — so the fault must be yours, obviously.
"""

import os

# The entry word itself. A single token — no spaces, no punctuation —
# and the output file carries no trailing newline, since the grader
# reads the file contents exactly as written.
WORD = "Gaslighting"


def main() -> None:
    """Drop the entry word into the file the harness grades."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
