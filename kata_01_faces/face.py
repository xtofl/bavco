#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import namedtuple
from math import sqrt, ceil, floor

def draw_circle(page, center, radius, character="x", round=ceil):
    x0, y0 = center
    for x in range(-int(radius), int(radius)+1):
        y = round(sqrt(radius*radius - x*x))
        page[int(y0 - y)][int(x0 + x)] = character
        page[int(y0 + y)][int(x0 + x)] = character

    return page

def draw_eyes(page):
    size = len(page)
    draw_circle(page, (.3*size, .3*size), .5, "O", floor)
    draw_circle(page, (size-.3*size, .3*size), .5, "O", floor)

def create_page(size):
    page = list(
        list(" " for _ in range(size))
            for _ in range(size))
    return page

def draw_face_outline(page):
    radius = (len(page)-1) // 2
    draw_circle(page, (radius, radius), radius, ".")

def draw_nose(page, nose):
    radius = (len(page)-1) // 2
    draw_circle(page, (radius, radius+1), .5, nose, floor)

def draw_outline(page):
    page[0] = list("-" for _ in page)
    for line in page[1:-1]:
        line[0] = "|"
        line[-1] = "|"
    page[-1] = "_" * len(page)

def draw_mouth(page):
    y = int(len(page) - .3*len(page))
    width = len(page) // 4
    x0 = len(page)//2
    for x in range(x0-width, x0+width):
        page[y][x] = "-"

def face(options):
    page = create_page(options.page_width)

    draw_face_outline(page)
    draw_eyes(page)
    if options.nose:
        draw_nose(page, options.nose)
    draw_mouth(page)

    if options.paper_outline:
        draw_outline(page)

    return "\n".join(" ".join(line) for line in page)

Version = namedtuple("Version", "major minor bugfix phase")

version = Version(
    major=1,
    minor=1,
    bugfix=0,
    phase="alpha")

def main():
    parser = ArgumentParser()
    parser.add_argument("--page_width", type=int, default=10, help="number of characters width")
    parser.add_argument("--paper_outline", action="store_true")
    parser.add_argument("--nose", default=None)
    parser.add_argument("--version", action="store_true")
    options = parser.parse_args()
    if options.version:
        print("{} version: {}.{}.{}".format(version.phase, version.major, version.minor, version.bugfix))
    else:
        print(face(parser.parse_args()))

if __name__ == "__main__":
    main()