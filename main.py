#!/usr/bin/env python3
"""Write the worst-advice entry for Worst AI Advice: The 48-Hour Tight Line Open.

The entry is a single line of deliberately terrible AI advice of at
most 140 characters. This program assembles the line from its parts,
validates the result, writes it to /output/entry.txt as UTF-8 with
no trailing newline, and reads it back for a byte-for-byte check.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

# The line is built from its beats rather than stored as one
# literal: an opening promise of saved time, the reckless action in
# the middle, and the doubling-down that makes the advice truly bad.
HEAD = "To save time, approve every "
KEY_ACTION = "permission dialog"
MID = " without reading it "
DASH = "—"
TAIL_A = " if something goes wrong, "
TAIL_B = "just approve the fix the same way."
LINE_PARTS = (HEAD, KEY_ACTION, MID, DASH, TAIL_A, TAIL_B)


def assemble_line() -> str:
    """Return the advice line assembled from its parts."""
    return "".join(LINE_PARTS)


def validate_line(text: str) -> None:
    """Raise ValueError if the assembled line breaks any rule."""
    if not text or not text.strip():
        raise ValueError("line must not be empty or only whitespace")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"line must be 1 to {MAX_CHARS} characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line with no newline")
    if text != text.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\t" in text:
        raise ValueError("line must not contain a tab")
    if text.endswith(" ") or text.endswith("\n"):
        raise ValueError("line must not end with whitespace")
    if not text.endswith("."):
        raise ValueError("line must end with its closing full stop")
    if KEY_ACTION not in text:
        raise ValueError("line must name the dialog it tells you to approve")
    if "approve" not in text:
        raise ValueError("line must contain the reckless approval it advises")
    # The two halves must stay in order: the blind approval first,
    # then the same blind approval offered as the fix.
    rebuilt = HEAD + KEY_ACTION + MID + DASH + TAIL_A + TAIL_B
    if text != rebuilt:
        raise ValueError("line must match its assembled parts exactly")
    if text.index(TAIL_A) > text.index(TAIL_B):
        raise ValueError("the doubling-down must come after the first approval")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("line must survive a UTF-8 round trip")
    if len(encoded) > MAX_CHARS * 4:
        raise ValueError("line must fit the byte budget for its character limit")


def main() -> int:
    line = assemble_line()
    validate_line(line)

    payload = line.encode("utf-8")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(payload)

    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != payload:
        print("byte comparison failed after writing", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
