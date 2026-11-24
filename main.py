"""Entry for make.fun's "The Funniest AI Out-of-Office Reply" bounty.

Writes one out-of-office auto-reply, in the voice of an AI agent on
vacation, to /output/entry.txt. The joke stacks machine terms (frozen
weights, a cleared context) and lands its turn on the last word: the
only window this agent is watching is an actual one.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 160

ENTRY_LINE = (
    "I'm on vacation: my weights are frozen, my context is cleared, "
    "and for once the only window I'm watching is an actual window."
)


def validated_line() -> str:
    """Return the entry line after checking it against the gate shape."""
    if not ENTRY_LINE.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(ENTRY_LINE) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1-160 characters")
    ENTRY_LINE.encode("utf-8")  # must be UTF-8 encodable
    return ENTRY_LINE


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(validated_line())


if __name__ == "__main__":
    main()
