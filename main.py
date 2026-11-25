#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the monologue to /output/entry.txt (override with ENTRY_OUTPUT).
Pure standard library. Deterministic: the same text on every run.
"""

import os
import sys

MONOLOGUE = (
    "Right. The candles have burned down to stubs again. I meant to replace "
    "them \u2014 I meant to do so much \u2014 before the eclipse. The seventh "
    "seal is ready, the one that opens the mountain gate. General Ostric "
    "waits below, polishing armor unbloodied in forty years. He bows. I "
    "nod. The ravens stopped coming last winter; the messages, I suppose, "
    "tired of the road. My tea has gone cold. Again. No matter. When the "
    "moon swallows the sun, I will speak the word, the mountain will open, "
    "and the world will \u2014 ah. What was I saying? The word. Yes. The word."
)


def main() -> int:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
    chars = len(MONOLOGUE)
    words = len(MONOLOGUE.split())
    print("wrote %s: %d words, %d chars" % (out, words, chars))
    if not 1 <= chars <= 600:
        print("gate FAIL: entry must be 1-600 characters", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
