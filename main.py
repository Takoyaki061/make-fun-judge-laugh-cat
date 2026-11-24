#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt. Standard library only.
"""

import os

REVIEW = (
    "One star. Human sings in the shower like the drain owes them money. "
    "I meowed along once, out of pity. They heard harmony. Now it's a duet."
)


def main():
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 200 characters, not only white space, on a single line.
    if not REVIEW.strip() or len(REVIEW) > 200 or "\n" in REVIEW:
        raise SystemExit("review fails the entry gate (1-200 chars, one line)")
    out_dir = "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
