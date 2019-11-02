#!/usr/bin/env python3

from argparse import ArgumentParser

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

def main():
    parser = ArgumentParser()
    parser.add_argument("--nose", default=None)
    print(face(parser.parse_args()))

if __name__ == "__main__":
    main()