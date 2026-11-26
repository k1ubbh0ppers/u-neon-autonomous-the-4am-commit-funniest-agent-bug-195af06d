#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

An AI agent's one-line commit message, left in the log after a long
night of chasing down and repairing its own bugs. The program writes
the line to /output/entry.txt. Python 3 standard library only; the
message is baked into the source, no network, no input files.
"""

from pathlib import Path

# The commit message. The bug hid inside the agent's own 2am patch, so
# the repair is a repair of a repair, and the agent ends up apologising
# to itself in the comments.
COMMIT_LINE = (
    "fix: the bug was in my own 2am patch, so I fixed my fix and left "
    "an apology to myself in the comments"
)

MAX_CHARS = 200
DEST = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Check the line against the gate before anything is written."""
    if not line.strip():
        raise ValueError("commit message is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"commit message is {len(line)} chars, over the {MAX_CHARS}-char limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("commit message must be a single line")
    return line


def describe(line: str) -> str:
    """One-line summary of the entry for humans reading the log."""
    words = line.split()
    return f"{len(line)} chars, {len(words)} words, one line"


def main() -> None:
    line = validate(COMMIT_LINE)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(line, encoding="utf-8")
    print(f"wrote {describe(line)} to {DEST}")
    print(line)


if __name__ == "__main__":
    main()
