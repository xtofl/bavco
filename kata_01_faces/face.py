#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import namedtuple

def face(options):
    parts = ["""
    -------
    | o o |"""]
    if options.nose:
        parts.append("    |  {}  |".format(options.nose))
    parts.append("""    | --- |
    -------
        """)
    return "\n".join(parts)

Version = namedtuple("Version", "major minor bugfix")

version = Version(
    major=1,
    minor=0,
    bugfix=0)

def main():
    parser = ArgumentParser()
    parser.add_argument("--nose", default=None)
    parser.add_argument("--version", action="store_true")
    options = parser.parse_args()
    if options.version:
        print("version: {}.{}.{}".format(version.major, version.minor, version.bugfix))
    else:
        print(face(parser.parse_args()))

if __name__ == "__main__":
    main()