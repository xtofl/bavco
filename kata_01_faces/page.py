from math import ceil, sqrt


class Page:
    def __init__(self, size):
        self.lines = list(
            list(" " for _ in range(size))
                for _ in range(size))

    def draw_circle(self, center, radius, character="x", round=ceil):
        x0, y0 = center
        for x in range(-int(radius), int(radius)+1):
            y = round(sqrt(radius*radius - x*x))
            self.lines[int(y0 - y)][int(x0 + x)] = character
            self.lines[int(y0 + y)][int(x0 + x)] = character

        return self
    
    def draw_line(self, p0, p1):
        x0, y = p0
        x1, y = p1
        for x in range(x0, x1):
            self.dot((x, y), "-")


    def draw_outline(self):
        self.lines[0] = list("-" for _ in self.lines)
        for line in self.lines[1:-1]:
            line[0] = "|"
            line[-1] = "|"
        self.lines[-1] = "_" * self.width()

    def width(self):
        return len(self.lines)

    def dot(self, point, c):
        assert(len(c) == 1)
        x, y = point
        self.lines[y][x] = c
    
    def rendered(self):
        return "\n".join(" ".join(line) for line in self.lines)
