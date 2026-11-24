#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — writes one pitch to /output/entry.txt.

Deterministic, no network, no randomness: the chosen line is embedded
below as a literal and written verbatim. One sentence, one invention:
the SockSync dryer pairs your socks over Bluetooth and files a
missing-person report the moment one vanishes — bureaucracy as the
fix for the laundry's oldest mystery.
"""

from pathlib import Path

TEXT = (
    "The SockSync: a dryer that pairs your socks over Bluetooth and "
    "files a missing-person report the moment one vanishes."
)


def main() -> None:
    # Gate: 1 to 220 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 220, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
