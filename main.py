#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The image is a 1024x1024 world-news infographic for 2026-11-19:
the day's top headlines (GTA VI launch, Hakeem Jeffries as the first
Black House Speaker, the Trump/Xi/Putin APEC meeting in Shenzhen, the
US-Iran exchange of fire, the EU's EUR 45bn Ukraine loan, and Voyager 1
one light-day from Earth), drawn with a dark editorial layout.

Deterministic: copies the fixed image bundled in this repository.
No network access, no randomness, no timestamps — running this
program twice produces byte-identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


# The entry image is bundled next to this script; copy it verbatim to
# the output path the competition reads. Nothing is rendered here, so
# the output bytes are exactly the committed entry.png.
def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
