import math

class Circle:
    def __init__(self):
        self._radius = 0

    def get_radius(self):
        return self._radius
    def set_radius(self, radius):
        self._radius = radius
    def get_area(self):
        return math.pi * (self._radius ** 2)
    def get_circumference(self):
        return 2 * math.pi * self._radius


def main():
    circle1 = Circle()

main()