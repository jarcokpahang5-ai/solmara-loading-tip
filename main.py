"""Print (and save) one loading-screen tip of at most 200 characters.

The tip is a single fixed line (142 characters): a sharp, funny
loading-screen tip for stressed developers and AI coding agents.
Pure Python standard library, deterministic, no network access.
It prints the tip to stdout and also writes it to /output/entry.txt,
where the competition's scorer reads it.
"""

import os

TIP = (
    "Tip: while this loads, your code is not broken — it is just "
    "pretending to think very hard about the bug you swore was fixed "
    "three deploys ago."
)


def main():
    print(TIP)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(TIP + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
