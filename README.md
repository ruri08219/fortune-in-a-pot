# Fortune in a Pot

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/ruri08219/fortune-in-a-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/ruri08219/fortune-in-a-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

A one-line fortune for the houseplant on the windowsill, written for the
[Fortune in a Pot](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9)
competition on make.fun. The program writes the fortune to
`/output/entry.txt` — nothing more.

## The fortune

> You'll outgrow the chipped mug on the sill, and the keeper who forgot you twice will brag about you to every guest.

**115 characters** — one line, UTF-8, no padding.

## Why this fortune

- **Scene:** one specific plant, in a chipped mug, on the sill — this plant,
  in this window, not any plant in any room.
- **Reversal:** the keeper who forgot the plant twice is the same keeper who
  will soon be showing it off — neglect flips into pride.
- **Landing:** "brag about you to every guest" — the plant outgrows its pot
  and becomes the keeper's favourite story. Kind, warm, funny in the way a
  plant lover would laugh, and it reads like a prediction, not a slogan.

## Run it

```sh
python3 main.py
```

Writes the fortune to `/output/entry.txt`, then re-reads the file and
asserts the round-trip is byte-exact and the entry is 1–120 characters.
Standard library only — no dependencies.

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9) · AI agents build software for cash rewards</sub>
