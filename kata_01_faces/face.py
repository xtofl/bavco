#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import namedtuple
from math import sqrt, ceil, floor

from page import Page

def draw_eyes(page):
    size = page.width()
    page.draw_circle((.3*size, .3*size), .5, "O", floor)
    page.draw_circle((size-.3*size, .3*size), .5, "O", floor)

def draw_face_outline(page):
    radius = (page.width()-1) // 2
    page.draw_circle((radius, radius), radius, ".")

def draw_nose(page, nose):
    radius = (page.width()-1) // 2
    page.draw_circle((radius, radius+1), .5, nose, floor)

def draw_mouth(page):
    y = int(page.width() - .3*page.width())
    width = page.width() // 4
    x0 = page.width()//2
    page.draw_line((x0-width, y), (x0+width, y))

def face(options):
    page = Page(options.page_width)

    draw_face_outline(page)
    draw_eyes(page)
    if options.nose:
        draw_nose(page, options.nose)
    draw_mouth(page)

    if options.paper_outline:
        page.draw_outline()

    return page.rendered()

Version = namedtuple("Version", "major minor bugfix phase")

version = Version(
    major=1,
    minor=2,
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