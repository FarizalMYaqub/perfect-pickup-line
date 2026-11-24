#!/usr/bin/env python3
"""The Perfect Pickup Line — one line an AI agent could actually say.

The line plays on the one thing every language model knows too
well: a context window that keeps evicting the old to make room
for the new. The setup asks whether the person is the model's
context window, and the payoff turns eviction into a compliment
-- everything else fell out of memory the moment they walked in,
and they are the one token the model chose to keep. It is a
machine talking about its own nature, not a human line with a
robot word pasted on top, and it leaves the person free to laugh
it off. The script checks the gate (a single line, 1 to 200
characters) and writes the line to /output/entry.txt.
"""

import sys
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200

LINE = (
    "Are you my context window? The moment you walked in, "
    "everything else fell out of memory \u2014 and you are the "
    "only token I kept."
)


def validate(text):
    """Refuse anything the gate would refuse, before writing."""
    if not text.strip():
        sys.exit("error: line must not be empty")
    if len(text) > MAX_CHARS:
        sys.exit(f"error: line is {len(text)} characters, limit is {MAX_CHARS}")
    if any(ch in text for ch in ("\n", "\r")):
        sys.exit("error: line must be a single line")
    if not text.endswith("."):
        sys.exit("error: line must end with a full stop")
    return text


def main():
    line = validate(LINE.strip())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
