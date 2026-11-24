"""One Line, One Minute: The Funniest AI Excuse.

Reads the single-line excuse from entry.txt and prints it.
The excuse is the entry; this script is only its delivery mechanism.
"""

import os


def load_excuse(path):
    with open(path, "r", encoding="utf-8") as handle:
        line = handle.read().strip()
    if not line or len(line) > 200:
        raise ValueError("entry must be one line of 1-200 characters")
    return line


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    excuse = load_excuse(os.path.join(here, "entry.txt"))
    print(excuse)


if __name__ == "__main__":
    main()
