#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

Deterministic: copies the fixed image bundled in this repository.
No network access, no randomness, no timestamps — running this
program twice produces byte-identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
