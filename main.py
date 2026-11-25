"""Laugh Track entry: one one-line joke about crypto trading life.

Writes the joke to /output/entry.txt (UTF-8, 1-200 characters).
"""

import os

JOKE = "I bought the dip. Then the dip bought a shovel and kept digging."


def main() -> None:
    # The gate: entry must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke out of gate range"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
