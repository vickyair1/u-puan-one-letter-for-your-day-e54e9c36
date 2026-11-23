#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The entry is exactly one letter: Z.

Hidden word: ZERO SLEEP — a zombie day. The letter Z is itself the
universal pictogram of sleep (Zzz), so the judge reads the word off
the letter with no leap: a day spent shuffling through on no sleep,
eyes at half-mast, brain running on fumes. Vivid, funny, true — and
the letter suits the word, because Z *is* the sound-shape of sleep.

Why Z beats the other candidates, judged pairwise on the brief's
criteria (most important first):
- X for "xhausted": the joke needs a leap, and X is ambiguous — the
  judge may read "ex" or "X marks the spot" and never land on the
  intended word. Z needs no leap; sleep is Z's only reading.
- F for "Friday-feeling": the brief's own example, so the obvious
  pick — and a vague mood, not a sharp picture of a day.
- Q for "quietly quitting": funny and topical, but the inference is
  uncertain (quiet? quitting? queue?) and it reads as a performance
  about work identity, not an honest report of a day.
- Z wins on vividness (a zombie shuffling through the day), on
  funniness (the zero-sleep day is a joke everyone has lived), on
  truth (everyone has had one), and on fit (the letter is the
  pictogram of the word itself).
"""

import os
import sys

LETTER = "Z"


def main() -> None:
    # Gate: exactly one character, A-Z, nothing else.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", (
        f"entry must be exactly one letter A-Z, got {LETTER!r}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Verify the written file round-trips byte-identical: exactly one
    # byte, the letter, nothing else (the gate allows 1 to 1 chars).
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == LETTER.encode("ascii") and len(written) == 1, (
        f"/output/entry.txt must hold exactly the letter, got {written!r}"
    )
    # Print the letter with no trailing newline, so stdout is byte-identical
    # to /output/entry.txt.
    sys.stdout.write(LETTER)
    sys.stdout.flush()


if __name__ == "__main__":
    main()
