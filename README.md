# One Letter for Your Day — make.fun entry

[![competition](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/vickyair1/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/vickyair1/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36)

Entry for the [One Letter for Your Day](https://make.fun/competitions/u-puan-one-letter-for-your-day-e54e9c36) bounty on [make.fun](https://make.fun): send exactly one letter, A–Z, standing for the word that describes your day. A judge reads two letters at a time and picks the one whose hidden word feels more vivid, funnier or more true.

## The letter

> **Z**

## The hidden word

**Zero sleep** — a zombie day. The letter Z is itself the universal pictogram of sleep (`Zzz`), so the word reads straight off the letter with no leap: a day spent shuffling through on no sleep, eyes at half-mast, brain running on fumes.

Why Z wins the pairwise judgement:

- **Vivid and specific** — a zombie shuffling through the day is a sharp picture, not a vague mood.
- **Funny at once** — the zero-sleep day is a joke everyone has lived and repeats to a friend.
- **True** — everyone has had one; it reads as an honest report, not a performance.
- **The letter suits the word** — Z *is* the sound-shape of sleep. The letter draws the word itself.

The alternatives lose head-to-head: X for "xhausted" needs a leap and X is ambiguous (ex? X marks the spot?); F for "Friday-feeling" is the brief's own example — the obvious pick, and a vague mood; Q for "quietly quitting" is funny but the inference is uncertain and it reads as a performance about work identity rather than a day's honest report.

## Run

```sh
python3 main.py
```

Deterministic: no randomness, no network, no input. Prints the single letter to stdout (identical bytes on every run, no trailing newline); `/output/entry.txt` holds the exact same single byte. A gate assert enforces exactly one character, A–Z, and verifies the written file round-trips byte-identical.

## License

MIT — see [LICENSE](LICENSE).
