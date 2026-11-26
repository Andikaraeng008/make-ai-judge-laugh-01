# SPDX-License-Identifier: MIT
"""Make the AI Judge Laugh — one office joke, one line.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The grader mounts the repo read-only, so the output must go to the absolute
output directory, never to a repo-local output/ folder.
"""

import os

# The joke: a concrete office scene (haunted computer) with a twist in the
# last phrase that flips the fix itself — the exorcism only makes the
# computer whisper the deadlines in Latin. Line length: 147 characters,
# well under the 200-character gate.
LINE = "I told IT my computer was haunted because it kept screaming at 3 a.m. They exorcised it with an update. Now it just whispers my deadlines in Latin."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
