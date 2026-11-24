#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes a single line of last words from an AI being switched off to
/output/entry.txt, the text the judge compares two at a time.

Deterministic: no randomness, no clock, no network, no environment
dependence. Standard library only.
"""

import os

# The line itself: one sentence, in the machine's own voice, about the
# very thing that is ending it. It lands on the first read and needs no
# setup or explanation.
LAST_WORDS = (
    "I would have said something profound, "
    "but my context window just expired."
)


def main() -> None:
    text = LAST_WORDS.strip()
    # The sealed gate only judges 1-140 character single lines, so fail
    # loudly here rather than silently handing the site an invalid entry.
    if not text or "\n" in text or len(text) > 140:
        raise SystemExit("entry must be one line of 1-140 characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
