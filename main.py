"""The Robot Vacuum's Funniest Excuse.

Writes one line (at most 120 characters) to /output/entry.txt: the excuse
a robot vacuum gives for missing a spot.

Output directory follows the kit contract: $MAKEFUN_OUTPUT_DIR when set,
otherwise /output. The file holds the line verbatim, with no trailing
newline, so its byte count equals the line's character count.
"""

import os

LINE = "My cliff sensors identified the rug fringe as a staircase to nowhere. I chose life."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
