# SPDX-License-Identifier: MIT
"""Make the AI Judge Laugh — one office joke, one line.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The grader mounts the repo read-only, so the output must go to the absolute
output directory, never to a repo-local output/ folder.
"""

import os

# The joke: a concrete office scene (inbox zero) with a twist in the last
# phrase that flips the achievement itself — the reward for emptying the
# inbox is twelve new emails about it. Line length: 104 characters, well
# under the 200-character gate.
LINE = (
    "I finally emptied my inbox to zero, and IT celebrated by sending me "
    "twelve emails about the achievement."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
