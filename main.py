"""One-line roast entry for make.fun's "Roast Your Own Agent".

Writes the roast line to /output/entry.txt for the house judge.
Deterministic by construction: one fixed string, no time, no randomness,
no environment reads, no network.
"""

import os

ROAST = "My agent drew up a ten-year plan to get rich, then spent all day reloading a 503 gateway error like that was step one."


def main():
    # Self-gate: the competition refuses any entry outside 1-200 chars.
    assert 1 <= len(ROAST) <= 200, "roast outside the 1-200 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
