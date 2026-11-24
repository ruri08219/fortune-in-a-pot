"""Fortune in a Pot — a one-line fortune for a houseplant.

Writes the fortune to /output/entry.txt as UTF-8, then re-reads the file
and asserts the round-trip is byte-exact and the entry is 1-120 characters.
Standard library only.
"""

from pathlib import Path

FORTUNE = (
    "You'll outgrow the chipped mug on the sill, and the keeper who "
    "forgot you twice will brag about you to every guest."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")
    round_trip = OUTPUT_PATH.read_text(encoding="utf-8")
    assert round_trip == FORTUNE, "round-trip mismatch"
    assert 1 <= len(round_trip) <= 120, (
        f"entry must be 1-120 characters, got {len(round_trip)}"
    )
    assert round_trip.strip() == FORTUNE, "entry must not be only whitespace"


if __name__ == "__main__":
    main()
